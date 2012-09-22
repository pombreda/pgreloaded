import os
import sys
import unittest
import pygame2.video as video


class VideoPixelAccessTest(unittest.TestCase):

    def setUp(self):
        if sys.version.startswith("3.1"):
            self.assertIsInstance = \
                lambda x, t: self.assertTrue(isinstance(x, t))
        video.init()

    def tearDown(self):
        video.quit()

    @unittest.skipIf(hasattr(sys, "pypy_version_info"),
                     "PyPy's ctypes can't do byref(value, offset)")
    def test_PixelView(self):
        sprite = video.SoftSprite(size=(10, 10), bpp=32)
        view = video.PixelView(sprite)
        view[1] = (0xAABBCCDD, ) * 10
        rcolor = video.prepare_color(0xAABBCCDD, sprite)
        for index, row in enumerate(view):
            if index == 1:
                for col in row:
                    self.assertEqual(col, rcolor)
            else:
                for col in row:
                    self.assertEqual(col, 0x0)

    @unittest.skip("not implemented")
    def test_pixels2d(self):
        sprite = video.SoftSprite(size=(5, 10), bpp=32, masks=(0xFF000000,
                                                               0x00FF0000,
                                                               0x0000FF00,
                                                               0x000000FF))
        video.fill(sprite, 0xAABBCCDD, (2, 2, 2, 2))
        nparray = video.pixels2d(sprite)

    @unittest.skip("not implemented")
    def test_pixels3d(self):
        sprite = video.SoftSprite(size=(5, 10), bpp=32, masks=(0xFF000000,
                                                               0x00FF0000,
                                                               0x0000FF00,
                                                               0x000000FF))
        video.fill(sprite, 0xAABBCCDD, (1, 2, 3, 4))
        nparray = video.pixels3d(sprite)


if __name__ == '__main__':
    sys.exit(unittest.main())
