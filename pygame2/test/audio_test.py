import sys
import unittest
import pygame2.openal.al as al
import pygame2.audio as audio
from pygame2.resources import Resources

RESOURCES = Resources(__file__, "resources")

class AudioTest(unittest.TestCase):
    __tags__ = ["openal"]

    def setUp(self):
        if sys.version.startswith("3.1"):
            self.assertIsInstance = \
                lambda x, t: self.assertTrue(isinstance(x, t))

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

    def test_SoundListener(self):
        listener = audio.SoundListener()
        self.assertIsInstance(listener, audio.SoundListener)
        self.assertEqual(listener.position, (0, 0, 0))
        self.assertEqual(listener.velocity, (0, 0, 0))
        self.assertEqual(listener.orientation, (0, 0, -1, 0, 1, 0))

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

    def test_SoundSource_queue(self):
        source = audio.SoundSource()
        self.assertIsInstance(source, audio.SoundSource)
        self.assertRaises(TypeError, source.queue, None)
        self.assertRaises(TypeError, source.queue, "Test")
        self.assertRaises(TypeError, source.queue, 123456)
        
        data = audio.SoundData()
        source.queue(data)

    @unittest.skip("not implemented")
    def test_SoundSink(self):
        sink = audio.SoundSink()
        self.assertIsInstance(sink, audio.SoundSink)
        

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
        snddata = audio.load_wav_file(wavfile)

        self.assertIsNone(snddata._bufid)
        self.assertEqual(snddata.format, al.AL_FORMAT_MONO16)
        self.assertEqual(snddata.frequency, 44100)
        self.assertEqual(snddata.size, 122880)

    @unittest.skip("not implemented")
    def test_load_ogg_file(self):
        oggfile = RESOURCES.get_path("hey.ogg")
        snddata = audio.load_ogg_file(oggfile)
        
        
    @unittest.skip("not implemented")
    def test_load_stream(self):
        pass


if __name__ == '__main__':
    sys.exit(unittest.main())
