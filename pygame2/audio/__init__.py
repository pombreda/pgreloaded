"""Audio system.

The audio module provides easy access to typical audio-related functionality,
such as playing and mixing sounds and music and adjusting the volume as well
as more complex features, e.g. channel selections, sound effects and more.
"""
import os
import wave
from pygame2.compat import experimental
from pygame2.ebs import System, Component
import pygame2.openal.alc as alc
import pygame2.openal.al as al
import pygame2.ogg.vorbisfile as vorbis


__all__ = ["SoundData", "SoundSource", "SoundSink", "load_file", "load_stream",
           "load_wav_file"
           ]

# channel/samplesize to OpenAL format mapping
_FORMATMAP = {(1, 8): al.AL_FORMAT_MONO8,
              (2, 8): al.AL_FORMAT_STEREO8,
              (1, 16): al.AL_FORMAT_MONO16,
              (2, 16): al.AL_FORMAT_STEREO16
              }


# Status of a source - should ideally match the AL_SOURCE_XXXXX bits
# without the AL_SOURCE_STATE bitmask
SOURCE_NONE =   0x01
SOURCE_PLAY =   0x02
SOURCE_PAUSE =  0x03
SOURCE_STOP =   0x04
SOURCE_REWIND = 0x09


class SoundListener(Component):
    """A simple sound listener."""
    def __init__(self, position=(0, 0, 0), velocity=(0, 0, 0),
                 orientation=(0, 0, -1, 0, 1, 0)):
        super(SoundListener, self).__init__()
        self.position = position
        self.velocity = velocity
        self.orientation = orientation


class SoundData(Component):
    """A buffered audio object."""
    def __init__(self, format=None, data=None, size=None, frequency=None):
        super(SoundData, self).__init__()
        self._bufid = None
        self.format = format
        self.data = data
        self.size = size
        self.frequency = frequency

    @property
    def bufid(self):
        """The OpenAL buffer id, if any."""
        return self._bufid


class SoundSource(Component):
    """A sound source.

    The SoundSource is an object within the application world, that can emit
    sounds.
    """
    def __init__(self, gain=1.0, pitch=1.0, position=(0, 0, 0),
                 velocity=(0, 0, 0)):
        """Creates a new SoundSource."""
        super(SoundSource, self).__init__()
        self._ssid = None
        self._buffers = []
        self.gain = gain
        self.pitch = pitch
        self.position = position
        self.velocity = velocity
        self.request = SOURCE_NONE

    @property
    def ssid(self):
        """The OpenAL source id, if any."""
        return self._ssid

    def queue(self, sounddata):
        """Appends a SoundData to the playback queue for the source."""
        if not isinstance(sounddata, SoundData):
            raise TypeError("sounddata must be a SoundData")
        self._buffers.append(sounddata)


class SoundSink(System):
    """Audio playback system.

    The SoundSink handles audio output for sound sources. It connects to an
    audio output device and manages the source settings, their buffer queues
    and the playback of them.
    """
    def __init__(self, device=None):
        """Creates a new SoundSink for a specific audio output device."""
        super(SoundSink, self).__init__()
        self.componenttypes = (SoundSource, )
        if isinstance(device, alc.ALCdevice):
            self._hasopened = False
            self.device = device
        else:
            self.device = alc.open_device(device)
            self._hasopened = True
        self.context = alc.create_context(self.device)
        self.activate()
        self._sources = {}
        self._buffers = {}

    def _create_source(self, source):
        """Creates a new OpenAL source from the the passed SoundSource."""
        ssid = None
        for kssid, ksource in self._sources.items():
            if ksource is None:
                # Got a free source
                ssid = kssid
                break
        if ssid is not None:
            source._ssid = ssid
            self._sources[ssid] = source
        else:
            # No free source
            ssid = al.gen_sources(1)[0]
            self._sources[ssid] = source
            source._ssid = ssid
        al.source_f(ssid, al.AL_GAIN, source.gain)
        al.source_f(ssid, al.AL_PITCH, source.pitch)
        al.source_fv(ssid, al.AL_POSITION, source.position)
        al.source_fv(ssid, al.AL_VELOCITY, source.velocity)
        return ssid

    def _create_buffers(self, source):
        """Creates a new set of OpenAL buffers from the passed
        SoundSource."""
        queue = []
        for snddata in source._buffers:
            if snddata._bufid is None:
                bufid = None
                for kbufid, kdata in self._buffers.items():
                    if kdata is None:
                        # free buffer found
                        bufid = kbufid
                        break
                if bufid is not None:
                    snddata._bufid = bufid
                    self._buffers[bufid] = snddata
                else:
                    # No free buffer id, create a new one
                    bufid = al.gen_buffers(1)[0]
                    self._buffers[bufid] = snddata
                    snddata._bufid = bufid
            # Buffer id assigned, now buffer the data.
            al.buffer_data(snddata._bufid, snddata.format, snddata.data,
                           snddata.frequency)
            queue.append(snddata._bufid)
        al.source_queue_buffers(source._ssid, queue)

    def __del__(self):
        """Deletes the SoundSink and also destroys the associated
        context and closes the bound audio output device."""
        if self.context:
            for ssid, source in self._sources.items():
                querystate = al.get_source_i(ssid, al.AL_SOURCE_STATE)
                if querystate != al.AL_STOPPED:
                    al.source_stop(ssid)
                al.delete_sources([ssid])
                source._ssid = None
            self._sources = {}
            al.delete_buffers(self._buffers.keys())
            self._buffers = {}
            alc.destroy_context(self.context)
            if self._hasopened:
                alc.close_device(self.device)
            self.context = None
            self.device = None

    def activate(self):
        """Marks the SoundSink as the currently active one.

        Subsequent OpenAL operations are done in the context of the
        SoundSink's bindings.
        """
        alc.make_context_current(self.context)

    def set_listener(self, listener):
        """Sets the listener position for the SoundSink.

        Note: this implicitly activates the SoundSink.
        """
        if not isinstance(listener, SoundListener):
            raise TypeError("listener must be a SoundListener")
        self.activate()
        al.listener_fv(al.AL_POSITION, listener.position)
        al.listener_fv(al.AL_VELOCITY, listener.velocity)
        al.listener_fv(al.AL_ORIENTATION, listener.orientation)

    def process_source(self, source):
        """Processes a SoundSource.

        Note: this does NOT activate the SoundSink. If another SoundSink
        is active, chances are good that the source is processed in that
        SoundSink.
        """
        ssid = source._ssid
        if ssid is None:
            ssid = self._create_source(source)
        # TODO: if the properties of the source changed, they must be
        # updated.
        self._create_buffers(source)
        querystate = al.get_source_i(ssid, al.AL_SOURCE_STATE)
        if source.request == SOURCE_NONE:
            # if no change is to be made, nothing will be done.
            pass
        elif source.request == SOURCE_REWIND:
            al.source_rewind(ssid)
            source.request = SOURCE_NONE
        elif source.request == SOURCE_PLAY:
            if querystate != al.AL_PLAYING:
                al.source_play(ssid)
            source.request = SOURCE_NONE
        elif source.request == SOURCE_STOP:
            if querystate != al.AL_STOPPED:
                al.source_stop(ssid)
            source.request = SOURCE_NONE
        elif source.request == SOURCE_PAUSE:
            if querystate != al.AL_PAUSED:
                al.source_pause(ssid)
            source.request = SOURCE_NONE
        else:
            raise ValueError("invalid request state on source")

    def process(self, world, components):
        """Processes SoundSource components, playing their attached
        buffers.

        Note: this implicitly activates the SoundSink.
        """
        process_source = self.process_source
        self.activate()
        for source in components:
            process_source(source)


def load_wav_file(fname):
    """Loads a WAV encoded audio file into a SoundData object."""
    fp = wave.open(fname, "rb")
    channels = fp.getnchannels()
    bitrate = fp.getsampwidth() * 8
    samplerate = fp.getframerate()

    data = SoundData()
    data.format = _FORMATMAP[(channels, bitrate)]
    data.data = fp.readframes(fp.getnframes())
    data.size = len(data.data)
    data.frequency = samplerate
    return data


@experimental
def load_ogg_file(fname):
    """Loads an Ogg-Vorbis encoded audio file into a SoundData object."""
    fp = vorbis.fopen(fname)
    finfo = vorbis.info(fp)
    length = vorbis.pcm_total(fp)

    data = SoundData()
    data.format = _FORMATMAP[(finfo.channels, 16)]
    data.data = vorbis.read(fp, length, word=2)[0]
    data.size = length
    data.frequency = finfo.rate


# supported extensions
_EXTENSIONS = {".wav": load_wav_file,
               ".ogg": load_ogg_file,
               }


def load_file(fname):
    """Loads an audio file into a SoundData object."""
    ext = os.path.splitext(fname)[1].lower()
    funcptr = _EXTENSIONS.get(ext, None)
    if not funcptr:
        raise ValueError("unsupported audio file type")
    return funcptr(fname)


def load_stream(source):
    """Loads an audio stream into a SoundData object."""
    raise NotImplementedError("not implemented yet")
