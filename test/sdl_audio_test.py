import sys
import unittest
import copy
import pygame2.sdl as sdl
from pygame2.sdl.error import SDLError
import pygame2.sdl.audio as audio


class SDLAudioTest(unittest.TestCase):
    __tags__ = ["sdl"]

    def setUp(self):
        sdl.init(sdl.SDL_INIT_EVERYTHING)
        if sys.version.startswith("3.1"):
            self.assertIsInstance = \
                lambda x, t: self.assertTrue(isinstance(x, t))

    def tearDown(self):
        sdl.quit_subsystem(sdl.SDL_INIT_EVERYTHING)
        sdl.quit()

    @unittest.skip("not implemented")
    def test_SDL_AUDIO_BITSIZE(self):
        pass

    @unittest.skip("not implemented")
    def test_SDL_AUDIO_ISFLOAT(self):
        pass

    @unittest.skip("not implemented")
    def test_SDL_AUDIO_ISBIGENDIAN(self):
        pass

    @unittest.skip("not implemented")
    def test_SDL_AUDIO_ISSIGNED(self):
        pass

    @unittest.skip("not implemented")
    def test_SDL_AUDIO_ISINT(self):
        pass

    @unittest.skip("not implemented")
    def test_SDL_AUDIO_ISLITTLEENDIAN(self):
        pass

    @unittest.skip("not implemented")
    def test_SDL_AUDIO_ISUNSIGNED(self):
        pass

    @unittest.skip("not implemented")
    def test_SDL_AudioSpec(self):
        pass

    @unittest.skip("not implemented")
    def test_SDL_AudioCVT(self):
        pass

    @unittest.skip("not implemented")
    def test_get_num_audio_drivers(self):
        pass

    @unittest.skip("not implemented")
    def test_get_audio_driver(self):
        pass

    @unittest.skip("not implemented")
    def test_audio_init(self):
        pass

    @unittest.skip("not implemented")
    def test_audio_quit(self):
        pass

    @unittest.skip("not implemented")
    def test_get_current_audio_driver(self):
        pass

    @unittest.skip("not implemented")
    def test_open_audio(self):
        pass

    @unittest.skip("not implemented")
    def test_get_num_audio_devices(self):
        pass

    @unittest.skip("not implemented")
    def test_get_audio_device_name(self):
        pass

    @unittest.skip("not implemented")
    def test_open_audio_device(self):
        pass

    @unittest.skip("not implemented")
    def test_get_audio_status(self):
        pass

    @unittest.skip("not implemented")
    def test_get_audio_device_status(self):
        pass

    @unittest.skip("not implemented")
    def test_pause_audio(self):
        pass

    @unittest.skip("not implemented")
    def test_pause_audio_device(self):
        pass

    @unittest.skip("not implemented")
    def test_load_wav_rw(self):
        pass

    @unittest.skip("not implemented")
    def test_load_wav(self):
        pass

    @unittest.skip("not implemented")
    def test_free_wav(self):
        pass

    @unittest.skip("not implemented")
    def test_build_audio_cvt(self):
        pass

    @unittest.skip("not implemented")
    def test_convert_audio(self):
        pass

    @unittest.skip("not implemented")
    def test_mix_audio(self):
        pass

    @unittest.skip("not implemented")
    def test_mix_audio_format(self):
        pass

    @unittest.skip("not implemented")
    def test_lock_unlock_audio(self):
        pass

    @unittest.skip("not implemented")
    def test_lock_unlock_audio_device(self):
        pass

    @unittest.skip("not implemented")
    def test_close_audio(self):
        pass

    @unittest.skip("not implemented")
    def test_close_audio_device(self):
        pass

    @unittest.skip("not implemented")
    def test_audio_device_connected(self):
        pass

if __name__ == '__main__':
    unittest.main()
