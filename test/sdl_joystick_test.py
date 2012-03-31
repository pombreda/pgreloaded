import sys
import unittest
import pygame2.sdl as sdl
from pygame2.sdl.error import SDLError
from pygame2.sdl.events import SDL_QUERY, SDL_ENABLE, SDL_IGNORE
import pygame2.sdl.joystick as joystick

class SDLJoystickTest (unittest.TestCase):
    __tags__ = [ "sdl" ]

    def setUp (self):
        if sys.version.startswith ("3.1"):
            self.assertIsInstance = lambda x, t: self.assertTrue (isinstance (x, t))
        sdl.init (sdl.SDL_INIT_JOYSTICK)
        self.jcount = joystick.joystick_num_joysticks ()
    
    def tearDown (self):
        sdl.quit_subsystem (sdl.SDL_INIT_JOYSTICK)
        sdl.quit ()

    def test_joystick_num_joysticks (self):
        retval = joystick.joystick_num_joysticks ()
        self.assertGreaterEqual (retval, 0)

    def test_joystick_name (self):
        if self.jcount == 0:
            self.skipTest ("no joysticks detected")
        for index in range (self.jcount):
            name = joystick.joystick_name (index)
            self.assertIsInstance (name, str)

        self.assertRaises (SDLError, joystick.joystick_name, self.jcount + 1)
        self.assertRaises (SDLError, joystick.joystick_name, -10)
        self.assertRaises (TypeError, joystick.joystick_name, "Test")
        self.assertRaises (TypeError, joystick.joystick_name, None)

    def test_joystick_open_opened_close (self):
        if self.jcount == 0:
            self.skipTest ("no joysticks detected")
        for index in range (self.jcount):
            stick = joystick.joystick_open (index)
            self.assertIsInstance (stick, joystick.SDL_Joystick)
            self.assertTrue (joystick.joystick_opened (index))
            joystick.joystick_close (stick)
            self.assertFalse (joystick.joystick_opened (index))

        self.assertRaises (SDLError, joystick.joystick_open, self.jcount + 1)
        self.assertRaises (SDLError, joystick.joystick_open, -10)
        self.assertRaises (TypeError, joystick.joystick_open, "Test")
        self.assertRaises (TypeError, joystick.joystick_open, None)
    
    def test_joystick_index (self):
        if self.jcount == 0:
            self.skipTest ("no joysticks detected")
        for index in range (self.jcount):
            stick = joystick.joystick_open (index)
            self.assertIsInstance (stick, joystick.SDL_Joystick)
            self.assertEqual (joystick.joystick_index (stick), index)
            joystick.joystick_close (stick)
        pass
    
    def test_joystick_num_axes (self):
        if self.jcount == 0:
            self.skipTest ("no joysticks detected")
        for index in range (self.jcount):
            stick = joystick.joystick_open (index)
            self.assertIsInstance (stick, joystick.SDL_Joystick)
            axes = joystick.joystick_num_axes (stick)
            self.assertGreaterEqual (axes, 0)
            joystick.joystick_close (stick)
    
    def test_joystick_num_balls (self):
        if self.jcount == 0:
            self.skipTest ("no joysticks detected")
        for index in range (self.jcount):
            stick = joystick.joystick_open (index)
            self.assertIsInstance (stick, joystick.SDL_Joystick)
            balls = joystick.joystick_num_balls (stick)
            self.assertGreaterEqual (balls, 0)
            joystick.joystick_close (stick)
    
    def test_joystick_num_buttons (self):
        if self.jcount == 0:
            self.skipTest ("no joysticks detected")
        for index in range (self.jcount):
            stick = joystick.joystick_open (index)
            self.assertIsInstance (stick, joystick.SDL_Joystick)
            buttons = joystick.joystick_num_buttons (stick)
            self.assertGreaterEqual (buttons, 0)
            joystick.joystick_close (stick)
    
    def test_joystick_num_hats (self):
        if self.jcount == 0:
            self.skipTest ("no joysticks detected")
        for index in range (self.jcount):
            stick = joystick.joystick_open (index)
            self.assertIsInstance (stick, joystick.SDL_Joystick)
            hats = joystick.joystick_num_hats (stick)
            self.assertGreaterEqual (hats, 0)
            joystick.joystick_close (stick)
    
    def test_joystick_update (self):
        if self.jcount == 0:
            self.skipTest ("no joysticks detected")
        joystick.joystick_update ()
    
    def test_joystick_event_state (self):
        if self.jcount == 0:
            self.skipTest ("no joysticks detected")
        for state in (SDL_IGNORE, SDL_ENABLE):
            news = joystick.joystick_event_state (state)
            self.assertEqual (news, state)
            query = joystick.joystick_event_state (SDL_QUERY)
            self.assertEqual (query, state)
    
    def test_joystick_get_axis (self):
        if self.jcount == 0:
            self.skipTest ("no joysticks detected")
        for index in range (self.jcount):
            stick = joystick.joystick_open (index)
            for axis in range (joystick.joystick_num_axes (stick)):
                val = joystick.joystick_get_axis (stick, axis)
                self.assertTrue (-32768 <= val <= 32767)
            joystick.joystick_close (stick)
    
    def test_joystick_get_ball (self):
        if self.jcount == 0:
            self.skipTest ("no joysticks detected")
        for index in range (self.jcount):
            stick = joystick.joystick_open (index)
            for ball in range (joystick.joystick_num_balls (stick)):
                dx, dy = joystick.joystick_get_ball (stick, ball)
                self.assertIsInstance (dx, int)
                self.assertIsInstance (dy, int)
                # TODO
            joystick.joystick_close (stick)
    
    def test_joystick_get_hat (self):
        if self.jcount == 0:
            self.skipTest ("no joysticks detected")
        for index in range (self.jcount):
            stick = joystick.joystick_open (index)
            for hat in range (joystick.joystick_num_hats (stick)):
                val = joystick.joystick_get_hat (stick, hat)
                self.assertIsInstance (val, int)
                # TODO
            joystick.joystick_close (stick)
    
    def test_joystick_get_button (self):
        if self.jcount == 0:
            self.skipTest ("no joysticks detected")
        for index in range (self.jcount):
            stick = joystick.joystick_open (index)
            for button in range (joystick.joystick_num_buttons (stick)):
                val = joystick.joystick_get_button (stick, button)
                self.assertIsInstance (val, bool)
            joystick.joystick_close (stick)
        pass

if __name__ == '__main__':
    unittest.main ()
