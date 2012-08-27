import sys
import unittest
import pygame2.video as video
import pygame2.sdl.video as sdlvideo
import pygame2.sdl.surface as sdlsurface
from pygame2.test.util.testutils import interactive, doprint


class VideoWindowTest(unittest.TestCase):

    def setUp(self):
        if sys.version.startswith("3.1"):
            self.assertIsInstance = \
                lambda x, t: self.assertTrue(isinstance(x, t))
        video.init()

    def tearDown(self):
        video.quit()

    def test_Window(self):
        flags = sdlvideo.SDL_WINDOW_BORDERLESS
        sizes = ((1, 1), (10, 10), (10, 20), (200, 17), (640, 480), (800, 600))
        for w, h in sizes:
            window = video.Window("Window", size=(w, h), flags=flags)
            self.assertEqual(window.size, (w, h))

        self.assertRaises(TypeError, video.Window, None, None, None, None)
        self.assertRaises(TypeError, video.Window, None, None, None)
        self.assertRaises(TypeError, video.Window, None, None)
        self.assertRaises(TypeError, video.Window, "Test", None, None, None)
        self.assertRaises(TypeError, video.Window, "Test", None, None)
        self.assertRaises(TypeError, video.Window, "Test", None)
        self.assertRaises(TypeError, video.Window, "Test", (1, 1), None, None)
        self.assertRaises(TypeError, video.Window, "Test", (1, 1), None)
            
    def test_Window_title(self):
        window = video.Window("Window", size=(10, 10))
        self.assertEqual(window.title, "Window")
        window.title = "Test1234"
        self.assertEqual(window.title, "Test1234")

        window.title = None
        self.assertEqual(window.title, "None")
        window.title = 1234
        self.assertEqual(window.title, "1234")

    @interactive("Was the window shown?")
    def test_Window_show(self):
        window = video.Window("Test Show Window", size=(200, 200))
        window.show()
        doprint("""Please check, if a window with the title
'Test Show Window' is shown""")

    @interactive("Did the window vanish from your sight and pop up again?")
    def test_Window_hide(self):
        window = video.Window("Test Hide Window", size=(200, 200))
        window.show()
        doprint("""Please check, if a window with the title
'Test Hide Window' is shown""")
        window.hide()
        doprint("Please check, that the window is not shown anymore")
        window.show()
        doprint("Please check, if the window is shown again")

    @interactive("Was the window maximized?")
    def test_Window_maximize(self):
        window = video.Window("Test Maximize Window", size=(200, 200),
                              flags=sdlvideo.SDL_WINDOW_RESIZABLE)
        window.show()
        doprint("""Please check, that a window with the title
'Test Maximize Window' is shown""")
        window.maximize()
        doprint("Please check, if the window was maximized properly")

    @interactive("Was the window minimized?")
    def test_Window_minimize(self):
        window = video.Window("Test Minimize Window", size=(200, 200))
        window.show()
        doprint("""Please check, that a window with the title
'Test Minimize Window' is shown""")
        window.minimize()
        doprint("Please check, if the window was minimized properly")

    @unittest.skip("not implemented")
    def test_Window_refresh(self):
        pass

    def test_Window_get_surface(self):
        window = video.Window("Surface", size=(200, 200))
        sf = window.get_surface()
        self.assertIsInstance(sf, sdlsurface.SDL_Surface)
        

if __name__ == '__main__':
    sys.exit(unittest.main())
