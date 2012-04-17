import sys
import unittest
import pygame2.sdl as sdl
import pygame2.sdl.version as version


class SDLVersionTest(unittest.TestCase):
    __tags__ = ["sdl"]

    def test_version(self):
        v = version.SDL_version(0, 0, 0)
        self.assertEqual(v.major, 0)
        self.assertEqual(v.minor, 0)
        self.assertEqual(v.patch, 0)

    def test_get_version(self):
        v = version.get_version()
        self.assertEqual(type(v), version.SDL_version)
        self.assertEqual(v.major, 2)
        self.assertEqual(v.minor, 0)
        self.assertEqual(v.patch, 0)

    def test_SDL_VERSIONNUM(self):
        self.assertEqual(version.SDL_VERSIONNUM(1, 2, 3), 1203)
        self.assertEqual(version.SDL_VERSIONNUM(4, 5, 6), 4506)
        self.assertEqual(version.SDL_VERSIONNUM(2, 0, 0), 2000)
        self.assertEqual(version.SDL_VERSIONNUM(17, 42, 3), 21203)

    def test_SDL_VERSION_ATLEAST(self):
        self.assertTrue(version.SDL_VERSION_ATLEAST(1, 2, 3))
        self.assertTrue(version.SDL_VERSION_ATLEAST(2, 0, 0))
        self.assertFalse(version.SDL_VERSION_ATLEAST(2, 0, 1))

    def test_get_revision(self):
        self.assertEqual(version.get_revision()[0:3], "hg-")

    def test_get_revision_number(self):
        self.assertGreaterEqual(version.get_revision_number(), 6302)

if __name__ == '__main__':
    sys.exit(unittest.main())
