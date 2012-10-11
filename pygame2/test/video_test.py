import os
import sys
import unittest
import pygame2.sdl as sdl
import pygame2.video as video


class VideoTest(unittest.TestCase):
    __tags__ = ["sdl"]

    def setUp(self):
        if sys.version.startswith("3.1"):
            self.assertIsInstance = \
                lambda x, t: self.assertTrue(isinstance(x, t))

    def tearDown(self):
        pass

    def test_init_quit(self):
        video.init()
        self.assertEqual(sdl.was_init(sdl.SDL_INIT_VIDEO),
                         sdl.SDL_INIT_VIDEO)
        video.quit()
        self.assertNotEqual(sdl.was_init(sdl.SDL_INIT_VIDEO),
                            sdl.SDL_INIT_VIDEO)
        video.init()
        video.init()
        video.init()
        self.assertEqual(sdl.was_init(sdl.SDL_INIT_VIDEO),
                         sdl.SDL_INIT_VIDEO)
        video.quit()
        self.assertNotEqual(sdl.was_init(sdl.SDL_INIT_VIDEO),
                            sdl.SDL_INIT_VIDEO)
        video.quit()
        video.quit()
        video.quit()
        self.assertNotEqual(sdl.was_init(sdl.SDL_INIT_VIDEO),
                            sdl.SDL_INIT_VIDEO)

    @unittest.skip("not implemented")
    def test_get_events(self):
        pass
                            
    def test_TestEventProcessor(self):
        proc = video.TestEventProcessor()
        self.assertIsInstance(proc, video.TestEventProcessor)


if __name__ == '__main__':
    sys.exit(unittest.main())
