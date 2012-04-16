import os
import sys
import unittest
import pygame2.resources as resources


class ResourcesTest(unittest.TestCase):

    def setUp(self):
        if sys.version.startswith("3.1"):
            self.assertIsInstance = \
                lambda x, t: self.assertTrue(isinstance(x, t))

    def tearDown(self):
        pass

    def test_open_zipfile(self):
        fpath = os.path.join(os.path.dirname(__file__), "resources")
        zfile = os.path.join(fpath, "resources.zip")
        
        # resources.zip is a packed version of resources/, which at
        # least contains
        #
        # resources/rwopstest.txt
        # resources/surfacetest.bmp

        resfile = resources.open_zipfile(zfile, "rwopstest.txt", "resources")
        self.assertIsNotNone(resfile)
        resfile = resources.open_zipfile(zfile, "resources/rwopstest.txt")
        self.assertIsNotNone(resfile)

        self.assertRaises(KeyError, resources.open_zipfile, zfile, "invalid")
        self.assertRaises(KeyError, resources.open_zipfile, zfile, None)
        self.assertRaises(KeyError, resources.open_zipfile, zfile,
                          "rwopstest.txt", "data")
        self.assertRaises(KeyError, resources.open_zipfile, zfile,
                          "rwopstest.txt", 1234)
        self.assertRaises(KeyError, resources.open_zipfile, zfile,
                          None, None)

        self.assertRaises(TypeError, resources.open_zipfile, None,
                          "rwopstest.txt")
        self.assertRaises(TypeError, resources.open_zipfile, None, None)
        self.assertRaises(TypeError, resources.open_zipfile, None,
                          "rwopstest.txt", "resources")

    def test_open_tarfile(self):
        fpath = os.path.join(os.path.dirname(__file__), "resources")
        tfile = os.path.join(fpath, "resources.tar.gz")
        
        # resources.tar.gz is a packed version of resources/, which at
        # least contains
        #
        # resources/rwopstest.txt
        # resources/surfacetest.bmp

        resfile = resources.open_tarfile(tfile, "rwopstest.txt", "resources")
        self.assertIsNotNone(resfile)
        resfile = resources.open_tarfile(tfile, "resources/rwopstest.txt")
        self.assertIsNotNone(resfile)

        # TODO: refine the error handling in open_tarfile()
        self.assertRaises(KeyError, resources.open_tarfile, tfile, "invalid")
        self.assertRaises(AttributeError, resources.open_tarfile, tfile, None)
        self.assertRaises(KeyError, resources.open_tarfile, tfile,
                          "rwopstest.txt", "data")
        self.assertRaises(KeyError, resources.open_tarfile, tfile,
                          "rwopstest.txt", 1234)
        self.assertRaises(AttributeError, resources.open_tarfile, tfile,
                          None, None)

        self.assertRaises(ValueError, resources.open_tarfile, None,
                          "rwopstest.txt")
        self.assertRaises(ValueError, resources.open_tarfile, None, None)
        self.assertRaises(ValueError, resources.open_tarfile, None,
                          "rwopstest.txt", "resources")

    @unittest.skip("not implemented")
    def test_open_url(self):
        pass

    def test_Resources(self):
        res = resources.Resources()
        self.assertIsInstance(res, resources.Resources)

    def test_Resources_add(self):
        fpath = os.path.join(os.path.dirname(__file__), "resources")
        sfile = os.path.join(fpath, "surfacetest.bmp")
        zfile = os.path.join(fpath, "resources.zip")

        res = resources.Resources()
        res.add(sfile)
        self.assertRaises(KeyError, res.get, "rwopstest.txt")
        self.assertIsNotNone(res.get("surfacetest.bmp"))

        res.add(zfile)
        self.assertIsNotNone(res.get("rwopstest.txt"))
        self.assertIsNotNone(res.get("surfacetest.bmp"))

    @unittest.skip("not implemented")
    def test_Resources_add_file(self):
        pass

    @unittest.skip("not implemented")
    def test_Resources_add_archive(self):
        pass

    @unittest.skip("not implemented")
    def test_Resources_get(self):
        pass

    @unittest.skip("not implemented")
    def test_Resources_get_filelike(self):
        pass

    @unittest.skip("not implemented")
    def test_Resources_get_path(self):
        pass

    @unittest.skip("not implemented")
    def test_Resources_scan(self):
        pass

if __name__ == '__main__':
    unittest.main()
