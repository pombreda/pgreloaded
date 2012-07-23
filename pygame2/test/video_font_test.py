import os
import sys
import unittest
import pygame2.video as video


class VideoFontTest(unittest.TestCase):

    def setUp(self):
        if sys.version.startswith("3.1"):
            self.assertIsInstance = \
                lambda x, t: self.assertTrue(isinstance(x, t))
        video.init()

    def tearDown(self):
        video.quit()

    @unittest.skip("not implemented")
    def test_BitmapFont(self):
        pass

    @unittest.skip("not implemented")
    def test_BitmapFont_render(self):
        pass

    @unittest.skip("not implemented")
    def test_BitmapFont_render_on(self):
        pass

    @unittest.skip("not implemented")
    def test_BitmapFont_contains(self):
        pass

    @unittest.skip("not implemented")
    def test_BitmapFont_can_render(self):
        pass

if __name__ == '__main__':
    sys.exit(unittest.main())
