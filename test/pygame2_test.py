import sys
import unittest
import pygame2


class Pygame2Test(unittest.TestCase):
    def test_get_set_dll_path(self):
        if sys.platform in ("win32", "cli"):
            self.assertIsNotNone(pygame2.get_dll_path())
        else:
            self.assertIsNone(pygame2.get_dll_path())
        # TODO

if __name__ == '__main__':
    unittest.main()
