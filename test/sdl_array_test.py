import sys
import unittest
import ctypes
import pygame2.sdl.array as array

singlebyteseq = [x for x in range(0x100)]
doublebyteseq = [x for x in range(0x10000)]
quadbyteseq = [0x00000000,
               0x000000FF,
               0x0000FF00,
               0x0000FFFF,
               0x00FF0000,
               0x00FF00FF,
               0x00FFFF00,
               0x00FFFFFF,
               0xFF000000,
               0xFF0000FF,
               0xFF00FF00,
               0xFFFF0000,
               0xFFFF00FF,
               0xFFFFFF00,
               0xFFFFFFFF
               ]


class SDLArrayTest(unittest.TestCase):

    def setUp(self):
        if sys.version.startswith("3.1"):
            self.assertIsInstance = \
                lambda x, t: self.assertTrue(isinstance(x, t))

    def tearDown(self):
        pass

    def test_to_ctypes(self):
        bytebuf, size = array.to_ctypes(singlebyteseq, ctypes.c_ubyte)
        self.assertEqual(size, len(singlebyteseq))
        for index, x in enumerate(bytebuf):
            self.assertEqual(x, singlebyteseq[index])

        bytebuf, size = array.to_ctypes(doublebyteseq, ctypes.c_ushort)
        self.assertEqual(size, len(doublebyteseq))
        for index, x in enumerate(bytebuf):
            self.assertEqual(x, doublebyteseq[index])

        bytebuf, size = array.to_ctypes(quadbyteseq, ctypes.c_uint)
        self.assertEqual(size, len(quadbyteseq))
        for index, x in enumerate(bytebuf):
            self.assertEqual(x, quadbyteseq[index])

    @unittest.skip("not implemented")
    def test_to_ctypes_view(self):
        singlebytes = bytearray(singlebyteseq)

if __name__ == '__main__':
    unittest.main()
