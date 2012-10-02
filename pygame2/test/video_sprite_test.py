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
        video.init()

    def tearDown(self):
        video.quit()

    def test_SpriteFactory(self):
        factory = video.SpriteFactory(video.SOFTWARE)
        self.assertIsInstance(factory, video.SpriteFactory)
        self.assertEqual(factory.default_args, {})

        factory = video.SpriteFactory(video.SOFTWARE, bananas="tasty")
        self.assertIsInstance(factory, video.SpriteFactory)
        self.assertEqual(factory.default_args, {"bananas": "tasty"})

        window = video.Window("Test", size=(1,1))
        renderer = video.RenderContext(window)

        factory = video.SpriteFactory(video.TEXTURE, renderer=renderer)
        self.assertIsInstance(factory, video.SpriteFactory)

        factory = video.SpriteFactory(video.TEXTURE, renderer=renderer)
        self.assertIsInstance(factory, video.SpriteFactory)
        self.assertEqual(factory.default_args, {"renderer": renderer})

        self.assertRaises(ValueError, video.SpriteFactory, "Test")
        self.assertRaises(ValueError, video.SpriteFactory, -456)
        self.assertRaises(ValueError, video.SpriteFactory, 123)
        self.assertRaises(ValueError, video.SpriteFactory, video.TEXTURE)

    def test_SpriteFactory_create_sprite(self):
        window = video.Window("Test", size=(1,1))
        renderer = video.RenderContext(window)
        tfactory = video.SpriteFactory(video.TEXTURE, renderer=renderer)
        sfactory = video.SpriteFactory(video.SOFTWARE)

        for w in range(0, 100):
            for h in range(0, 100):
                for bpp in (1, 4, 8, 12, 15, 16, 24, 32):
                    sprite = sfactory.create_sprite(size=(w, h), bpp=bpp)
                    self.assertIsInstance(sprite, video.SoftwareSprite)

                if w == 0 or h == 0:
                    self.assertRaises(SDLError, tfactory.create_sprite,
                                      size=(w, h))
                    continue
                sprite = tfactory.create_sprite(size=(w, h))
                self.assertIsInstance(sprite, video.TextureSprite)

    def test_SpriteFactory_create_software_sprite(self):
        factory = video.SpriteFactory(video.SOFTWARE)
        for w in range(0, 100):
            for h in range(0, 100):
                for bpp in (1, 4, 8, 12, 15, 16, 24, 32):
                    sprite = factory.create_software_sprite((w, h), bpp)
                    self.assertIsInstance(sprite, video.SoftwareSprite)

        self.assertRaises(ValueError, factory.create_software_sprite, (-1, -1))
        self.assertRaises(ValueError, factory.create_software_sprite, (-10, 5))
        self.assertRaises(ValueError, factory.create_software_sprite, (10, -5))
        self.assertRaises(TypeError, factory.create_software_sprite, size=None)
        self.assertRaises(SDLError, factory.create_software_sprite, bpp=-1)
        self.assertRaises(TypeError, factory.create_software_sprite, masks=5)
        self.assertRaises((ArgumentError, TypeError),
                          factory.create_software_sprite,
                          masks=(None, None, None, None))
        self.assertRaises((ArgumentError, TypeError),
                          factory.create_software_sprite,
                          masks=("Test", 1, 2, 3))

    def test_SpriteFactory_create_texture_sprite(self):
        window = video.Window("Test", size=(1,1))
        renderer = video.RenderContext(window)
        factory = video.SpriteFactory(video.TEXTURE, renderer=renderer)
        for w in range(1, 100):
            for h in range(1, 100):
                sprite = factory.create_texture_sprite(renderer, size=(w, h))
                self.assertIsInstance(sprite, video.TextureSprite)
                #del sprite

    @unittest.skip("not implemented")
    def test_SpriteFactory_from_image(self):
        window = video.Window("Test", size=(1,1))
        renderer = video.RenderContext(window)
        tfactory = video.SpriteFactory(video.TEXTURE, renderer=renderer)
        sfactory = video.SpriteFactory(video.SOFTWARE)

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

    def test_Sprite(self):
        class MSprite(video.Sprite):
            @property
            def size(self):
                return None

        sprite = MSprite()
        self.assertIsInstance(sprite, MSprite)
        self.assertIsInstance(sprite, video.Sprite)

    @unittest.skip("not implemented")
    def test_Sprite_position_xy(self):
        pass

    @unittest.skip("not implemented")
    def test_Sprite_area(self):
        pass

    @unittest.skip("not implemented")
    def test_SoftwareSprite(self):
        sprite = video.SoftwareSprite()
        self.assertIsInstance(sprite, video.SoftwareSprite)

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
    def test_TextureSprite_sdize(self):
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
