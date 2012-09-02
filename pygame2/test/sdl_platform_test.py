import sys
import unittest
import pygame2.sdl as sdl
import pygame2.sdl.platform as platform


class SDLPlatformTest(unittest.TestCase):
    __tags__ = ["sdl"]

    def test_get_platform(self):
        retval = platform.get_platform()
        if sys.platform in ("win32", "cygwin", "cli"):
            self.assertEqual(retval, "Windows")
        elif sys.platform.startswith("linux"):
            self.assertEqual(retval, "Linux")
        elif sys.platform.startswith("freebsd"):
            self.assertEqual(retval, "FreeBSD")
        elif sys.platform.startswith("darwin"):
            self.assertEqial(retval, "Mac OS X")
        # Do not check others atm, since we are unsure about what Python will
        # return here.

if __name__ == '__main__':
    sys.exit(unittest.main())
