import sys
import unittest
import pygame2.ogg as ogg


class OGGTest(unittest.TestCase):
    __tags__ = ["ogg", "vorbis"]

    def setUp(self):
        if sys.version.startswith("3.1"):
            self.assertIsInstance = \
                lambda x, t: self.assertTrue(isinstance(x, t))

    def test_OggError(self):
        error = ogg.OggError()
        self.assertIsInstance(error, ogg.OggError)
        self.assertEqual(error.msg, None)
        self.assertEqual(str(error), "None")

        def doraise(msg):
            raise ogg.OggError(msg)

        self.assertRaises(ogg.OggError, doraise, None)
        self.assertRaises(ogg.OggError, doraise, "test")


if __name__ == '__main__':
    sys.exit(unittest.main())
