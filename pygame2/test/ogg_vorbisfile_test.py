import sys
import unittest
from pygame2.resources import Resources
import pygame2.ogg as ogg
import pygame2.ogg.vorbisfile as vorbisfile

RESOURCES = Resources(__file__, "resources")

@unittest.skip("The ogg.vorbisfile module is very unstable at the moment")
class OGGVorbisFileTest(unittest.TestCase):
    __tags__ = ["ogg", "vorbis"]

    def setUp(self):
        if sys.version.startswith("3.1"):
            self.assertIsInstance = \
                lambda x, t: self.assertTrue(isinstance(x, t))

    def tearDown(self):
        pass

    def test_OggVorbis_File(self):
        ovfile = vorbisfile.OggVorbis_File()
        self.assertIsInstance(ovfile, vorbisfile.OggVorbis_File)

    def test_clear(self):
        fname = RESOURCES.get_path("hey.ogg")
        ovfile = vorbisfile.fopen(fname)
        self.assertIsInstance(ovfile, vorbisfile.OggVorbis_File)
        vorbisfile.clear(ovfile)

        self.assertRaises(TypeError, vorbisfile.clear, 1234)
        self.assertRaises(TypeError, vorbisfile.clear, None)
        self.assertRaises(TypeError, vorbisfile.clear, "test")

    def test_fopen(self):
        fname = RESOURCES.get_path("hey.ogg")
        ovfile = vorbisfile.fopen(fname)
        self.assertIsInstance(ovfile, vorbisfile.OggVorbis_File)
        vorbisfile.clear(ovfile)

        fname = RESOURCES.get_path("hey.wav")
        self.assertRaises(ogg.OggError, vorbisfile.fopen, fname)
        self.assertRaises(ogg.OggError, vorbisfile.fopen, "invalid")
        self.assertRaises(TypeError, vorbisfile.fopen, 1234)
        self.assertRaises(TypeError, vorbisfile.fopen, None)

    def test_pcm_total(self):
        fname = RESOURCES.get_path("hey.ogg")
        ovfile = vorbisfile.fopen(fname)
        self.assertIsInstance(ovfile, vorbisfile.OggVorbis_File)
        self.assertEqual(vorbisfile.pcm_total(ovfile), 61440)
        vorbisfile.clear(ovfile)

        self.assertRaises(ogg.OggError, vorbisfile.pcm_total, ovfile)
        self.assertRaises(TypeError, vorbisfile.pcm_total, 1234)
        self.assertRaises(TypeError, vorbisfile.pcm_total, None)
        self.assertRaises(TypeError, vorbisfile.pcm_total, "test")

    @unittest.skip("not implemented")
    def test_read(self):
        pass

    def test_info(self):
        fname = RESOURCES.get_path("hey.ogg")
        ovfile = vorbisfile.fopen(fname)
        self.assertIsInstance(ovfile, vorbisfile.OggVorbis_File)
        ovinfo = vorbisfile.info(ovfile)
        self.assertIsInstance(ovinfo, vorbisfile.vorbis_info)

        self.assertEqual(ovinfo.version, 0)
        self.assertEqual(ovinfo.channels, 1)
        self.assertEqual(ovinfo.rate, 44100)
        self.assertEqual(ovinfo.bitrate_upper, 0)
        self.assertEqual(ovinfo.bitrate_nominal, 96000)
        self.assertEqual(ovinfo.bitrate_lower, 0)

        vorbisfile.clear(ovfile)

if __name__ == '__main__':
    sys.exit(unittest.main())
