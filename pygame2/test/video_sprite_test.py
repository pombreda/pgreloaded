import sys
import unittest
from ctypes import ArgumentError
from pygame2.resources import Resources
import pygame2.video as video
from pygame2.sdl import SDLError
from pygame2.sdl.surface import SDL_Surface, create_rgb_surface

RESOURCES = Resources(__file__, "resources")


class MSprite(video.Sprite):
    def __init__(self, w=0, h=0):
        super(MSprite, self).__init__()
        self._size = w, h

    @property
    def size(self):
        return self._size


class VideoSpriteTest(unittest.TestCase):
    __tags__ = ["sdl"]

    def setUp(self):
        if sys.version.startswith("3.1"):
            self.assertIsInstance = \
                lambda x, t: self.assertTrue(isinstance(x, t))
        video.init()

    def tearDown(self):
        video.quit()

    def check_pixels(self, view, w, h, sprite, c1, c2, cx=0, cy=0):
        msg = "color mismatch at %d,%d: %d not in %s"
        cx = cx + sprite.x
        cy = cy + sprite.y
        cw, ch = sprite.size
        cmy = cy + ch
        cmx = cx + cw
        for y in range(w):
            for x in range(h):
                if cy <= y < cmy and cx <= x < cmx:
                    self.assertEqual(view[y][x], c1,
                                     msg % (x, y, view[y][x], c1))
                else:
                    self.assertTrue(view[y][x] in c2,
                                    msg % (x, y, view[y][x], c2))

    def test_SpriteFactory(self):
        factory = video.SpriteFactory(video.SOFTWARE)
        self.assertIsInstance(factory, video.SpriteFactory)
        self.assertEqual(factory.default_args, {})

        factory = video.SpriteFactory(video.SOFTWARE, bananas="tasty")
        self.assertIsInstance(factory, video.SpriteFactory)
        self.assertEqual(factory.default_args, {"bananas": "tasty"})

        window = video.Window("Test", size=(1, 1))
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
        window = video.Window("Test", size=(1, 1))
        renderer = video.RenderContext(window)
        factory = video.SpriteFactory(video.TEXTURE, renderer=renderer)
        for w in range(1, 100):
            for h in range(1, 100):
                sprite = factory.create_texture_sprite(renderer, size=(w, h))
                self.assertIsInstance(sprite, video.TextureSprite)
                #del sprite

    def test_SpriteFactory_from_image(self):
        window = video.Window("Test", size=(1, 1))
        renderer = video.RenderContext(window)
        tfactory = video.SpriteFactory(video.TEXTURE, renderer=renderer)
        sfactory = video.SpriteFactory(video.SOFTWARE)

        for suffix in ("bmp", "png", "jpg"):
            imgname = RESOURCES.get_path("surfacetest.%s" % suffix)
            tsprite = tfactory.from_image(imgname)
            self.assertIsInstance(tsprite, video.TextureSprite)
            ssprite = sfactory.from_image(imgname)
            self.assertIsInstance(ssprite, video.SoftwareSprite)

        for factory in (tfactory, sfactory):
            self.assertRaises((AttributeError, SDLError),
                              factory.from_image, None)
            self.assertRaises((IOError, SDLError),
                              factory.from_image, "banana")
            self.assertRaises((AttributeError, IOError, SDLError),
                              factory.from_image, 12345)

    @unittest.skip("not implemented")
    def test_SpriteFactory_from_object(self):
        pass

    def test_SpriteFactory_from_surface(self):
        window = video.Window("Test", size=(1, 1))
        renderer = video.RenderContext(window)
        tfactory = video.SpriteFactory(video.TEXTURE, renderer=renderer)
        sfactory = video.SpriteFactory(video.SOFTWARE)

        sf = create_rgb_surface(10, 10, 32)
        tsprite = tfactory.from_surface(sf)
        self.assertIsInstance(tsprite, video.TextureSprite)
        ssprite = sfactory.from_surface(sf)
        self.assertIsInstance(ssprite, video.SoftwareSprite)
        del sf

        for factory in (tfactory, sfactory):
            self.assertRaises((AttributeError, ArgumentError, TypeError),
                              factory.from_surface, None)
            self.assertRaises((AttributeError, ArgumentError, TypeError),
                              factory.from_surface, "test")
            self.assertRaises((AttributeError, ArgumentError, TypeError),
                              factory.from_surface, 1234)

    def test_SpriteRenderer(self):
        renderer = video.SpriteRenderer()
        self.assertIsInstance(renderer, video.SpriteRenderer)
        self.assertIsNotNone(renderer.sortfunc)
        self.assertTrue(video.Sprite in renderer.componenttypes)

    def test_SpriteRenderer_sortfunc(self):
        def func(p):
            pass

        renderer = video.SpriteRenderer()
        self.assertIsNotNone(renderer.sortfunc)
        renderer.sortfunc = func
        self.assertEqual(renderer.sortfunc, func)

        def setf(x, f):
            x.sortfunc = f
        self.assertRaises(TypeError, setf, renderer, None)
        self.assertRaises(TypeError, setf, renderer, "Test")
        self.assertRaises(TypeError, setf, renderer, 1234)

    @unittest.skip("not implemented")
    def test_SpriteRenderer_render(self):
        pass

    @unittest.skip("not implemented")
    def test_SpriteRenderer_process(self):
        pass

    def test_SoftwareSpriteRenderer(self):
        self.assertRaises(TypeError, video.SoftwareSpriteRenderer)
        self.assertRaises(TypeError, video.SoftwareSpriteRenderer, None)
        self.assertRaises(TypeError, video.SoftwareSpriteRenderer, "Test")
        self.assertRaises(TypeError, video.SoftwareSpriteRenderer, 12345)

        window = video.Window("Test", size=(1, 1))
        renderer = video.SoftwareSpriteRenderer(window)
        self.assertIsInstance(renderer, video.SpriteRenderer)
        self.assertEqual(renderer.window, window.window)
        self.assertIsInstance(renderer.surface, SDL_Surface)

        renderer = video.SoftwareSpriteRenderer(window.window)
        self.assertIsInstance(renderer, video.SpriteRenderer)
        self.assertEqual(renderer.window, window.window)
        self.assertIsInstance(renderer.surface, SDL_Surface)

        self.assertIsNotNone(renderer.sortfunc)
        self.assertFalse(video.Sprite in renderer.componenttypes)
        self.assertTrue(video.SoftwareSprite in renderer.componenttypes)

    @unittest.skipIf(hasattr(sys, "pypy_version_info"),
                     "PyPy's ctypes can't do byref(value, offset)")
    def test_SoftwareSpriteRenderer_render(self):
        sf1= create_rgb_surface(12, 7, 32)
        sp1 = video.SoftwareSprite(sf1, True)
        video.fill(sp1, 0xFF0000)

        sf2 = create_rgb_surface(3, 9, 32)
        sp2 = video.SoftwareSprite(sf2, True)
        video.fill(sp2, 0x00FF00)
        sprites = [sp1, sp2]

        window = video.Window("Test", size=(20, 20))
        renderer = video.SoftwareSpriteRenderer(window)
        self.assertIsInstance(renderer, video.SpriteRenderer)

        self.assertRaises(AttributeError, renderer.render, None, None, None)
        self.assertRaises(AttributeError, renderer.render, [None, None],
                          None, None)

        for x, y in ((0, 0), (3, 3), (20, 20), (1, 12), (5, 6)):
            sp1.position = x, y
            renderer.render(sp1)
            view = video.PixelView(renderer.surface)
            self.check_pixels(view, 20, 20, sp1, 0xFF0000, (0x0, ))
            del view
            video.fill(renderer.surface, 0x0)
        sp1.position = 0, 0
        sp2.position = 14, 1
        renderer.render(sprites)
        view = video.PixelView(renderer.surface)
        self.check_pixels(view, 20, 20, sp1, 0xFF0000, (0x0, 0x00FF00))
        self.check_pixels(view, 20, 20, sp2, 0x00FF00, (0x0, 0xFF0000))
        del view
        video.fill(renderer.surface, 0x0)
        renderer.render(sprites, 1, 2)
        view = video.PixelView(renderer.surface)
        self.check_pixels(view, 20, 20, sp1, 0xFF0000, (0x0, 0x00FF00), 1, 2)
        self.check_pixels(view, 20, 20, sp2, 0x00FF00, (0x0, 0xFF0000), 1, 2)
        del view

    @unittest.skipIf(hasattr(sys, "pypy_version_info"),
                     "PyPy's ctypes can't do byref(value, offset)")
    def test_SoftwareSpriteRenderer_process(self):
        sf1= create_rgb_surface(5, 10, 32)
        sp1 = video.SoftwareSprite(sf1, True)
        sp1.depth = 0
        video.fill(sp1, 0xFF0000)

        sf2 = create_rgb_surface(5, 10, 32)
        sp2 = video.SoftwareSprite(sf2, True)
        sp2.depth = 99
        video.fill(sp2, 0x00FF00)
        sprites = [sp1, sp2]

        window = video.Window("Test", size=(20, 20))
        renderer = video.SoftwareSpriteRenderer(window)

        renderer.process("fakeworld", sprites)
        view = video.PixelView(renderer.surface)
        # Only sp2 wins, since its depth is higher
        self.check_pixels(view, 20, 20, sp1, 0x00FF00, (0x0, ))
        self.check_pixels(view, 20, 20, sp2, 0x00FF00, (0x0, ))
        del view

        self.assertRaises(TypeError, renderer.process, None, None)

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
        sprite = MSprite()
        self.assertIsInstance(sprite, MSprite)
        self.assertIsInstance(sprite, video.Sprite)

    def test_Sprite_position_xy(self):
        sprite = MSprite()
        positions = [(x, y) for x in range(-50, 50) for y in range(-50, 50)]
        for x, y in positions:
            sprite.position = x, y
            self.assertEqual(sprite.position, (x, y))
            sprite.x = x + 1
            sprite.y = y + 1
            self.assertEqual(sprite.position, (x + 1, y + 1))

    def test_Sprite_area(self):
        sizes = [(w, h) for w in range(0, 200) for h in range(0, 200)]
        for w, h in sizes:
            sprite = MSprite(w, h)
            self.assertEqual(sprite.size, (w, h))
            self.assertEqual(sprite.area, (0, 0, w, h))
            sprite.position = w, h
            self.assertEqual(sprite.area, (w, h, 2*w, 2*h))

    def test_SoftwareSprite(self):
        self.assertRaises(TypeError, video.SoftwareSprite, None, None)
        self.assertRaises(TypeError, video.SoftwareSprite, None, True)
        self.assertRaises(TypeError, video.SoftwareSprite, None, False)

        sf = create_rgb_surface(10, 10, 32)
        sprite = video.SoftwareSprite(sf, False)
        self.assertEqual(sprite.surface, sf)
        self.assertFalse(sprite.free)

        sprite = video.SoftwareSprite(sf, True)
        self.assertEqual(sprite.surface, sf)
        self.assertTrue(sprite.free)

    def test_SoftwareSprite_position_xy(self):
        sf = create_rgb_surface(10, 10, 32)
        sprite = video.SoftwareSprite(sf, True)

        self.assertEqual(sprite.position, (0, 0))
        positions = [(x, y) for x in range(-50, 50) for y in range(-50, 50)]
        for x, y in positions:
            sprite.position = x, y
            self.assertEqual(sprite.position, (x, y))
            sprite.x = x + 1
            sprite.y = y + 1
            self.assertEqual(sprite.position, (x + 1, y + 1))

    def test_SoftwareSprite_size(self):
        sizes = [(w, h) for w in range(0, 200) for h in range(0, 200)]
        for w, h in sizes:
            sf = create_rgb_surface(w, h, 32)
            sprite = video.SoftwareSprite(sf, True)
            self.assertEqual(sprite.size, (w, h))

    def test_SoftwareSprite_area(self):
        sf = create_rgb_surface(10, 10, 32)
        sprite = video.SoftwareSprite(sf, True)
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
    def test_RenderContext(self):
        pass

    @unittest.skip("not implemented")
    def test_RenderContext_color(self):
        pass

    @unittest.skip("not implemented")
    def test_RenderContext_blendmode(self):
        pass

    @unittest.skip("not implemented")
    def test_RenderContext_clear(self):
        pass

    @unittest.skip("not implemented")
    def test_RenderContext_copy(self):
        pass

    @unittest.skip("not implemented")
    def test_RenderContext_draw_line(self):
        pass

    @unittest.skip("not implemented")
    def test_RenderContext_draw_point(self):
        pass

    @unittest.skip("not implemented")
    def test_RenderContext_draw_rect(self):
        pass

    @unittest.skip("not implemented")
    def test_RenderContext_fill(self):
        pass


if __name__ == '__main__':
    sys.exit(unittest.main())
