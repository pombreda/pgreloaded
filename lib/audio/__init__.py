"""Audio system.

The audio module provides easy access to typical audio-related functionality,
such as playing and mixing sounds and music and adjusting the volume as well
as more complex features, e.g. channel selections, sound effects and more.
"""
import os
import wave
from pygame2.ebs import System, Component
import pygame2.openal.alc as alc
import pygame2.openal.al as al


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


class SoundData(Component):
    """A buffered audio object."""
    def __init__(self):
        super(SoundData, self).__init__()
        self._bufid = None
        self.format = None
        self.data = None
        self.size = None
        self.frequency = None

    @property
    def bufid(self):
        """The OpenAL buffer id, if any."""
        return self._bufid


class SoundSource(Component):
    """A sound source.

    The SoundSource is an object within the application world, that can emit
    sounds.
    """
    def __init__(self):
        """Creates a new SoundSource."""
        super(SoundSource, self).__init__()
        self._ssid = None
        self._buffers = []
        self.gain = 1.0
        self.pitch = 1.0
        self.position = (0, 0, 0)
        self.velocity = (0, 0, 0)
        self.request = SOURCE_NONE

    @property
    def ssid(self):
        """The OpenAL source id, if any."""
        return self._ssid

    def queue(self, sounddata):
        """Appends a SoundData to the playback queue for the source."""
        if not isinstance(sounddata, SoundData):
            raise TypeError("sounddata must be a SoundData")
        self._buffers.append(sounddata.bufid)


class SoundSink(System):
    """Audio playback system.

    The SoundSink handles audio output for sound sources. It connects to an
    audio output device and manages the source settings, their buffer queues
    and the playback of them.
    """
    def __init__(self, device=None, minsources=5):
        """Creates a new SoundSink for a specific audio output device."""
        super(SoundSink, self).__init__(self)
        self.componenttypes = (SoundSource, )
        self.device = alc.open_device(device)
        self.context = alc.create_context(self.device)
        self._sources = {}
        if minsources > 0:
            ssids = al.gen_sources(minsources)
            for ssid in ssids:
                self._sources[ssid] = None

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
            return
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

    def __del__(self):
        """Deletes the SoundSink and also destroys the associated
        context and closes the bound audio output device."""
        if self.context:
            alc.destroy_context(self.context)
            alc.close_device(self.device)
            self.context = None
            self.device = None

    def process(self, world, components):
        """Processes SoundSource components, playing their attached
        buffers."""
        for source in components:
            ssid = source._ssid or self._create_source(source)
            # TODO: if the properties of the source changed, they must be
            # updated.
            for bufid in source.buffers:
                al.source_queue_buffers(ssid, bufid)
            querystate = al.get_source_f(ssid, al.AL_SOURCE_STATE)
            if source.requeststate == SOURCE_NONE:
                # if no change is to be made, nothing will be done.
                pass
            elif source.requeststate == SOURCE_REWIND:
                al.source_rewind(ssid)
                source.requeststate = SOURCE_NONE
            elif source.requeststate == SOURCE_PLAY:
                if querystate != al.AL_PLAYING:
                    al.source_play(ssid)
                source.requeststate = SOURCE_NONE
            elif source.requeststate == SOURCE_STOP:
                if querystate != al.AL_STOPPED:
                    al.source_stop(ssid)
                source.requeststate = SOURCE_NONE
            elif source.requeststate == SOURCE_PAUSE:
                if querystate != al.AL_PAUSED:
                    al.source_pause(ssid)
                source.requeststate = SOURCE_NONE
            else:
                raise ValueError("invalid request state on source")



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


# supported extensions
_EXTENSIONS = {".wav": load_wav_file,
               #".ogg": load_ogg_file,
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
