import sys
import unittest
import pygame2.sdl as sdl
import pygame2.sdl.keyboard as keyboard
import pygame2.sdl.scancode as scancode
import pygame2.sdl.keycode as keycode
import pygame2.sdl.video as video


class SDLKeyboardTest(unittest.TestCase):
    __tags__ = ["sdl"]

    def setUp(self):
        if sys.version.startswith("3.1"):
            self.assertIsInstance = \
                lambda x, t: self.assertTrue(isinstance(x, t))
        sdl.init(sdl.SDL_INIT_VIDEO)

    def tearDown(self):
        sdl.quit_subsystem(sdl.SDL_INIT_VIDEO)
        sdl.quit()

    def test_SDL_Keysym(self):
        keysym = keyboard.SDL_Keysym()
        self.assertEqual(keysym.scancode, 0)
        self.assertEqual(keysym.sym, 0)
        self.assertEqual(keysym.mod, 0)
        self.assertEqual(keysym.unicode, "\0")

        keysym = keyboard.SDL_Keysym(1, 2, 3, "b")
        self.assertEqual(keysym.scancode, 1)
        self.assertEqual(keysym.sym, 2)
        self.assertEqual(keysym.mod, 3)
        self.assertEqual(keysym.unicode, "b")

        uval = "\u0220"
        if sys.version_info[0] < 3:
            uval = unichr(8224)
        keysym = keyboard.SDL_Keysym(17, 32, 88, uval)
        self.assertEqual(keysym.scancode, 17)
        self.assertEqual(keysym.sym, 32)
        self.assertEqual(keysym.mod, 88)
        self.assertEqual(keysym.unicode, uval)

    def test_get_keyboard_focus(self):
        window = keyboard.get_keyboard_focus()
        self.assertEqual(window, None)
        rwin = video.create_window("", 10, 10, 10, 10, 0)
        window = keyboard.get_keyboard_focus()
        if window:
            self.assertEqual(video.get_window_id(window),
                             video.get_window_id(rwin))
        video.destroy_window(rwin)

        window = keyboard.get_keyboard_focus()
        self.assertEqual(window, None)

    def test_get_keyboard_state(self):
        states = keyboard.get_keyboard_state()
        self.assertEqual(len(states), scancode.SDL_NUM_SCANCODES)
        for state in states:
            self.assertEqual(state, 0)

    def test_get_key_from_name(self):
        for x in range(26):  # a-z
            key = keyboard.get_key_from_name(chr(x + 97))
            self.assertEqual(key, x + 97)

        val = keyboard.get_key_from_name(123)
        self.assertEqual(val, keycode.SDLK_UNKNOWN)

        for x in range(10):
            key = keyboard.get_key_from_name(x)
            self.assertEqual(key, 48 + x)

        val = keyboard.get_key_from_name(self)
        self.assertEqual(val, keycode.SDLK_UNKNOWN)

    def test_get_key_from_scancode(self):
        p = 0
        for x in (scancode.SDL_SCANCODE_A,
                  scancode.SDL_SCANCODE_B,
                  scancode.SDL_SCANCODE_C):
            key = keyboard.get_key_from_scancode(x)
            self.assertEqual(key, p + 97)
            p += 1

        p = 0
        for x in range(scancode.SDL_SCANCODE_1, scancode.SDL_SCANCODE_0):
            key = keyboard.get_key_from_scancode(x)
            self.assertEqual(key, 49 + p)
            p += 1

        self.assertRaises(TypeError, keyboard.get_key_from_scancode, self)
        self.assertRaises(TypeError, keyboard.get_key_from_scancode, "Test")
        self.assertRaises(TypeError, keyboard.get_key_from_scancode, None)

    def test_get_key_name(self):
        x = 65  # SDL maps everything against upper-case letters
        for key in range(ord('a'), ord('z')):
            ch = chr(x)
            name = keyboard.get_key_name(key)
            self.assertEqual(name, ch)
            x += 1

    def test_get_set_mod_state(self):
        initial = keyboard.get_mod_state()
        for state in(keycode.KMOD_NUM | keycode.KMOD_CAPS | keycode.KMOD_MODE,
                      keycode.KMOD_NUM | keycode.KMOD_CAPS,
                      keycode.KMOD_CAPS):
            keyboard.set_mod_state(state)
            self.assertEqual(keyboard.get_mod_state(), state)

        state = keycode.KMOD_NUM
        keyboard.set_mod_state(state)
        self.assertEqual(keyboard.get_mod_state(), state)

        keyboard.set_mod_state(initial)
        self.assertEqual(keyboard.get_mod_state(), initial)

    def test_get_scancode_from_key(self):
        codes = range(scancode.SDL_SCANCODE_1, scancode.SDL_SCANCODE_0)
        xoff = 0
        for key in range(ord('1'), ord('0')):
            code = keyboard.get_scancode_from_key(key)
            self.assertEqual(code, codes[xoff])
            xoff += 1

        key = keyboard.get_scancode_from_key(477)
        self.assertEqual(key, scancode.SDL_SCANCODE_UNKNOWN)

        self.assertRaises(TypeError, keyboard.get_scancode_from_key, None)
        self.assertRaises(TypeError, keyboard.get_scancode_from_key, "Test")
        self.assertRaises(TypeError, keyboard.get_scancode_from_key, self)

    def test_get_scancode_from_name(self):
        codes = range(scancode.SDL_SCANCODE_A, scancode.SDL_SCANCODE_Z)
        xoff = 0
        for key in range(ord('a'), ord('z')):
            ch = chr(key)
            code = keyboard.get_scancode_from_name(ch)
            self.assertEqual(code, codes[xoff])
            xoff += 1

        key = keyboard.get_scancode_from_name("")
        self.assertEqual(key, scancode.SDL_SCANCODE_UNKNOWN)

        key = keyboard.get_scancode_from_name(None)
        self.assertEqual(key, scancode.SDL_SCANCODE_UNKNOWN)

        key = keyboard.get_scancode_from_name("Test")
        self.assertEqual(key, scancode.SDL_SCANCODE_UNKNOWN)

        key = keyboard.get_scancode_from_name(self)
        self.assertEqual(key, scancode.SDL_SCANCODE_UNKNOWN)

    def test_get_scancode_name(self):
        names = range(ord('A'), ord('Z'))
        xoff = 0
        for code in range(scancode.SDL_SCANCODE_A, scancode.SDL_SCANCODE_Z):
            name = keyboard.get_scancode_name(code)
            self.assertEqual(name, chr(names[xoff]))
            xoff += 1

        name = keyboard.get_scancode_name(0)
        self.assertEqual(name, "")

        self.assertRaises(ValueError, keyboard.get_scancode_name, -22)
        self.assertRaises(ValueError, keyboard.get_scancode_name,
                           scancode.SDL_NUM_SCANCODES)

        self.assertRaises(TypeError, keyboard.get_scancode_from_key, None)
        self.assertRaises(TypeError, keyboard.get_scancode_from_key, "Test")
        self.assertRaises(TypeError, keyboard.get_scancode_from_key, self)

    @unittest.skip("not implemented")
    def test_set_text_input_rect(self):
        pass

    @unittest.skip("not implemented")
    def test_start_text_input(self):
        pass

    @unittest.skip("not implemented")
    def test_stop_text_input(self):
        pass

if __name__ == '__main__':
    sys.exit(unittest.main())
