import sys
import unittest
import pygame2.sdl as sdl
import pygame2.sdlttf as sdlttf


class SDLTTFTest(unittest.TestCase):
    __tags__ = ["sdl", "sdlttf"]

    def setUp(self):
        sdl.init(0)
        sdlttf.init()

    def tearDown(self):
        sdl.quit()
        sdlttf.quit()

    @unittest.skip("not implemented")
    def test_TTF_Font(self):
        font = sdlttf.TTF_Font()
        self.assertIsInstance(font, sdlttf.TTF_Font)

    @unittest.skip("not implemented")
    def test_init_quit(self):
        pass

    @unittest.skip("not implemented")
    def test_open_close_font(self):
        pass

    @unittest.skip("not implemented")
    def test_open_font_index(self):
        pass

    @unittest.skip("not implemented")
    def test_open_font_rw(self):
        pass

    @unittest.skip("not implemented")
    def test_open_font_index_rw(self):
        pass

    @unittest.skip("not implemented")
    def test_get_set_font_style(self):
        pass

    @unittest.skip("not implemented")
    def test_get_set_font_outline(self):
        pass

    @unittest.skip("not implemented")
    def test_get_set_font_hinting(self):
        pass

    @unittest.skip("not implemented")
    def test_font_height(self):
        pass

    @unittest.skip("not implemented")
    def test_font_ascent(self):
        pass

    @unittest.skip("not implemented")
    def test_font_descent(self):
        pass

    @unittest.skip("not implemented")
    def test_font_line_skip(self):
        pass

    @unittest.skip("not implemented")
    def test_get_set_font_kerning(self):
        pass

    @unittest.skip("not implemented")
    def test_font_faces(self):
        pass

    @unittest.skip("not implemented")
    def test_font_face_is_fixed_width(self):
        pass

    @unittest.skip("not implemented")
    def test_font_face_family_name(self):
        pass

    @unittest.skip("not implemented")
    def test_font_face_style_name(self):
        pass

    @unittest.skip("not implemented")
    def test_glyph_is_provided(self):
        pass

    @unittest.skip("not implemented")
    def test_glyph_metrics(self):
        pass

    @unittest.skip("not implemented")
    def test_size(self):
        pass

    @unittest.skip("not implemented")
    def test_render_solid(self):
        pass

    @unittest.skip("not implemented")
    def test_render_shaded(self):
        pass

    @unittest.skip("not implemented")
    def test_render_blended(self):
        pass

    @unittest.skip("not implemented")
    def test_get_kerning_size(self):
        pass


if __name__ == '__main__':
    sys.exit(unittest.main())
