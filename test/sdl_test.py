import sys
import unittest
import pygame2.sdl as sdl

class SDLTest (unittest.TestCase):
    __tags__ = [ "sdl" ]
    
    def test_init_timer (self):
        self.assertEqual (sdl.init (sdl.SDL_INIT_TIMER), 0)
        ret = sdl.was_init (sdl.SDL_INIT_TIMER)
        self.assertEqual (sdl.SDL_INIT_TIMER, sdl.SDL_INIT_TIMER)
        sdl.quit_subsystem (sdl.SDL_INIT_TIMER)
        sdl.quit ()
        
    def test_init_audio (self):
        self.assertEqual (sdl.init (sdl.SDL_INIT_AUDIO), 0)
        ret = sdl.was_init (sdl.SDL_INIT_AUDIO)
        self.assertEqual (ret, sdl.SDL_INIT_AUDIO)
        sdl.quit_subsystem (sdl.SDL_INIT_AUDIO)
        sdl.quit ()
        
    def test_init_video (self):
        self.assertEqual (sdl.init (sdl.SDL_INIT_VIDEO), 0)
        ret = sdl.was_init (sdl.SDL_INIT_VIDEO)
        self.assertEqual (ret, sdl.SDL_INIT_VIDEO)
        sdl.quit_subsystem (sdl.SDL_INIT_VIDEO)
        sdl.quit ()
        
    def test_init_joystick (self):
        self.assertEqual (sdl.init (sdl.SDL_INIT_JOYSTICK), 0)
        ret = sdl.was_init (sdl.SDL_INIT_JOYSTICK)
        self.assertEqual (ret, sdl.SDL_INIT_JOYSTICK)
        sdl.quit_subsystem (sdl.SDL_INIT_JOYSTICK)
        sdl.quit ()
        
    def test_init_haptic (self):
        if sys.platform.startswith ("freebsd"):
            return # not supported yet
        self.assertEqual (sdl.init (sdl.SDL_INIT_HAPTIC), 0)
        ret = sdl.was_init (sdl.SDL_INIT_HAPTIC)
        self.assertEqual (ret, sdl.SDL_INIT_HAPTIC)
        sdl.quit_subsystem (sdl.SDL_INIT_HAPTIC)
        sdl.quit ()

if __name__ == '__main__':
    unittest.main ()
