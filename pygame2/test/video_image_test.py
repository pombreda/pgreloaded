import os
import sys
import unittest
from pygame2.resources import Resources
import pygame2.video as video
import pygame2.sdl.surface as sdlsurface

RESOURCES = Resources(__file__, "resources")

formats = ("bmp",
           "cur",
           "gif",
           "ico",
           "jpg",
           # "lbm",
           "pbm",
           "pcx",
           "pgm",
           "png",
           "pnm",
           "ppm",
           "tga",
           "tif",
           "webp",
           "xcf",
           "xpm",
           # "xv",
           )


class VideoImageTest(unittest.TestCase):

    def setUp(self):
        if sys.version.startswith("3.1"):
            self.assertIsInstance = \
                lambda x, t: self.assertTrue(isinstance(x, t))
        video.init()

    def tearDown(self):
        video.quit()

    def test_get_image_formats(self):
        self.assertIsInstance(video.get_image_formats(), tuple)
        supformats = video.get_image_formats()
        for fmt in formats:
            self.assertTrue(fmt in supformats)

    def test_load_image(self):
        # TODO: add image comparision to check, if it actually does the
        # right thing (SDL2 BMP loaded image?)
        # Add argument tests
        try:
            import PIL
            _HASPIL = True
        except ImportError:
            _HASPIL = False

        fname = "surfacetest.%s"
        for fmt in formats:
            filename = RESOURCES.get_path(fname % fmt)
            sprite = video.load_image(filename)
            self.assertIsInstance(sprite, video.Sprite)
            sf = video.load_image(filename, True)
            self.assertIsInstance(sf, sdlsurface.SDL_Surface)

            # Force only PIL
            if _HASPIL and fmt not in ("webp", "xcf"):
                sprite = video.load_image(filename, enforce="PIL")
                self.assertIsInstance(sprite, video.Sprite)
                sf = video.load_image(filename, True, enforce="PIL")
                self.assertIsInstance(sf, sdlsurface.SDL_Surface)

            # Force only pygame2.sdlimage
            sprite = video.load_image(filename, enforce="SDL")
            self.assertIsInstance(sprite, video.Sprite)
            sf = video.load_image(filename, True, enforce="SDL")
            self.assertIsInstance(sf, sdlsurface.SDL_Surface)


if __name__ == '__main__':
    sys.exit(unittest.main())
