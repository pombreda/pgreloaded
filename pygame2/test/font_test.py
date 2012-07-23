import sys
import unittest
import pygame2.font as font


class FontTest(unittest.TestCase):
    __tags__ = []

    def test_init(self):
        font.init()
        
    def test_list_fonts(self):
        sansfonts = [f for f in font.list_fonts() if "sans" in f[0]]
        self.assertGreaterEqual(len(sansfonts), 1)

    def test_get_fonts(self):
        fontnames = ["sans", "arial", "helvetica", "times new roman", "serif"]
        # At least two fonts must be found.
        success = 0
        for fname in fontnames:
            count = len(font.get_fonts(fname))
            if count >= 1:
                success += 1
            count = len(font.get_fonts(fname, font.STYLE_BOLD))
            if count >= 1:
                success += 1
            count = len(font.get_fonts(fname, font.STYLE_ITALIC))
            if count >= 1:
                success += 1
            count = len(font.get_fonts(fname, font.STYLE_ITALIC|font.STYLE_BOLD))
            if count >= 1:
                success += 1
        
        self.assertGreaterEqual(success, 4,
            "did not meet enough font criteria for get_fonts()")
        
    def test_get_font(self):
        fontnames = ["sans", "arial", "helvetica", "times new roman", "serif"]
        # At least two fonts must be found.
        success = 0
        for fname in fontnames:
            fontfile = font.get_font(fname)
            if fontfile is not None:
                success += 1
        
        self.assertGreaterEqual(success, 2,
            "could not find the required fonts for get_font()")

if __name__ == '__main__':
    sys.exit(unittest.main())
