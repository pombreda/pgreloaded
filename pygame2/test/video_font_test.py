import sys
import unittest
from pygame2.resources import Resources
import pygame2.video as video
import pygame2.sdl.surface as sdlsurface

RESOURCES = Resources(__file__, "resources")
FONTMAP = ["0123456789",
           "ABCDEFGHIJ",
           "KLMNOPQRST",
           "UVWXYZ    ",
           "abcdefghij",
           "klmnopqrst",
           "uvwxyz    ",
           ",;.:!?-+()"
           ]


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
        sf = sdlsurface.load_bmp(RESOURCES.get_path("font.bmp"))
        self.assertIsInstance(sf, sdlsurface.SDL_Surface)
        font = video.BitmapFont(sf, (32, 32), FONTMAP)
        self.assertIsInstance(font, video.BitmapFont)
        sdlsurface.free_surface(sf)

        sprite = video.SoftSprite(RESOURCES.get_path("font.bmp"))
        self.assertIsInstance(sprite, video.SoftwareSprite)
        font = video.BitmapFont(sprite, (32, 32), FONTMAP)
        self.assertIsInstance(font, video.BitmapFont)

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
