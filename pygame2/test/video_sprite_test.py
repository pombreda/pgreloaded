import os
import sys
import unittest
import pygame2.video as video


class VideoSpriteTest(unittest.TestCase):

    def setUp(self):
        if sys.version.startswith("3.1"):
            self.assertIsInstance = \
                lambda x, t: self.assertTrue(isinstance(x, t))

    def tearDown(self):
        pass

    @unittest.skip("not implemented")
    def test_SpriteRenderer(self):
        pass

    @unittest.skip("not implemented")
    def test_SpriteRenderer_render(self):
        pass

    @unittest.skip("not implemented")
    def test_SpriteRenderer_process(self):
        pass

    def test_Sprite(self):
        sprite = video.Sprite(size=(10, 10), bpp=32)
        sprite.area = 10

    @unittest.skip("not implemented")
    def test_Sprite_position(self):
        pass

    @unittest.skip("not implemented")
    def test_Sprite_size(self):
        pass

    @unittest.skip("not implemented")
    def test_Sprite_area(self):
        pass

if __name__ == '__main__':
    sys.exit(unittest.main())
