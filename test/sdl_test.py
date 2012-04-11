import sys
import unittest
import pygame2.sdl as sdl


class SDLTest(unittest.TestCase):
    __tags__ = ["sdl"]

    def setUp(self):
        sdl.init(0)
    
    def tearDown(self):
        sdl.quit()
    
    def test_init_timer(self):
        sdl.init(sdl.SDL_INIT_TIMER)
        ret = sdl.was_init(sdl.SDL_INIT_TIMER)
        self.assertEqual(ret, sdl.SDL_INIT_TIMER)
        sdl.quit_subsystem(sdl.SDL_INIT_TIMER)

    def test_init_audio(self):
        sdl.init(sdl.SDL_INIT_AUDIO)
        ret = sdl.was_init(sdl.SDL_INIT_AUDIO)
        self.assertEqual(ret, sdl.SDL_INIT_AUDIO)
        sdl.quit_subsystem(sdl.SDL_INIT_AUDIO)

    def test_init_video(self):
        sdl.init(sdl.SDL_INIT_VIDEO)
        ret = sdl.was_init(sdl.SDL_INIT_VIDEO)
        self.assertEqual(ret, sdl.SDL_INIT_VIDEO)
        sdl.quit_subsystem(sdl.SDL_INIT_VIDEO)

    def test_init_joystick(self):
        sdl.init(sdl.SDL_INIT_JOYSTICK)
        ret = sdl.was_init(sdl.SDL_INIT_JOYSTICK)
        self.assertEqual(ret, sdl.SDL_INIT_JOYSTICK)
        sdl.quit_subsystem(sdl.SDL_INIT_JOYSTICK)

    def test_init_haptic(self):
        if sys.platform.startswith("freebsd"):
            # not supported yet
            self.skipTest("haptic is not supported on this platform")
        sdl.init(sdl.SDL_INIT_HAPTIC)
        ret = sdl.was_init(sdl.SDL_INIT_HAPTIC)
        self.assertEqual(ret, sdl.SDL_INIT_HAPTIC)
        sdl.quit_subsystem(sdl.SDL_INIT_HAPTIC)

    def test_get_error(self):
        sdl.clear_error()
        self.assertEqual(sdl.get_error(), "")

    def test_set_error(self):
        self.assertEqual(sdl.get_error(), "")
        sdl.set_error("A Unit Test Error Message")
        self.assertEqual(sdl.get_error(), "A Unit Test Error Message")
        sdl.clear_error()
        sdl.set_error("A Unit Test Error Message")
        self.assertEqual(sdl.get_error(), "A Unit Test Error Message")
        self.assertEqual(sdl.get_error(), "A Unit Test Error Message")
        sdl.clear_error()
        sdl.set_error("123456789")
        self.assertEqual(sdl.get_error(), "123456789")

if __name__ == '__main__':
    unittest.main()
