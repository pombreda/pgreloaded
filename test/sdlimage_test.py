import sys
import unittest
import pygame2.sdl as sdl
import pygame2.sdlimage as sdlimage


class SDLImageTest(unittest.TestCase):
    __tags__ = ["sdl", "sdlimage"]

    def setUp(self):
        sdl.init(0)
        sdlimage.init()

    def tearDown(self):
        sdl.quit()
        sdlimage.quit()

    @unittest.skip("not implemented")
    def test_init_quit(self):
        pass

    @unittest.skip("not implemented")
    def test_load(self):
        pass

    @unittest.skip("not implemented")
    def test_load_rw(self):
        pass

    @unittest.skip("not implemented")
    def test_load_texture(self):
        pass

    @unittest.skip("not implemented")
    def test_texture_rw(self):
        pass

    @unittest.skip("not implemented")
    def test_texture_typed_rw(self):
        pass

    @unittest.skip("not implemented")
    def test_load_typed_rw(self):
        pass

    @unittest.skip("not implemented")
    def test_load_bmp_rw(self):
        pass

    @unittest.skip("not implemented")
    def test_load_cur_rw(self):
        pass

    @unittest.skip("not implemented")
    def test_load_gif_rw(self):
        pass

    @unittest.skip("not implemented")
    def test_load_ico_rw(self):
        pass

    @unittest.skip("not implemented")
    def test_load_jpg_rw(self):
        pass

    @unittest.skip("not implemented")
    def test_load_lbm_rw(self):
        pass

    @unittest.skip("not implemented")
    def test_load_pcx_rw(self):
        pass

    @unittest.skip("not implemented")
    def test_load_png_rw(self):
        pass

    @unittest.skip("not implemented")
    def test_load_pnm_rw(self):
        pass

    @unittest.skip("not implemented")
    def test_load_tga_rw(self):
        pass

    @unittest.skip("not implemented")
    def test_load_tif_rw(self):
        pass

    @unittest.skip("not implemented")
    def test_load_webp_rw(self):
        pass

    @unittest.skip("not implemented")
    def test_load_xcf_rw(self):
        pass

    @unittest.skip("not implemented")
    def test_load_xpm_rw(self):
        pass

    @unittest.skip("not implemented")
    def test_load_xv_rw(self):
        pass

    @unittest.skip("not implemented")
    def test_is_bmp(self):
        pass

    @unittest.skip("not implemented")
    def test_is_cur(self):
        pass

    @unittest.skip("not implemented")
    def test_is_gif(self):
        pass

    @unittest.skip("not implemented")
    def test_is_ico(self):
        pass

    @unittest.skip("not implemented")
    def test_is_jpg(self):
        pass

    @unittest.skip("not implemented")
    def test_is_lbm(self):
        pass

    @unittest.skip("not implemented")
    def test_is_pcx(self):
        pass

    @unittest.skip("not implemented")
    def test_is_png(self):
        pass

    @unittest.skip("not implemented")
    def test_is_pnm(self):
        pass

    @unittest.skip("not implemented")
    def test_is_tif(self):
        pass

    @unittest.skip("not implemented")
    def test_is_webp(self):
        pass

    @unittest.skip("not implemented")
    def test_is_xcf(self):
        pass

    @unittest.skip("not implemented")
    def test_is_xpm(self):
        pass

    @unittest.skip("not implemented")
    def test_is_xv(self):
        pass

if __name__ == '__main__':
    sys.exit(unittest.main())
