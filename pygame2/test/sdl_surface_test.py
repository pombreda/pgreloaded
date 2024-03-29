import os
import sys
import array
import unittest
import ctypes
from pygame2.resources import Resources
import pygame2.sdl as sdl
import pygame2.sdl.surface as surface
import pygame2.sdl.rect as rect
import pygame2.sdl.rwops as rwops
import pygame2.sdl.pixels as pixels
import pygame2.sdl.video as video
import pygame2.array as pgarray
from pygame2.video import PixelView

RESOURCES = Resources(__file__, "resources")

alldepths = (1, 4, 8, 12, 15, 16, 24, 32)
indexdepths = (1, 4, 8)
rgbdepths = (8, 12, 15, 16)
rgbadepths = (16, 24, 32)

rgba_pixelations_16x16 = (
    # 32-bit 16x16 RGBA surface
    ([x << 24 for x in range(16 * 16)], 32, 16,
     (0xFF000000, 0x00FF0000, 0x0000FF00, 0x000000FF),
     pixels.SDL_PIXELFORMAT_RGBA8888),
    # 16-bit 16x16 RGBA surface
    ([x << 8 for x in range(16 * 16)], 16, 16,
     (0xF000, 0x0F00, 0x00F0, 0x000F),
     pixels.SDL_PIXELFORMAT_RGB444),
    )

blitsizes = ((2, 2), (5, 5), (10, 10), (20, 20),
             (2, 4), (5, 3), (8, 12), (27, 9),
             )

blitpositions = (
    rect.SDL_Rect(0, 0),
    rect.SDL_Rect(4, 4),
    rect.SDL_Rect(10, 10),
    rect.SDL_Rect(15, 15),
    rect.SDL_Rect(-2, 1),
    rect.SDL_Rect(3, -4),
    rect.SDL_Rect(0, 3),
    rect.SDL_Rect(4, 0),
    rect.SDL_Rect(12, 6),
    rect.SDL_Rect(13, 22),
    )


# TODO: mostly covers positive tests right now - fix this!
class SDLSurfaceTest(unittest.TestCase):
    __tags__ = ["sdl"]

    def setUp(self):
        if sys.version.startswith("3.1"):
            self.assertIsInstance = \
                lambda x, t: self.assertTrue(isinstance(x, t))
        sdl.init(sdl.SDL_INIT_EVERYTHING)

    def tearDown(self):
        sdl.quit()

    def test_SDL_Surface(self):
        sf = surface.SDL_Surface()
        self.assertIsInstance(sf, surface.SDL_Surface)
        # TODO: property checks

    def test_convert_pixels(self):
        for buf, bpp, pitch, masks, fmt in rgba_pixelations_16x16:
            bytecount = bpp // 8
            arflag = None
            if bpp == 32:
                arflag = "I"
            elif bpp == 16:
                arflag = "H"
            src = pgarray.CTypesView(array.array(arflag, buf), bytecount)
            dst = surface.convert_pixels(16, 16, fmt, src, 16 * bytecount,
                                         fmt, 16 * bytecount)
            for index, val in enumerate(dst):
                self.assertEqual(val, src.view[index])

    def test_convert_surface(self):
        pfmt = pixels.alloc_format(pixels.SDL_PIXELFORMAT_RGB444)
        for fmt in pixels.ALL_PIXELFORMATS:
            if pixels.SDL_ISPIXELFORMAT_FOURCC(fmt):
                continue
            if fmt in (pixels.SDL_PIXELFORMAT_RGB332,
                       pixels.SDL_PIXELFORMAT_ARGB2101010):
                # SDL2 segfault in the DUFFS_LOOOP() macros
                # http://bugzilla.libsdl.org/show_bug.cgi?id=1534
                continue
            bpp, rmask, gmask, bmask, amask = \
                pixels.pixelformat_enum_to_masks(fmt)
            sf = surface.create_rgb_surface(10, 20, bpp, rmask, gmask,
                                            bmask, amask)
            self.assertIsInstance(sf, surface.SDL_Surface)
            csf = surface.convert_surface(sf, pfmt, 0)
            self.assertIsInstance(csf, surface.SDL_Surface)
            surface.free_surface(sf)
            surface.free_surface(csf)

        sf = surface.create_rgb_surface(10, 10, 32, 0, 0, 0)
        self.assertRaises((AttributeError, TypeError),
                          surface.convert_surface, None, None, None)
        self.assertRaises((AttributeError, TypeError),
                          surface.convert_surface, sf, None, None)
        self.assertRaises((AttributeError, TypeError),
                          surface.convert_surface, sf, "Test", 0)
        self.assertRaises((AttributeError, TypeError),
                          surface.convert_surface, sf, 12345, 0)
        self.assertRaises((AttributeError, TypeError),
                          surface.convert_surface, None, pfmt, 0)
        self.assertRaises((AttributeError, TypeError),
                          surface.convert_surface, "Test", pfmt, 0)
        self.assertRaises((AttributeError, TypeError),
                          surface.convert_surface, 12345, pfmt, 0)
        pixels.free_format(pfmt)
        surface.free_surface(sf)

    def test_convert_surface_format(self):
        pfmt = pixels.SDL_PIXELFORMAT_RGB444
        for fmt in pixels.ALL_PIXELFORMATS:
            if pixels.SDL_ISPIXELFORMAT_FOURCC(fmt):
                continue
            if fmt in (pixels.SDL_PIXELFORMAT_RGB332,
                       pixels.SDL_PIXELFORMAT_ARGB2101010):
                # SDL2 segault in the DUFFS_LOOP() macros
                # http://bugzilla.libsdl.org/show_bug.cgi?id=1534
                continue
            bpp, rmask, gmask, bmask, amask = \
                pixels.pixelformat_enum_to_masks(fmt)
            sf = surface.create_rgb_surface(10, 20, bpp, rmask, gmask,
                                            bmask, amask)
            self.assertIsInstance(sf, surface.SDL_Surface)
            csf = surface.convert_surface_format(sf, pfmt, 0)
            self.assertIsInstance(csf, surface.SDL_Surface)
            surface.free_surface(sf)
            surface.free_surface(csf)

    def test_create_rgb_surface(self):
        for w in range(1, 100, 5):
            for h in range(1, 100, 5):
                for bpp in alldepths:
                    sf = surface.create_rgb_surface(w, h, bpp)
                    self.assertIsInstance(sf, surface.SDL_Surface)
                    surface.free_surface(sf)

        for fmt in pixels.ALL_PIXELFORMATS:
            if pixels.SDL_ISPIXELFORMAT_FOURCC(fmt):
                continue
            for w in range(1, 100, 5):
                for h in range(1, 100, 5):
                    bpp, rmask, gmask, bmask, amask = \
                        pixels.pixelformat_enum_to_masks(fmt)
                    sf = surface.create_rgb_surface(w, h, bpp, rmask, gmask,
                                                    bmask, amask)
                    self.assertIsInstance(sf, surface.SDL_Surface)
                    surface.free_surface(sf)

        # Broken ones
        # sizes = [(0, 0), (65536, 65536)]
        # for (w, h) in sizes:
        #    for bpp in alldepths:
        #        print w, h, bpp
        #        sf = surface.create_rgb_surface(w, h, bpp)
        #        self.assertIsInstance(sf, surface.SDL_Surface)
        #        surface.free_surface(sf)
        
        # TODO: raises a SDL Out of memory error, but 65536 works?!
        #
        # sf = surface.create_rgb_surface(65535, 65535, 32)
        # self.assertIsInstance(sf, surface.SDL_Surface)
        
        self.assertRaises(sdl.SDLError, surface.create_rgb_surface, 1, 1, 66)
        self.assertRaises(sdl.SDLError, surface.create_rgb_surface, 1, 1, 0)
        self.assertRaises(sdl.SDLError, surface.create_rgb_surface, 1, 1, 8,
                          0xf0, 0x0f, 0x01, 0x02)
        self.assertRaises(sdl.SDLError, surface.create_rgb_surface, 1, 1, 16,
                          0xf0, 0x0f, 0x01, 0x02)
        self.assertRaises(sdl.SDLError, surface.create_rgb_surface, 1, 1, 24,
                          0xf0, 0x0f, 0x01, 0x02)
        self.assertRaises(sdl.SDLError, surface.create_rgb_surface, 1, 1, 32,
                          0xf0, 0x0f, 0x01, 0x02)

    def test_create_rgb_surface_from(self):
        for buf, bpp, pitch, masks, fmt in rgba_pixelations_16x16:
            arflag = None
            if bpp == 32:
                arflag = "I"
            elif bpp == 16:
                arflag = "H"
            bytebuf = pgarray.CTypesView(array.array(arflag, buf))
            sf = surface.create_rgb_surface_from(bytebuf.to_bytes(), 16, 16,
                                                 bpp, pitch, masks[0],
                                                 masks[1], masks[2], masks[3])
            self.assertIsInstance(sf, surface.SDL_Surface)
            surface.free_surface(sf)

    def test_fill_rect(self):
        rectlist = (rect.SDL_Rect(0, 0, 0, 0),
                    rect.SDL_Rect(0, 0, 10, 10),
                    rect.SDL_Rect(0, 0, -10, 10),
                    rect.SDL_Rect(0, 0, -10, -10),
                    rect.SDL_Rect(-10, -10, 10, 10),
                    rect.SDL_Rect(10, -10, 10, 10),
                    rect.SDL_Rect(10, 10, 10, 10),
                    )

        for fmt in pixels.ALL_PIXELFORMATS:
            if pixels.SDL_ISPIXELFORMAT_FOURCC(fmt):
                continue
            if pixels.SDL_BITSPERPIXEL(fmt) < 8:
                continue  # Skip < 8bpp, SDL_FillRect does not work on those
            for w in range(1, 100, 5):
                for h in range(1, 100, 5):
                    bpp, rmask, gmask, bmask, amask = \
                        pixels.pixelformat_enum_to_masks(fmt)
                    sf = surface.create_rgb_surface(w, h, bpp, rmask, gmask,
                                                    bmask, amask)
                    self.assertIsInstance(sf, surface.SDL_Surface)
                    for r in rectlist:
                        # TODO: check for changed pixels
                        surface.fill_rect(sf, r, 0xff00ff00)
                    surface.free_surface(sf)

    def test_fill_rects(self):
        rectlist = (rect.SDL_Rect(0, 0, 0, 0),
                    rect.SDL_Rect(0, 0, 10, 10),
                    rect.SDL_Rect(0, 0, -10, 10),
                    rect.SDL_Rect(0, 0, -10, -10),
                    rect.SDL_Rect(-10, -10, 10, 10),
                    rect.SDL_Rect(10, -10, 10, 10),
                    rect.SDL_Rect(10, 10, 10, 10),
                    )

        for fmt in pixels.ALL_PIXELFORMATS:
            if pixels.SDL_ISPIXELFORMAT_FOURCC(fmt):
                continue
            if pixels.SDL_BITSPERPIXEL(fmt) < 8:
                continue  # Skip < 8bpp, SDL_FillRect does not work on those
            for w in range(1, 100, 5):
                for h in range(1, 100, 5):
                    bpp, rmask, gmask, bmask, amask = \
                        pixels.pixelformat_enum_to_masks(fmt)
                    sf = surface.create_rgb_surface(w, h, bpp, rmask, gmask,
                                                    bmask, amask)
                    self.assertIsInstance(sf, surface.SDL_Surface)
                    # TODO: check for changed pixels
                    surface.fill_rects(sf, rectlist, 0xff00ff00)
                    surface.free_surface(sf)

    def test_free_surface(self):
        self.assertRaises((AttributeError, TypeError),
                          surface.free_surface, None)
        self.assertRaises((AttributeError, TypeError),
                          surface.free_surface, "Test")
        self.assertRaises((AttributeError, TypeError),
                          surface.free_surface, 5)

        formats = (pixels.SDL_PIXELFORMAT_INDEX1LSB,
                   pixels.SDL_PIXELFORMAT_RGB332,
                   pixels.SDL_PIXELFORMAT_RGBA4444,
                   pixels.SDL_PIXELFORMAT_BGR888,
                   pixels.SDL_PIXELFORMAT_ARGB8888,
                   pixels.SDL_PIXELFORMAT_ARGB2101010
                   )
        for fmt in formats:
            bpp, rmask, gmask, bmask, amask = \
                pixels.pixelformat_enum_to_masks(fmt)
            sf = surface.create_rgb_surface(5, 5, bpp, rmask, gmask, bmask,
                                            amask)
            surface.free_surface(sf)

    def test_get_set_clip_rect(self):
        rectlist = ((rect.SDL_Rect(0, 0, 0, 0), False, False),
                    (rect.SDL_Rect(2, 2, 0, 0), False, False),
                    (rect.SDL_Rect(2, 2, 5, 1), True, True),
                    (rect.SDL_Rect(6, 5, 10, 3), True, False),
                    (rect.SDL_Rect(0, 0, 10, 10), True, True),
                    (rect.SDL_Rect(0, 0, -10, 10), False, False),
                    (rect.SDL_Rect(0, 0, -10, -10), False, False),
                    (rect.SDL_Rect(-10, -10, 10, 10), False, False),
                    (rect.SDL_Rect(10, -10, 10, 10), False, False),
                    (rect.SDL_Rect(10, 10, 10, 10), True, False)
                    )

        sf = surface.create_rgb_surface(15, 15, 32)
        clip = surface.get_clip_rect(sf)
        self.assertIsInstance(clip, rect.SDL_Rect)
        self.assertEqual(clip, rect.SDL_Rect(0, 0, 15, 15))

        for r, clipsetval, cmpval in rectlist:
            retval = surface.set_clip_rect(sf, r)
            clip = surface.get_clip_rect(sf)
            self.assertEqual(retval, clipsetval,
                "Could not set clip rect %s" % r)
            self.assertEqual(clip == r, cmpval,
                "Could not set clip rect %s" % r)
        surface.free_surface(sf)

    def test_get_set_color_key(self):
        colorkeys = ((0, 0, 0),
                     (32, 64, 128),
                     (10, 20, 30),
                     (1, 2, 4),
                     (255, 255, 255),
                     (128, 128, 128),
                     (127, 127, 127),
                     )
        for fmt in pixels.ALL_PIXELFORMATS:
            if pixels.SDL_ISPIXELFORMAT_FOURCC(fmt):
                continue
            pformat = pixels.alloc_format(fmt)
            bpp, rmask, gmask, bmask, amask = \
                pixels.pixelformat_enum_to_masks(fmt)
            sf = surface.create_rgb_surface(10, 10, bpp, rmask, gmask, bmask,
                                            amask)
            for r, g, b in colorkeys:
                key = pixels.map_rgb(pformat, r, g, b)
                surface.set_color_key(sf, 1, key)
                skey = surface.get_color_key(sf)
                self.assertEqual(skey, key,
                    "Could not set color key (%d, %d, %d)" % (r, g, b))
            pixels.free_format(pformat)
            surface.free_surface(sf)

    def test_get_set_surface_alpha_mod(self):
        for fmt in pixels.ALL_PIXELFORMATS:
            if pixels.SDL_ISPIXELFORMAT_FOURCC(fmt):
                continue
            bpp, rmask, gmask, bmask, amask = \
                pixels.pixelformat_enum_to_masks(fmt)
            sf = surface.create_rgb_surface(10, 10, bpp, rmask, gmask, bmask,
                                            amask)
            salpha = surface.get_surface_alpha_mod(sf)
            self.assertEqual(salpha, 255)
            for alpha in range(0, 255):
                surface.set_surface_alpha_mod(sf, alpha)
                salpha = surface.get_surface_alpha_mod(sf)
                self.assertEqual(salpha, alpha)
            surface.free_surface(sf)

    def test_get_set_surface_blend_mode(self):
        modes = (video.SDL_BLENDMODE_NONE,
                 video.SDL_BLENDMODE_BLEND,
                 video.SDL_BLENDMODE_ADD,
                 video.SDL_BLENDMODE_MOD
                 )
        for fmt in pixels.ALL_PIXELFORMATS:
            if pixels.SDL_ISPIXELFORMAT_FOURCC(fmt):
                continue
            bpp, rmask, gmask, bmask, amask = \
                pixels.pixelformat_enum_to_masks(fmt)
            sf = surface.create_rgb_surface(10, 10, bpp, rmask, gmask, bmask,
                                            amask)
            for mode in modes:
                surface.set_surface_blend_mode(sf, mode)
                smode = surface.get_surface_blend_mode(sf)
                self.assertEqual(smode, mode)
            surface.free_surface(sf)

    def test_get_set_surface_color_mod(self):
        colormods = ((0, 0, 0),
                     (32, 64, 128),
                     (10, 20, 30),
                     (1, 2, 4),
                     (255, 255, 255),
                     (128, 128, 128),
                     (127, 127, 127),
                     )
        for fmt in pixels.ALL_PIXELFORMATS:
            if pixels.SDL_ISPIXELFORMAT_FOURCC(fmt):
                continue
            bpp, rmask, gmask, bmask, amask = \
                pixels.pixelformat_enum_to_masks(fmt)
            sf = surface.create_rgb_surface(10, 10, bpp, rmask, gmask, bmask,
                                            amask)
            for r, g, b in colormods:
                surface.set_surface_color_mod(sf, r, g, b)
                sr, sg, sb = surface.get_surface_color_mod(sf)
                self.assertEqual((sr, sg, sb), (r, g, b))
            surface.free_surface(sf)

    def test_lock_unlock_MUSTLOCK_surface(self):
        colormods = ((0, 0, 0),
                     (32, 64, 128),
                     (10, 20, 30),
                     (1, 2, 4),
                     (255, 255, 255),
                     (128, 128, 128),
                     (127, 127, 127),
                     )
        for fmt in pixels.ALL_PIXELFORMATS:
            if pixels.SDL_ISPIXELFORMAT_FOURCC(fmt):
                continue
            bpp, rmask, gmask, bmask, amask = \
                pixels.pixelformat_enum_to_masks(fmt)
            sf = surface.create_rgb_surface(10, 10, bpp, rmask, gmask, bmask,
                                            amask)
            # TODO: locking seems to be only necessary for RLE surfaces...
            if surface.SDL_MUSTLOCK(sf):
                self.assertFalse(sf.locked)
                surface.lock_surface(sf)
                self.assertTrue(sf.locked)
                surface.lock_surface(sf)
                self.assertTrue(sf.locked)
                surface.lock_surface(sf)
                self.assertTrue(sf.locked)
                surface.unlock_surface(sf)
                self.assertTrue(sf.locked)
                surface.unlock_surface(sf)
                self.assertTrue(sf.locked)
                surface.unlock_surface(sf)
                self.assertFalse(sf.locked)
            surface.free_surface(sf)

    def test_lower_blit(self):
        bpp = 32
        w, h = 10, 10
        # no alpha to prevent blending
        masks = (0xFF000000, 0x00FF0000, 0x0000FF00, 0x00000000)
        dest = surface.create_rgb_surface(w, h, bpp, masks[0], masks[1],
                                          masks[2], masks[3])
        pixelsize = h * dest.pitch
        rowlen = dest.pitch // 4

        sources = []
        for width, height in blitsizes:
            src = surface.create_rgb_surface(width, height, bpp, masks[0],
                                             masks[1], masks[2], masks[3])
            surface.fill_rect(src, None, 0xFFFFFFFF)  # fill with white
            sources.append(src)

        for src in sources:
            for pos in blitpositions:
                drect = pos.__copy__()
                surface.fill_rect(dest, None, 0x0)  # fill with black
                surface.lower_blit(src, src.clip_rect, dest, drect)
                buf = ctypes.cast(dest.pixels,
                                  ctypes.POINTER(ctypes.c_ubyte * pixelsize))
                pbuf = pgarray.CTypesView(buf.contents, itemsize=1,
                                          objsize=pixelsize)
                iview = pbuf.to_uint32()
                pw = drect.x + drect.w
                ph = drect.y + drect.h
                for y in range(dest.size[1]):
                    for x in range(dest.size[0]):
                        col = iview[y * rowlen + x]
                        if y >= drect.y and y < ph and \
                                x >= drect.x and x < pw:
                            self.assertEqual(col, 0xFFFFFFFF, msg="""color
mismatch at %d,%d for %s: %d != %d""" % (y, x, pos, col, 0xFFFFFFFF))
                        else:
                            self.assertEqual(col, 0x0, msg="""color mismatch
at %d,%d for %s: %d != %d""" % (y, x, pos, col, 0x0))

        while len(sources) > 0:
            sf = sources.pop()
            surface.free_surface(sf)
        surface.free_surface(dest)

    @unittest.skip("not implemented")
    def test_lower_blit_scaled(self):
        pass

    def test_upper_blit(self):
        bpp = 32
        w, h = 10, 10
        # no alpha to prevent blending
        masks = (0xFF000000, 0x00FF0000, 0x0000FF00, 0x00000000)
        dest = surface.create_rgb_surface(w, h, bpp, masks[0], masks[1],
                                          masks[2], masks[3])
        pixelsize = h * dest.pitch
        rowlen = dest.pitch // 4

        sources = []
        for width, height in blitsizes:
            src = surface.create_rgb_surface(width, height, bpp, masks[0],
                                             masks[1], masks[2], masks[3])
            surface.fill_rect(src, None, 0xFFFFFFFF)  # fill with white
            sources.append(src)

        for src in sources:
            for pos in blitpositions:
                drect = pos.__copy__()
                surface.fill_rect(dest, None, 0x0)  # fill with black
                surface.upper_blit(src, None, dest, drect)
                buf = ctypes.cast(dest.pixels,
                                  ctypes.POINTER(ctypes.c_ubyte * pixelsize))
                pbuf = pgarray.CTypesView(buf.contents, itemsize=1,
                                          objsize=pixelsize)
                iview = pbuf.to_uint32()
                pw = drect.x + drect.w
                ph = drect.y + drect.h
                for y in range(dest.size[1]):
                    for x in range(dest.size[0]):
                        col = iview[y * rowlen + x]
                        if y >= drect.y and y < ph and \
                                x >= drect.x and x < pw:
                            self.assertEqual(col, 0xFFFFFFFF, msg="""color
mismatch at %d,%d for %s: %d != %d""" % (x, y, pos, col, 0xFFFFFFFF))
                        else:
                            self.assertEqual(col, 0x0, msg="""color mismatch
at %d,%d for %s: %d != %d""" % (x, y, pos, col, 0x0))

        while len(sources) > 0:
            sf = sources.pop()
            surface.free_surface(sf)
        surface.free_surface(dest)

    def test_blit_surface(self):
        bpp = 32
        w, h = 10, 10
        # no alpha to prevent blending
        masks = (0xFF000000, 0x00FF0000, 0x0000FF00, 0x00000000)
        dest = surface.create_rgb_surface(w, h, bpp, masks[0], masks[1],
                                          masks[2], masks[3])
        pixelsize = h * dest.pitch
        rowlen = dest.pitch // 4

        sources = []
        for width, height in blitsizes:
            src = surface.create_rgb_surface(width, height, bpp, masks[0],
                                             masks[1], masks[2], masks[3])
            surface.fill_rect(src, None, 0xFFFFFFFF)  # fill with white
            sources.append(src)

        for src in sources:
            for pos in blitpositions:
                drect = pos.__copy__()
                surface.fill_rect(dest, None, 0x0)  # fill with black
                surface.blit_surface(src, None, dest, drect)
                buf = ctypes.cast(dest.pixels,
                                  ctypes.POINTER(ctypes.c_ubyte * pixelsize))
                pbuf = pgarray.CTypesView(buf.contents, itemsize=1,
                                          objsize=pixelsize)
                iview = pbuf.to_uint32()
                pw = drect.x + drect.w
                ph = drect.y + drect.h
                for y in range(dest.size[1]):
                    for x in range(dest.size[0]):
                        col = iview[y * rowlen + x]
                        if y >= drect.y and y < ph and \
                                x >= drect.x and x < pw:
                            self.assertEqual(col, 0xFFFFFFFF, msg="""color
mismatch at %d,%d for %s: %d != %d""" % (y, x, pos, col, 0xFFFFFFFF))
                        else:
                            self.assertEqual(col, 0x0, msg="""color mismatch
at %d,%d for %s: %d != %d""" % (y, x, pos, col, 0x0))

        while len(sources) > 0:
            sf = sources.pop()
            surface.free_surface(sf)
        surface.free_surface(dest)

    @unittest.skip("not implemented")
    def test_upper_blit_scaled(self):
        pass

    @unittest.skip("not implemented")
    def test_soft_stretch(self):
        pass

    def test_set_surface_palette(self):
        invpalette = pixels.alloc_palette(10)
        palette = pixels.alloc_palette(1 << 16)
        sf = surface.create_rgb_surface(10, 10, 16)

        self.assertRaises((AttributeError, TypeError),
                          surface.set_surface_palette, None, None)
        self.assertRaises((AttributeError, TypeError),
                          surface.set_surface_palette, None, palette)
        self.assertIsNone(sf.format.palette)
        surface.set_surface_palette(sf, palette)
        self.assertIsNotNone(sf.format.palette)
        self.assertRaises(sdl.SDLError, surface.set_surface_palette, sf,
                          invpalette)
        self.assertIsNotNone(sf.format.palette)
        surface.set_surface_palette(sf, None)
        self.assertIsNone(sf.format.palette)

        surface.free_surface(sf)
        pixels.free_palette(invpalette)
        pixels.free_palette(palette)

    @unittest.skip("not implemented")
    def test_set_surface_rle(self):
        pass

    def test_load_bmp_rw(self):
        imgfile = RESOURCES.get("surfacetest.bmp")
        imgrw = rwops.rw_from_object(imgfile)
        imgsurface = surface.load_bmp_rw(imgrw, False)
        self.assertIsInstance(imgsurface, surface.SDL_Surface)
        surface.free_surface(imgsurface)

        self.assertRaises(TypeError, surface.load_bmp_rw, "Test")
        self.assertRaises(TypeError, surface.load_bmp_rw, None)
        self.assertRaises(TypeError, surface.load_bmp_rw, 1234)

    def test_load_bmp(self):
        fpath = os.path.join(os.path.dirname(__file__), "resources")
        imgpath = os.path.join(fpath, "surfacetest.bmp")
        imgsurface = surface.load_bmp(imgpath)
        self.assertIsInstance(imgsurface, surface.SDL_Surface)
        surface.free_surface(imgsurface)

        self.assertRaises(sdl.SDLError, surface.load_bmp, "invalid path")
        self.assertRaises(sdl.SDLError, surface.load_bmp, None)
        self.assertRaises(sdl.SDLError, surface.load_bmp, 1234)

    @unittest.skip("not implemented")
    def test_save_bmp_rw(self):
        pass

    @unittest.skip("not implemented")
    def test_save_bmp(self):
        pass

if __name__ == '__main__':
    sys.exit(unittest.main())
