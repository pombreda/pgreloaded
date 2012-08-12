import sys
import unittest
import pygame2.sdl as sdl
import pygame2.sdl.video as video
import pygame2.sdl.syswm as syswm


class SDLSysWMTest(unittest.TestCase):
    __tags__ = ["sdl"]

    def setUp(self):
        if sys.version.startswith("3.1"):
            self.assertIsInstance = \
                lambda x, t: self.assertTrue(isinstance(x, t))
        video.init()

    def tearDown(self):
        video.quit()

    def test_get_window_wm_info(self):
        window = video.create_window("Test", 10, 10, 10, 10,
                                     video.SDL_WINDOW_HIDDEN)
        wminfo = syswm.get_window_wm_info(window)
        self.assertEqual(wminfo.version.major, 2)
        self.assertEqual(wminfo.version.minor, 0)
        self.assertEqual(wminfo.version.patch, 0)
        video.destroy_window(window)
        # TODO: not sure, what to test here specifically


if __name__ == '__main__':
    sys.exit(unittest.main())
