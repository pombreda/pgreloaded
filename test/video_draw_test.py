import os
import sys
import unittest
import pygame2.array as array
import pygame2.sdl.surface as surface
import pygame2.sdl.pixels as pixels
import pygame2.video as video


class VideoDrawTest(unittest.TestCase):

    def setUp(self):
        if sys.version.startswith("3.1"):
            self.assertIsInstance = \
                lambda x, t: self.assertTrue(isinstance(x, t))
        video.init()

    def tearDown(self):
        video.quit()

    def test_fill(self):
        sprite = video.Sprite(size=(50, 50), bpp=32)
        pixels = sprite.surface.pixels

    @unittest.skip("not implemented")
    def test_prepare_color(self):
        pass

if __name__ == '__main__':
    sys.exit(unittest.main())
