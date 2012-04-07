import sys
import unittest
import pygame2.sdl as sdl
import pygame2.sdl.cpuinfo as cpuinfo

_HASMP = True
try:
    import multiprocessing
except:
    _HASMP = False


class SDLCPUInfoTest(unittest.TestCase):
    __tags__ = ["sdl"]

    def setUp(self):
        if sys.version.startswith("3.1"):
            self.assertIsInstance = \
                lambda x, t: self.assertTrue(isinstance(x, t))

    def test_get_cpu_cache_line_size(self):
        ret = cpuinfo.get_cpu_cache_line_size()
        self.assertIsInstance(ret, int)

    @unittest.skipIf(not _HASMP, "no multiprocessing module found")
    def test_get_cpu_count(self):
        self.assertEqual(multiprocessing.cpu_count(),
                         cpuinfo.get_cpu_count())

    def test_has_3dnow(self):
        ret = cpuinfo.has_3dnow()
        self.assertIsInstance(ret, bool)

    def test_has_altivec(self):
        ret = cpuinfo.has_altivec()
        self.assertIsInstance(ret, bool)

    def test_has_mmx(self):
        ret = cpuinfo.has_mmx()
        self.assertIsInstance(ret, bool)

    def test_has_rdtsc(self):
        ret = cpuinfo.has_rdtsc()
        self.assertIsInstance(ret, bool)

    def test_has_sse(self):
        ret = cpuinfo.has_sse()
        self.assertIsInstance(ret, bool)

    def test_has_sse2(self):
        ret = cpuinfo.has_sse2()
        self.assertIsInstance(ret, bool)

    def test_has_sse3(self):
        ret = cpuinfo.has_sse3()
        self.assertIsInstance(ret, bool)

    def test_has_sse41(self):
        ret = cpuinfo.has_sse41()
        self.assertIsInstance(ret, bool)

    def test_has_sse42(self):
        ret = cpuinfo.has_sse42()
        self.assertIsInstance(ret, bool)

if __name__ == '__main__':
    unittest.main()
