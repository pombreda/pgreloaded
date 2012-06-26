import sys
import unittest
from pygame2.test import RESOURCES
import pygame2.sdl as sdl
from pygame2.sdl.pixels import SDL_Color
import pygame2.sdl.rwops as rwops
import pygame2.sdl.surface as surface
import pygame2.sdlttf as sdlttf


class SDLTTFTest(unittest.TestCase):
    __tags__ = ["sdl", "sdlttf"]

    def setUp(self):
        if sys.version.startswith("3.1"):
            self.assertIsInstance = \
                lambda x, t: self.assertTrue(isinstance(x, t))
        sdl.init(0)
        sdlttf.init()

    def tearDown(self):
        sdl.quit()
        sdlttf.quit()

    def test_TTF_Font(self):
        font = sdlttf.TTF_Font()
        self.assertIsInstance(font, sdlttf.TTF_Font)

    @unittest.skip("not implemented")
    def test_init_quit(self):
        pass

    def test_open_close_font(self):
        filename = RESOURCES.get_path("tuffy.ttf")
        for x in range(-10, 15):
            font = sdlttf.open_font(filename, x)
            self.assertIsInstance(font, sdlttf.TTF_Font)
            sdlttf.close_font(font)
        self.assertRaises(TypeError, sdlttf.open_font, None, None)
        self.assertRaises(TypeError, sdlttf.open_font, filename, None)
        self.assertRaises(ValueError, sdlttf.open_font, filename, "abcd")
        self.assertRaises(TypeError, sdlttf.open_font, None, "abcd")
        self.assertRaises(sdl.SDLError, sdlttf.open_font, "test", 10)

    def test_open_font_index(self):
        filename = RESOURCES.get_path("tuffy.ttf")
        for x in range(-10, 15):
            font = sdlttf.open_font_index(filename, x, 0)
            self.assertIsInstance(font, sdlttf.TTF_Font)
            sdlttf.close_font(font)
        self.assertRaises(TypeError, sdlttf.open_font_index, None, None, None)
        self.assertRaises(TypeError, sdlttf.open_font_index, filename, None,
                          None)
        self.assertRaises(TypeError, sdlttf.open_font_index, filename, 10, None)
        self.assertRaises(TypeError, sdlttf.open_font_index, filename, None, 0)
        self.assertRaises(TypeError, sdlttf.open_font_index, filename, None, 0)
        self.assertRaises(ValueError, sdlttf.open_font_index, filename, 10, -2)
        self.assertRaises(sdl.SDLError, sdlttf.open_font_index, "test", 10, 0)

    def test_open_font_rw(self):
        fp = RESOURCES.get("tuffy.ttf")
        fontrw = rwops.rw_from_object(fp)
        for x in range(-10, 15):
            fp.seek(0)
            font = sdlttf.open_font_rw(fontrw, False, x)
            self.assertIsInstance(font, sdlttf.TTF_Font)
            sdlttf.close_font(font)
        fp.seek(0)
        self.assertRaises(TypeError, sdlttf.open_font_rw, None, False, None)
        self.assertRaises(TypeError, sdlttf.open_font_rw, None, False, 10)
        self.assertRaises(TypeError, sdlttf.open_font_rw, fontrw, False, None)

    def test_open_font_index_rw(self):
        fp = RESOURCES.get("tuffy.ttf")
        fontrw = rwops.rw_from_object(fp)
        for x in range(-10, 15):
            fp.seek(0)
            font = sdlttf.open_font_index_rw(fontrw, False, x, 0)
            self.assertIsInstance(font, sdlttf.TTF_Font)
            sdlttf.close_font(font)
        fp.seek(0)
        self.assertRaises(TypeError, sdlttf.open_font_index_rw, None, False,
                          None, None)
        self.assertRaises(TypeError, sdlttf.open_font_index_rw, None, False,
                          10, None)
        self.assertRaises(TypeError, sdlttf.open_font_index_rw, None, False,
                          None, 0)
        self.assertRaises(TypeError, sdlttf.open_font_index_rw, fontrw, False,
                          None, 0)
        self.assertRaises(TypeError, sdlttf.open_font_index_rw, fontrw, False,
                          10, None)

    def test_get_set_font_style(self):
        filename = RESOURCES.get_path("tuffy.ttf")
        font = sdlttf.open_font(filename, 10)
        self.assertIsInstance(font, sdlttf.TTF_Font)
        self.assertEqual (sdlttf.get_font_style(font), sdlttf.TTF_STYLE_NORMAL)
        sdlttf.set_font_style(font, sdlttf.TTF_STYLE_BOLD)
        self.assertEqual (sdlttf.get_font_style(font), sdlttf.TTF_STYLE_BOLD)
        sdlttf.set_font_style(font, sdlttf.TTF_STYLE_BOLD |
                              sdlttf.TTF_STYLE_ITALIC)
        self.assertEqual (sdlttf.get_font_style(font), sdlttf.TTF_STYLE_BOLD |
                          sdlttf.TTF_STYLE_ITALIC)
        sdlttf.set_font_style(font, sdlttf.TTF_STYLE_BOLD |
                              sdlttf.TTF_STYLE_UNDERLINE)
        self.assertRaises(TypeError, sdlttf.get_font_style, None)
        self.assertRaises(TypeError, sdlttf.get_font_style, "test")
        self.assertRaises(TypeError, sdlttf.get_font_style, 1234)
        self.assertRaises(TypeError, sdlttf.set_font_style, font, None)
        self.assertRaises(TypeError, sdlttf.set_font_style, "test", None)
        self.assertRaises(TypeError, sdlttf.set_font_style, 1234, None)
        self.assertRaises(TypeError, sdlttf.set_font_style, "test", 3)
        self.assertRaises(TypeError, sdlttf.set_font_style, 1234, 4)
        self.assertRaises(TypeError, sdlttf.set_font_style, font, "test")
        sdlttf.close_font(font)

    def test_get_set_font_outline(self):
        filename = RESOURCES.get_path("tuffy.ttf")
        font = sdlttf.open_font(filename, 10)
        self.assertEqual(sdlttf.get_font_outline(font), 0)
        for x in range(-10, 10):
            sdlttf.set_font_outline(font, x)
            self.assertEqual(sdlttf.get_font_outline(font), x)
        self.assertRaises(TypeError, sdlttf.set_font_outline, None, None)
        self.assertRaises(TypeError, sdlttf.set_font_outline, font, None)
        self.assertRaises(ValueError, sdlttf.set_font_outline, font, "test")
        self.assertRaises(TypeError, sdlttf.set_font_outline, None, "test")
        self.assertRaises(TypeError, sdlttf.set_font_outline, None, 123)
        self.assertRaises(TypeError, sdlttf.get_font_outline, None)
        self.assertRaises(TypeError, sdlttf.get_font_outline, None)
        sdlttf.close_font(font)

    def test_get_set_font_hinting(self):
        filename = RESOURCES.get_path("tuffy.ttf")
        font = sdlttf.open_font(filename, 10)
        self.assertEqual(sdlttf.get_font_hinting(font),
                         sdlttf.TTF_HINTING_NORMAL)
        for hint in (sdlttf.TTF_HINTING_NORMAL, sdlttf.TTF_HINTING_LIGHT,
                     sdlttf.TTF_HINTING_MONO, sdlttf.TTF_HINTING_NONE):
            sdlttf.set_font_hinting(font, hint)
            self.assertEqual(sdlttf.get_font_hinting(font), hint)
        self.assertRaises(TypeError, sdlttf.set_font_hinting, None, None)
        self.assertRaises(TypeError, sdlttf.set_font_hinting, font, None)
        self.assertRaises(TypeError, sdlttf.set_font_hinting, None, 1)
        self.assertRaises(TypeError, sdlttf.set_font_hinting, font, "test")
        self.assertRaises(TypeError, sdlttf.set_font_hinting, None, "test")
        self.assertRaises(TypeError, sdlttf.get_font_hinting, None)
        sdlttf.close_font(font)

    def test_font_height(self):
        filename = RESOURCES.get_path("tuffy.ttf")
        last = cur = 0
        for ptsize in range(-10, 10):
            font = sdlttf.open_font(filename, ptsize)
            cur = sdlttf.font_height(font)
            self.assertGreaterEqual(cur, last)
            last = cur
            sdlttf.close_font(font)
        self.assertRaises(TypeError, sdlttf.font_height, None)
        self.assertRaises(TypeError, sdlttf.font_height, 1234)
        self.assertRaises(TypeError, sdlttf.font_height, "test")

    def test_font_ascent(self):
        filename = RESOURCES.get_path("tuffy.ttf")
        last = cur = 0
        for ptsize in range(-10, 10):
            font = sdlttf.open_font(filename, ptsize)
            cur = sdlttf.font_ascent(font)
            self.assertGreaterEqual(cur, last)
            last = cur
            sdlttf.close_font(font)
        self.assertRaises(TypeError, sdlttf.font_ascent, None)
        self.assertRaises(TypeError, sdlttf.font_ascent, 1234)
        self.assertRaises(TypeError, sdlttf.font_ascent, "test")

    def test_font_descent(self):
        filename = RESOURCES.get_path("tuffy.ttf")
        last = cur = 0
        for ptsize in range(-10, 10):
            font = sdlttf.open_font(filename, ptsize)
            cur = sdlttf.font_descent(font)
            self.assertLessEqual(cur, last)
            last = cur
            sdlttf.close_font(font)
        self.assertRaises(TypeError, sdlttf.font_descent, None)
        self.assertRaises(TypeError, sdlttf.font_descent, 1234)
        self.assertRaises(TypeError, sdlttf.font_descent, "test")

    def test_font_line_skip(self):
        filename = RESOURCES.get_path("tuffy.ttf")
        last = cur = 0
        for ptsize in range(-10, 10):
            font = sdlttf.open_font(filename, ptsize)
            cur = sdlttf.font_line_skip(font)
            self.assertGreaterEqual(cur, last)
            last = cur
            sdlttf.close_font(font)
        self.assertRaises(TypeError, sdlttf.font_line_skip, None)
        self.assertRaises(TypeError, sdlttf.font_line_skip, 1234)
        self.assertRaises(TypeError, sdlttf.font_line_skip, "test")

    def test_get_set_font_kerning(self):
        filename = RESOURCES.get_path("tuffy.ttf")
        font = sdlttf.open_font(filename, 10)
        self.assertEqual(sdlttf.get_font_kerning(font), True)
        sdlttf.set_font_kerning(font, False)
        self.assertEqual(sdlttf.get_font_kerning(font), False)
        sdlttf.set_font_kerning(font, True)
        self.assertEqual(sdlttf.get_font_kerning(font), True)
        sdlttf.set_font_kerning(font, False)
        self.assertEqual(sdlttf.get_font_kerning(font), False)
        self.assertRaises(TypeError, sdlttf.get_font_kerning, None)
        self.assertRaises(TypeError, sdlttf.get_font_kerning, "test")
        self.assertRaises(TypeError, sdlttf.get_font_kerning, 1234)
        self.assertRaises(TypeError, sdlttf.set_font_kerning, None, None)
        self.assertRaises(TypeError, sdlttf.set_font_kerning, "test", "test")
        self.assertRaises(TypeError, sdlttf.set_font_kerning, 1234, None)
        sdlttf.close_font(font)

    def test_font_faces(self):
        filename = RESOURCES.get_path("tuffy.ttf")
        font = sdlttf.open_font(filename, 10)
        self.assertGreaterEqual(sdlttf.font_faces(font), 1)
        self.assertRaises(TypeError, sdlttf.font_faces, None)
        self.assertRaises(TypeError, sdlttf.font_faces, "test")
        self.assertRaises(TypeError, sdlttf.font_faces, 1234)
        sdlttf.close_font(font)

    def test_font_face_is_fixed_width(self):
        filename = RESOURCES.get_path("tuffy.ttf")
        font = sdlttf.open_font(filename, 10)
        self.assertFalse(sdlttf.font_face_is_fixed_width(font))
        self.assertRaises(TypeError, sdlttf.font_face_is_fixed_width, None)
        self.assertRaises(TypeError, sdlttf.font_face_is_fixed_width, "test")
        self.assertRaises(TypeError, sdlttf.font_face_is_fixed_width, 1234)
        sdlttf.close_font(font)

    def test_font_face_family_name(self):
        filename = RESOURCES.get_path("tuffy.ttf")
        font = sdlttf.open_font(filename, 10)
        self.assertEqual(sdlttf.font_face_family_name(font), "Tuffy")
        self.assertRaises(TypeError, sdlttf.font_face_family_name, None)
        self.assertRaises(TypeError, sdlttf.font_face_family_name, "test")
        self.assertRaises(TypeError, sdlttf.font_face_family_name, 1234)
        sdlttf.close_font(font)

    def test_font_face_style_name(self):
        filename = RESOURCES.get_path("tuffy.ttf")
        font = sdlttf.open_font(filename, 10)
        self.assertEqual(sdlttf.font_face_style_name(font), "Regular")
        self.assertRaises(TypeError, sdlttf.font_face_style_name, None)
        self.assertRaises(TypeError, sdlttf.font_face_style_name, "test")
        self.assertRaises(TypeError, sdlttf.font_face_style_name, 1234)
        sdlttf.close_font(font)

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

    def test_render_blended(self):
        filename = RESOURCES.get_path("tuffy.ttf")
        font = sdlttf.open_font(filename, 10)
        color = SDL_Color(0, 0, 0)
        sf = sdlttf.render_blended(font, "Example", color)
        self.assertIsInstance(sf, surface.SDL_Surface)
        surface.free_surface(sf)

    @unittest.skip("not implemented")
    def test_get_kerning_size(self):
        pass


if __name__ == '__main__':
    sys.exit(unittest.main())
