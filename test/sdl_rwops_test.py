import os
import sys
import ctypes
import unittest
from io import BytesIO
from pygame2.compat import *
import pygame2.sdl.rwops as rwops


# TODO: extended checks for r/w operations outside of buffer ranges, invalid
# values, etc.!
class SDLRWopsTest(unittest.TestCase):
    __tags__ = ["sdl"]

    def setUp(self):
        fpath = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                             "resources")
        self.testfile = os.path.join(fpath, "rwopstest.txt")

        if sys.version.startswith("3.1"):
            self.assertIsInstance = \
                lambda x, t: self.assertTrue(isinstance(x, t))

    def tearDown(self):
        pass

    def test_SDL_RWops(self):
        rw = rwops.SDL_RWops()
        self.assertIsInstance(rw, rwops.SDL_RWops)

    def test_rw_from_file(self):
        rw = rwops.rw_from_file(self.testfile, "r")
        self.assertIsInstance(rw, rwops.SDL_RWops)
        # Read the first 42 bytes(sic!). It should be:
        # 'This is a test file for pygame2.sdl.rwops!'
        length = 42
        buf = BytesIO()
        while length >= 2:
            # Reading in two bytes - we have plain text(1-byte encoding), so
            # we read in 2 characters at a time. This means that the first
            # character is always stored in the lo byte.
            ch = rwops.read_le_16(rw)
            buf.write(byteify(chr(ch & 0x00FF), "utf-8"))
            buf.write(byteify(chr(ch >> 8), "utf-8"))
            length -= 2
        self.assertEqual(stringify(buf.getvalue(), "utf-8"),
                         "This is a test file for pygame2.sdl.rwops!")

    @unittest.skip("not implemented")
    def test_rw_from_fp(self):
        pass

    @unittest.skip("not implemented")
    def test_rw_from_mem(self):
        pass

    @unittest.skip("not implemented")
    def test_rw_from_const_mem(self):
        pass

    def test_rw_from_object(self):
        buf = BytesIO()
        rw = rwops.rw_from_object(buf)
        self.assertIsInstance(rw, rwops.SDL_RWops)

        for s in("Test", "Test", "Test", "Banana"):
            buf.write(byteify(s, "utf-8"))
            length = rwops.rw_seek(rw, 0, rwops.RW_SEEK_END)
            rwops.rw_seek(rw, 0, rwops.RW_SEEK_SET)
            self.assertEqual(len(buf.getvalue()), length)
        rwops.rw_close(rw)
        self.assertTrue(buf.closed)
        self.assertRaises(ValueError, buf.write, "Test")
        self.assertRaises(ValueError, buf.getvalue)

    def test_rw_seek_tell(self):
        data = byteify("A Teststring of length 25", "utf-8")
        buf = BytesIO(data)
        rw = rwops.rw_from_object(buf)
        self.assertIsInstance(rw, rwops.SDL_RWops)

        pos = rwops.rw_seek(rw, 0, rwops.RW_SEEK_END)
        self.assertTrue(pos == buf.tell() == len(data))
        pos = rwops.rw_seek(rw, 0, rwops.RW_SEEK_SET)
        self.assertTrue(pos == buf.tell() == 0)

        pos = rwops.rw_seek(rw, 15, rwops.RW_SEEK_CUR)
        self.assertTrue(pos == buf.tell() == 15)
        pos = rwops.rw_seek(rw, -3, rwops.RW_SEEK_CUR)
        self.assertTrue(pos == buf.tell() == 12)
        pos = rwops.rw_seek(rw, 7, rwops.RW_SEEK_CUR)
        self.assertTrue(pos == buf.tell() == 19)

        pos = rwops.rw_seek(rw, -11, rwops.RW_SEEK_END)
        self.assertTrue(pos == buf.tell() == 14)

        pos = rwops.rw_seek(rw, 8, rwops.RW_SEEK_SET)
        self.assertTrue(pos == buf.tell() == 8)

        pos = rwops.rw_seek(rw, -2, rwops.RW_SEEK_SET)
        # The String
        self.assertEqual(pos, -1)
        self.assertTrue(buf.tell() == 8)
        pos = rwops.rw_seek(rw, 12, rwops.RW_SEEK_END)
        self.assertTrue(pos == buf.tell() == len(data) + 12)

    def test_rw_read(self):
        self.assertRaises(NotImplementedError, rwops.rw_read, 0, 0, 0, 0)

    def test_rw_write(self):
        self.assertRaises(NotImplementedError, rwops.rw_read, 0, 0, 0, 0)

    def test_rw_close(self):
        data = byteify("A Teststring", "utf-8")
        buf = BytesIO(data)
        rw = rwops.rw_from_object(buf)
        self.assertIsInstance(rw, rwops.SDL_RWops)

        self.assertEqual(buf.getvalue(), data)
        rwops.rw_close(rw)
        self.assertRaises(ValueError, buf.getvalue)

    @unittest.skip("not implemented")
    def test_alloc_free_rw(self):
        pass

    def test_read_le_16(self):
        data = byteify("A Teststring", "utf-8")
        buf = BytesIO(data)
        rw = rwops.rw_from_object(buf)
        self.assertIsInstance(rw, rwops.SDL_RWops)

        ch = rwops.read_le_16(rw)
        self.assertEqual(chr(ch & 0x00FF), "A")
        self.assertEqual(chr(ch >> 8), " ")

        pos = rwops.rw_seek(rw, 8, rwops.RW_SEEK_SET)
        self.assertEqual(pos, 8)
        ch = rwops.read_le_16(rw)
        self.assertEqual(chr(ch & 0x00FF), "r")
        self.assertEqual(chr(ch >> 8), "i")

    def test_read_be_16(self):
        data = byteify("A Teststring", "utf-8")
        buf = BytesIO(data)
        rw = rwops.rw_from_object(buf)
        self.assertIsInstance(rw, rwops.SDL_RWops)

        ch = rwops.read_be_16(rw)
        self.assertEqual(chr(ch & 0x00FF), " ")
        self.assertEqual(chr(ch >> 8), "A")

        pos = rwops.rw_seek(rw, 8, rwops.RW_SEEK_SET)
        self.assertEqual(pos, 8)
        ch = rwops.read_be_16(rw)
        self.assertEqual(chr(ch & 0x00FF), "i")
        self.assertEqual(chr(ch >> 8), "r")

    def test_read_le_32(self):
        data = byteify("A Teststring", "utf-8")
        buf = BytesIO(data)
        rw = rwops.rw_from_object(buf)
        self.assertIsInstance(rw, rwops.SDL_RWops)

        ch = rwops.read_le_32(rw)
        self.assertEqual(chr(ch & 0x000000FF), "A")
        self.assertEqual(chr((ch & 0x0000FF00) >> 8), " ")
        self.assertEqual(chr((ch & 0x00FF0000) >> 16), "T")
        self.assertEqual(chr((ch & 0xFF000000) >> 24), "e")

        pos = rwops.rw_seek(rw, 8, rwops.RW_SEEK_SET)
        self.assertEqual(pos, 8)
        ch = rwops.read_le_32(rw)
        self.assertEqual(chr(ch & 0x000000FF), "r")
        self.assertEqual(chr((ch & 0x0000FF00) >> 8), "i")
        self.assertEqual(chr((ch & 0x00FF0000) >> 16), "n")
        self.assertEqual(chr((ch & 0xFF000000) >> 24), "g")

    def test_read_be_32(self):
        data = byteify("A Teststring", "utf-8")
        buf = BytesIO(data)
        rw = rwops.rw_from_object(buf)
        self.assertIsInstance(rw, rwops.SDL_RWops)

        ch = rwops.read_be_32(rw)
        self.assertEqual(chr(ch & 0x000000FF), "e")
        self.assertEqual(chr((ch & 0x0000FF00) >> 8), "T")
        self.assertEqual(chr((ch & 0x00FF0000) >> 16), " ")
        self.assertEqual(chr((ch & 0xFF000000) >> 24), "A")

        pos = rwops.rw_seek(rw, 8, rwops.RW_SEEK_SET)
        self.assertEqual(pos, 8)
        ch = rwops.read_be_32(rw)
        self.assertEqual(chr(ch & 0x000000FF), "g")
        self.assertEqual(chr((ch & 0x0000FF00) >> 8), "n")
        self.assertEqual(chr((ch & 0x00FF0000) >> 16), "i")
        self.assertEqual(chr((ch & 0xFF000000) >> 24), "r")

    def test_read_le_64(self):
        data = byteify("A Teststring 64b", "utf-8")
        buf = BytesIO(data)
        rw = rwops.rw_from_object(buf)
        self.assertIsInstance(rw, rwops.SDL_RWops)

        ch = rwops.read_le_64(rw)
        self.assertEqual(chr(ch & 0x00000000000000FF), "A")
        self.assertEqual(chr((ch & 0x000000000000FF00) >> 8), " ")
        self.assertEqual(chr((ch & 0x0000000000FF0000) >> 16), "T")
        self.assertEqual(chr((ch & 0x00000000FF000000) >> 24), "e")
        self.assertEqual(chr((ch & 0x000000FF00000000) >> 32), "s")
        self.assertEqual(chr((ch & 0x0000FF0000000000) >> 40), "t")
        self.assertEqual(chr((ch & 0x00FF000000000000) >> 48), "s")
        self.assertEqual(chr((ch & 0xFF00000000000000) >> 56), "t")

        pos = rwops.rw_seek(rw, 8, rwops.RW_SEEK_SET)
        self.assertEqual(pos, 8)
        ch = rwops.read_le_64(rw)
        self.assertEqual(chr(ch & 0x00000000000000FF), "r")
        self.assertEqual(chr((ch & 0x000000000000FF00) >> 8), "i")
        self.assertEqual(chr((ch & 0x0000000000FF0000) >> 16), "n")
        self.assertEqual(chr((ch & 0x00000000FF000000) >> 24), "g")
        self.assertEqual(chr((ch & 0x000000FF00000000) >> 32), " ")
        self.assertEqual(chr((ch & 0x0000FF0000000000) >> 40), "6")
        self.assertEqual(chr((ch & 0x00FF000000000000) >> 48), "4")
        self.assertEqual(chr((ch & 0xFF00000000000000) >> 56), "b")

    def test_read_be_64(self):
        data = byteify("A Teststring 64b", "utf-8")
        buf = BytesIO(data)
        rw = rwops.rw_from_object(buf)
        self.assertIsInstance(rw, rwops.SDL_RWops)

        ch = rwops.read_be_64(rw)
        self.assertEqual(chr(ch & 0x00000000000000FF), "t")
        self.assertEqual(chr((ch & 0x000000000000FF00) >> 8), "s")
        self.assertEqual(chr((ch & 0x0000000000FF0000) >> 16), "t")
        self.assertEqual(chr((ch & 0x00000000FF000000) >> 24), "s")
        self.assertEqual(chr((ch & 0x000000FF00000000) >> 32), "e")
        self.assertEqual(chr((ch & 0x0000FF0000000000) >> 40), "T")
        self.assertEqual(chr((ch & 0x00FF000000000000) >> 48), " ")
        self.assertEqual(chr((ch & 0xFF00000000000000) >> 56), "A")

        pos = rwops.rw_seek(rw, 8, rwops.RW_SEEK_SET)
        self.assertEqual(pos, 8)
        ch = rwops.read_be_64(rw)
        self.assertEqual(chr(ch & 0x00000000000000FF), "b")
        self.assertEqual(chr((ch & 0x000000000000FF00) >> 8), "4")
        self.assertEqual(chr((ch & 0x0000000000FF0000) >> 16), "6")
        self.assertEqual(chr((ch & 0x00000000FF000000) >> 24), " ")
        self.assertEqual(chr((ch & 0x000000FF00000000) >> 32), "g")
        self.assertEqual(chr((ch & 0x0000FF0000000000) >> 40), "n")
        self.assertEqual(chr((ch & 0x00FF000000000000) >> 48), "i")
        self.assertEqual(chr((ch & 0xFF00000000000000) >> 56), "r")

    def test_write_le_16(self):
        data = byteify("A Teststring", "utf-8")
        buf = BytesIO(data)
        rw = rwops.rw_from_object(buf)
        self.assertIsInstance(rw, rwops.SDL_RWops)

        value = ((ord("q") << 8) | (ord("%")))
        rwops.write_le_16(rw, value)
        self.assertEqual(stringify(buf.getvalue(), "utf-8"), "%qTeststring")

        rwops.rw_seek(rw, 6, rwops.RW_SEEK_SET)
        rwops.write_le_16(rw, value)
        self.assertEqual(stringify(buf.getvalue(), "utf-8"), "%qTest%qring")

    def test_write_be_16(self):
        data = byteify("A Teststring", "utf-8")
        buf = BytesIO(data)
        rw = rwops.rw_from_object(buf)
        self.assertIsInstance(rw, rwops.SDL_RWops)

        value = ((ord("q") << 8) | (ord("%")))
        rwops.write_be_16(rw, value)
        self.assertEqual(stringify(buf.getvalue(), "utf-8"), "q%Teststring")

        rwops.rw_seek(rw, 6, rwops.RW_SEEK_SET)
        rwops.write_be_16(rw, value)
        self.assertEqual(stringify(buf.getvalue(), "utf-8"), "q%Testq%ring")

    def test_write_le_32(self):
        data = byteify("A Teststring", "utf-8")
        buf = BytesIO(data)
        rw = rwops.rw_from_object(buf)
        self.assertIsInstance(rw, rwops.SDL_RWops)

        value = ((ord("a") << 24) |
                 (ord("c") << 16) |
                 (ord("f") <<  8) |
                 (ord("z"))
                 )
        rwops.write_le_32(rw, value)
        self.assertEqual(stringify(buf.getvalue(), "utf-8"), "zfcaststring")

        rwops.rw_seek(rw, 6, rwops.RW_SEEK_SET)
        rwops.write_le_32(rw, value)
        self.assertEqual(stringify(buf.getvalue(), "utf-8"), "zfcastzfcang")

    def test_write_be_32(self):
        data = byteify("A Teststring", "utf-8")
        buf = BytesIO(data)
        rw = rwops.rw_from_object(buf)
        self.assertIsInstance(rw, rwops.SDL_RWops)

        value = ((ord("a") << 24) |
                 (ord("c") << 16) |
                 (ord("f") <<  8) |
                 (ord("z"))
                 )
        rwops.write_be_32(rw, value)
        self.assertEqual(stringify(buf.getvalue(), "utf-8"), "acfzststring")

        rwops.rw_seek(rw, 6, rwops.RW_SEEK_SET)
        rwops.write_be_32(rw, value)
        self.assertEqual(stringify(buf.getvalue(), "utf-8"), "acfzstacfzng")

    def test_write_le_64(self):
        data = byteify("A Teststring", "utf-8")
        buf = BytesIO(data)
        rw = rwops.rw_from_object(buf)
        self.assertIsInstance(rw, rwops.SDL_RWops)

        value = ((ord("q") << 56) |
                 (ord("w") << 48) |
                 (ord("b") << 40) |
                 (ord("k") << 32) |
                 (ord("a") << 24) |
                 (ord("c") << 16) |
                 (ord("f") <<  8) |
                 (ord("z"))
                 )

        rwops.write_le_64(rw, value)
        self.assertEqual(stringify(buf.getvalue(), "utf-8"), "zfcakbwqring")

        rwops.rw_seek(rw, 4, rwops.RW_SEEK_SET)
        rwops.write_le_64(rw, value)
        self.assertEqual(stringify(buf.getvalue(), "utf-8"), "zfcazfcakbwq")

    def test_write_be_64(self):
        data = byteify("A Teststring", "utf-8")
        buf = BytesIO(data)
        rw = rwops.rw_from_object(buf)
        self.assertIsInstance(rw, rwops.SDL_RWops)

        value = ((ord("q") << 56) |
                 (ord("w") << 48) |
                 (ord("b") << 40) |
                 (ord("k") << 32) |
                 (ord("a") << 24) |
                 (ord("c") << 16) |
                 (ord("f") <<  8) |
                 (ord("z"))
                 )

        rwops.write_be_64(rw, value)
        self.assertEqual(stringify(buf.getvalue(), "utf-8"), "qwbkacfzring")

        rwops.rw_seek(rw, 4, rwops.RW_SEEK_SET)
        rwops.write_be_64(rw, value)
        self.assertEqual(stringify(buf.getvalue(), "utf-8"), "qwbkqwbkacfz")

if __name__ == '__main__':
    sys.exit(unittest.main())
