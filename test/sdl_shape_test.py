import sys
import unittest
import pygame2.sdl as sdl
import pygame2.sdl.shape as shape
import pygame2.sdl.video as video
import pygame2.sdl.surface as surface


class SDLShapeTest(unittest.TestCase):
    __tags__ = ["sdl"]

    def setUp(self):
        sdl.init(sdl.SDL_INIT_EVERYTHING)
        if sys.version.startswith("3.1"):
            self.assertIsInstance = \
                lambda x, t: self.assertTrue(isinstance(x, t))

    def tearDown(self):
        sdl.quit_subsystem(sdl.SDL_INIT_EVERYTHING)
        sdl.quit()

    def test_create_shaped_window(self):
        flags = (video.SDL_WINDOW_HIDDEN, )
        for flag in flags:
            window = shape.create_shaped_window("Test", 10, 10, 10, 10, flag)
            self.assertIsInstance(window, video.SDL_Window)
            video.destroy_window(window)

    def test_is_shaped_window(self):
        flags = (video.SDL_WINDOW_HIDDEN, )
        for flag in flags:
            window = shape.create_shaped_window("Test", 10, 10, 10, 10, flag)
            self.assertIsInstance(window, video.SDL_Window)
            val = shape.is_shaped_window(window)
            self.assertTrue(val)
            video.destroy_window(window)

            window = video.create_window("Test", 10, 10, 10, 10, flag)
            self.assertIsInstance(window, video.SDL_Window)
            val = shape.is_shaped_window(window)
            self.assertFalse(val)
            video.destroy_window(window)

    def test_set_window_shape(self):
        sf = surface.create_rgb_surface(10, 10, 32)
        mode = shape.SDL_WindowShapeMode()
        mode.mode = shape.ShapeModeDefault
        mode.parameters = shape.SDL_WindowShapeParams()
        mode.parameters.binarizationCutoff = 1

        flags = (video.SDL_WINDOW_HIDDEN, )
        for flag in flags:
            # TODO: find out, how shaping is supposed to work :-)
            # window = shape.create_shaped_window("Test", 10, 10, 10, 10, flag)
            # self.assertIsInstance(window, video.SDL_Window)
            # self.assertTrue(shape.is_shaped_window(window))

            # self.assertRaises(TypeError, shape.set_window_shape,
            #                   None, None, None)
            # self.assertRaises(TypeError, shape.set_window_shape,
            #                   window, None, None)
            # self.assertRaises(TypeError, shape.set_window_shape,
            #                   window, sf, None)
            # self.assertRaises(TypeError, shape.set_window_shape,
            #                   "Test", sf, mode)
            # self.assertRaises(TypeError, shape.set_window_shape,
            #                   window, 12345, mode)
            # self.assertRaises(TypeError, shape.set_window_shape,
            #                   window, sf, "Test")

            # shape.set_window_shape(window, sf, mode)
            # wmode = shape.get_shaped_window_mode(window)
            # self.assertEqual(wmode.mode, mode.mode)
            # self.assertEqual(wmode.parameters.binarizationCutoff,
            #                  mode.parameters.binarizationCutoff)
            # video.destroy_window(window)

            window = video.create_window("Test", 10, 10, 10, 10, flag)
            self.assertIsInstance(window, video.SDL_Window)
            self.assertRaises(sdl.SDLError, shape.set_window_shape,
                              window, sf, mode)
            video.destroy_window(window)

    def test_get_shaped_window_mode(self):
        flags = (video.SDL_WINDOW_HIDDEN, )
        for flag in flags:
            window = shape.create_shaped_window("Test", 10, 10, 10, 10, flag)
            self.assertIsInstance(window, video.SDL_Window)
            mode = shape.get_shaped_window_mode(window)
            self.assertIsInstance(mode, shape.SDL_WindowShapeMode)
            video.destroy_window(window)

if __name__ == '__main__':
    sys.exit(unittest.main())
