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
        rects = ((0, 0, 3, 2),
                 (2, 3, 4, 2),
                 (5, -1, 2, 2),
                 (1, 7, 4, 8)
                 )
        sprite = video.Sprite(size=(10, 10), bpp=32)
        view = video.PixelView(sprite)
        for rect in rects:
            video.fill(sprite, 0)
            colorval = video.prepare_color(0xAABBCCDD, sprite)
            video.fill(sprite, 0xAABBCCDD, rect)
            for y, row in enumerate(view):
                for x, col in enumerate(row):
                    if y >= rect[1] and y < (rect[1] + rect[3]):
                        if x >= rect[0] and x < (rect[0] + rect[2]):
                            self.assertEqual(col, colorval,
                                             "color mismatch at (x, y)")
                        else:
                            self.assertEqual(col, 0,
                                             "color mismatch at (x, y)")

                    else:
                        self.assertEqual(col, 0, "color mismatch at (x, y)")

    @unittest.skip("not implemented")
    def test_prepare_color(self):
        pass

if __name__ == '__main__':
    sys.exit(unittest.main())
