import unittest
import pygame2.sdl as sdl
import pygame2.sdl.error as error

class SDLErrorTest (unittest.TestCase):
    __tags__ = [ "sdl" ]
    
    def setUp (self):
        sdl.init (sdl.SDL_INIT_EVERYTHING)
        error.clear_error ()
    
    def tearDown (self):
        sdl.quit_subsystem (sdl.SDL_INIT_EVERYTHING)
        sdl.quit ()
    
    def test_get_error (self):
        self.assertEqual (error.get_error (), "")
        
    def test_set_error (self):
        self.assertEqual (error.get_error (), "")
        error.set_error ("A Unit Test Error Message")
        self.assertEqual (error.get_error (), "A Unit Test Error Message")
        error.clear_error ()
        error.set_error ("A Unit Test Error Message")
        self.assertEqual (error.get_error (), "A Unit Test Error Message")
        self.assertEqual (error.get_error (), "A Unit Test Error Message")
        error.clear_error ()
        error.set_error ("123456789")
        self.assertEqual (error.get_error (), "123456789")

if __name__ == '__main__':
    unittest.main ()
