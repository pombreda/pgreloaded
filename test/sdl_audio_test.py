import sys
import unittest
import copy
import pygame2.sdl as sdl
from pygame2.sdl.error import SDLError
import pygame2.sdl.audio as audio

_DRIVER = "dummy"
if sys.platform.startswith("freebsd"):
    _DRIVER = "dsp"

class SDLAudioTest(unittest.TestCase):
    __tags__ = ["sdl"]

    def setUp(self):
        sdl.init()
        if sys.version.startswith("3.1"):
            self.assertIsInstance = \
                lambda x, t: self.assertTrue(isinstance(x, t))

        def audio_cb(userdata, audiobytes, length):
            pass

        self.audiocallback = audio.SDL_AudioCallback(audio_cb)

    def tearDown(self):
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

    def test_get_num_audio_drivers(self):
        count = audio.get_num_audio_drivers()
        self.assertGreaterEqual(count, 1)

    def test_get_audio_driver(self):
        founddummy = False
        drivercount = audio.get_num_audio_drivers()
        for index in range(drivercount):
            drivername = audio.get_audio_driver(index)
            self.assertIsInstance(drivername, str)
            if drivername == "dummy":
                founddummy = True
        self.assertTrue(founddummy, "could not find dummy driver")
        self.assertRaises(SDLError, audio.get_audio_driver, -1)
        self.assertRaises(SDLError, audio.get_audio_driver, drivercount + 1)
        self.assertRaises(TypeError, audio.get_audio_driver, "Test")
        self.assertRaises(TypeError, audio.get_audio_driver, None)

    def test_audio_init_quit(self):
        success = 0
        for index in range(audio.get_num_audio_drivers()):
            drivername = audio.get_audio_driver(index)
            try:
                audio.audio_init(drivername)
                success += 1
            except SDLError:
                continue
            audio.audio_quit()
        self.assertGreaterEqual(success, 1,
                                "Could not initialize any sound driver")

    def test_get_current_audio_driver(self):
        success = 0
        for index in range(audio.get_num_audio_drivers()):
            drivername = audio.get_audio_driver(index)
            try:
                audio.audio_init(drivername)
                current = audio.get_current_audio_driver()
                self.assertEqual(current, drivername)
                success += 1
            except SDLError:
                continue
            audio.audio_quit()
        self.assertGreaterEqual(success, 1,
                                "Could not initialize any sound driver")

    @unittest.skip("not implemented")
    def test_open_audio(self):
        audio.audio_init("dummy")
        print audio.get_current_audio_driver()
        reqspec = audio.SDL_AudioSpec(44100, audio.AUDIO_U16SYS, 2, 8192,
                                      self.audiocallback, None)
        audiospec = audio.open_audio(reqspec)
        print audiospec
        audio.audio_quit()
                
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
