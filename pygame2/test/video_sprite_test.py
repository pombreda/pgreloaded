import sys
import unittest
from ctypes import ArgumentError
import pygame2.video as video
from pygame2.sdl import SDLError


class VideoSpriteTest(unittest.TestCase):

    def setUp(self):
        if sys.version.startswith("3.1"):
            self.assertIsInstance = \
                lambda x, t: self.assertTrue(isinstance(x, t))
        pass

    def tearDown(self):
        pass

    @unittest.skip("not implemented")
    def test_SpriteFactory(self):
        pass

    @unittest.skip("not implemented")
    def test_SpriteFactory_create_sprite(self):
        pass

    @unittest.skip("not implemented")
    def test_SpriteFactory_create_software_sprite(self):
        pass

    @unittest.skip("not implemented")
    def test_SpriteFactory_create_texture_sprite(self):
        pass

    @unittest.skip("not implemented")
    def test_SpriteFactory_from_image(self):
        pass

    @unittest.skip("not implemented")
    def test_SpriteFactory_from_object(self):
        pass

    @unittest.skip("not implemented")
    def test_SpriteFactory_from_surface(self):
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
    def test_SoftwareSpriteRenderer(self):
        pass

    @unittest.skip("not implemented")
    def test_SoftwareSpriteRenderer_render(self):
        pass

    @unittest.skip("not implemented")
    def test_SoftwareSpriteRenderer_process(self):
        pass

    @unittest.skip("not implemented")
    def test_TextureSpriteRenderer(self):
        pass

    @unittest.skip("not implemented")
    def test_TextureSpriteRenderer_render(self):
        pass

    @unittest.skip("not implemented")
    def test_TextureSpriteRenderer_process(self):
        pass

    @unittest.skip("not implemented")
    def test_Sprite(self):
        pass

    @unittest.skip("not implemented")
    def test_Sprite_position_xy(self):
        pass

    @unittest.skip("not implemented")
    def test_SoftwareSprite(self):
        for w in range(0, 100):
            for h in range(0, 100):
                for bpp in (1, 4, 8, 12, 15, 16, 24, 32):
                    sprite = video.SoftwareSprite(size=(w, h), bpp=bpp)
                    self.assertIsInstance(sprite, video.SoftwareSprite)
        sprite = video.SoftwareSprite()
        self.assertIsInstance(sprite, video.SoftwareSprite)

        self.assertRaises(ValueError, video.SoftwareSprite, size=(-1, -1))
        self.assertRaises(ValueError, video.SoftwareSprite, size=(-10, 5))
        self.assertRaises(ValueError, video.SoftwareSprite, size=(10, -5))
        self.assertRaises(TypeError, video.SoftwareSprite, size=None)
        self.assertRaises(SDLError, video.SoftwareSprite, bpp=-1)
        self.assertRaises(TypeError, video.SoftwareSprite, masks=5)
        self.assertRaises((ArgumentError, TypeError), video.SoftwareSprite,
                          masks=(None, None, None, None))
        self.assertRaises((ArgumentError, TypeError), video.SoftwareSprite,
                          masks=("Test", 1, 2, 3))
        # TODO: tests for source argument

    @unittest.skip("not implemented")
    def test_SoftwareSprite_position_xy(self):
        sprite = video.SoftwareSprite(size=(10, 10), bpp=32)
        self.assertEqual(sprite.position, (0, 0))
        positions = [(x, y) for x in range(-50, 50) for y in range(-50, 50)]
        for x, y in positions:
            sprite.position = x, y
            self.assertEqual(sprite.position, (x, y))
            sprite.x = x + 1
            sprite.y = y + 1
            self.assertEqual(sprite.position, (x + 1, y + 1))

    @unittest.skip("not implemented")
    def test_SoftwareSprite_size(self):
        sizes = [(w, h) for w in range(0, 200) for h in range(0, 200)]
        for w, h in sizes:
            sprite = video.SoftwareSprite(size=(w, h), bpp=32)
            self.assertEqual(sprite.size, (w, h))
        # TODO: (65535, 65535) throws an Out of Memory exception, but 65536
        # works?
        sizes = [(0, 0), (65536, 65536)]
        for (w, h) in sizes:
            sprite = video.SoftwareSprite(size=(w, h), bpp=32)
            self.assertEqual(sprite.size, (w, h))

    @unittest.skip("not implemented")
    def test_SoftwareSprite_area(self):
        sprite = video.SoftwareSprite(size=(10, 10), bpp=32)
        self.assertEqual(sprite.area, (0, 0, 10, 10))
        def setarea(s, v):
            s.area = v
        self.assertRaises(AttributeError, setarea, sprite, (1, 2, 3, 4))

        sprite.position = 7, 3
        self.assertEqual(sprite.area, (7, 3, 17, 13))
        sprite.position = -22, 99
        self.assertEqual(sprite.area, (-22, 99, -12, 109))

    @unittest.skip("not implemented")
    def test_TextureSprite(self):
        pass

    @unittest.skip("not implemented")
    def test_TextureSprite_position_xy(self):
        pass

    @unittest.skip("not implemented")
    def test_TextureSprite_size(self):
        pass

    @unittest.skip("not implemented")
    def test_TextureSprite_area(self):
        pass

    @unittest.skip("not implemented")
    def test_Renderer(self):
        pass

    @unittest.skip("not implemented")
    def test_Renderer_color(self):
        pass

    @unittest.skip("not implemented")
    def test_Renderer_blendmode(self):
        pass

    @unittest.skip("not implemented")
    def test_Renderer_clear(self):
        pass

    @unittest.skip("not implemented")
    def test_Renderer_copy(self):
        pass

    @unittest.skip("not implemented")
    def test_Renderer_draw_line(self):
        pass

    @unittest.skip("not implemented")
    def test_Renderer_draw_point(self):
        pass

    @unittest.skip("not implemented")
    def test_Renderer_draw_rect(self):
        pass

    @unittest.skip("not implemented")
    def test_Renderer_fill(self):
        pass


if __name__ == '__main__':
    sys.exit(unittest.main())
