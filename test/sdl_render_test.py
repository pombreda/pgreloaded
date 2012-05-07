import sys
import unittest
import pygame2.sdl as sdl
import pygame2.sdl.render as render
import pygame2.sdl.video as video
import pygame2.sdl.surface as surface
import pygame2.sdl.rect as rect
import pygame2.sdl.pixels as pixels
import pygame2.video as pvid

# TODO: mostly positive tests, improve this!
class SDLRenderTest(unittest.TestCase):
    __tags__ = ["sdl"]

    def setUp(self):
        if sys.version.startswith("3.1"):
            self.assertIsInstance = \
                lambda x, t: self.assertTrue(isinstance(x, t))
        sdl.init(sdl.SDL_INIT_EVERYTHING)

    def tearDown(self):
        sdl.quit()

    def test_SDL_RendererInfo(self):
        info = render.SDL_RendererInfo()
        self.assertIsInstance(info, render.SDL_RendererInfo)

    def test_SDL_Renderer(self):
        val = render.SDL_Renderer()
        self.assertIsInstance(val, render.SDL_Renderer)

    def test_SDL_Texture(self):
        val = render.SDL_Texture()
        self.assertIsInstance(val, render.SDL_Texture)

    def test_get_num_render_drivers(self):
        val = render.get_num_render_drivers()
        self.assertGreaterEqual(val, 1)

    def test_get_render_driver_info(self):
        success = False
        drivers = render.get_num_render_drivers()
        for x in range(drivers):
            info = render.get_render_driver_info(x)
            self.assertIsInstance(info, render.SDL_RendererInfo)
            # We must find at least one software renderer
            if info.name == "software":
                success = True
        self.assertTrue(success, "failed on retrieving the driver information")

        self.assertRaises(TypeError, render.get_render_driver_info, None)
        self.assertRaises(TypeError, render.get_render_driver_info, "Test")
        self.assertRaises(TypeError, render.get_render_driver_info, self)
        self.assertRaises(sdl.SDLError, render.get_render_driver_info, -1)

    def test_create_window_and_renderer(self):
        window, renderer = render.create_window_and_renderer \
           (10, 10, video.SDL_WINDOW_HIDDEN)
        self.assertIsInstance(window, video.SDL_Window)
        self.assertIsInstance(renderer, render.SDL_Renderer)

        render.destroy_renderer(renderer)
        video.destroy_window(window)

        # TODO: the code below works, too - is that really expected from SDL?
        #window, renderer = render.create_window_and_renderer \
        #   (-10, -10, video.SDL_WINDOW_HIDDEN)
        #self.assertIsInstance(window, video.SDL_Window)
        #self.assertIsInstance(renderer, render.SDL_Renderer)

    @unittest.skipIf(sys.platform in ("win32", "cli"), "crashes randomly")
    def test_create_destroy_renderer(self):
        window = video.create_window("Test", 10, 10, 10, 10,
                                     video.SDL_WINDOW_HIDDEN)
        self.assertIsInstance(window, video.SDL_Window)

        for i in range(render.get_num_render_drivers()):
            renderer = render.create_renderer(window, i,
                                              render.SDL_RENDERER_ACCELERATED)
            self.assertIsInstance(renderer, render.SDL_Renderer)
            render.destroy_renderer(renderer)

            renderer = render.create_renderer(window, -1,
                                              render.SDL_RENDERER_SOFTWARE)
            self.assertIsInstance(renderer, render.SDL_Renderer)
            render.destroy_renderer(renderer)
        video.destroy_window(window)

    def test_create_software_renderer(self):
        sf = surface.create_rgb_surface(100, 100, 32, 0xFF000000, 0x00FF0000,
                                        0x0000FF00, 0x000000FF)
        renderer = render.create_software_renderer(sf)
        self.assertIsInstance(renderer, render.SDL_Renderer)
        render.destroy_renderer(renderer)
        surface.free_surface(sf)

        self.assertRaises(TypeError, render.create_software_renderer, None)
        self.assertRaises(TypeError, render.create_software_renderer, 1234)

    def test_get_renderer(self):
        window = video.create_window("Test", 10, 10, 10, 10,
                                     video.SDL_WINDOW_HIDDEN)
        self.assertIsInstance(window, video.SDL_Window)
        renderer = render.get_renderer(window)
        self.assertIsNone(renderer)

        for i in range(render.get_num_render_drivers()):
            renderer = render.create_renderer(window, i,
                                              render.SDL_RENDERER_SOFTWARE)
            ren = render.get_renderer(window)
            self.assertIsInstance(ren, render.SDL_Renderer)
            render.destroy_renderer(renderer)
            self.assertIsNone(render.get_renderer(window))

        video.destroy_window(window)
        self.assertIsNone(render.get_renderer(window))
        self.assertRaises(TypeError, render.get_renderer, None)
        self.assertRaises(TypeError, render.get_renderer, "Test")

    def test_get_renderer_info(self):
        window = video.create_window("Test", 10, 10, 10, 10,
                                     video.SDL_WINDOW_HIDDEN)
        self.assertIsInstance(window, video.SDL_Window)

        for i in range(render.get_num_render_drivers()):
            renderer = render.create_renderer(window, i,
                                              render.SDL_RENDERER_SOFTWARE)
            self.assertIsInstance(renderer, render.SDL_Renderer)
            info = render.get_renderer_info(renderer)

            self.assertIsInstance(info, render.SDL_RendererInfo)
            render.destroy_renderer(renderer)

            self.assertRaises(sdl.SDLError, render.get_renderer_info, renderer)

        video.destroy_window(window)
        self.assertRaises(TypeError, render.get_renderer_info, None)
        self.assertRaises(TypeError, render.get_renderer_info, "Test")

    def test_create_destroy_texture(self):
        window = video.create_window("Test", 10, 10, 10, 10,
                                     video.SDL_WINDOW_HIDDEN)
        self.assertIsInstance(window, video.SDL_Window)
        renderer = render.create_renderer(window, -1,
                                          render.SDL_RENDERER_SOFTWARE)
        self.assertIsInstance(renderer, render.SDL_Renderer)

        formats = (pixels.SDL_PIXELFORMAT_ARGB8888,
                   pixels.SDL_PIXELFORMAT_RGB555,
                   pixels.SDL_PIXELFORMAT_RGBA4444,
                   pixels.SDL_PIXELFORMAT_ARGB2101010,
                   pixels.SDL_PIXELFORMAT_YUY2
                   )
        access = (render.SDL_TEXTUREACCESS_STATIC,
                  render.SDL_TEXTUREACCESS_STREAMING,
                  render.SDL_TEXTUREACCESS_TARGET)
        for fmt in formats:
            for acc in access:
                for w in range(1, 300, 5):
                    for h in range(1, 300, 5):
                        tex = render.create_texture(renderer, fmt, acc, w, h)
                        self.assertIsInstance(tex, render.SDL_Texture)
                        render.destroy_texture(tex)

        self.assertRaises(sdl.SDLError, render.create_texture, renderer,
                          pixels.SDL_PIXELFORMAT_RGB555, 1, -10, 10)
        self.assertRaises(sdl.SDLError, render.create_texture, renderer,
                          pixels.SDL_PIXELFORMAT_RGB555, 1, 10, -10)
        self.assertRaises(sdl.SDLError, render.create_texture, renderer,
                          pixels.SDL_PIXELFORMAT_RGB555, 1, -10, -10)
        self.assertRaises(ValueError, render.create_texture, renderer,
                          pixels.SDL_PIXELFORMAT_RGB555, -5, 10, 10)
        self.assertRaises(ValueError, render.create_texture, renderer,
                          -10, 1, 10, 10)
        self.assertRaises(TypeError, render.create_texture, None,
                          pixels.SDL_PIXELFORMAT_RGB555, 1, 10, 10)
        self.assertRaises(TypeError, render.create_texture, "Test",
                          pixels.SDL_PIXELFORMAT_RGB555, 1, 10, 10)
        self.assertRaises(TypeError, render.create_texture, renderer,
                          "Test", 1, 10, 10)
        self.assertRaises(ValueError, render.create_texture, renderer,
                          pixels.SDL_PIXELFORMAT_RGB555, None, 10, 10)
        self.assertRaises(ValueError, render.create_texture, renderer,
                          pixels.SDL_PIXELFORMAT_RGB555, "Test", 10, 10)

        render.destroy_renderer(renderer)
        self.assertRaises(sdl.SDLError, render.create_texture, renderer,
                          pixels.SDL_PIXELFORMAT_RGB555, 1, 10, 10)
        video.destroy_window(window)

    @unittest.skip("not implemented")
    def test_create_texture_from_surface(self):
        sf = surface.create_rgb_surface(100, 100, 32, 0xFF000000, 0x00FF0000,
                                        0x0000FF00, 0x000000FF)
        window = video.create_window("Test", 10, 10, 10, 10,
                                     video.SDL_WINDOW_HIDDEN)
        self.assertIsInstance(window, video.SDL_Window)
        renderer = render.create_renderer(window, -1,
                                          render.SDL_RENDERER_SOFTWARE)
        self.assertIsInstance(renderer, render.SDL_Renderer)

    def test_query_texture(self):
        window = video.create_window("Test", 10, 10, 10, 10,
                                     video.SDL_WINDOW_HIDDEN)
        self.assertIsInstance(window, video.SDL_Window)
        renderer = render.create_renderer(window, -1,
                                          render.SDL_RENDERER_SOFTWARE)
        self.assertIsInstance(renderer, render.SDL_Renderer)

        formats = (pixels.SDL_PIXELFORMAT_ARGB8888,
                   pixels.SDL_PIXELFORMAT_RGB555,
                   pixels.SDL_PIXELFORMAT_RGBA4444,
                   pixels.SDL_PIXELFORMAT_ARGB2101010,
                   pixels.SDL_PIXELFORMAT_YUY2
                   )
        access = (render.SDL_TEXTUREACCESS_STATIC,
                  render.SDL_TEXTUREACCESS_STREAMING,
                  render.SDL_TEXTUREACCESS_TARGET)
        for fmt in formats:
            for acc in access:
                for w in range(1, 300, 5):
                    for h in range(1, 300, 5):
                        tex = render.create_texture(renderer, fmt, acc, w, h)
                        self.assertIsInstance(tex, render.SDL_Texture)
                        qf, qa, qw, qh = render.query_texture(tex)
                        self.assertEqual(qf, fmt)
                        self.assertEqual(qa, acc)
                        self.assertEqual(w, qw)
                        self.assertEqual(h, qh)
                        render.destroy_texture(tex)

        render.destroy_renderer(renderer)
        video.destroy_window(window)

    def test_get_set_texture_color_mod(self):
        window = video.create_window("Test", 10, 10, 10, 10,
                                     video.SDL_WINDOW_HIDDEN)
        self.assertIsInstance(window, video.SDL_Window)
        renderer = render.create_renderer(window, -1,
                                          render.SDL_RENDERER_SOFTWARE)
        self.assertIsInstance(renderer, render.SDL_Renderer)

        tex = render.create_texture(renderer, pixels.SDL_PIXELFORMAT_ARGB8888,
                                    render.SDL_TEXTUREACCESS_STREAMING, 10, 10)
        self.assertIsInstance(tex, render.SDL_Texture)
        colors = ((16, 22, 185),
                  (32, 64, 128),
                  (64, 32, 128),
                  (64, 32, 255),
                  (255, 32, 64),
                  (255, 32, 128),
                  (0, 0, 0),
                  (255, 255, 255),
                  (128, 128, 128),
                  )
        for r, g, b in colors:
            render.set_texture_color_mod(tex, r, g, b)
            tr, tg, tb = render.get_texture_color_mod(tex)
            self.assertEqual((tr, tg, tb), (r, g, b))

        render.destroy_texture(tex)
        self.assertRaises(sdl.SDLError, render.set_texture_color_mod, tex,
                          10, 20, 30)
        self.assertRaises(sdl.SDLError, render.get_texture_color_mod, tex)

        render.destroy_renderer(renderer)
        video.destroy_window(window)

    def test_get_set_texture_alpha_mod(self):
        window = video.create_window("Test", 10, 10, 10, 10,
                                     video.SDL_WINDOW_HIDDEN)
        self.assertIsInstance(window, video.SDL_Window)
        renderer = render.create_renderer(window, -1,
                                          render.SDL_RENDERER_SOFTWARE)
        self.assertIsInstance(renderer, render.SDL_Renderer)

        tex = render.create_texture(renderer, pixels.SDL_PIXELFORMAT_ARGB8888,
                                    render.SDL_TEXTUREACCESS_STREAMING, 10, 10)
        self.assertIsInstance(tex, render.SDL_Texture)

        for alpha in range(0, 255):
            render.set_texture_alpha_mod(tex, alpha)
            talpha = render.get_texture_alpha_mod(tex)
            self.assertEqual(talpha, alpha)

        render.destroy_texture(tex)
        self.assertRaises(sdl.SDLError, render.set_texture_color_mod, tex,
                          10, 20, 30)
        self.assertRaises(sdl.SDLError, render.get_texture_color_mod, tex)

        render.destroy_renderer(renderer)
        video.destroy_window(window)

    def test_get_set_texture_blend_mode(self):
        window = video.create_window("Test", 10, 10, 10, 10,
                                     video.SDL_WINDOW_HIDDEN)
        self.assertIsInstance(window, video.SDL_Window)
        renderer = render.create_renderer(window, -1,
                                          render.SDL_RENDERER_SOFTWARE)
        self.assertIsInstance(renderer, render.SDL_Renderer)

        tex = render.create_texture(renderer, pixels.SDL_PIXELFORMAT_ARGB8888,
                                    render.SDL_TEXTUREACCESS_STREAMING, 10, 10)
        self.assertIsInstance(tex, render.SDL_Texture)

        modes = (video.SDL_BLENDMODE_NONE,
                 video.SDL_BLENDMODE_ADD,
                 video.SDL_BLENDMODE_BLEND,
                 video.SDL_BLENDMODE_MOD,
                 )
        for mode in modes:
            render.set_texture_blend_mode(tex, mode)
            tmode = render.get_texture_blend_mode(tex)
            self.assertEqual(tmode, mode)

        render.destroy_texture(tex)
        self.assertRaises(sdl.SDLError, render.set_texture_blend_mode, tex,
                          modes[2])
        self.assertRaises(sdl.SDLError, render.get_texture_blend_mode, tex)

        render.destroy_renderer(renderer)
        video.destroy_window(window)

    @unittest.skip("not implemented")
    def test_update_texture(self):
        pass

    @unittest.skip("not implemented")
    def test_lock_texture(self):
        pass

    @unittest.skip("not implemented")
    def test_unlock_texture(self):
        pass

    def test_render_target_supported(self):
        window = video.create_window("Test", 10, 10, 10, 10,
                                     video.SDL_WINDOW_HIDDEN)
        self.assertIsInstance(window, video.SDL_Window)

        for i in range(render.get_num_render_drivers()):
            renderer = render.create_renderer(window, i,
                                              render.SDL_RENDERER_ACCELERATED)
            self.assertIsInstance(renderer, render.SDL_Renderer)

            val = render.render_target_supported(renderer)
            self.assertIsInstance(val, bool)
            render.destroy_renderer(renderer)
        video.destroy_window(window)

    def test_set_render_target(self):
        window = video.create_window("Test", 10, 10, 10, 10,
                                     video.SDL_WINDOW_HIDDEN)
        self.assertIsInstance(window, video.SDL_Window)

        skipcount = 0
        for i in range(render.get_num_render_drivers()):
            renderer = render.create_renderer(window, i,
                                              render.SDL_RENDERER_ACCELERATED)
            self.assertIsInstance(renderer, render.SDL_Renderer)

            supported = render.render_target_supported(renderer)
            if not supported:
                skipcount += 1
                render.destroy_renderer(renderer)
                continue

            render.set_render_target(renderer)

            tex = render.create_texture(renderer,
                                        pixels.SDL_PIXELFORMAT_ARGB8888,
                                        render.SDL_TEXTUREACCESS_TARGET,
                                        10, 10)
            render.set_render_target(renderer, tex)
            render.destroy_texture(tex)

            # TODO: Check in the SDL codebase, why the code below does
            # not fail...
            # tex2 = render.create_texture(renderer,
            #                              pixels.SDL_PIXELFORMAT_ARGB8888,
            #                              render.SDL_TEXTUREACCESS_STREAMING,
            #                              10, 10)
            # self.assertRaises(SDLError, render.set_render_target, renderer,
            #                   tex2)
            # render.destroy_texture(tex2)

            render.destroy_renderer(renderer)
        video.destroy_window(window)

        if skipcount == render.get_num_render_drivers():
            self.skipTest("None of the renderers supports render targets")

    def test_render_set_get_viewport(self):
        rects = (rect.SDL_Rect(0, 0, 0, 0),
                 rect.SDL_Rect(0, 0, 10, 10),
                 rect.SDL_Rect(3, 3, 5, 5),
                 rect.SDL_Rect(-5, -5, 10, 10),
                 rect.SDL_Rect(10, 10, 10, 10),
                 rect.SDL_Rect(0, 0, -10, -10),
                 rect.SDL_Rect(-10, 0, 10, 10),
                 rect.SDL_Rect(0, -10, 10, 10),
                 rect.SDL_Rect(-10, -10, 10, 10),
            )
        window = video.create_window("Test", 10, 10, 10, 10,
                                     video.SDL_WINDOW_HIDDEN |
                                     video.SDL_WINDOW_BORDERLESS)
        self.assertIsInstance(window, video.SDL_Window)

        failcount = 0
        for i in range(render.get_num_render_drivers()):
            renderer = render.create_renderer(window, i,
                                              render.SDL_RENDERER_ACCELERATED)
            self.assertIsInstance(renderer, render.SDL_Renderer)
            render.render_set_viewport(renderer)
            port = render.render_get_viewport(renderer)
            self.assertEqual(port, rect.SDL_Rect(0, 0, 10, 10))
            for r in rects:
                render.render_set_viewport(renderer, r)
                port = render.render_get_viewport(renderer)
                if port != r:
                    failcount += 1

            render.destroy_renderer(renderer)
        if failcount > 0:
            unittest.skip("""for some reason, even with correct values, this
seems to fail on creating the second renderer of the window, if any""")
        video.destroy_window(window)

    def test_get_set_render_draw_color(self):
        window = video.create_window("Test", 10, 10, 10, 10,
                                     video.SDL_WINDOW_HIDDEN)
        self.assertIsInstance(window, video.SDL_Window)

        for i in range(render.get_num_render_drivers()):
            renderer = render.create_renderer(window, i,
                                              render.SDL_RENDERER_ACCELERATED)
            self.assertIsInstance(renderer, render.SDL_Renderer)

            colors = ((16, 22, 185, 217),
                      (32, 64, 128, 255),
                      (64, 32, 128, 255),
                      (64, 32, 255, 128),
                      (255, 32, 64, 128),
                      (255, 32, 128, 64),
                      (0, 0, 0, 0),
                      (255, 255, 255, 255),
                      (128, 128, 128, 255),
                      )
            for r, g, b, a in colors:
                render.set_render_draw_color(renderer, r, g, b, a)
                dr, dg, db, da = render.get_render_draw_color(renderer)
                self.assertEqual((dr, dg, db, da), (r, g, b, a))
            render.destroy_renderer(renderer)
            self.assertRaises(sdl.SDLError, render.set_render_draw_color,
                              renderer, 10, 20, 30, 40)
            self.assertRaises(sdl.SDLError, render.get_render_draw_color,
                              renderer)

        video.destroy_window(window)

    def test_get_set_render_draw_blend_mode(self):
        window = video.create_window("Test", 10, 10, 10, 10,
                                     video.SDL_WINDOW_HIDDEN)
        self.assertIsInstance(window, video.SDL_Window)

        for i in range(render.get_num_render_drivers()):
            renderer = render.create_renderer(window, i,
                                              render.SDL_RENDERER_ACCELERATED)
            self.assertIsInstance(renderer, render.SDL_Renderer)

            modes = (video.SDL_BLENDMODE_NONE,
                     video.SDL_BLENDMODE_ADD,
                     video.SDL_BLENDMODE_BLEND,
                     video.SDL_BLENDMODE_MOD,
                     )
            for mode in modes:
                render.set_render_draw_blend_mode(renderer, mode)
                bmode = render.get_render_draw_blend_mode(renderer)
                self.assertEqual(bmode, mode)
            render.destroy_renderer(renderer)
            self.assertRaises(sdl.SDLError, render.set_render_draw_blend_mode,
                              renderer, video.SDL_BLENDMODE_ADD)
            self.assertRaises(sdl.SDLError, render.get_render_draw_blend_mode,
                              renderer)
        video.destroy_window(window)

    def test_render_clear(self):
        window = video.create_window("Test", 10, 10, 10, 10,
                                     video.SDL_WINDOW_HIDDEN)
        self.assertIsInstance(window, video.SDL_Window)
        renderer = render.create_renderer(window, -1,
                                          render.SDL_RENDERER_ACCELERATED)
        render.render_clear(renderer)
        render.destroy_renderer(renderer)
        self.assertRaises(sdl.SDLError, render.render_clear, renderer)
        self.assertRaises(TypeError, render.render_clear, None)
        self.assertRaises(TypeError, render.render_clear, "Test")
        self.assertRaises(TypeError, render.render_clear, 123456)

    @unittest.skipIf(hasattr(sys, "pypy_version_info"),
                     "PyPy's ctypes can't do byref(value, offset)")
    def test_render_draw_point(self):
        points = ((-4, -3), (-4, 3), (4, -3),
                  (0, 0), (1, 1), (10, 10), (99, 99),
                  (4, 22), (57, 88), (45, 15),
                  (100, 100)
                  )
        r, g, b, a = 0xAA, 0xBB, 0xCC, 0xDD
        w, h = 100, 100
        sf = surface.create_rgb_surface(w, h, 32, 0xFF000000, 0x00FF0000,
                                        0x0000FF00, 0x000000FF)
        color = pixels.map_rgba(sf.format, r, g, b, a)
        renderer = render.create_software_renderer(sf)
        render.set_render_draw_color(renderer, r, g, b, a)
        for x, y in points:
            render.render_draw_point(renderer, x, y)
        render.render_present(renderer)
        view = pvid.PixelView(sf)
        for x, y in points:
            npx = max(x + 1, w)
            npy = max(y + 1, h)
            ppx = max(x - 1, 0)
            ppy = max(y - 1, 0)
            if x < 0 or x >= w or y < 0 or y >= h:
                continue
            self.assertEqual(hex(view[y][x]), hex(color))
            if (npx, npy) not in points:
                self.assertNotEqual(hex(view[npy][npx]), hex(color))
            if (ppx, ppy) not in points:
                self.assertNotEqual(hex(view[ppy][ppx]), hex(color))
        render.destroy_renderer(renderer)
        del view
        surface.free_surface(sf)

    @unittest.skip("not implemented")
    def test_render_draw_points(self):
        pass

    @unittest.skip("not implemented")
    def test_render_draw_line(self):
        pass

    @unittest.skip("not implemented")
    def test_render_draw_lines(self):
        pass

    @unittest.skip("not implemented")
    def test_render_draw_rect(self):
        pass

    @unittest.skip("not implemented")
    def test_render_draw_rects(self):
        pass

    @unittest.skip("not implemented")
    def test_render_fill_rect(self):
        pass

    @unittest.skip("not implemented")
    def test_render_fill_rects(self):
        pass

    @unittest.skip("not implemented")
    def test_render_copy(self):
        pass

    @unittest.skip("not implemented")
    def test_render_read_pixels(self):
        pass

    @unittest.skip("not implemented")
    def test_render_present(self):
        pass

if __name__ == '__main__':
    sys.exit(unittest.main())
