import os
import unittest
import pygame2
import pygame2.freetype as ft
import pygame2.freetype.constants as ft_const

FONTDIR = os.path.dirname (os.path.abspath (__file__))

class FreeTypeFontTest(unittest.TestCase):
    __tags__ = [ "sdl", "freetype" ]

    def get_fixed_font (self):
        return ft.Font(os.path.join (FONTDIR, 'test_fixed.otf'))
    def get_sans_font (self):
        return ft.Font(os.path.join (FONTDIR, 'test_sans.ttf'))
    def get_fixed_fontfile (self):
        return open (os.path.join (FONTDIR, 'test_fixed.otf'), 'rb')
    def get_sans_fontfile (self):
        return open (os.path.join (FONTDIR, 'test_sans.ttf'), 'rb')

    def setUp (self):
        ft.init ()
        pygame2.sdl.video.init()

    def tearDown (self):
        pygame2.sdl.video.quit()
        ft.quit ()

    def test_pygame2_freetype_Font__from_stream (self):
        fp = self.get_fixed_fontfile ()
        f = ft.Font (fp)
        def test_size(s):
            self.assertTrue(isinstance(s, tuple))
            self.assertEqual(len(s), 2)
            self.assertTrue(isinstance(s[0], int))
            self.assertTrue(isinstance(s[1], int))

        size = f.get_size("ABCDabcd", ptsize=24)
        test_size(size)
        self.assertTrue(size > (0, 0), size)
        self.assertTrue(size[0] > size[1])
        del f
        fp.close ()

        fp = self.get_sans_fontfile ()
        f = ft.Font (fp)
        def test_size(s):
            self.assertTrue(isinstance(s, tuple))
            self.assertEqual(len(s), 2)
            self.assertTrue(isinstance(s[0], int))
            self.assertTrue(isinstance(s[1], int))

        size = f.get_size("ABCDabcd", ptsize=24)
        test_size(size)
        self.assertTrue(size > (0, 0), size)
        self.assertTrue(size[0] > size[1])
        del f
        fp.close ()

    def test_pygame2_freetype_Font_fixed_width(self):
        f = self.get_sans_font ()
        self.assertFalse(f.fixed_width)

        f = self.get_fixed_font ()
        self.assertFalse(f.fixed_width)

        # TODO: Find a real fixed width font to test with
        
    def test_pygame2_freetype_Font_get_metrics(self):
        font = self.get_sans_font ()
        
        # test for floating point values (BBOX_EXACT)
        metrics = font.get_metrics('ABCD', ptsize=24, bbmode=ft_const.BBOX_EXACT)
        self.assertEqual(len(metrics), len('ABCD'))
        self.assertTrue(isinstance(metrics, list))

        for metrics_tuple in metrics:
            self.assertTrue(isinstance(metrics_tuple, tuple))
            self.assertEqual(len(metrics_tuple), 5)
            for m in metrics_tuple:
                self.assertTrue(isinstance(m, float))

        # test for integer values (BBOX_PIXEL)
        metrics = font.get_metrics('foobar', ptsize=24, bbmode=ft_const.BBOX_PIXEL)
        self.assertEqual(len(metrics), len('foobar'))
        self.assertTrue(isinstance(metrics, list))

        for metrics_tuple in metrics:
            self.assertTrue(isinstance(metrics_tuple, tuple))
            self.assertEqual(len(metrics_tuple), 5)
            for m in metrics_tuple:
                self.assertTrue(isinstance(m, int))

        # test for empty string
        metrics = font.get_metrics('', ptsize=24)
        self.assertEqual(metrics, [])
        metrics = font.get_metrics('', ptsize=24, bbmode=ft_const.BBOX_EXACT)
        self.assertEqual(metrics, [])
        metrics = font.get_metrics('', ptsize=24, bbmode=ft_const.BBOX_PIXEL)
        self.assertEqual(metrics, [])

        # test for invalid string
        self.assertRaises(TypeError, font.get_metrics, 24, 24)

    def test_pygame2_freetype_Font_get_size(self):
        font = self.get_sans_font ()

        def test_size(s):
            self.assertTrue(isinstance(s, tuple))
            self.assertEqual(len(s), 2)
            self.assertTrue(isinstance(s[0], int))
            self.assertTrue(isinstance(s[1], int))

        size_default = font.get_size("ABCDabcd", ptsize=24)
        test_size(size_default)
        self.assertTrue(size_default > (0, 0), size_default)
        self.assertTrue(size_default[0] > size_default[1])

        size_bigger = font.get_size("ABCDabcd", ptsize=32)
        test_size(size_bigger)
        self.assertTrue(size_bigger > size_default)

        size_bolden = font.get_size("ABCDabcd", ptsize=24, style=ft_const.STYLE_BOLD)
        test_size(size_bolden)
        self.assertTrue(size_bolden > size_default)

        font.vertical = True
        size_vert = font.get_size("ABCDabcd", ptsize=24)
        test_size(size_vert)
        self.assertTrue(size_vert[0] < size_vert[1])
        font.vertical = False

        # TODO: Slanted text is slightly wider!
        size_italic = font.get_size("ABCDabcd", ptsize=24, style=ft_const.STYLE_ITALIC)
        test_size(size_italic)
        self.assertTrue(size_italic[0] > size_default[0])
        self.assertTrue(size_italic[1] == size_default[1])

        # TODO: Text size must consider the underline!
        size_under = font.get_size("ABCDabcd", ptsize=24, style=ft_const.STYLE_UNDERLINE)
        test_size(size_under)
        self.assertTrue(size_under[0] == size_default[0])
        self.assertTrue(size_under[1] > size_default[1])

        # Empty strings.
        size_null = font.get_size("", ptsize=24, style=ft_const.STYLE_UNDERLINE)
        test_size (size_null)
        self.assertTrue (size_null[0] == size_null[1] == 0)
        size_null = font.get_size("", ptsize=24, style=ft_const.STYLE_BOLD)
        test_size (size_null)
        self.assertTrue (size_null[0] == size_null[1] == 0)
        size_null = font.get_size("", ptsize=24, style=ft_const.STYLE_ITALIC)
        test_size (size_null)
        self.assertTrue (size_null[0] == size_null[1] == 0)
        size_null = font.get_size("", ptsize=24)
        test_size (size_null)
        self.assertTrue (size_null[0] == size_null[1] == 0)

    def test_pygame2_freetype_Font_height(self):
        f = self.get_sans_font ()
        self.assertEqual(f.height, 2355)

        f = self.get_fixed_font ()
        self.assertEqual(f.height, 1100)
        
    def test_pygame2_freetype_Font_name(self):
        f = self.get_sans_font ()
        self.assertEqual(f.name, 'Liberation Sans')

        f = self.get_fixed_font ()
        self.assertEqual(f.name, 'Inconsolata')
        
    def test_pygame2_freetype_Font_render(self):
        font = self.get_sans_font ()
        
        surf = pygame2.sdl.video.Surface(800, 600)
        color = pygame2.base.Color(0, 0, 0)

        # make sure we always have a valid fg color
        self.assertRaises(TypeError, font.render, 'FoobarBaz')
        self.assertRaises(TypeError, font.render, 'FoobarBaz', None)

        # render to new surface
        rend = font.render('FoobarBaz', pygame2.base.Color(0, 0, 0), ptsize=24)
        self.assertTrue(isinstance(rend, tuple))
        self.assertTrue(isinstance(rend[0], pygame2.base.Surface))
        self.assertTrue(isinstance(rend[1], int))
        self.assertTrue(isinstance(rend[2], int))

        # render to existing surface
        rend = font.render('FoobarBaz', color, ptsize=24, dest=(surf, 32, 32))
        self.assertTrue(isinstance(rend, tuple))
        self.assertTrue(rend[0] == surf)
        self.assertTrue(isinstance(rend[1], int))
        self.assertTrue(isinstance(rend[2], int))

        # render empty to new surface
        rend = font.render('', pygame2.base.Color(0, 0, 0), ptsize=24)
        self.assertTrue(isinstance(rend, tuple))
        self.assertTrue(isinstance(rend[0], pygame2.base.Surface))
        self.assertTrue(isinstance(rend[1], int) and rend[1] == 0)
        self.assertTrue(isinstance(rend[2], int) and rend[2] == 0)
        self.assertTrue(rend[0].size == (0, 0))
        
        # render empty to existing surface
        rend = font.render('', color, ptsize=24, dest=(surf, 32, 32))
        self.assertTrue(isinstance(rend, tuple))
        self.assertTrue(rend[0] == surf)
        self.assertTrue(isinstance(rend[1], int) and rend[1] == 0)
        self.assertTrue(isinstance(rend[2], int) and rend[2] == 0)
        
        # misc parameter test
        self.assertRaises(ValueError, font.render, 'foobar', color)
        self.assertRaises(TypeError, font.render, 'foobar', color, "",ptsize=24)
        self.assertRaises(ValueError, font.render, 'foobar', color, None,
                          style=42, ptsize=24)
        self.assertRaises(TypeError, font.render, 'foobar', color, None,
                          style=None, ptsize=24)
        self.assertRaises(ValueError, font.render,'foobar', color, None,
                          style=97, ptsize=24)

    def test_pygame2_freetype_Font_style(self):
        font = self.get_sans_font ()

        # make sure STYLE_NORMAL is the default value
        self.assertEqual(ft_const.STYLE_NORMAL, font.style)

        # make sure we check for style type
        try:    font.style = "None"
        except TypeError: pass
        else:   self.fail("Failed style assignement")

        try:    font.style = None
        except TypeError: pass
        else:   self.fail("Failed style assignement")

        # make sure we only accept valid constants
        try:    font.style = 112
        except ValueError: pass
        else:   self.fail("Failed style assignement")

        # make assure no assignements happened
        self.assertEqual(ft_const.STYLE_NORMAL, font.style)

        # test assignement
        font.style = ft_const.STYLE_UNDERLINE
        self.assertEqual(ft_const.STYLE_UNDERLINE, font.style)

        # test complex styles
        st = (  ft_const.STYLE_BOLD | ft_const.STYLE_UNDERLINE |
                ft_const.STYLE_ITALIC )

        font.style = st
        self.assertEqual(st, font.style)

        # revert changes
        font.style = ft_const.STYLE_NORMAL
        self.assertEqual(ft_const.STYLE_NORMAL, font.style)

    def todo_test_pygame2_freetype_Font_copy (self):

        # __doc__ (as of 2010-04-07) for pygame2.freetype.Font.copy:

        # Creates a copy of the Font.
        
        font = self.get_sans_font ()
        fontcopy = font.copy ()
    
    def todo_test_pygame2_freetype_Font_antialiased(self):

        # __doc__ (as of 2009-12-14) for pygame2.freetype.Font.antialiased:

        # Gets or sets the font's antialiasing mode. This defaults to True
        # on all fonts, which will be rendered by default antialiased.
        # 
        # Setting this to true will change all rendering methods to use
        # glyph bitmaps without antialiasing, which supposes a small speed gain
        # and a significant memory gain because of the way glyphs are cached.

        self.fail() 

    def todo_test_pygame2_freetype_Font_bold(self):

        # __doc__ (as of 2009-12-14) for pygame2.freetype.Font.bold:

        # Gets or sets whether the font will be bold when drawing text.
        # This default style value will be used for all text rendering and
        # size calculations unless overriden specifically in the render()
        # or get_size() calls, via the 'style' parameter.

        self.fail() 

    def todo_test_pygame2_freetype_Font_italic(self):

        # __doc__ (as of 2009-12-14) for pygame2.freetype.Font.italic:

        # Gets or sets whether the font will be slanted when drawing text.
        # This default style value will be used for all text rendering and
        # size calculations unless overriden specifically in the render()
        # or get_size() calls, via the 'style' parameter.

        self.fail() 

    def todo_test_pygame2_freetype_Font_render_raw(self):

        # __doc__ (as of 2009-12-14) for pygame2.freetype.Font.render_raw:

        # render_raw(text [, ptsize]) -> int, int, bytes
        # 
        # Renders a text to a byte buffer.
        # 
        # Renders the string *text* to a raw buffer of bytes, each byte
        # representing the opacity of the glyph's raster image in
        # grayscale.
        # 
        # The width (pitch) and height of the rendered text, together with
        # the bytes buffer, will be returned in a tuple.
        # 
        # The rendering is done using the font's default size in points.
        # Optionally you may specify another point size to use.

        self.fail() 

    def todo_test_pygame2_freetype_Font_underline(self):

        # __doc__ (as of 2009-12-14) for pygame2.freetype.Font.underline:

        # Gets or sets whether the font will be underlined when drawing text.
        # This default style value will be used for all text rendering and
        # size calculations unless overriden specifically in the render()
        # or get_size() calls, via the 'style' parameter.

        self.fail() 

    def todo_test_pygame2_freetype_Font_vertical(self):

        # __doc__ (as of 2009-12-14) for pygame2.freetype.Font.vertical:

        # Gets or sets whether the font is a vertical font such as fonts
        # representing Kanji glyphs or other styles of vertical writing.
        # 
        # Changing this attribute will cause the font to be rendering
        # vertically, and affects all other methods which manage glyphs
        # or text layouts to use vertical metrics accordingly.
        # 
        # Note that the FreeType library doesn't automatically detect
        # whether a font contains glyphs which are always supposed to
        # be drawn vertically, so this attribute must be set manually
        # by the user.
        # 
        # Also note that several font formats (specially bitmap based
        # ones) don't contain the necessary metrics to draw glyphs
        # vertically, so drawing in those cases will give unspecified
        # results.

        self.fail() 

if __name__ == '__main__':
    unittest.main()
