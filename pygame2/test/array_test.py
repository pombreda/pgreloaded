import sys
import array
import ctypes
import struct
import unittest
import pygame2.array as pgarray

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

singlebytebuf = array.array("B", singlebyteseq)
doublebytebuf = array.array("H", doublebyteseq)
quadbytebuf = array.array("I", quadbyteseq)

USHORT_SIZE = struct.calcsize("H")
UINT_SIZE = struct.calcsize("I")
UBYTE_SIZE = struct.calcsize("B")


def create_16b(seq, offset):
    if sys.byteorder == 'little':
        return (seq[offset] | seq[offset + 1] << 8)
    else:
        return (seq[offset] << 8 | seq[offset + 1])


def create_32b(seq, size, offset):
    if sys.byteorder == 'little':
        if size == 1:
            return (seq[offset] |
                    seq[offset + 1] << 8 |
                    seq[offset + 2] << 16 |
                    seq[offset + 3] << 24)
        elif size == 2:
            return (seq[offset] | seq[offset + 1] << 16)
    else:
        if size == 1:
            return (seq[offset] << 24 |
                    seq[offset + 1] << 16 |
                    seq[offset + 2] << 8 |
                    seq[offset + 3])
        elif size == 2:
            return (seq[offset] << 16 | seq[offset + 1])


def create_64b(seq, size, offset):
    if sys.byteorder == 'little':
        if size == 1:
            return (seq[offset] |
                    seq[offset + 1] << 8 |
                    seq[offset + 2] << 16 |
                    seq[offset + 3] << 24 |
                    seq[offset + 4] << 32 |
                    seq[offset + 5] << 40 |
                    seq[offset + 6] << 48 |
                    seq[offset + 7] << 56)
        elif size == 2:
            return (seq[offset] |
                    seq[offset + 1] << 16 |
                    seq[offset + 2] << 32 |
                    seq[offset + 3] << 48)
        elif size == 4:
            return (seq[offset] | seq[offset + 1] << 32)

    else:
        if size == 1:
            return (seq[offset] << 56 |
                    seq[offset + 1] << 48 |
                    seq[offset + 2] << 40 |
                    seq[offset + 3] << 32 |
                    seq[offset + 4] << 24 |
                    seq[offset + 5] << 16 |
                    seq[offset + 6] << 8 |
                    seq[offset + 7])
        elif size == 2:
            return (seq[offset] << 48 |
                    seq[offset + 1] << 32 |
                    seq[offset + 2] << 16 |
                    seq[offset + 3])
        elif size == 4:
            return (seq[offset] << 32 | seq[offset])


def lobyte16(val):
    return val & 0x00FF


def hibyte16(val):
    return val >> 8 & 0x00FF


def lobytes32(val):
    return val & 0x0000FFFF


def hibytes32(val):
    return val >> 16 & 0x0000FFFF


def ltrbyte32(val, pos):
    if sys.byteorder == 'little':
        if pos == 0:
            return val & 0x000000FF
        elif pos == 1:
            return (val & 0x0000FF00) >> 8
        elif pos == 2:
            return (val & 0x00FF0000) >> 16
        elif pos == 3:
            return (val & 0xFF000000) >> 24
        else:
            raise IndexError("invalid position")
    else:
        if pos == 3:
            return (val & 0x000000FF)
        elif pos == 2:
            return (val & 0x0000FF00) >> 8
        elif pos == 1:
            return (val & 0x00FF0000) >> 16
        elif pos == 0:
            return (val & 0xFF000000) >> 24
        else:
            raise IndexError("invalid position")


class ArrayTest(unittest.TestCase):

    def setUp(self):
        if sys.version.startswith("3.1"):
            self.assertIsInstance = \
                lambda x, t: self.assertTrue(isinstance(x, t))

    def tearDown(self):
        pass

    def test_to_ctypes(self):
        for seq, dtype in ((singlebyteseq, ctypes.c_ubyte),
                           (singlebytebuf, ctypes.c_ubyte),
                           (doublebyteseq, ctypes.c_ushort),
                           (doublebytebuf, ctypes.c_ushort),
                           (quadbyteseq, ctypes.c_uint),
                           (quadbytebuf, ctypes.c_uint)):
            bytebuf, size = pgarray.to_ctypes(seq, dtype)
            self.assertEqual(size, len(seq))
            for index, x in enumerate(bytebuf):
                self.assertEqual(x, seq[index])

    def test_CTypesView__singlebytes(self):
        buf1 = pgarray.CTypesView(singlebyteseq, docopy=True)
        buf2 = pgarray.CTypesView(singlebytebuf, docopy=False)
        for singlebytes, shared in ((buf1, False), (buf2, True)):
            self.assertIsInstance(singlebytes, pgarray.CTypesView)
            # Pypy 1.8.0 does not support ctypes.from_buffer(), hence we
            # never will receive a shared one
            if hasattr(sys, "pypy_version_info"):
                shared = False
            self.assertEqual(singlebytes.is_shared, shared)
            self.assertEqual(singlebytes.bytesize, len(singlebyteseq))
            for index, val in enumerate(singlebytes.to_bytes()):
                self.assertEqual(val, singlebyteseq[index])

            offset = 0
            for val in singlebytes.to_uint16():
                seqval = create_16b(singlebyteseq, offset)
                self.assertEqual(val, seqval)
                offset += 2

            offset = 0
            for val in singlebytes.to_uint32():
                seqval = create_32b(singlebyteseq, 1, offset)
                self.assertEqual(val, seqval)
                offset += 4

            offset = 0
            for val in singlebytes.to_uint64():
                seqval = create_64b(singlebyteseq, 1, offset)
                self.assertEqual(val, seqval)
                offset += 8

    def test_CTypesView__doublebytes(self):
        buf1 = pgarray.CTypesView(doublebyteseq, USHORT_SIZE, docopy=True)
        buf2 = pgarray.CTypesView(doublebytebuf, USHORT_SIZE, docopy=False)
        for singlebytes, shared in ((buf1, False), (buf2, True)):
            self.assertIsInstance(singlebytes, pgarray.CTypesView)
            # Pypy 1.8.0 does not support ctypes.from_buffer(), hence we
            # never will receive a shared one
            if hasattr(sys, "pypy_version_info"):
                shared = False
            self.assertEqual(singlebytes.is_shared, shared)
            self.assertEqual(singlebytes.bytesize, len(doublebyteseq) * 2)
            offset = 0
            cnt = 0
            for val in singlebytes.to_bytes():
                if cnt > 0:
                    self.assertEqual(val, hibyte16(doublebyteseq[offset]))
                    cnt = 0
                    offset += 1
                else:
                    self.assertEqual(val, lobyte16(doublebyteseq[offset]))
                    cnt += 1

            offset = 0
            for val in singlebytes.to_uint16():
                self.assertEqual(val, doublebyteseq[offset])
                offset += 1

            offset = 0
            for val in singlebytes.to_uint32():
                seqval = create_32b(doublebyteseq, 2, offset)
                self.assertEqual(val, seqval)
                offset += 2

            offset = 0
            for val in singlebytes.to_uint64():
                seqval = create_64b(doublebyteseq, 2, offset)
                self.assertEqual(val, seqval)
                offset += 4

    def test_CTypesView__quadbytes(self):
        buf1 = pgarray.CTypesView(quadbyteseq, UINT_SIZE, docopy=True)
        buf2 = pgarray.CTypesView(quadbytebuf, UINT_SIZE, docopy=False)
        for singlebytes, shared in ((buf1, False), (buf2, True)):
            self.assertIsInstance(singlebytes, pgarray.CTypesView)
            # Pypy 1.8.0 does not support ctypes.from_buffer(), hence we
            # never will receive a shared one
            if hasattr(sys, "pypy_version_info"):
                shared = False
            self.assertEqual(singlebytes.is_shared, shared)
            self.assertEqual(singlebytes.bytesize, len(quadbyteseq) * 4)
            offset = 0
            cnt = 0
            for val in singlebytes.to_bytes():
                self.assertEqual(val, ltrbyte32(quadbyteseq[offset], cnt))
                if cnt == 3:
                    offset += 1
                    cnt = 0
                else:
                    cnt += 1

            cnt = 0
            offset = 0
            for val in singlebytes.to_uint16():
                if cnt > 0:
                    self.assertEqual(val, hibytes32(quadbyteseq[offset]))
                    cnt = 0
                    offset += 1
                else:
                    self.assertEqual(val, lobytes32(quadbyteseq[offset]))
                    cnt += 1

            offset = 0
            for val in singlebytes.to_uint32():
                self.assertEqual(val, quadbyteseq[offset])
                offset += 1

            offset = 0
            for val in singlebytes.to_uint64():
                seqval = create_64b(quadbyteseq, 4, offset)
                self.assertEqual(val, seqval)
                offset += 2

    def test_CTypesView__repr__(self):
        seqs = ((singlebyteseq, UBYTE_SIZE, 1, False),
                (doublebyteseq, USHORT_SIZE, 2, False),
                (quadbyteseq, UINT_SIZE, 4, False),
                (singlebytebuf, UBYTE_SIZE, 1, True),
                (doublebytebuf, USHORT_SIZE, 2, True),
                (quadbytebuf, UINT_SIZE, 4, True),
                )
        for seq, size, factor, shared in seqs:
            buf = pgarray.CTypesView(seq, size, not shared)
            otype = type(seq).__name__
            if not shared:
                otype = 'array'

            # Pypy 1.8.0 does not support ctypes.from_buffer(), hence we
            # never will receive a shared one
            if hasattr(sys, "pypy_version_info"):
                shared = False
            text = "CTypesView(type=%s, bytesize=%d, shared=%s)" % \
                (otype, len(seq) * factor, shared)
            self.assertEqual(text, repr(buf))

    def test_MemoryView(self):
        self.assertRaises(TypeError, pgarray.MemoryView, 5, 1, (1,))
        self.assertRaises(TypeError, pgarray.MemoryView, None, 1, (1,))

        source = "Example buffer"
        view = pgarray.MemoryView(source, 1, (len(source),))
        for index, val in enumerate(view):
            self.assertEqual(val, source[index])

        view = pgarray.MemoryView(source, 1, (2, 7))
        word1 = view[0]  # "Example"
        word2 = view[1]  # " buffer"
        self.assertEqual(len(view), 2)
        self.assertEqual(len(word1), 7)
        self.assertEqual(len(word2), 7)
        for index, val in enumerate(word1):
            self.assertEqual(val, source[index])
        for index, val in enumerate(word2):
            self.assertEqual(val, source[index + 7])
        # TODO: more tests

    def test_MemoryView_ndim_strides(self):
        source = "Example buffer"
        view = pgarray.MemoryView(source, 1, (len(source),))
        self.assertEqual(view.ndim, 1)
        self.assertEqual(view.strides, (len(source),))
        view = pgarray.MemoryView(source, 1, (2, 7))
        self.assertEqual(view.ndim, 2)
        self.assertEqual(view.strides, (2, 7))
        view = pgarray.MemoryView(source, 1, (7, 2))
        self.assertEqual(view.ndim, 2)
        self.assertEqual(view.strides, (7, 2))
        view = pgarray.MemoryView(source, 1, (2, 2, 2))
        self.assertEqual(view.ndim, 3)
        self.assertEqual(view.strides, (2, 2, 2))

    def test_MemoryView_itemsize(self):
        source = "Example buffer"
        view = pgarray.MemoryView(source, 1, (len(source),))
        self.assertEqual(view.itemsize, 1)
        view = pgarray.MemoryView(source, 7, (1, 7))
        self.assertEqual(view.itemsize, 7)

    def test_MemoryView_size(self):
        source = "Example buffer"
        view = pgarray.MemoryView(source, 1, (len(source),))
        self.assertEqual(view.size, len(source))
        view = pgarray.MemoryView(source, 7, (1, 7))
        self.assertEqual(view.size, len(source))

    def test_MemoryView_source(self):
        source = "Example buffer"
        view = pgarray.MemoryView(source, 1, (len(source),))
        self.assertEqual(view.source, source)

    def test_to_tuple(self):
        ar = (ctypes.c_int * 20)()
        for i in range(20):
            ar[i] = i
        vtuple = pgarray.to_tuple(ar)
        self.assertIsInstance(vtuple, tuple)
        for index, value in enumerate(vtuple):
            self.assertEqual(value, ar[index])

    def test_to_list(self):
        ar = (ctypes.c_int * 20)()
        for i in range(20):
            ar[i] = i
        vlist = pgarray.to_list(ar)
        self.assertIsInstance(vlist, list)
        for index, value in enumerate(vlist):
            self.assertEqual(value, ar[index])

    def test_create_array(self):
        barr = bytes(bytearray(singlebyteseq))
        for i in (1, 2, 4, 8):
            parr = pgarray.create_array(barr, i)
            self.assertIsInstance(parr, array.array)
            if i == 1:
                self.assertEqual(parr[0], 0x0)
            elif i == 2:
                self.assertEqual(parr[0], 0x0100)
            elif i == 4:
                self.assertEqual(parr[0], 0x03020100)
        for i in (0, 3, 5, 6, 7, 9, 10, 12, "test", self):
            self.assertRaises(TypeError, pgarray.create_array, barr, i)


if __name__ == '__main__':
    sys.exit(unittest.main())
