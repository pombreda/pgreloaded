import sys
import unittest
import pygame2.sdl as sdl
import pygame2.sdl.clipboard as clipboard
from pygame2.test.util.testutils import interactive, doprint


def is_win_or_mac():
    return sys.platform in ("win32", "cygwin", "darwin")


class SDLClipboardTest(unittest.TestCase):
    __tags__ = ["sdl"]

    def setUp(self):
        sdl.init(sdl.SDL_INIT_EVERYTHING)

    def tearDown(self):
        sdl.quit_subsystem(sdl.SDL_INIT_EVERYTHING)
        sdl.quit()

    @unittest.skipIf(not is_win_or_mac(), "we would need a SDL window")
    @interactive()
    def test_has_clipboard_text(self):
        doprint("Please put some text on the clipboard")
        self.assertTrue(clipboard.has_clipboard_text())

    @unittest.skipIf(not is_win_or_mac(), "we would need a SDL window")
    @interactive("Does the shown value match the clipboard content?")
    def test_get_clipboard_text(self):
        doprint("Please put some text on the clipboard")
        retval = clipboard.get_clipboard_text()
        doprint("Clipboard content: '%s'" % retval)

    @unittest.skipIf(not is_win_or_mac(), "we would need a SDL window")
    def test_set_clipboard_text(self):
        self.assertIsNone(clipboard.set_clipboard_text("Test content"))
        retval = clipboard.get_clipboard_text()
        self.assertEqual(retval, "Test content")

        self.assertIsNone(clipboard.set_clipboard_text(""))
        retval = clipboard.get_clipboard_text()
        self.assertEqual(retval, "")

        self.assertIsNone(clipboard.set_clipboard_text("Test content"))
        retval = clipboard.get_clipboard_text()
        self.assertEqual(retval, "Test content")

        self.assertIsNone(clipboard.set_clipboard_text(None))
        retval = clipboard.get_clipboard_text()
        self.assertEqual(retval, str(None))

if __name__ == '__main__':
    unittest.main()
