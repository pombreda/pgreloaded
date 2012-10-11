import os
import sys
import unittest
import copy
import pygame2.sdl as sdl
import pygame2.sdl.audio as audio


# We won't use pygame2.sdl.audio.audio_init() and
# pygame2.sdl.audio.audio_quit() here, since they only set the internal
# states of the SDL audio subsystem without configuring the other parts
# of the system correctly.
class SDLAudioTest(unittest.TestCase):
    __tags__ = ["sdl"]

    def setUp(self):
        sdl.init(0)
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
        self.assertRaises(sdl.SDLError, audio.get_audio_driver, -1)
        self.assertRaises(sdl.SDLError, audio.get_audio_driver,
                          drivercount + 1)
        self.assertRaises(TypeError, audio.get_audio_driver, "Test")
        self.assertRaises(TypeError, audio.get_audio_driver, None)

    def test_get_current_audio_driver(self):
        success = 0
        for index in range(audio.get_num_audio_drivers()):
            drivername = audio.get_audio_driver(index)
            try:
                os.environ["SDL_AUDIODRIVER"] = drivername
                # Certain drivers fail without bringing up the correct
                # return value, such as the esd, if it is not running.
                sdl.init_subsystem(sdl.SDL_INIT_AUDIO)
                driver = audio.get_current_audio_driver()
                # Do not handle wrong return values.
                if driver is not None:
                    self.assertEqual(drivername, driver)
                    success += 1
            except sdl.SDLError:
                pass
            else:
                sdl.quit_subsystem(sdl.SDL_INIT_AUDIO)
        self.assertGreaterEqual(success, 1,
                                "Could not initialize any sound driver")

    def test_open_audio(self):
        os.environ["SDL_AUDIODRIVER"] = "dummy"
        sdl.init_subsystem(sdl.SDL_INIT_AUDIO)
        reqspec = audio.SDL_AudioSpec(44100, audio.AUDIO_U16SYS, 2, 8192,
                                      self.audiocallback, None)
        spec = audio.open_audio(reqspec)
        self.assertIsInstance(spec, audio.SDL_AudioSpec)
        self.assertEqual(spec.format, reqspec.format)
        self.assertEqual(spec.freq, reqspec.freq)
        self.assertEqual(spec.channels, reqspec.channels)
        audio.close_audio()
        sdl.quit_subsystem(sdl.SDL_INIT_AUDIO)

    def test_get_num_audio_devices(self):
        os.environ["SDL_AUDIODRIVER"] = "dummy"
        sdl.init_subsystem(sdl.SDL_INIT_AUDIO)
        outnum = audio.get_num_audio_devices()
        self.assertGreaterEqual(outnum, 1)
        innum = audio.get_num_audio_devices(True)
        self.assertGreaterEqual(innum, 0)
        sdl.quit_subsystem(sdl.SDL_INIT_AUDIO)

    def test_get_audio_device_name(self):
        os.environ["SDL_AUDIODRIVER"] = "dummy"
        sdl.init_subsystem(sdl.SDL_INIT_AUDIO)
        outnum = audio.get_num_audio_devices()
        for x in range(outnum):
            name = audio.get_audio_device_name(x)
            self.assertIsNotNone(name)
        innum = audio.get_num_audio_devices(True)
        for x in range(innum):
            name = audio.get_audio_device_name(x, True)
            self.assertIsNotNone(name)
        self.assertRaises(sdl.SDLError, audio.get_audio_device_name, -1)
        self.assertRaises(sdl.SDLError, audio.get_audio_device_name, -1, True)
        sdl.quit_subsystem(sdl.SDL_INIT_AUDIO)

        self.assertRaises(sdl.SDLError, audio.get_audio_device_name, 0)
        self.assertRaises(sdl.SDLError, audio.get_audio_device_name, 0, True)

    def test_open_close_audio_device(self):
        os.environ["SDL_AUDIODRIVER"] = "dummy"
        sdl.init_subsystem(sdl.SDL_INIT_AUDIO)
        reqspec = audio.SDL_AudioSpec(44100, audio.AUDIO_U16SYS, 2, 8192,
                                      self.audiocallback, None)
        outnum = audio.get_num_audio_devices()
        for x in range(outnum):
            name = audio.get_audio_device_name(x)
            self.assertIsNotNone(name)
            deviceid, spec = audio.open_audio_device(name, False, reqspec, 0)
            self.assertGreaterEqual(deviceid, 2)
            self.assertIsInstance(spec, audio.SDL_AudioSpec)
            self.assertEqual(spec.format, reqspec.format)
            self.assertEqual(spec.freq, reqspec.freq)
            self.assertEqual(spec.channels, reqspec.channels)
            audio.close_audio_device(deviceid)
        sdl.quit_subsystem(sdl.SDL_INIT_AUDIO)

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
    sys.exit(unittest.main())
