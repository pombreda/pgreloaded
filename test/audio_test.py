import sys
import unittest
import pygame2.openal.al as al
import pygame2.audio as audio
from pygame2.test import RESOURCES

class AudioTest(unittest.TestCase):
    __tags__ = ["openal"]

    def setUp(self):
        if sys.version.startswith("3.1"):
            self.assertIsInstance = \
                lambda x, t: self.assertTrue(isinstance(x, t))
        pass

    def tearDown(self):
        pass

    def test_SoundData(self):
        data = audio.SoundData()
        self.assertIsInstance(data, audio.SoundData)
        self.assertIsNone(data.bufid)
        self.assertIsNone(data.format)
        self.assertIsNone(data.data)
        self.assertIsNone(data.size)
        self.assertIsNone(data.frequency)

    def test_SoundSource(self):
        source = audio.SoundSource()
        self.assertIsInstance(source, audio.SoundSource)
        self.assertIsNone(source.ssid)
        self.assertIsNone(source.ssid)
        self.assertEqual(source._buffers, list())
        self.assertEqual(source.gain, 1.0)
        self.assertEqual(source.pitch, 1.0)
        self.assertEqual(source.position, (0, 0, 0))
        self.assertEqual(source.velocity, (0, 0, 0))
        self.assertEqual(source.request, audio.SOURCE_NONE)

    @unittest.skip("not implemented")
    def test_SoundSource_queue(self):
        pass

    @unittest.skip("not implemented")
    def test_SoundSink(self):
        pass

    @unittest.skip("not implemented")
    def test_SoundSink_process(self):
        pass

    def test_load_file(self):
        wavfile = RESOURCES.get_path("hey.wav")
        snddata = audio.load_file(wavfile)

        self.assertIsNone(snddata.bufid)
        self.assertEqual(snddata.format, al.AL_FORMAT_MONO16)
        self.assertEqual(snddata.frequency, 44100)
        self.assertEqual(snddata.size, 122880)

    def test_load_wav_file(self):
        wavfile = RESOURCES.get_path("hey.wav")
        snddata = audio.load_file(wavfile)

        self.assertIsNone(snddata._bufid)
        self.assertEqual(snddata.format, al.AL_FORMAT_MONO16)
        self.assertEqual(snddata.frequency, 44100)
        self.assertEqual(snddata.size, 122880)

    @unittest.skip("not implemented")
    def test_load_stream(self):
        pass


if __name__ == '__main__':
    sys.exit(unittest.main())
