import sys
import unittest
from pygame2.resources import Resources
import pygame2.sdl as sdl
import pygame2.sdl.render as render
import pygame2.sdl.rwops as rwops
import pygame2.sdl.surface as surface
import pygame2.sdl.version as version
import pygame2.sdlimage as sdlimage

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


class SDLImageTest(unittest.TestCase):
    __tags__ = ["sdl", "sdlimage"]

    def setUp(self):
        if sys.version.startswith("3.1"):
            self.assertIsInstance = \
                lambda x, t: self.assertTrue(isinstance(x, t))
        sdl.init(0)
        sdlimage.init()

    def tearDown(self):
        sdl.quit()
        sdlimage.quit()

    @unittest.skip("not implemented")
    def test_init_quit(self):
        pass

    def test_linked_version(self):
        v = sdlimage.linked_version()
        self.assertEqual(type(v), version.SDL_version)
        self.assertEqual(v.major, 1)
        self.assertEqual(v.minor, 2)
        self.assertGreaterEqual(v.patch, 13)

    def test_load(self):
        fname = "surfacetest.%s"
        for fmt in formats:
            filename = RESOURCES.get_path(fname % fmt)
            sf = sdlimage.load(filename)
            self.assertIsInstance(sf, surface.SDL_Surface)
            surface.free_surface(sf)
        self.assertRaises(sdl.SDLError, sdlimage.load,
                          RESOURCES.get_path("rwopstest.txt"))
        self.assertRaises(TypeError, sdlimage.load, None)
        self.assertRaises(TypeError, sdlimage.load, 1234)

    def test_load_rw(self):
        fname = "surfacetest.%s"
        for fmt in formats:
            if fmt == "tga":
                # SDL_image does not support loading TGA via IMG_Load_RW()
                continue
            fp = RESOURCES.get(fname % fmt)
            sf = sdlimage.load_rw(rwops.rw_from_object(fp), False)
            self.assertIsInstance(sf, surface.SDL_Surface)
            surface.free_surface(sf)

    def test_load_texture(self):
        sf = surface.create_rgb_surface(10, 10, 32)
        rd = render.create_software_renderer(sf)

        fname = "surfacetest.%s"
        for fmt in formats:
            filename = RESOURCES.get_path(fname % fmt)
            tex = sdlimage.load_texture(rd, filename)
            self.assertIsInstance(tex, render.SDL_Texture)
            render.destroy_texture(tex)

        self.assertRaises(sdl.SDLError, sdlimage.load_texture, rd,
                          RESOURCES.get_path("rwopstest.txt"))

        self.assertRaises(sdl.SDLError, sdlimage.load_texture, rd, None)
        self.assertRaises(sdl.SDLError, sdlimage.load_texture, rd, 1234)
        self.assertRaises((AttributeError, TypeError),
                          sdlimage.load_texture, None,
                          RESOURCES.get_path("surfacetest.bmp"))
        self.assertRaises((AttributeError, TypeError),
                          sdlimage.load_texture, "Test",
                          RESOURCES.get_path("surfacetest.bmp"))
        self.assertRaises((AttributeError, TypeError),
                          sdlimage.load_texture, 1234,
                          RESOURCES.get_path("surfacetest.bmp"))

        render.destroy_renderer(rd)
        surface.free_surface(sf)

    def test_load_texture_rw(self):
        sf = surface.create_rgb_surface(10, 10, 32)
        rd = render.create_software_renderer(sf)

        fname = "surfacetest.%s"
        for fmt in formats:
            if fmt == "tga":
                # SDL_image does not support loading TGA via
                # IMG_LoadTexture_RW()
                continue
            fp = RESOURCES.get(fname % fmt)
            tex = sdlimage.load_texture_rw(rd, rwops.rw_from_object(fp), False)
            self.assertIsInstance(tex, render.SDL_Texture)
            render.destroy_texture(tex)

        render.destroy_renderer(rd)
        surface.free_surface(sf)

    def test_load_texture_typed_rw(self):
        sf = surface.create_rgb_surface(10, 10, 32)
        rd = render.create_software_renderer(sf)

        fname = "surfacetest.%s"
        for fmt in formats:
            fp = RESOURCES.get(fname % fmt)
            tex = sdlimage.load_texture_typed_rw(rd, rwops.rw_from_object(fp),
                                                 False, fmt.upper())
            self.assertIsInstance(tex, render.SDL_Texture)
            render.destroy_texture(tex)
        render.destroy_renderer(rd)
        surface.free_surface(sf)

    def test_load_typed_rw(self):
        fname = "surfacetest.%s"
        for fmt in formats:
            fp = RESOURCES.get(fname % fmt)
            sf = sdlimage.load_typed_rw(rwops.rw_from_object(fp), False,
                                        fmt.upper())
            self.assertIsInstance(sf, surface.SDL_Surface)
            surface.free_surface(sf)

    def test_load_bmp_rw(self):
        fp = RESOURCES.get("surfacetest.bmp")
        sf = sdlimage.load_bmp_rw(rwops.rw_from_object(fp))
        self.assertIsInstance(sf, surface.SDL_Surface)
        surface.free_surface(sf)

    def test_load_cur_rw(self):
        fp = RESOURCES.get("surfacetest.cur")
        sf = sdlimage.load_cur_rw(rwops.rw_from_object(fp))
        self.assertIsInstance(sf, surface.SDL_Surface)
        surface.free_surface(sf)
        pass

    def test_load_gif_rw(self):
        fp = RESOURCES.get("surfacetest.gif")
        sf = sdlimage.load_gif_rw(rwops.rw_from_object(fp))
        self.assertIsInstance(sf, surface.SDL_Surface)
        surface.free_surface(sf)

    def test_load_ico_rw(self):
        fp = RESOURCES.get("surfacetest.ico")
        sf = sdlimage.load_ico_rw(rwops.rw_from_object(fp))
        self.assertIsInstance(sf, surface.SDL_Surface)
        surface.free_surface(sf)

    def test_load_jpg_rw(self):
        fp = RESOURCES.get("surfacetest.jpg")
        sf = sdlimage.load_jpg_rw(rwops.rw_from_object(fp))
        self.assertIsInstance(sf, surface.SDL_Surface)
        surface.free_surface(sf)

    @unittest.skip("not implemented")
    def test_load_lbm_rw(self):
        fp = RESOURCES.get("surfacetest.lbm")
        sf = sdlimage.load_lbm_rw(rwops.rw_from_object(fp))
        self.assertIsInstance(sf, surface.SDL_Surface)
        surface.free_surface(sf)

    def test_load_pcx_rw(self):
        fp = RESOURCES.get("surfacetest.pcx")
        sf = sdlimage.load_pcx_rw(rwops.rw_from_object(fp))
        self.assertIsInstance(sf, surface.SDL_Surface)
        surface.free_surface(sf)

    def test_load_png_rw(self):
        fp = RESOURCES.get("surfacetest.png")
        sf = sdlimage.load_png_rw(rwops.rw_from_object(fp))
        self.assertIsInstance(sf, surface.SDL_Surface)
        surface.free_surface(sf)

    def test_load_pnm_rw(self):
        fp = RESOURCES.get("surfacetest.pnm")
        sf = sdlimage.load_pnm_rw(rwops.rw_from_object(fp))
        self.assertIsInstance(sf, surface.SDL_Surface)
        surface.free_surface(sf)

    def test_load_tga_rw(self):
        fp = RESOURCES.get("surfacetest.tga")
        sf = sdlimage.load_tga_rw(rwops.rw_from_object(fp))
        self.assertIsInstance(sf, surface.SDL_Surface)
        surface.free_surface(sf)

    def test_load_tif_rw(self):
        fp = RESOURCES.get("surfacetest.tif")
        sf = sdlimage.load_tif_rw(rwops.rw_from_object(fp))
        self.assertIsInstance(sf, surface.SDL_Surface)
        surface.free_surface(sf)

    def test_load_webp_rw(self):
        fp = RESOURCES.get("surfacetest.webp")
        sf = sdlimage.load_webp_rw(rwops.rw_from_object(fp))
        self.assertIsInstance(sf, surface.SDL_Surface)
        surface.free_surface(sf)

    def test_load_xcf_rw(self):
        fp = RESOURCES.get("surfacetest.xcf")
        sf = sdlimage.load_xcf_rw(rwops.rw_from_object(fp))
        self.assertIsInstance(sf, surface.SDL_Surface)
        surface.free_surface(sf)

    def test_load_xpm_rw(self):
        fp = RESOURCES.get("surfacetest.xpm")
        sf = sdlimage.load_xpm_rw(rwops.rw_from_object(fp))
        self.assertIsInstance(sf, surface.SDL_Surface)
        surface.free_surface(sf)

    @unittest.skip("not implemented")
    def test_load_xv_rw(self):
        fp = RESOURCES.get("surfacetest.xv")
        sf = sdlimage.load_xpm_rw(rwops.rw_from_object(fp))
        self.assertIsInstance(sf, surface.SDL_Surface)
        surface.free_surface(sf)

    def test_is_bmp(self):
        fname = "surfacetest.%s"
        for fmt in formats:
            imgrw = rwops.rw_from_object(RESOURCES.get(fname % fmt))
            if fmt == "bmp":
                self.assertTrue(sdlimage.is_bmp(imgrw))
            else:
                self.assertFalse(sdlimage.is_bmp(imgrw))

    def test_is_cur(self):
        fname = "surfacetest.%s"
        for fmt in formats:
            imgrw = rwops.rw_from_object(RESOURCES.get(fname % fmt))
            if fmt == "cur":
                self.assertTrue(sdlimage.is_cur(imgrw))
            else:
                self.assertFalse(sdlimage.is_cur(imgrw))

    def test_is_gif(self):
        fname = "surfacetest.%s"
        for fmt in formats:
            imgrw = rwops.rw_from_object(RESOURCES.get(fname % fmt))
            if fmt == "gif":
                self.assertTrue(sdlimage.is_gif(imgrw))
            else:
                self.assertFalse(sdlimage.is_gif(imgrw))

    def test_is_ico(self):
        fname = "surfacetest.%s"
        for fmt in formats:
            imgrw = rwops.rw_from_object(RESOURCES.get(fname % fmt))
            if fmt == "ico":
                self.assertTrue(sdlimage.is_ico(imgrw))
            else:
                self.assertFalse(sdlimage.is_ico(imgrw))

    def test_is_jpg(self):
        fname = "surfacetest.%s"
        for fmt in formats:
            imgrw = rwops.rw_from_object(RESOURCES.get(fname % fmt))
            if fmt == "jpg":
                self.assertTrue(sdlimage.is_jpg(imgrw))
            else:
                self.assertFalse(sdlimage.is_jpg(imgrw))

    @unittest.skip("not implemented")
    def test_is_lbm(self):
        fname = "surfacetest.%s"
        for fmt in formats:
            imgrw = rwops.rw_from_object(RESOURCES.get(fname % fmt))
            if fmt == "lbm":
                self.assertTrue(sdlimage.is_lbm(imgrw))
            else:
                self.assertFalse(sdlimage.is_lbm(imgrw))

    def test_is_pcx(self):
        fname = "surfacetest.%s"
        for fmt in formats:
            imgrw = rwops.rw_from_object(RESOURCES.get(fname % fmt))
            if fmt == "pcx":
                self.assertTrue(sdlimage.is_pcx(imgrw))
            else:
                self.assertFalse(sdlimage.is_pcx(imgrw))

    def test_is_png(self):
        fname = "surfacetest.%s"
        for fmt in formats:
            imgrw = rwops.rw_from_object(RESOURCES.get(fname % fmt))
            if fmt == "png":
                self.assertTrue(sdlimage.is_png(imgrw))
            else:
                self.assertFalse(sdlimage.is_png(imgrw))

    def test_is_pnm(self):
        fname = "surfacetest.%s"
        for fmt in formats:
            imgrw = rwops.rw_from_object(RESOURCES.get(fname % fmt))
            if fmt in ("pnm", "pbm", "ppm", "pgm"):
                self.assertTrue(sdlimage.is_pnm(imgrw))
            else:
                self.assertFalse(sdlimage.is_pnm(imgrw))

    def test_is_tif(self):
        fname = "surfacetest.%s"
        for fmt in formats:
            imgrw = rwops.rw_from_object(RESOURCES.get(fname % fmt))
            if fmt == "tif":
                self.assertTrue(sdlimage.is_tif(imgrw))
            else:
                self.assertFalse(sdlimage.is_tif(imgrw))

    def test_is_webp(self):
        fname = "surfacetest.%s"
        for fmt in formats:
            imgrw = rwops.rw_from_object(RESOURCES.get(fname % fmt))
            if fmt == "webp":
                self.assertTrue(sdlimage.is_webp(imgrw))
            else:
                self.assertFalse(sdlimage.is_webp(imgrw))

    def test_is_xcf(self):
        fname = "surfacetest.%s"
        for fmt in formats:
            imgrw = rwops.rw_from_object(RESOURCES.get(fname % fmt))
            if fmt == "xcf":
                self.assertTrue(sdlimage.is_xcf(imgrw))
            else:
                self.assertFalse(sdlimage.is_xcf(imgrw))

    def test_is_xpm(self):
        fname = "surfacetest.%s"
        for fmt in formats:
            imgrw = rwops.rw_from_object(RESOURCES.get(fname % fmt))
            if fmt == "xpm":
                self.assertTrue(sdlimage.is_xpm(imgrw))
            else:
                self.assertFalse(sdlimage.is_xpm(imgrw))

    @unittest.skip("not implemented")
    def test_is_xv(self):
        fname = "surfacetest.%s"
        for fmt in formats:
            imgrw = rwops.rw_from_object(RESOURCES.get(fname % fmt))
            if fmt == "xv":
                self.assertTrue(sdlimage.is_xv(imgrw))
            else:
                self.assertFalse(sdlimage.is_xv(imgrw))

    @unittest.skipIf(hasattr(sys, "pypy_version_info"),
                     "PyPy's ctypes fails to pass a correct string array")
    def test_read_xpm_from_array(self):
        fp = RESOURCES.get("surfacetest.xpm")
        xpm = b""
        fp.readline()  # /* XPM */
        fp.readline()  # static char * surfacetest_xpm[] = {
        lbuf = fp.readlines()
        for line in lbuf:
            if line.endswith(b"};"):
                xpm += line[1:-4]
            else:
                xpm += line[1:-3]
        sf = sdlimage.read_xpm_from_array(xpm)
        self.assertIsInstance(sf, surface.SDL_Surface)
        surface.free_surface(sf)


if __name__ == '__main__':
    sys.exit(unittest.main())
