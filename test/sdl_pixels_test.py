import sys
import unittest
import copy
import pygame2.sdl as sdl
from pygame2.sdl.error import SDLError
import pygame2.sdl.pixels as pixels
from pygame2.sdl.pixels import SDL_Color

class SDLPixelsTest (unittest.TestCase):
    __tags__ = [ "sdl" ]

    def setUp (self):
        sdl.init (sdl.SDL_INIT_EVERYTHING)
        if sys.version.startswith ("3.1"):
            self.assertIsInstance = lambda x, t: self.assertTrue (isinstance (x, t))
    
    def tearDown (self):
        sdl.quit_subsystem (sdl.SDL_INIT_EVERYTHING)
        sdl.quit ()

    def test_SDL_FOURCC (self):
        self.assertRaises (TypeError, pixels.SDL_FOURCC, None, None, None, None)
        self.assertRaises (TypeError, pixels.SDL_FOURCC, "a", None, None, None)
        self.assertRaises (TypeError, pixels.SDL_FOURCC, None, "a", None, None)
        self.assertRaises (TypeError, pixels.SDL_FOURCC, None, None, "a", None)
        self.assertRaises (TypeError, pixels.SDL_FOURCC, None, None, None, "a")
        self.assertRaises (TypeError, pixels.SDL_FOURCC, "a", "a", None, None)
        self.assertRaises (TypeError, pixels.SDL_FOURCC, "a", "a", "a", None)
        self.assertRaises (TypeError, pixels.SDL_FOURCC, "a", "a", "a", 1)
        self.assertRaises (TypeError, pixels.SDL_FOURCC, "a", "a", 5, 1)
        self.assertRaises (TypeError, pixels.SDL_FOURCC, "a", 17, 5, 1)
        self.assertEqual (pixels.SDL_FOURCC ("0", "0", "0", "0"), 0x30303030)
        self.assertEqual (pixels.SDL_FOURCC ("1", "1", "1", "1"), 0x31313131)
        self.assertEqual (pixels.SDL_FOURCC ("1", "2", "3", "4"), 0x34333231)
        self.assertEqual (pixels.SDL_FOURCC ("4", "3", "2", "1"), 0x31323334)
    
    def test_SDL_DEFINE_PIXELFORMAT (self):
        fmt = pixels.SDL_DEFINE_PIXELFORMAT (pixels.SDL_PIXELTYPE_INDEX1,
                                             pixels.SDL_BITMAPORDER_4321, 0,
                                             1, 0)
        self.assertEqual (fmt, pixels.SDL_PIXELFORMAT_INDEX1LSB)

        fmt = pixels.SDL_DEFINE_PIXELFORMAT (pixels.SDL_PIXELTYPE_PACKED16,
                                             pixels.SDL_PACKEDORDER_XRGB,
                                             pixels.SDL_PACKEDLAYOUT_4444,
                                             12, 2)
        self.assertEqual (fmt, pixels.SDL_PIXELFORMAT_RGB444)

        fmt = pixels.SDL_DEFINE_PIXELFORMAT (pixels.SDL_PIXELTYPE_PACKED16,
                                             pixels.SDL_PACKEDORDER_ABGR,
                                             pixels.SDL_PACKEDLAYOUT_1555,
                                             16, 2)
        self.assertEqual (fmt, pixels.SDL_PIXELFORMAT_ABGR1555)

        
    def test_SDL_PIXELTYPE (self):
        self.assertEqual (pixels.SDL_PIXELTYPE (pixels.SDL_PIXELFORMAT_INDEX1LSB), pixels.SDL_PIXELTYPE_INDEX1)
        self.assertEqual (pixels.SDL_PIXELTYPE (pixels.SDL_PIXELFORMAT_INDEX1MSB), pixels.SDL_PIXELTYPE_INDEX1)
        self.assertEqual (pixels.SDL_PIXELTYPE (pixels.SDL_PIXELFORMAT_INDEX4LSB), pixels.SDL_PIXELTYPE_INDEX4)
        self.assertEqual (pixels.SDL_PIXELTYPE (pixels.SDL_PIXELFORMAT_ARGB8888), pixels.SDL_PIXELTYPE_PACKED32)

    def test_SDL_PIXELORDER (self):
        self.assertEqual (pixels.SDL_PIXELORDER (pixels.SDL_PIXELFORMAT_INDEX1LSB), pixels.SDL_BITMAPORDER_4321)
        self.assertEqual (pixels.SDL_PIXELORDER (pixels.SDL_PIXELFORMAT_INDEX1MSB), pixels.SDL_BITMAPORDER_1234)
        self.assertEqual (pixels.SDL_PIXELORDER (pixels.SDL_PIXELFORMAT_INDEX4LSB), pixels.SDL_BITMAPORDER_4321)
        self.assertEqual (pixels.SDL_PIXELORDER (pixels.SDL_PIXELFORMAT_ARGB8888), pixels.SDL_PACKEDORDER_ARGB)
        
    def test_SDL_PIXELLAYOUT (self):
        self.assertEqual (pixels.SDL_PIXELLAYOUT (pixels.SDL_PIXELFORMAT_INDEX1LSB), pixels.SDL_PACKEDLAYOUT_NONE)
        self.assertEqual (pixels.SDL_PIXELLAYOUT (pixels.SDL_PIXELFORMAT_RGB332), pixels.SDL_PACKEDLAYOUT_332)
        self.assertEqual (pixels.SDL_PIXELLAYOUT (pixels.SDL_PIXELFORMAT_ARGB8888), pixels.SDL_PACKEDLAYOUT_8888)

    def test_SDL_BITSPERPIXEL (self):
        self.assertEqual (pixels.SDL_BITSPERPIXEL (pixels.SDL_PIXELFORMAT_INDEX1LSB), 1)
        self.assertEqual (pixels.SDL_BITSPERPIXEL (pixels.SDL_PIXELFORMAT_INDEX4LSB), 4)
        self.assertEqual (pixels.SDL_BITSPERPIXEL (pixels.SDL_PIXELFORMAT_RGB332), 8)
        self.assertEqual (pixels.SDL_BITSPERPIXEL (pixels.SDL_PIXELFORMAT_ARGB8888), 32)
        # TODO: clarify
        #self.assertEqual (pixels.SDL_BITSPERPIXEL (pixels.SDL_PIXELFORMAT_YUY2), 85)
        #self.assertEqual (pixels.SDL_BITSPERPIXEL (pixels.SDL_PIXELFORMAT_IYUV), 89)
        #self.assertEqual (pixels.SDL_BITSPERPIXEL (pixels.SDL_PIXELFORMAT_UYVY), 89)
        
    def test_SDL_BYTESPERPIXEL (self):
        self.assertEqual (pixels.SDL_BYTESPERPIXEL (pixels.SDL_PIXELFORMAT_INDEX1LSB), 0)
        self.assertEqual (pixels.SDL_BYTESPERPIXEL (pixels.SDL_PIXELFORMAT_INDEX4LSB), 0)
        self.assertEqual (pixels.SDL_BYTESPERPIXEL (pixels.SDL_PIXELFORMAT_RGB332), 1)
        self.assertEqual (pixels.SDL_BYTESPERPIXEL (pixels.SDL_PIXELFORMAT_ARGB8888), 4)
        self.assertEqual (pixels.SDL_BYTESPERPIXEL (pixels.SDL_PIXELFORMAT_YUY2), 2)
        self.assertEqual (pixels.SDL_BYTESPERPIXEL (pixels.SDL_PIXELFORMAT_IYUV), 1)
        self.assertEqual (pixels.SDL_BYTESPERPIXEL (pixels.SDL_PIXELFORMAT_UYVY), 2)
        
    def test_SDL_ISPIXELFORMAT_INDEXED (self):
        self.assertTrue (pixels.SDL_ISPIXELFORMAT_INDEXED (pixels.SDL_PIXELFORMAT_INDEX1LSB))
        self.assertTrue (pixels.SDL_ISPIXELFORMAT_INDEXED (pixels.SDL_PIXELFORMAT_INDEX1MSB))
        self.assertTrue (pixels.SDL_ISPIXELFORMAT_INDEXED (pixels.SDL_PIXELFORMAT_INDEX4LSB))
        self.assertTrue (pixels.SDL_ISPIXELFORMAT_INDEXED (pixels.SDL_PIXELFORMAT_INDEX4MSB))
        self.assertTrue (pixels.SDL_ISPIXELFORMAT_INDEXED (pixels.SDL_PIXELFORMAT_INDEX8))
        self.assertFalse (pixels.SDL_ISPIXELFORMAT_INDEXED (pixels.SDL_PIXELFORMAT_RGB332))
        self.assertFalse (pixels.SDL_ISPIXELFORMAT_INDEXED (pixels.SDL_PIXELFORMAT_ARGB8888))
        self.assertFalse (pixels.SDL_ISPIXELFORMAT_INDEXED (pixels.SDL_PIXELFORMAT_YUY2))
        
    def test_SDL_ISPIXELFORMAT_ALPHA (self):
        self.assertTrue (pixels.SDL_ISPIXELFORMAT_ALPHA (pixels.SDL_PIXELFORMAT_ARGB8888))
        self.assertTrue (pixels.SDL_ISPIXELFORMAT_ALPHA (pixels.SDL_PIXELFORMAT_RGBA8888))
        self.assertTrue (pixels.SDL_ISPIXELFORMAT_ALPHA (pixels.SDL_PIXELFORMAT_RGBA4444))
        self.assertTrue (pixels.SDL_ISPIXELFORMAT_ALPHA (pixels.SDL_PIXELFORMAT_ABGR1555))
        self.assertFalse (pixels.SDL_ISPIXELFORMAT_ALPHA (pixels.SDL_PIXELFORMAT_INDEX1LSB))
        self.assertFalse (pixels.SDL_ISPIXELFORMAT_ALPHA (pixels.SDL_PIXELFORMAT_INDEX4MSB))
        self.assertFalse (pixels.SDL_ISPIXELFORMAT_ALPHA (pixels.SDL_PIXELFORMAT_RGB332))
        self.assertFalse (pixels.SDL_ISPIXELFORMAT_ALPHA (pixels.SDL_PIXELFORMAT_YUY2))
        self.assertFalse (pixels.SDL_ISPIXELFORMAT_ALPHA (pixels.SDL_PIXELFORMAT_RGBX8888))
        
    def test_SDL_ISPIXELFORMAT_FOURCC (self):
        self.assertTrue (pixels.SDL_ISPIXELFORMAT_FOURCC (pixels.SDL_PIXELFORMAT_YV12))
        self.assertTrue (pixels.SDL_ISPIXELFORMAT_FOURCC (pixels.SDL_PIXELFORMAT_IYUV))
        self.assertTrue (pixels.SDL_ISPIXELFORMAT_FOURCC (pixels.SDL_PIXELFORMAT_YUY2))
        self.assertTrue (pixels.SDL_ISPIXELFORMAT_FOURCC (pixels.SDL_PIXELFORMAT_UYVY))
        self.assertTrue (pixels.SDL_ISPIXELFORMAT_FOURCC (pixels.SDL_PIXELFORMAT_YVYU))
        self.assertFalse (pixels.SDL_ISPIXELFORMAT_FOURCC (pixels.SDL_PIXELFORMAT_ARGB8888))
        self.assertFalse (pixels.SDL_ISPIXELFORMAT_FOURCC (pixels.SDL_PIXELFORMAT_ARGB4444))
        self.assertFalse (pixels.SDL_ISPIXELFORMAT_FOURCC (pixels.SDL_PIXELFORMAT_INDEX8))
    
    def test_get_pixel_format_name (self):
        self.assertEqual (pixels.get_pixelformat_name \
            (pixels.SDL_PIXELFORMAT_INDEX1LSB), "SDL_PIXELFORMAT_INDEX1LSB")
        self.assertEqual (pixels.get_pixelformat_name \
            (pixels.SDL_PIXELFORMAT_UNKNOWN), "SDL_PIXELFORMAT_UNKNOWN")
        self.assertEqual (pixels.get_pixelformat_name \
            (pixels.SDL_PIXELFORMAT_UYVY), "SDL_PIXELFORMAT_UYVY")
        self.assertEqual (pixels.get_pixelformat_name \
            (99999), "SDL_PIXELFORMAT_UNKNOWN")

    def test_masks_to_pixelformat_enum (self):
        if sys.byteorder == "little":
            val = pixels.masks_to_pixelformat_enum \
                (32, 0xFF000000, 0x00FF0000, 0x0000FF00, 0x000000FF)
        else:
            val = pixels.masks_to_pixelformat_enum \
                (32, 0x000000FF, 0x0000FF00, 0x00FF0000, 0xFF000000)
        self.assertEqual (val, pixels.SDL_PIXELFORMAT_RGBA8888)
        if sys.byteorder == "little":
            val = pixels.masks_to_pixelformat_enum \
                (32, 0xFF000000, 0x00FF0000, 0x0000FF00, 0)
        else:
            val = pixels.masks_to_pixelformat_enum \
                (32, 0, 0x000000FF, 0x0000FF00, 0x00FF0000)
        self.assertEqual (val, pixels.SDL_PIXELFORMAT_RGBX8888)
        val = pixels.masks_to_pixelformat_enum (1, 0, 0, 0, 0)
        self.assertEqual (val, pixels.SDL_PIXELFORMAT_INDEX1MSB) # not LSB
        val = pixels.masks_to_pixelformat_enum (17, 3, 6, 64, 255)
        self.assertEqual (val, pixels.SDL_PIXELFORMAT_UNKNOWN)
        val = pixels.masks_to_pixelformat_enum (None, None, None, None, None)
        self.assertEqual (val, pixels.SDL_PIXELFORMAT_UNKNOWN)
        
    def test_pixelformat_enum_to_masks (self):
        val = pixels.pixelformat_enum_to_masks \
            (pixels.SDL_PIXELFORMAT_INDEX1LSB)
        self.assertEqual (val, (1, 0, 0, 0, 0))
        val = pixels.pixelformat_enum_to_masks \
            (pixels.SDL_PIXELFORMAT_INDEX1MSB)
        self.assertEqual (val, (1, 0, 0, 0, 0))
        
        val = pixels.pixelformat_enum_to_masks (pixels.SDL_PIXELFORMAT_RGBA8888)
        if sys.byteorder == "little":
            self.assertEqual (val,
                (32, 0xFF000000, 0x00FF0000, 0x0000FF00, 0x000000FF))
        else:
            self.assertEqual (val,
                (32, 0x000000FF, 0x0000FF00, 0x00FF0000, 0xFF000000))
        val = pixels.pixelformat_enum_to_masks (pixels.SDL_PIXELFORMAT_RGBX8888)
        if sys.byteorder == "little":
            self.assertEqual (val, (32, 0xFF000000, 0x00FF0000, 0x0000FF00, 0))
        else:
            self.assertEqual (val, (32, 0, 0x0000FF00, 0x00FF0000, 0xFF000000))
        self.assertRaises (SDLError, pixels.pixelformat_enum_to_masks, 99999)

        val = pixels.pixelformat_enum_to_masks (None)
        self.assertEqual (val, (0, 0, 0, 0, 0))
        val = pixels.pixelformat_enum_to_masks (pixels.SDL_PIXELFORMAT_UNKNOWN)
        self.assertEqual (val, (0, 0, 0, 0, 0))
        
    def test_alloc_free_format (self):
        format = pixels.alloc_format (pixels.SDL_PIXELFORMAT_RGBA8888)
        self.assertIsInstance (format, pixels.SDL_PixelFormat)
        self.assertEqual (format.format, pixels.SDL_PIXELFORMAT_RGBA8888)
        self.assertEqual (format.BitsPerPixel, 32)
        self.assertEqual (format.BytesPerPixel, 4)
        pixels.free_format (format)
        
        format = pixels.alloc_format (pixels.SDL_PIXELFORMAT_INDEX1LSB)
        self.assertIsInstance (format, pixels.SDL_PixelFormat)
        self.assertEqual (format.format, pixels.SDL_PIXELFORMAT_INDEX1LSB)
        self.assertEqual (format.BitsPerPixel, 1)
        self.assertEqual (format.BytesPerPixel, 1)
        pixels.free_format (format)
        
        format = pixels.alloc_format (pixels.SDL_PIXELFORMAT_INDEX4MSB)
        self.assertIsInstance (format, pixels.SDL_PixelFormat)
        self.assertEqual (format.format, pixels.SDL_PIXELFORMAT_INDEX4MSB)
        self.assertEqual (format.BitsPerPixel, 4)
        self.assertEqual (format.BytesPerPixel, 1)
        pixels.free_format (format)

        self.assertRaises (SDLError, pixels.alloc_format,
                           pixels.SDL_PIXELFORMAT_UYVY)
        self.assertRaises (SDLError, pixels.alloc_format,
                           pixels.SDL_PIXELFORMAT_YUY2)

    def test_alloc_free_palette (self):
        self.assertRaises (TypeError, pixels.alloc_palette, None)
        self.assertRaises (TypeError, pixels.alloc_palette, "Test")
        self.assertRaises (ValueError, pixels.alloc_palette, -5)
        
        palette = pixels.alloc_palette (10)
        self.assertIsInstance (palette, pixels.SDL_Palette)
        self.assertEqual (palette.ncolors, 10)
        self.assertEqual (len (palette.colors), 10)
        for x in range (palette.ncolors):
            self.assertIsInstance (palette.colors[x], SDL_Color)
        palette.colors[3].r = 70
        self.assertEqual (palette.colors[3].r, 70)
        color = palette.colors[4]
        self.assertEqual (palette.colors[4].g, 255)
        self.assertEqual (color.g, 255)
        color.g = 33
        self.assertEqual (color.g, 33)
        self.assertEqual (palette.colors[4].g, 33)
        pixels.free_palette (palette)
        
    def test_calculate_gamma_ramp (self):
        self.assertRaises (TypeError, pixels.calculate_gamma_ramp, None)
        self.assertRaises (TypeError, pixels.calculate_gamma_ramp, "Test")
        self.assertRaises (ValueError, pixels.calculate_gamma_ramp, 7)
        self.assertRaises (ValueError, pixels.calculate_gamma_ramp, -0.00002)
        vals = pixels.calculate_gamma_ramp (0)
        self.assertEqual (len (vals), 256)
        for x in vals:
            self.assertEqual (x, 0)
        vals = pixels.calculate_gamma_ramp (1)
        self.assertEqual (len (vals), 256)
        p = 0
        for x in vals:
            self.assertEqual (x, p)
            p += 257
        vals = pixels.calculate_gamma_ramp (0.5)
        self.assertEqual (len (vals), 256)
        p, step = 0, 1
        for x in vals:
            if p == 33124:
                p = 33123 # dubios rounding correction - is this really correct?
            self.assertEqual (x, p)
            p = x + step
            step += 2

    def test_get_rgb (self):
        # TODO: invalid parameters
        format = pixels.alloc_format (pixels.SDL_PIXELFORMAT_RGBA8888)
        self.assertIsInstance (format, pixels.SDL_PixelFormat)
        rgb = pixels.get_rgb (0xFFAA8811, format)
        self.assertEqual (rgb, (0xFF, 0xAA, 0x88))
        rgb = pixels.get_rgb (0x00000000, format)
        self.assertEqual (rgb, (0x00, 0x00, 0x00))
        rgb = pixels.get_rgb (0xFFFFFFFF, format)
        self.assertEqual (rgb, (0xFF, 0xFF, 0xFF))
        rgb = pixels.get_rgb (0x11223344, format)
        self.assertEqual (rgb, (0x11, 0x22, 0x33))
        pixels.free_format (format)
        fmts = (pixels.SDL_PIXELFORMAT_INDEX1LSB,
                pixels.SDL_PIXELFORMAT_INDEX1MSB)
        for fmt in fmts:
            format = pixels.alloc_format (fmt)
            self.assertIsInstance (format, pixels.SDL_PixelFormat)
            rgb = pixels.get_rgb (0x11223344, format)
            self.assertEqual (rgb, (0xFF, 0xFF, 0xFF))
            rgb = pixels.get_rgb (0x00000000, format)
            # TODO: Seems to be always (0xFF, 0xFF, 0xFF) ???
            #self.assertEqual (rgb, (0x00, 0x00, 0x00))
            pixels.free_format (format)
        fmts = (pixels.SDL_PIXELFORMAT_INDEX4LSB,
                pixels.SDL_PIXELFORMAT_INDEX4MSB)
        for fmt in fmts:
            format = pixels.alloc_format (fmt)
            self.assertIsInstance (format, pixels.SDL_PixelFormat)
            # TODO
            pixels.free_format (format)

    def test_get_rgba (self):
        # TODO: invalid parameters
        format = pixels.alloc_format (pixels.SDL_PIXELFORMAT_RGBA8888)
        self.assertIsInstance (format, pixels.SDL_PixelFormat)
        rgba = pixels.get_rgba (0xFFAA8811, format)
        self.assertEqual (rgba, (0xFF, 0xAA, 0x88, 0x11))
        rgba = pixels.get_rgba (0x00000000, format)
        self.assertEqual (rgba, (0x00, 0x00, 0x00, 0x00))
        rgba = pixels.get_rgba (0xFFFFFFFF, format)
        self.assertEqual (rgba, (0xFF, 0xFF, 0xFF, 0xFF))
        rgba = pixels.get_rgba (0x11223344, format)
        self.assertEqual (rgba, (0x11, 0x22, 0x33, 0x44))
        pixels.free_format (format)
        fmts = (pixels.SDL_PIXELFORMAT_INDEX1LSB,
                pixels.SDL_PIXELFORMAT_INDEX1MSB)
        for fmt in fmts:
            format = pixels.alloc_format (fmt)
            self.assertIsInstance (format, pixels.SDL_PixelFormat)
            rgba = pixels.get_rgba (0x11223344, format)
            self.assertEqual (rgba, (0xFF, 0xFF, 0xFF, 0xFF))
            rgba = pixels.get_rgba (0x00000000, format)
            # TODO: Seems to be always (0xFF, 0xFF, 0xFF) ???
            #self.assertEqual (rgb, (0x00, 0x00, 0x00))
            pixels.free_format (format)
        fmts = (pixels.SDL_PIXELFORMAT_INDEX4LSB,
                pixels.SDL_PIXELFORMAT_INDEX4MSB)
        for fmt in fmts:
            format = pixels.alloc_format (fmt)
            self.assertIsInstance (format, pixels.SDL_PixelFormat)
            # TODO
            pixels.free_format (format)
        
    def test_map_rgb (self):
        format = pixels.alloc_format (pixels.SDL_PIXELFORMAT_RGBA8888)
        self.assertIsInstance (format, pixels.SDL_PixelFormat)
        val = pixels.map_rgb (format, 0xFF, 0xAA, 0x88)
        self.assertEqual (val, 0xFFAA88FF)
        
        format = pixels.alloc_format (None)
        self.assertIsInstance (format, pixels.SDL_PixelFormat)
        self.assertEqual (format.format, pixels.SDL_PIXELFORMAT_UNKNOWN)
        val = pixels.map_rgb (format, 0xFF, 0xAA, 0x88)
        self.assertEqual (val, 0x0)
        
        self.assertRaises (SDLError, pixels.alloc_format, "Test")
        self.assertRaises (Exception, pixels.alloc_format, self)
        
    def test_map_rgba (self):
        format = pixels.alloc_format (pixels.SDL_PIXELFORMAT_RGBA8888)
        self.assertIsInstance (format, pixels.SDL_PixelFormat)
        val = pixels.map_rgba (format, 0xFF, 0xAA, 0x88, 0x11)
        self.assertEqual (val, 0xFFAA8811)
        
        format = pixels.alloc_format (None)
        self.assertIsInstance (format, pixels.SDL_PixelFormat)
        self.assertEqual (format.format, pixels.SDL_PIXELFORMAT_UNKNOWN)
        val = pixels.map_rgba (format, 0xFF, 0xAA, 0x88, 0x11)
        self.assertEqual (val, 0x0)

        self.assertRaises (SDLError, pixels.alloc_format, "Test")
        self.assertRaises (Exception, pixels.alloc_format, self)
        
    @unittest.skip("not implemented")
    def test_set_palette_colors (self):
        # TODO
        pass
        
    @unittest.skip("not implemented")
    def test_set_pixelformat_palette (self):
        # TODO
        pass

    @unittest.skip ("not implemented")
    def test_SDL_PixelFormat (self):
        format = pixels.SDL_PixelFormat ()
        self.assertIsInstance (format, pixels.SDL_PixelFormat)

    @unittest.skip ("not implemented")
    def test_SDL_Palette (self):
        palette = pixels.SDL_Palette ()
        self.assertIsInstance (palette, pixels.SDL_Palette)

    def test_SDL_Color (self):
        c1 = SDL_Color ()
        self.assertEqual ((c1.r, c1.g, c1.b), (0xFF, 0xFF, 0xFF))

        c1 = SDL_Color ()
        c2 = SDL_Color ()
        c3 = SDL_Color (0, 127, 255)
        self.assertEqual (c1, c2)
        self.assertNotEqual (c1, c3)

    def test_SDL_Color__repr__ (self):
        c1 = SDL_Color ()
        self.assertEqual ("SDL_Color(r=255, g=255, b=255)", repr(c1))
        c2 = eval (repr (c1))
        self.assertEqual (c2, c1)
        c3 = eval (repr (c2))
        self.assertEqual (c3, c2)
    
    def test_SDL_Color__copy__ (self):
        c = SDL_Color ()
        c2 = copy.copy (c)
        self.assertEqual (c, c2)
        
        c = SDL_Color (10, 20, 30)
        c2 = copy.copy (c)
        self.assertEqual (c, c2)

    def test_SDL_Color__eq__ (self):
        self.assertTrue (SDL_Color(255, 0, 0) == SDL_Color(255, 0, 0))
        self.assertTrue (SDL_Color(0, 255, 0) == SDL_Color(0, 255, 0))
        self.assertTrue (SDL_Color(0, 0, 255) == SDL_Color(0, 0, 255))
        self.assertTrue (SDL_Color(0, 0, 0) == SDL_Color(0, 0, 0))
        
        self.assertFalse (SDL_Color(0, 0, 0) == SDL_Color(255, 0, 0))
        self.assertFalse (SDL_Color(0, 0, 0) == SDL_Color(0, 255, 0))
        self.assertFalse (SDL_Color(0, 0, 0) == SDL_Color(0, 0, 255))
        
    def test_SDL_Color__ne__ (self):
        self.assertTrue (SDL_Color(0, 0, 0) != SDL_Color(255, 0, 0))
        self.assertTrue (SDL_Color(0, 0, 0) != SDL_Color(0, 255, 0))
        self.assertTrue (SDL_Color(0, 0, 0) != SDL_Color(0, 0, 255))
        
        self.assertFalse (SDL_Color(255, 0, 0) != SDL_Color(255, 0, 0))
        self.assertFalse (SDL_Color(0, 255, 0) != SDL_Color(0, 255, 0))
        self.assertFalse (SDL_Color(0, 0, 255) != SDL_Color(0, 0, 255))

    def test_SDL_Color_r (self):
        c1 = SDL_Color ()
        
        def setr (color, val):
            color.r = val
        
        for x in range (0, 255):
            c1.r = x
            self.assertEqual (c1.r, x)
            
        # TODO
        #self.assertRaises (ValueError, setr,  c1, -1)
        #self.assertRaises (ValueError, setr,  c1, 256)
        self.assertRaises (TypeError, setr,  c1, "Test")
        self.assertRaises (TypeError, setr,  c1, None)
    
    def test_SDL_Color_g (self):
        c1 = SDL_Color ()
        
        def setg (color, val):
            color.g = val
        
        for x in range (0, 255):
            c1.g = x
            self.assertEqual (c1.g, x)

        # TODO
        #self.assertRaises (ValueError, setg,  c1, -1)
        #self.assertRaises (ValueError, setg,  c1, 256)
        self.assertRaises (TypeError, setg,  c1, "Test")
        self.assertRaises (TypeError, setg,  c1, None)
    
    def test_SDL_Color_b (self):
        c1 = SDL_Color ()
        
        def setb (color, val):
            color.b = val
        
        for x in range (0, 255):
            c1.b = x
            self.assertEqual (c1.b, x)
            
        # TODO
        #self.assertRaises (ValueError, setb,  c1, -1)
        #self.assertRaises (ValueError, setb,  c1, 256)
        self.assertRaises (TypeError, setb,  c1, "Test")
        self.assertRaises (TypeError, setb,  c1, None)
        
if __name__ == '__main__':
    unittest.main ()
