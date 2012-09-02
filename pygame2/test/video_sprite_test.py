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

    @unittest.skip("not implemented")
    def test_Sprite(self):
        pass

    def test_Sprite_position_xy(self):
        sprite = video.Sprite(size=(10, 10), bpp=32)
        self.assertEqual(sprite.position, (0, 0))
        positions = [(x, y) for x in range(-50, 50) for y in range(-50, 50)]
        for x, y in positions:
            sprite.position = x, y
            self.assertEqual(sprite.position, (x, y))
            sprite.x = x + 1
            sprite.y = y + 1
            self.assertEqual(sprite.position, (x + 1, y + 1))


    def test_Sprite_size(self):
        sizes = [(w, h) for w in range(0, 200) for h in range(0, 200)]
        for w, h in sizes:
            sprite = video.Sprite(size=(w, h), bpp=32)
            self.assertEqual(sprite.size, (w, h))
        # TODO: (65535, 65535) throws an Out of Memory exception, but 65536
        # works?
        sizes = [(0, 0), (65536, 65536)]
        for (w, h) in sizes:
            sprite = video.Sprite(size=(w, h), bpp=32)
            self.assertEqual(sprite.size, (w, h))

    def test_Sprite_area(self):
        sprite = video.Sprite(size=(10, 10), bpp=32)
        self.assertEqual(sprite.area, (0, 0, 10, 10))
        def setarea(s, v):
            s.area = v
        self.assertRaises(AttributeError, setarea, sprite, (1, 2, 3, 4))

        sprite.position = 7, 3
        self.assertEqual(sprite.area, (7, 3, 17, 13))
        sprite.position = -22, 99
        self.assertEqual(sprite.area, (-22, 99, -12, 109))

if __name__ == '__main__':
    sys.exit(unittest.main())
