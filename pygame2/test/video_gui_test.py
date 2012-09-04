import sys
import unittest
import pygame2.video as video


class VideoGUITest(unittest.TestCase):

    def setUp(self):
        if sys.version.startswith("3.1"):
            self.assertIsInstance = \
                lambda x, t: self.assertTrue(isinstance(x, t))
        video.init()

    def tearDown(self):
        video.quit()

    @unittest.skip("not implemented")
    def test_Button(self):
        pass

    @unittest.skip("not implemented")
    def test_CheckButton(self):
        pass

    @unittest.skip("not implemented")
    def test_TextEntry(self):
        pass

    @unittest.skip("not implemented")
    def test_UIProcessor(self):
        pass

    @unittest.skip("not implemented")
    def test_UIProcessor_activate(self):
        pass

    @unittest.skip("not implemented")
    def test_UIProcessor_deactivate(self):
        pass

    @unittest.skip("not implemented")
    def test_UIProcessor_dispatch(self):
        pass

    @unittest.skip("not implemented")
    def test_UIProcessor_mousedown(self):
        pass

    @unittest.skip("not implemented")
    def test_UIProcessor_mouseup(self):
        pass

    @unittest.skip("not implemented")
    def test_UIProcessor_mousemotion(self):
        pass

    @unittest.skip("not implemented")
    def test_UIProcessor_passevent(self):
        pass

    @unittest.skip("not implemented")
    def test_UIProcessor_process(self):
        pass

    @unittest.skip("not implemented")
    def test_UIProcessor_textinput(self):
        pass

if __name__ == '__main__':
    sys.exit(unittest.main())
