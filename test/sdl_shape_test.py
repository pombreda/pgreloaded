import sys
import unittest
import pygame2.sdl as sdl
from pygame2.sdl.error import SDLError
import pygame2.sdl.shape as shape
import pygame2.sdl.video as video


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

    @unittest.skip("not implemented")
    def test_set_window_shape(self):
        pass

    def test_get_shaped_window_mode(self):
        flags = (video.SDL_WINDOW_HIDDEN, )
        for flag in flags:
            window = shape.create_shaped_window("Test", 10, 10, 10, 10, flag)
            self.assertIsInstance(window, video.SDL_Window)
            mode = shape.get_shaped_window_mode(window)
            self.assertIsInstance(mode, shape.SDL_WindowShapeMode)
            video.destroy_window(window)

if __name__ == '__main__':
    unittest.main()
