import sys
import math
import unittest
import pygame2.sdl as sdl
import pygame2.sdl.endian as endian


class SDLEndianTest(unittest.TestCase):
    __tags__ = ["sdl"]

    def test_SDL_BYTEORDER(self):
        if sys.byteorder == "little":
            self.assertEqual(endian.SDL_BYTEORDER, endian.SDL_LIL_ENDIAN)
        else:
            self.assertEqual(endian.SDL_BYTEORDER, endian.SDL_BIG_ENDIAN)

    def test_swap16(self):
        self.assertEqual(endian.swap16(0xFF00), 0x00FF)
        self.assertEqual(endian.swap16(0x0001), 0x0100)
        self.assertEqual(endian.swap16(0x0032), 0x3200)
        self.assertEqual(endian.swap16(0x0FF0), 0xF00F)
        self.assertEqual(endian.swap16(0x00FF), 0xFF00)
        self.assertEqual(endian.swap16(0x1234), 0x3412)
        if sys.byteorder == "little":
            self.assertEqual(endian.swap16, endian.swap_be_16)
            self.assertNotEqual(endian.swap16, endian.swap_le_16)
        else:
            self.assertNotEqual(endian.swap16, endian.swap_be_16)
            self.assertEqual(endian.swap16, endian.swap_le_16)

    def test_swap32(self):
        self.assertEqual(endian.swap32(0xFF000000), 0x000000FF)
        self.assertEqual(endian.swap32(0x00FF0000), 0x0000FF00)
        self.assertEqual(endian.swap32(0x0000FF00), 0x00FF0000)
        self.assertEqual(endian.swap32(0x000000FF), 0xFF000000)
        self.assertEqual(endian.swap32(0x12345678), 0x78563412)
        self.assertEqual(endian.swap32(0xFF00FF00), 0x00FF00FF)
        if sys.byteorder == "little":
            self.assertEqual(endian.swap32, endian.swap_be_32)
            self.assertNotEqual(endian.swap32, endian.swap_le_32)
        else:
            self.assertNotEqual(endian.swap32, endian.swap_be_32)
            self.assertEqual(endian.swap32, endian.swap_le_32)

    def test_swap64(self):
        self.assertEqual(endian.swap64(0xFF00000000000000), 0x00000000000000FF)
        self.assertEqual(endian.swap64(0x00FF000000000000), 0x000000000000FF00)
        self.assertEqual(endian.swap64(0x0000FF0000000000), 0x0000000000FF0000)
        self.assertEqual(endian.swap64(0x000000FF00000000), 0x00000000FF000000)
        self.assertEqual(endian.swap64(0x00000000FF000000), 0x000000FF00000000)
        self.assertEqual(endian.swap64(0x0000000000FF0000), 0x0000FF0000000000)
        self.assertEqual(endian.swap64(0x000000000000FF00), 0x00FF000000000000)
        self.assertEqual(endian.swap64(0x00000000000000FF), 0xFF00000000000000)
        self.assertEqual(endian.swap64(0x0123456789ABCDEF), 0xEFCDAB8967452301)
        if sys.byteorder == "little":
            self.assertEqual(endian.swap64, endian.swap_be_64)
            self.assertNotEqual(endian.swap64, endian.swap_le_64)
        else:
            self.assertNotEqual(endian.swap64, endian.swap_be_64)
            self.assertEqual(endian.swap64, endian.swap_le_64)

    def test_swap_float(self):
        v = -100.0
        while v < 101:
            p = endian.swap_float(v)
            self.assertNotEqual(p, v)
            self.assertEqual(endian.swap_float(p), v)
            v += 0.1
        values = (sys.float_info.epsilon,
                  sys.float_info.min,
                  sys.float_info.max,
                  - sys.float_info.min,
                  math.pi,
                  - math.pi
                  )
        for v in values:
            p = endian.swap_float(v)
            self.assertNotEqual(p, v)
            self.assertEqual(endian.swap_float(p), v)

        if sys.byteorder == "little":
            self.assertEqual(endian.swap_float, endian.swap_float_be)
            self.assertNotEqual(endian.swap_float, endian.swap_float_le)
        else:
            self.assertNotEqual(endian.swap_float, endian.swap_float_be)
            self.assertEqual(endian.swap_float, endian.swap_float_le)


if __name__ == '__main__':
    sys.exit(unittest.main())
