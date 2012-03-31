import sys
from ctypes.util import find_library
import unittest
import pygame2.sdl as sdl
import pygame2.sdl.video as video
from  pygame2.sdl.surface import SDL_Surface
from  pygame2.sdl.error import SDLError
import pygame2.sdl.rect as rect
import pygame2.sdl.pixels as pixels
from pygame2.test.util.testutils import interactive, doprint

if sys.version_info[0] >= 3:
    long = int

def has_opengl_lib ():
    for libname in ("gl", "opengl", "opengl32"):
        path = find_library (libname)
        if path is not None:
            return True

def get_opengl_path ():
    for libname in ("gl", "opengl", "opengl32"):
        path = find_library (libname)
        if path is not None:
            return path

# TODO: mostly covers positive tests right now - fix this!
class SDLVideoTest (unittest.TestCase):
    __tags__ = [ "sdl" ]
    
    def setUp (self):
        if sys.version.startswith ("3.1"):
            self.assertIsInstance = lambda x, t: self.assertTrue (isinstance (x, t))
        video.init ()
    
    def tearDown (self):
        video.quit ()
    
    def test_SDL_WINDOWPOS_UNDEFINED_DISPLAY (self):
        for x in range (0xFFFF):
            self.assertEqual (video.SDL_WINDOWPOS_UNDEFINED_MASK | x,
                              video.SDL_WINDOWPOS_UNDEFINED_DISPLAY (x))
            self.assertEqual ((video.SDL_WINDOWPOS_UNDEFINED_DISPLAY (x) &
                               video.SDL_WINDOWPOS_UNDEFINED_MASK),
                              video.SDL_WINDOWPOS_UNDEFINED_MASK)
            self.assertTrue (video.SDL_WINDOWPOS_UNDEFINED_DISPLAY (x) !=
                             video.SDL_WINDOWPOS_CENTERED_DISPLAY (x))

    def test_SDL_WINDOWPOS_ISUNDEFINED (self):
        self.assertTrue (video.SDL_WINDOWPOS_ISUNDEFINED \
                             (video.SDL_WINDOWPOS_UNDEFINED))
        self.assertFalse (video.SDL_WINDOWPOS_ISUNDEFINED \
                             (video.SDL_WINDOWPOS_CENTERED))
        for x in range (0xFFFF):
            self.assertTrue (video.SDL_WINDOWPOS_ISUNDEFINED \
                                 (video.SDL_WINDOWPOS_UNDEFINED_DISPLAY (x)))
            
        
    def test_SDL_WINDOWPOS_CENTERED_DISPLAY (self):
        for x in range (0xFFFF):
            self.assertEqual (video.SDL_WINDOWPOS_CENTERED_MASK | x,
                              video.SDL_WINDOWPOS_CENTERED_DISPLAY (x))
            self.assertEqual ((video.SDL_WINDOWPOS_CENTERED_DISPLAY (x) &
                               video.SDL_WINDOWPOS_CENTERED_MASK),
                              video.SDL_WINDOWPOS_CENTERED_MASK)
            self.assertTrue (video.SDL_WINDOWPOS_CENTERED_DISPLAY (x) !=
                             video.SDL_WINDOWPOS_UNDEFINED_DISPLAY (x))
    
    def test_SDL_WINDOWPOS_ISCENTERED (self):
        self.assertTrue (video.SDL_WINDOWPOS_ISCENTERED \
                             (video.SDL_WINDOWPOS_CENTERED))
        self.assertFalse (video.SDL_WINDOWPOS_ISCENTERED \
                             (video.SDL_WINDOWPOS_UNDEFINED))
        for x in range (0xFFFF):
            self.assertTrue (video.SDL_WINDOWPOS_ISCENTERED \
                                 (video.SDL_WINDOWPOS_CENTERED_DISPLAY (x)))
    
    def test_SDL_DisplayMode (self):
        mode = video.SDL_DisplayMode ()
        self.assertIsInstance (mode, video.SDL_DisplayMode)
        for fmt in range (0, 10):
            for w in range (0, 20):
                for h in range (0, 30):
                    for r in range (0, 40):
                        mode = video.SDL_DisplayMode (fmt, w, h, r)
                        self.assertIsInstance (mode, video.SDL_DisplayMode)
                        self.assertEqual (mode.format, fmt)
                        self.assertEqual (mode.w, w)
                        self.assertEqual (mode.h, h)
                        self.assertEqual (mode.refresh_rate, r)
        self.assertRaises (TypeError, video.SDL_DisplayMode, "Test")
        self.assertRaises (TypeError, video.SDL_DisplayMode, "Test", 10, 10, 10)
        self.assertRaises (TypeError, video.SDL_DisplayMode, 10, "Test", 10, 10)
        self.assertRaises (TypeError, video.SDL_DisplayMode, 10, 10, "Test", 10)
        self.assertRaises (TypeError, video.SDL_DisplayMode, 10, 10, 10, "Test")
        self.assertRaises (TypeError, video.SDL_DisplayMode, None)
        self.assertRaises (TypeError, video.SDL_DisplayMode, None, 10, 10, 10)
        self.assertRaises (TypeError, video.SDL_DisplayMode, 10, None, 10, 10)
        self.assertRaises (TypeError, video.SDL_DisplayMode, 10, 10, None, 10)
        self.assertRaises (TypeError, video.SDL_DisplayMode, 10, 10, 10, None)
    
    def test_SDL_DisplayMode__eq__ (self):
        DMode = video.SDL_DisplayMode
        self.assertTrue (DMode () == DMode ())
        self.assertTrue (DMode (10, 0, 0, 0) == DMode (10, 0, 0, 0))
        self.assertTrue (DMode (10, 10, 0, 0) == DMode (10, 10, 0, 0))
        self.assertTrue (DMode (10, 10, 10, 0) == DMode (10, 10, 10, 0))
        self.assertTrue (DMode (10, 10, 10, 10) == DMode (10, 10, 10, 10))
        self.assertTrue (DMode (0, 10, 0, 0) == DMode (0, 10, 0, 0))
        self.assertTrue (DMode (0, 0, 10, 0) == DMode (0, 0, 10, 0))
        self.assertTrue (DMode (0, 0, 0, 10) == DMode (0, 0, 0, 10))
        
        self.assertFalse (DMode () == DMode (10, 0, 0, 0))
        self.assertFalse (DMode (10, 0, 0, 0) == DMode (0, 0, 0, 0))
        self.assertFalse (DMode (10, 0, 0, 0) == DMode (0, 10, 0, 0))
        self.assertFalse (DMode (10, 0, 0, 0) == DMode (0, 0, 10, 0))
        self.assertFalse (DMode (10, 0, 0, 0) == DMode (0, 0, 0, 10))

    def test_SDL_DisplayMode__ne__ (self):
        DMode = video.SDL_DisplayMode
        self.assertFalse (DMode () != DMode ())
        self.assertFalse (DMode (10, 0, 0, 0) != DMode (10, 0, 0, 0))
        self.assertFalse (DMode (10, 10, 0, 0) != DMode (10, 10, 0, 0))
        self.assertFalse (DMode (10, 10, 10, 0) != DMode (10, 10, 10, 0))
        self.assertFalse (DMode (10, 10, 10, 10) != DMode (10, 10, 10, 10))
        self.assertFalse (DMode (0, 10, 0, 0) != DMode (0, 10, 0, 0))
        self.assertFalse (DMode (0, 0, 10, 0) != DMode (0, 0, 10, 0))
        self.assertFalse (DMode (0, 0, 0, 10) != DMode (0, 0, 0, 10))
        
        self.assertTrue (DMode () != DMode (10, 0, 0, 0))
        self.assertTrue (DMode (10, 0, 0, 0) != DMode (0, 0, 0, 0))
        self.assertTrue (DMode (10, 0, 0, 0) != DMode (0, 10, 0, 0))
        self.assertTrue (DMode (10, 0, 0, 0) != DMode (0, 0, 10, 0))
        self.assertTrue (DMode (10, 0, 0, 0) != DMode (0, 0, 0, 10))
    
    @unittest.skip ("not implemented")
    def test_SDL_Window (self):
        pass

    def test_get_num_video_drivers (self):
        numdrivers = video.get_num_video_drivers ()
        self.assertGreaterEqual (numdrivers, 1)

    def test_get_video_driver (self):
        numdrivers = video.get_num_video_drivers ()
        for i in range (numdrivers):
            name = video.get_video_driver (i)
            self.assertIsInstance (name, str)
    
    def test_get_current_video_driver (self):
        curdriver = video.get_current_video_driver ()
        found = False
        numdrivers = video.get_num_video_drivers ()
        for i in range (numdrivers):
            name = video.get_video_driver (i)
            if name == curdriver:
                found = True
                break
        self.assertTrue (found, "Current video driver not found")

    def test_get_num_video_displays (self):
        numdisplays = video.get_num_video_displays ()
        self.assertGreaterEqual (numdisplays, 1)
    
    def test_get_num_display_modes (self):
        numdisplays = video.get_num_video_displays ()
        for index in range (numdisplays):
            modes = video.get_num_display_modes (index)
            self.assertGreaterEqual (modes, 1)
    
    def test_get_display_mode (self):
        numdisplays = video.get_num_video_displays ()
        for index in range (numdisplays):
            modes = video.get_num_display_modes (index)
            for mode in range(modes):
                dmode = video.get_display_mode (index, mode)
                self.assertIsInstance (dmode, video.SDL_DisplayMode)

    def test_get_current_display_mode (self):
        numdisplays = video.get_num_video_displays ()
        for index in range (numdisplays):
            dmode = video.get_current_display_mode (index)
            self.assertIsInstance (dmode, video.SDL_DisplayMode)

    def test_get_desktop_display_mode (self):
        numdisplays = video.get_num_video_displays ()
        for index in range (numdisplays):
            dmode = video.get_desktop_display_mode (index)
            self.assertIsInstance (dmode, video.SDL_DisplayMode)

    def test_get_closest_display_mode (self):
        numdisplays = video.get_num_video_displays ()
        for index in range (numdisplays):
            modes = video.get_num_display_modes (index)
            for mode in range(modes):
                dmode = video.get_display_mode (index, mode)
                self.assertIsInstance (dmode, video.SDL_DisplayMode)
                cmode = video.SDL_DisplayMode (dmode.format,
                                               dmode.w - 1, dmode.h - 1,
                                               dmode.refresh_rate)
                closest = video.get_closest_display_mode (index, cmode)
                self.assertEqual (closest, dmode)

    def test_init (self):
        video.init ()
        video.init ()
        video.init ()
        video.quit()
        video.init ()

    def test_quit (self):
        video.quit ()
        video.quit ()
        video.quit ()
        video.init ()

    def test_get_display_bounds (self):
        numdisplays = video.get_num_video_displays ()
        for index in range (numdisplays):
            bounds = video.get_display_bounds (index)
            self.assertIsInstance (bounds, rect.SDL_Rect)
            self.assertFalse (rect.rect_empty (bounds))

    def test_screensaver (self):
        initial = video.is_screensaver_enabled ()
        self.assertIsInstance (initial, bool)
        
        video.enable_screensaver ()
        self.assertTrue (video.is_screensaver_enabled ())
        video.enable_screensaver ()
        self.assertTrue (video.is_screensaver_enabled ())
        video.disable_screensaver ()
        self.assertFalse (video.is_screensaver_enabled ())
        video.disable_screensaver ()
        self.assertFalse (video.is_screensaver_enabled ())
        video.enable_screensaver ()
        self.assertTrue (video.is_screensaver_enabled ())
        video.disable_screensaver ()
        self.assertFalse (video.is_screensaver_enabled ())
        
        if initial:
            video.enable_screensaver ()
        else:
            video.disable_screensaver ()

    def test_create_window (self):
        # Borderless to ensure that the size check works
        flags = (video.SDL_WINDOW_BORDERLESS, 
                 video.SDL_WINDOW_BORDERLESS | video.SDL_WINDOW_HIDDEN)
        for flag in flags:
            window = video.create_window ("Test", 10, 10, 10, 10, flag)
            self.assertIsInstance (window, video.SDL_Window)
            self.assertEqual (window.position, (10, 10))
            self.assertEqual (window.size, (10, 10))
            self.assertEqual (window.flags & flag, flag)
            self.assertEqual (window.title, "Test")
            video.destroy_window (window)
        # TODO

    def test_destroy_window (self):
        flags = (video.SDL_WINDOW_BORDERLESS, 
                 video.SDL_WINDOW_BORDERLESS | video.SDL_WINDOW_HIDDEN)
        for flag in flags:
            window = video.create_window ("Test", 10, 10, 10, 10, flag)
            # TODO: how to check for this in a meaningful way?
            video.destroy_window (window)

    @unittest.skip ("not implemented")
    def test_create_window_from (self):
        pass
        
    def test_get_window_display (self):
        numdisplays = video.get_num_video_displays ()
        flags = (video.SDL_WINDOW_BORDERLESS,
                 video.SDL_WINDOW_BORDERLESS | video.SDL_WINDOW_HIDDEN)
        for flag in flags:
            window = video.create_window ("Test", 10, 10, 10, 10, flag) 
            self.assertIsInstance (window, video.SDL_Window)
            self.assertEqual (window.position, (10, 10))
            self.assertEqual (window.size, (10, 10))
            self.assertEqual (window.flags & flag, flag)
            self.assertEqual (window.title, "Test")
            
            dindex = video.get_window_display (window)
            self.assertTrue (0 <= dindex <= numdisplays,
                             "Invalid display index")
            video.destroy_window (window)
            self.assertRaises (SDLError, video.get_window_display, window)

    def test_get_window_display_mode (self):
        flags = (video.SDL_WINDOW_BORDERLESS,
                 video.SDL_WINDOW_BORDERLESS | video.SDL_WINDOW_HIDDEN)
        for flag in flags:
            window = video.create_window ("Test", 10, 10, 10, 10, flag)
            dmode = video.get_window_display_mode (window)
            self.assertIsInstance (dmode, video.SDL_DisplayMode)
            video.destroy_window (window)
            self.assertRaises (SDLError, video.get_window_display_mode, window)

    def test_set_window_display_mode (self):
        flags = (video.SDL_WINDOW_BORDERLESS,
                 video.SDL_WINDOW_BORDERLESS | video.SDL_WINDOW_HIDDEN)
        for flag in flags:
            window = video.create_window ("Test", 10, 10, 10, 10, flag)
            dindex = video.get_window_display (window)
            dmode = video.get_current_display_mode (dindex)
            
            video.set_window_display_mode (window, dmode)
            wmode = video.get_window_display_mode (window)
            self.assertEqual (dmode.format, wmode.format)
            self.assertEqual (dmode.w, wmode.w)
            self.assertEqual (dmode.h, wmode.h)
            self.assertEqual (dmode.refresh_rate, wmode.refresh_rate)
            
            video.set_window_display_mode (window)
            wmode = video.get_window_display_mode (window)
            self.assertNotEqual (dmode.w, wmode.w)
            self.assertNotEqual (dmode.h, wmode.h)
            
            video.destroy_window (window)
            self.assertRaises (SDLError, video.set_window_display_mode, window,
                               dmode)
    
    def test_get_window_pixelformat (self):
        flags = (video.SDL_WINDOW_BORDERLESS,
                 video.SDL_WINDOW_BORDERLESS | video.SDL_WINDOW_HIDDEN)
        for flag in flags:
            window = video.create_window ("Test", 10, 10, 10, 10, flag)
            fmt = video.get_window_pixelformat (window)
            self.assertTrue (type (fmt) in (int, long))
            video.destroy_window (window)
            self.assertRaises (SDLError, video.get_window_pixelformat, window)

    def test_get_window_id (self):
        flags = (video.SDL_WINDOW_BORDERLESS,
                 video.SDL_WINDOW_BORDERLESS | video.SDL_WINDOW_HIDDEN)
        for flag in flags:
            window = video.create_window ("Test", 10, 10, 10, 10, flag)
            id = video.get_window_id (window)
            self.assertIsInstance (id, int)
            video.destroy_window (window)
            self.assertRaises (SDLError, video.get_window_id, window)

    def test_get_window_from_id (self):
        flags = (video.SDL_WINDOW_BORDERLESS,
                 video.SDL_WINDOW_BORDERLESS | video.SDL_WINDOW_HIDDEN)
        for flag in flags:
            window = video.create_window ("Test", 10, 10, 10, 10, flag)
            id = video.get_window_id (window)
            window2 = video.get_window_from_id (id)
            self.assertEqual (video.get_window_id (window),
                              video.get_window_id (window2))
            self.assertEqual (video.get_window_title (window),
                              video.get_window_title (window2))
            self.assertEqual (video.get_window_position (window),
                              video.get_window_position (window2))
            self.assertEqual (video.get_window_size (window),
                              video.get_window_size (window2))

    @unittest.skip ("currently fails for whatever reason...")
    def test_get_window_flags (self):
        flags = (video.SDL_WINDOW_BORDERLESS, 
                 video.SDL_WINDOW_BORDERLESS | video.SDL_WINDOW_HIDDEN,
                 video.SDL_WINDOW_RESIZABLE | video.SDL_WINDOW_MINIMIZED)
        for flag in flags:
            window = video.create_window ("Test", 10, 10, 10, 10, flag)
            wflags = video.get_window_flags (window)
            # TODO: this constantly fails - why?
            self.assertEqual ((wflags & flag), flag)

    def test_get_set_window_title (self):
        window = video.create_window ("Test", 10, 10, 10, 10, 0) 
        self.assertEqual (video.get_window_title (window), "Test")
        video.set_window_title (window, "Hello there")
        self.assertEqual (video.get_window_title (window), "Hello there")
        video.set_window_title (window, 123456789)
        self.assertEqual (video.get_window_title (window), "123456789")
        video.destroy_window (window)
        self.assertRaises (SDLError, video.get_window_title, window)
    
    @unittest.skip ("not implemented")
    def test_set_window_icon (self):
        pass
    
    def test_get_set_window_data (self):
        window = video.create_window ("Test", 10, 10, 10, 10, 0) 
        self.assertIsInstance (window, video.SDL_Window)
        values = { "text" : "Teststring",
                   "object" : self,
                   "list" : [1, 2, 3, 4],
                   "tuple" : ("a", 1, self)
                }
    
        for k, v in values.items ():
            retval = video.get_window_data (window, k)
            self.assertIsNone (retval)
            video.set_window_data (window, k, v)
            retval = video.get_window_data (window, k)
            self.assertEquals (retval, v)
        video.destroy_window (window)

    def test_get_set_window_position (self):
        window = video.create_window ("Test", 10, 10, 10, 10, 0)
        self.assertEqual (video.get_window_position (window), (10, 10))
        video.set_window_position (window, 0, 0)
        self.assertEqual (video.get_window_position (window), (0, 0))
        video.set_window_position (window, 600, 900)
        self.assertEqual (video.get_window_position (window), (600, 900))
        video.set_window_position (window, -200, -10)
        self.assertEqual (video.get_window_position (window), (-200, -10))
        video.destroy_window (window)

    def test_get_set_window_size (self):
        flags = video.SDL_WINDOW_BORDERLESS
        window = video.create_window ("Test", 10, 10, 10, 10, flags)
        self.assertEqual (video.get_window_size (window), (10, 10))
        self.assertEqual (window.size, (10, 10))
        video.set_window_size (window, 0, 0)
        self.assertEqual (video.get_window_size (window), (0, 0))
        self.assertEqual (window.size, (0, 0))
        video.set_window_size (window, 600, 900)
        self.assertEqual (video.get_window_size (window), (600, 900))
        self.assertEqual (window.size, (600, 900))
        video.set_window_size (window, -200, -10)
        self.assertEqual (video.get_window_size (window), (-200, -10))
        self.assertEqual (window.size, (-200, -10))
        video.destroy_window (window)

    @interactive ("Was the window shown?")
    def test_show_window (self):
        window = video.create_window ("test_show_window", 200, 200, 200, 200, 0)
        video.show_window (window)
        doprint ("Please check, if a window with the title 'test_show_window' is shown")
        video.destroy_window (window)
        
    @interactive ("Did the window vanish from your sight and pop up again?")
    def test_hide_window (self):
        window = video.create_window ("test_hide_window", 200, 200, 200, 200, 0)
        video.show_window (window)
        doprint ("Please check, if a window with the title 'test_hide_window' is shown")
        video.hide_window (window)
        doprint ("Please check, that the window is not shown anymore")
        video.show_window (window)
        doprint ("Please check, if the window is shown again")
        video.destroy_window (window)
    
    @unittest.skip ("Seems not to work at the moment")
    @interactive ("Did the window raise properly?")
    def test_raise_window (self):
        window = video.create_window ("test_raise_window", 200, 200, 200, 200,
                                      0)
        video.show_window (window)
        doprint ("Please check, that a window with the title 'test_raise_window' is shown")
        doprint ("Move another window on top of the window, so it is hidden")
        video.raise_window (window)
        doprint ("The window should be raised to the foreground now")
        video.destroy_window (window)
    
    @interactive ("Was the window maximized?")
    def test_maximize_window (self):
        window = video.create_window ("test_maximize_window", 200, 200,
                                      200, 200, video.SDL_WINDOW_RESIZABLE)
        video.show_window (window)
        doprint ("Please check, that a window with the title 'test_maximize_window' is shown")
        video.maximize_window (window)
        doprint ("Please check, if the window was maximized properly")
        video.destroy_window (window)
        
    @interactive ("Was the window minimized?")
    def test_minimize_window (self):
        window = video.create_window ("test_minimize_window", 200, 200,
                                      200, 200, 0)
        video.show_window (window)
        doprint ("Please check, that a window with the title 'test_minimize_window' is shown")
        video.minimize_window (window)
        doprint ("Please check, if the window was minimized properly")
        video.destroy_window (window)
    
    @unittest.skip ("seems not to work correctly at the moment")
    @interactive ("Was the window maximized and restored properly?")
    def test_restore_window (self):
        window = video.create_window ("test_restore_window", 200, 200,
                                      200, 200, video.SDL_WINDOW_RESIZABLE)
        video.show_window (window)
        doprint ("Please check, that a window with the title 'test_restore_window' is shown")
        video.maximize_window (window)
        doprint ("Please check, if the window was maximized properly")
        video.restore_window (window)
        doprint ("Please check, if the window was restored properly")
        video.destroy_window (window)

    def test_set_window_fullscreen (self):
        # TODO: HIDDEN avoids flickering, but is this really a sufficient test?
        flags = (video.SDL_WINDOW_BORDERLESS | video.SDL_WINDOW_HIDDEN, 
                 video.SDL_WINDOW_BORDERLESS | video.SDL_WINDOW_HIDDEN,
                 video.SDL_WINDOW_RESIZABLE | video.SDL_WINDOW_MINIMIZED | \
                 video.SDL_WINDOW_HIDDEN)
        for flag in flags:
            window = video.create_window ("Test", 0, 0, 1024, 768, flag)
            video.set_window_fullscreen (window, True)
            flags = video.get_window_flags (window)
            self.assertEqual (flags & video.SDL_WINDOW_FULLSCREEN,
                              video.SDL_WINDOW_FULLSCREEN)
            video.set_window_fullscreen (window, False)
            flags = video.get_window_flags (window)
            self.assertNotEqual (flags & video.SDL_WINDOW_FULLSCREEN,
                                 video.SDL_WINDOW_FULLSCREEN)
            video.destroy_window (window)

    def test_get_window_surface (self):
        flags = (video.SDL_WINDOW_BORDERLESS, 
                 video.SDL_WINDOW_BORDERLESS | video.SDL_WINDOW_HIDDEN,
                 video.SDL_WINDOW_RESIZABLE | video.SDL_WINDOW_MINIMIZED)
        for flag in flags:
            window = video.create_window ("Test", 200, 200, 200, 200, flag)
            surface = video.get_window_surface (window)
            self.assertIsInstance (surface, SDL_Surface)
            video.destroy_window (window)
            self.assertRaises (SDLError, video.get_window_surface, window)
    
    def test_update_window_surface (self):
        flags = (video.SDL_WINDOW_BORDERLESS, 
                 video.SDL_WINDOW_BORDERLESS | video.SDL_WINDOW_HIDDEN,
                 video.SDL_WINDOW_RESIZABLE | video.SDL_WINDOW_MINIMIZED)
        for flag in flags:
            window = video.create_window ("Test", 200, 200, 200, 200, flag)
            video.update_window_surface (window)
            video.destroy_window (window)

    def test_update_window_surface_rects (self):
        rectlist = [rect.SDL_Rect (), rect.SDL_Rect (10, 10, 10, 10),
                    rect.SDL_Rect (0, 0, 5, 4), rect.SDL_Rect (-5, -5, 6, 2)]
        flags = (video.SDL_WINDOW_BORDERLESS, 
                 video.SDL_WINDOW_BORDERLESS | video.SDL_WINDOW_HIDDEN,
                 video.SDL_WINDOW_RESIZABLE | video.SDL_WINDOW_MINIMIZED)
        for flag in flags:
            window = video.create_window ("Test", 200, 200, 200, 200, flag)
            self.assertRaises (SDLError, video.update_window_surface_rects,
                               window, rectlist)
            surface = video.get_window_surface (window)
            video.update_window_surface_rects (window, rectlist)
            video.destroy_window (window)
    
    def test_get_set_window_grab (self):
        flags = (video.SDL_WINDOW_BORDERLESS, 
                 video.SDL_WINDOW_BORDERLESS | video.SDL_WINDOW_HIDDEN,
                 video.SDL_WINDOW_RESIZABLE | video.SDL_WINDOW_MINIMIZED)
        for flag in flags:
            window = video.create_window ("Test", 200, 200, 200, 200, flag)
            self.assertFalse (video.get_window_grab (window))
            video.set_window_grab (window, True)
            self.assertTrue (video.get_window_grab (window))
            video.set_window_grab (window, 0)
            self.assertFalse (video.get_window_grab (window))
            video.set_window_grab (window, "Test")
            self.assertTrue (video.get_window_grab (window))
            video.set_window_grab (window, None)
            self.assertFalse (video.get_window_grab (window))
    
    def test_get_set_window_brightness (self):
        flags = (video.SDL_WINDOW_BORDERLESS,
                 video.SDL_WINDOW_BORDERLESS | video.SDL_WINDOW_HIDDEN,
                 video.SDL_WINDOW_RESIZABLE | video.SDL_WINDOW_MINIMIZED)
        for flag in flags:
            window = video.create_window ("Test", 200, 200, 200, 200, flag)
            orig = video.get_window_brightness (window)
            self.assertIsInstance (orig, float)
            # Go from 0.0, 0.1 ... to 3.0
            gammas = (x * 0.1 for x in range (0, 20))
            count = 0
            for b in gammas:
                try:
                    video.set_window_brightness (window, b)
                except:
                    pass # ignore the issue, if the gamma is not supported
                else:
                    val = video.get_window_brightness (window)
                    self.assertAlmostEqual (val, b)
                    count += 1
             # At least one gamma (1.0) must have worked.
            self.assertTrue (count > 0)
    
    @unittest.skip ("not implemented")
    def test_set_window_gamma_ramp (self):
        pass
    
    @unittest.skip ("not implemented")
    def test_get_window_gamma_ramp (self):
        pass
    
    def test_gl_load_unload_library (self):
        # Try the default library
        self.assertTrue (video.gl_load_library ())
        video.gl_unload_library ()
        
        if has_opengl_lib ():
            self.assertTrue (video.gl_load_library (get_opengl_path ()))
            video.gl_unload_library ()
        
        self.assertRaises (SDLError, video.gl_load_library, "Test")
        self.assertRaises (SDLError, video.gl_load_library, False)
        self.assertRaises (SDLError, video.gl_load_library, 0)

    def test_gl_get_proc_address (self):
        procaddr = video.gl_get_proc_address ("glGetString")
        self.assertIsNone (procaddr)
        
        self.assertTrue (video.gl_load_library ())
        
        # Behaviour is undefined as long as there is no window and context.
        window = video.create_window ("OpenGL", 10, 10, 10, 10,
                                      video.SDL_WINDOW_OPENGL)
        ctx = video.gl_create_context (window)
        
        procaddr = video.gl_get_proc_address ("glGetString")
        self.assertTrue (procaddr is not None and int(procaddr) != 0)
        
        procaddr = video.gl_get_proc_address ("glForWhackoPeople")
        self.assertIsNone (procaddr)
        
        video.gl_delete_context (ctx)
        video.destroy_window (window)
        video.gl_unload_library ()

        procaddr = video.gl_get_proc_address ("glGetString")
        self.assertIsNone (procaddr)
        
    def test_gl_extension_supported (self):
        self.assertFalse (video.gl_extension_supported ("GL_EXT_bgra"))

        self.assertTrue (video.gl_load_library ())
        window = video.create_window ("OpenGL", 10, 10, 10, 10,
                                      video.SDL_WINDOW_OPENGL)
        ctx = video.gl_create_context (window)

        self.assertTrue (video.gl_extension_supported ("GL_EXT_bgra"))

        video.gl_delete_context (ctx)
        video.destroy_window (window)
        video.gl_unload_library ()
        
        self.assertFalse (video.gl_extension_supported ("GL_EXT_bgra"))
    
    def test_gl_get_set_attribute (self):
        self.assertRaises (SDLError, video.gl_get_attribute,
                           video.SDL_GL_DEPTH_SIZE)
        self.assertRaises (SDLError, video.gl_set_attribute,
                           1455, 24)
        
        self.assertTrue (video.gl_load_library ())

        window = video.create_window ("OpenGL", 10, 10, 10, 10,
                                      video.SDL_WINDOW_OPENGL)
        ctx = video.gl_create_context (window)
        
        depth = video.gl_get_attribute (video.SDL_GL_DEPTH_SIZE)

        video.gl_delete_context (ctx)
        video.destroy_window (window)
        
        newdepth = 24
        if depth == 8:
            newdepth = 16
        elif depth == 16:
            newdepth = 24
        elif depth == 24:
            newdepth = 16
        video.gl_set_attribute (video.SDL_GL_DEPTH_SIZE, newdepth)
        
        window = video.create_window ("OpenGL", 10, 10, 10, 10,
                                      video.SDL_WINDOW_OPENGL)
        ctx = video.gl_create_context (window)
        
        val = video.gl_get_attribute (video.SDL_GL_DEPTH_SIZE)
        self.assertNotEqual(depth, val)
        self.assertEqual(val, newdepth)
        
        video.gl_delete_context (ctx)
        video.destroy_window (window)
        video.gl_unload_library ()

    def test_gl_create_delete_context (self):
        self.assertRaises (TypeError, video.gl_create_context, None)
        self.assertRaises (TypeError, video.gl_create_context, "Test")
        self.assertRaises (TypeError, video.gl_create_context, 1234)
        
        window = video.create_window ("No OpenGL", 10, 10, 10, 10,
                                      video.SDL_WINDOW_BORDERLESS)
        self.assertRaises (SDLError, video.gl_create_context, window)
        video.destroy_window (window)
        
        window = video.create_window ("OpenGL", 10, 10, 10, 10,
                                      video.SDL_WINDOW_OPENGL)
        ctx = video.gl_create_context (window)

        video.gl_delete_context (ctx)
        video.destroy_window (window)
        
        #print ctx
        #window = video.create_window ("OpenGL", 10, 10, 10, 10,
        #                              video.SDL_WINDOW_OPENGL)
        #ctx = video.gl_create_context (window)

    @unittest.skip ("not implemented")
    def test_gl_make_current (self):
        pass
    
    @unittest.skip ("not implemented")
    def test_gl_set_swap_interval (self):
        pass
    
    @unittest.skip ("not implemented")
    def test_gl_get_swap_interval (self):
        pass
    
    @unittest.skip ("not implemented")
    def test_gl_swap_window (self):
        pass

if __name__ == '__main__':
    unittest.main ()
