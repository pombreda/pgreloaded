import sys
import unittest
import pygame2.sdl as sdl
import pygame2.sdl.hints as hints


class SDLHintsTest(unittest.TestCase):
    __tags__ = ["sdl"]

    def setUp(self):
        sdl.init(sdl.SDL_INIT_EVERYTHING)

    def tearDown(self):
        sdl.quit_subsystem(sdl.SDL_INIT_EVERYTHING)
        sdl.quit()

    def test_clear_hints(self):
        self.assertEqual(hints.set_hint("TEST", "32"), 1)
        self.assertEqual(hints.get_hint("TEST"), "32")
        hints.clear_hints()
        self.assertEqual(hints.get_hint("TEST"), None)

    def test_get_hint(self):
        self.assertEqual(hints.set_hint("TEST", "32"), 1)
        self.assertEqual(hints.get_hint("TEST"), "32")
        self.assertEqual(hints.set_hint(hints.SDL_HINT_RENDER_DRIVER,
                                        "dummy"), 1)
        self.assertEqual(hints.get_hint(hints.SDL_HINT_RENDER_DRIVER), "dummy")

    def test_set_hint(self):
        self.assertEqual(hints.set_hint("TEST", "32"), 1)
        self.assertEqual(hints.get_hint("TEST"), "32")
        self.assertEqual(hints.set_hint("TEST", "abcdef"), 1)
        self.assertEqual(hints.get_hint("TEST"), "abcdef")
        self.assertEqual(hints.set_hint("", ""), 1)
        self.assertEqual(hints.get_hint(""), "")

    def test_set_hint_with_priority(self):
        self.assertEqual(hints.set_hint_with_priority
                         ("TEST", "32", hints.SDL_HINT_DEFAULT), 1)
        self.assertEqual(hints.get_hint("TEST"), "32")
        self.assertEqual(hints.set_hint_with_priority
                         ("TEST", "abcdef", hints.SDL_HINT_NORMAL), 1)
        self.assertEqual(hints.get_hint("TEST"), "abcdef")
        self.assertEqual(hints.set_hint_with_priority
                         ("", "", hints.SDL_HINT_OVERRIDE), 1)
        self.assertEqual(hints.get_hint(""), "")


        self.assertRaises(ValueError, hints.set_hint_with_priority,
                          "TEST", "123456789", 12)
        self.assertRaises(ValueError, hints.set_hint_with_priority,
                          "TEST", "123456789", -78)
        self.assertRaises(ValueError, hints.set_hint_with_priority,
                          "TEST", "123456789", None)
        self.assertRaises(ValueError, hints.set_hint_with_priority,
                          "TEST", "123456789", "bananas")

if __name__ == '__main__':
    sys.exit(unittest.main())
