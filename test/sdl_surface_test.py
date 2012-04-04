import array
import sys
import unittest
import pygame2.sdl as sdl
import pygame2.sdl.surface as surface
from pygame2.sdl.error import SDLError
import pygame2.sdl.rect as rect
import pygame2.sdl.pixels as pixels
import pygame2.sdl.video as video
import pygame2.sdl.array as sdlarray

alldepths = (1, 4, 8, 12, 15, 16, 24, 32)
indexdepths = (1, 4, 8)
rgbdepths = (8, 12, 15, 16)
rgbadepths = (16, 24, 32)

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

    @unittest.skip("not implemented")
    def test_convert_pixels(self):
        pass

    @unittest.skip("not implemented")
    def test_convert_surface(self):
        pass

    @unittest.skip("not implemented")
    def test_convert_surface_format(self):
        pass

    def ttest_create_rgb_surface(self):
        for w in range (1, 100):
            for h in range(1, 100):
                for bpp in alldepths:
                    sf = surface.create_rgb_surface(w, h, bpp)
                    self.assertIsInstance(sf, surface.SDL_Surface)
                    surface.free_surface(sf)

        for fmt in pixels.ALL_PIXELFORMATS:
            if pixels.SDL_ISPIXELFORMAT_FOURCC(fmt):
                continue
            for w in range (1, 100):
                for h in range(1, 100):
                    bpp, rmask, gmask, bmask, amask = \
                        pixels.pixelformat_enum_to_masks(fmt)
                    sf = surface.create_rgb_surface(w, h, bpp, rmask, gmask,
                                                    bmask, amask)
                    self.assertIsInstance(sf, surface.SDL_Surface)
                    surface.free_surface(sf)

        self.assertRaises(SDLError, surface.create_rgb_surface, 1, 1, 66)
        self.assertRaises(SDLError, surface.create_rgb_surface, 1, 1, 0)
        self.assertRaises(SDLError, surface.create_rgb_surface, 1, 1, 8,
                          0xf0, 0x0f, 0x01, 0x02)
        self.assertRaises(SDLError, surface.create_rgb_surface, 1, 1, 16,
                          0xf0, 0x0f, 0x01, 0x02)
        self.assertRaises(SDLError, surface.create_rgb_surface, 1, 1, 24,
                          0xf0, 0x0f, 0x01, 0x02)
        self.assertRaises(SDLError, surface.create_rgb_surface, 1, 1, 32,
                          0xf0, 0x0f, 0x01, 0x02)

    def test_create_rgb_surface_from(self):
        # 16x16 surfaces with 256 values
        pixelations = (([x << 24 for x in range(16 * 16)], 32, 16,
                        (0xFF000000, 0x00FF0000, 0x0000FF00, 0x000000FF)),
                       ([x << 8 for x in range(16 * 16)], 16, 16,
                        (0xF000, 0x0F00, 0x00F0, 0x000F)),
                       ([x for x in range(16 * 16)], 8, 16,
                        (0x0, 0x0, 0x0, 0x0)),
                       )
        for pixels, bpp, pitch, masks in pixelations:
            arflag = "B"
            if bpp == 32:
                arflag = "L"
            elif bpp == 16:
                arflag = "H"
            bytebuf = sdlarray.CTypesView(array.array(arflag, pixels))
            sf = surface.create_rgb_surface_from(bytebuf.to_bytes(), 16, 16,
                                                 bpp, pitch, masks[0],
                                                 masks[1], masks[2], masks[3])
            self.assertIsInstance(sf, surface.SDL_Surface)
            surface.free_surface(sf)


    def ttest_fill_rect(self):
        rectlist = (
            rect.SDL_Rect (0, 0, 0, 0),
            rect.SDL_Rect (0, 0, 10, 10),
            rect.SDL_Rect (0, 0, -10, 10),
            rect.SDL_Rect (0, 0, -10, -10),
            rect.SDL_Rect (-10, -10, 10, 10),
            rect.SDL_Rect (10, -10, 10, 10),
            rect.SDL_Rect (10, 10, 10, 10),
            )

        for fmt in pixels.ALL_PIXELFORMATS:
            if pixels.SDL_ISPIXELFORMAT_FOURCC(fmt):
                continue
            if pixels.SDL_BITSPERPIXEL(fmt) < 8:
                continue  # Skip < 8bpp, SDL_FillRect does not work on those
            for w in range (1, 60):
                for h in range(1, 60):
                    bpp, rmask, gmask, bmask, amask = \
                        pixels.pixelformat_enum_to_masks(fmt)
                    sf = surface.create_rgb_surface(w, h, bpp, rmask, gmask,
                                                    bmask, amask)
                    self.assertIsInstance(sf, surface.SDL_Surface)
                    for r in rectlist:
                        # TODO: check for changed pixels
                        surface.fill_rect(sf, r, 0xff00ff00)
                    surface.free_surface(sf)

    def ttest_fill_rects(self):
        rectlist = (
            rect.SDL_Rect (0, 0, 0, 0),
            rect.SDL_Rect (0, 0, 10, 10),
            rect.SDL_Rect (0, 0, -10, 10),
            rect.SDL_Rect (0, 0, -10, -10),
            rect.SDL_Rect (-10, -10, 10, 10),
            rect.SDL_Rect (10, -10, 10, 10),
            rect.SDL_Rect (10, 10, 10, 10),
            )

        for fmt in pixels.ALL_PIXELFORMATS:
            if pixels.SDL_ISPIXELFORMAT_FOURCC(fmt):
                continue
            if pixels.SDL_BITSPERPIXEL(fmt) < 8:
                continue  # Skip < 8bpp, SDL_FillRect does not work on those
            for w in range (1, 60):
                for h in range(1, 60):
                    bpp, rmask, gmask, bmask, amask = \
                        pixels.pixelformat_enum_to_masks(fmt)
                    sf = surface.create_rgb_surface(w, h, bpp, rmask, gmask,
                                                    bmask, amask)
                    self.assertIsInstance(sf, surface.SDL_Surface)
                    # TODO: check for changed pixels
                    surface.fill_rects(sf, rectlist, 0xff00ff00)
                    surface.free_surface(sf)

    def test_free_surface(self):
        self.assertRaises(TypeError, surface.free_surface, None)
        self.assertRaises(TypeError, surface.free_surface, "Test")
        self.assertRaises(TypeError, surface.free_surface, 5)

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
        rectlist = (
            (rect.SDL_Rect (0, 0, 0, 0), False, False),
            (rect.SDL_Rect (2, 2, 0, 0), False, False),
            (rect.SDL_Rect (2, 2, 5, 1), True, True),
            (rect.SDL_Rect (6, 5, 10, 3), True, False),
            (rect.SDL_Rect (0, 0, 10, 10), True, True),
            (rect.SDL_Rect (0, 0, -10, 10), False, False),
            (rect.SDL_Rect (0, 0, -10, -10), False, False),
            (rect.SDL_Rect (-10, -10, 10, 10), False, False),
            (rect.SDL_Rect (10, -10, 10, 10), False, False),
            (rect.SDL_Rect (10, 10, 10, 10), True, False)
            )

        sf = surface.create_rgb_surface(15, 15, 32)
        clip = surface.get_clip_rect(sf)
        self.assertIsInstance(clip, rect.SDL_Rect)
        self.assertEqual (clip, rect.SDL_Rect(0, 0, 15, 15))

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
                    "Could not set color key (%d, %d, %d)" %(r, g, b))
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

    @unittest.skip("not implemented")
    def test_lock_unlock_surface(self):
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
    
    @unittest.skip("not implemented")
    def test_SDL_MUSTLOCK(self):
        pass

    @unittest.skip("not implemented")
    def test_lower_blit(self):
        pass

    @unittest.skip("not implemented")
    def test_lower_blit_scaled(self):
        pass

    @unittest.skip("not implemented")
    def test_upper_blit(self):
        pass

    @unittest.skip("not implemented")
    def test_blit_surface(self):
        pass

    @unittest.skip("not implemented")
    def test_upper_blit_scaled(self):
        pass

    @unittest.skip("not implemented")
    def test_soft_stretch(self):
        pass

    @unittest.skip("not implemented")
    def test_set_surface_palette(self):
        pass

    @unittest.skip("not implemented")
    def test_set_surface_rle(self):
        pass

if __name__ == '__main__':
    unittest.main()
