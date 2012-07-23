import sys
import unittest
import pygame2.video as video


class VideoWindowTest(unittest.TestCase):

    def setUp(self):
        if sys.version.startswith("3.1"):
            self.assertIsInstance = \
                lambda x, t: self.assertTrue(isinstance(x, t))
        video.init()

    def tearDown(self):
        video.quit()

    @unittest.skip("not implemented")
    def test_Window(self):
        pass

    @unittest.skip("not implemented")
    def test_Window_title(self):
        pass

    @unittest.skip("not implemented")
    def test_Window_show(self):
        pass

    @unittest.skip("not implemented")
    def test_Window_hide(self):
        pass

    @unittest.skip("not implemented")
    def test_Window_maximize(self):
        pass

    @unittest.skip("not implemented")
    def test_Window_minimize(self):
        pass

    @unittest.skip("not implemented")
    def test_Window_refresh(self):
        pass

    @unittest.skip("not implemented")
    def test_Window_get_surface(self):
        pass

if __name__ == '__main__':
    sys.exit(unittest.main())
