"""
Wrapper methods around the SDL2 audio routines.
"""
import ctypes
from pygame2.compat import *
from pygame2.sdl import sdltype, dll, SDLError
from pygame2.sdl.rwops import SDL_RWops, rw_from_file
from pygame2.sdl.endian import SDL_BYTEORDER, SDL_LIL_ENDIAN

__all__ = [""]


SDL_AUDIO_MASK_BITSIZE = 0xFF
SDL_AUDIO_MASK_DATATYPE = 1 << 8
SDL_AUDIO_MASK_ENDIAN = 1 << 12
SDL_AUDIO_MASK_SIGNED = 1 << 15


def SDL_AUDIO_BITSIZE(x):
    """Gets the bitsize of an audio format."""
    return x & SDL_AUDIO_MASK_BITSIZE


def SDL_AUDIO_ISFLOAT(x):
    """Checks, if the audio format is a float format."""
    return x & SDL_AUDIO_MASK_DATATYPE


def SDL_AUDIO_ISBIGENDIAN(x):
    """Checks, if the audio format is in big-endian byte order."""
    return x & SDL_AUDIO_MASK_ENDIAN


def SDL_AUDIO_ISSIGNED(x):
    """Checks, if the audio format uses signed values."""
    return x & SDL_AUDIO_MASK_SIGNED


def SDL_AUDIO_ISINT(x):
    """Checks, if the audio format is an int format."""
    return not SDL_AUDIO_ISFLOAT(x)


def SDL_AUDIO_ISLITTLEENDIAN(x):
    """Checks, if the audio format is in little-endian byte order."""
    return not SDL_AUDIO_ISBIGENDIAN(x)


def SDL_AUDIO_ISUNSIGNED(x):
    """Checks, if the audio format usses unsigned values."""
    return not SDL_AUDIO_ISSIGNED(x)


AUDIO_U8     = 0x0008
AUDIO_S8     = 0x8008
AUDIO_U16LSB = 0x0010
AUDIO_S16LSB = 0x8010
AUDIO_U16MSB = 0x1010
AUDIO_S16MSB = 0x9010
AUDIO_U16    = AUDIO_U16LSB
AUDIO_S16    = AUDIO_S16LSB
AUDIO_S32LSB = 0x8020
AUDIO_S32MSB = 0x9020
AUDIO_S32    = AUDIO_S32LSB
AUDIO_F32LSB = 0x8120
AUDIO_F32MSB = 0x9120
AUDIO_F32    = AUDIO_F32LSB

if SDL_BYTEORDER == SDL_LIL_ENDIAN:
    AUDIO_U16SYS = AUDIO_U16LSB
    AUDIO_S16SYS = AUDIO_S16LSB
    AUDIO_S32SYS = AUDIO_S32LSB
    AUDIO_F32SYS = AUDIO_F32LSB
else:
    AUDIO_U16SYS = AUDIO_U16MSB
    AUDIO_S16SYS = AUDIO_S16MSB
    AUDIO_S32SYS = AUDIO_S32MSB
    AUDIO_F32SYS = AUDIO_F32MSB

SDL_AUDIO_ALLOW_FREQUENCY_CHANGE = 0x00000001
SDL_AUDIO_ALLOW_FORMAT_CHANGE    = 0x00000002
SDL_AUDIO_ALLOW_CHANNELS_CHANGE  = 0x00000004
SDL_AUDIO_ALLOW_ANY_CHANGE       = (SDL_AUDIO_ALLOW_FREQUENCY_CHANGE |
                                    SDL_AUDIO_ALLOW_FORMAT_CHANGE |
                                    SDL_AUDIO_ALLOW_CHANNELS_CHANGE
                                    )

SDL_AUDIO_STOPPED = 0
SDL_AUDIO_PLAYING = 1
SDL_AUDIO_PAUSED  = 2

SDL_MIX_MAXVOLUME = 128

SDL_AudioCallback = ctypes.CFUNCTYPE(None, ctypes.c_void_p,
                                     ctypes.POINTER(ctypes.c_ubyte),
                                     ctypes.c_int)


class SDL_AudioSpec(ctypes.Structure):
    """Audio specification."""
    _fields_ = [("freq", ctypes.c_int),
                ("format", ctypes.c_ushort),
                ("channels", ctypes.c_ubyte),
                ("silence", ctypes.c_ubyte),
                ("samples", ctypes.c_ushort),
                ("_padding", ctypes.c_ushort),
                ("size", ctypes.c_uint),
                ("callback", SDL_AudioCallback),
                ("userdata", ctypes.c_void_p)
                ]

    def __init__(self, frequency, aformat, channels, samples,
                 callback, userdata=None):
        self.freq = frequency
        self.format = aformat
        self.channels = channels
        self.samples = samples
        if callback is None:
            self.callback = SDL_AudioCallback()
        else:
            self.callback = callback
        if userdata is None:
            self.userdata = ctypes.c_void_p(0)
        else:
            self.userdata = ctypes.cast(ctypes.py_object(userdata),
                                        ctypes.c_void_p)

    def __repr__(self):
        return """SDL_AudioSpec(freq=%d, format=%d, channels=%d, silence=%d,
samples=%d, size=%d)""" % (self.freq, self.format, self.channels, self.silence,
                           self.samples, self.size)

class SDL_AudioCVT(ctypes.Structure):
    pass


SDL_AudioFilter = ctypes.CFUNCTYPE(None, ctypes.POINTER(SDL_AudioCVT),
                                   ctypes.c_ushort)


SDL_AudioCVT._fields_ = [("_needed", ctypes.c_int),
                         ("_src_format", ctypes.c_ushort),
                         ("_dst_format", ctypes.c_ushort),
                         ("_rate_incr", ctypes.c_double),
                         ("_buf", ctypes.POINTER(ctypes.c_ubyte)),
                         ("_len", ctypes.c_int),
                         ("_len_cvt", ctypes.c_int),
                         ("_len_mult", ctypes.c_int),
                         ("_len_ratio", ctypes.c_double),
                         ("_filters", (SDL_AudioFilter * 10)),
                         ("_filter_index", ctypes.c_int)
                         ]


@sdltype("SDL_GetNumAudioDrivers", None, ctypes.c_int)
def get_num_audio_drivers():
    """Gets the numver of built in audio drivers.
    """
    return dll.SDL_GetNumAudioDrivers()


@sdltype("SDL_GetAudioDriver", [ctypes.c_int], ctypes.c_char_p)
def get_audio_driver(index):
    """Gets the name of a specific audio driver.
    """
    if type(index) is not int:
        raise TypeError("index must be an int")
    retval = dll.SDL_GetAudioDriver(index)
    if retval is None or not bool(retval):
        raise SDLError()
    return stringify(retval, "utf-8")


@sdltype("SDL_AudioInit", [ctypes.c_char_p], ctypes.c_int)
def audio_init(drivername):
    """Initializes the SDL audio subsystem  with the passed driver.

    NOTE: Do not use init() - those might lead to SIGSEGV crashes - use
    the SDL_AUDIODRIVER environment variable before calling
    pygame2.sdl.init_subsystem() instead.
    """
    drivername = byteify(drivername, "utf-8")
    retval = dll.SDL_AudioInit(drivername)
    if retval != 0:
        raise SDLError()


@sdltype("SDL_AudioQuit", None, None)
def audio_quit():
    """Quits the SDL audio subsystem.

    NOTE: Do not use quit() - this might lead to inconsistent internal
    SDL2 states - use pygame2.sdl.quit_subsystem() instead.
    """
    dll.SDL_AudioQuit()


@sdltype("SDL_GetCurrentAudioDriver", None, ctypes.c_char_p)
def get_current_audio_driver():
    """Gets the currently used audio driver.
    """
    retval = dll.SDL_GetCurrentAudioDriver()
    if retval is None or not bool(retval):
        return None
    return stringify(retval, "utf-8")


@sdltype("SDL_OpenAudio", [ctypes.POINTER(SDL_AudioSpec),
                           ctypes.POINTER(SDL_AudioSpec)], ctypes.c_int)
def open_audio(desired):
    """Opens the audio device with the desired parameters.

    If the return value is None, the audio data passed to the set
    callback function in desired will be guaranteed to be in the
    requested format, and will be automatically converted to the
    hardware audio format if necessary.
    """
    if not isinstance(desired, SDL_AudioSpec):
        raise TypeError("desired must be a SDL_AudioSpec")
    obtained = SDL_AudioSpec(0, 0, 0, 0, None, None)
    retval = dll.SDL_OpenAudio(ctypes.byref(desired), ctypes.byref(obtained))
    if retval == -1:
        raise SDLError()
    return obtained


@sdltype("SDL_GetNumAudioDevices", [ctypes.c_int], ctypes.c_int)
def get_num_audio_devices(iscapture=False):
    """Gets the number of available audio devices.

    If iscapture is True, only input (capture) devices are queried,
    otherwise only output devices are queried. In some cases, this might
    return -1, indicating that the number of available devices could not
    be determined (e.g. for network sound servers). You should check for
    an error by calling pygame2.sdl.get_error() in those cases.
    """
    if bool(iscapture):
        return dll.SDL_GetNumAudioDevices(1)
    else:
        return dll.SDL_GetNumAudioDevices(0)


@sdltype("SDL_GetAudioDeviceName", [ctypes.c_int, ctypes.c_int],
         ctypes.c_char_p)
def get_audio_device_name(index, iscapture):
    """
    """
    retval = dll.SDL_GetAudioDeviceName(index, iscapture)
    if retval is None or not bool(retval):
        raise SDLError()
    return stringify(retval, "utf-8")


@sdltype("SDL_OpenAudioDevice", [ctypes.c_char_p, ctypes.c_int,
                                 ctypes.POINTER(SDL_AudioSpec),
                                 ctypes.POINTER(SDL_AudioSpec), ctypes.c_int],
         ctypes.c_uint)
def open_audio_device(device, iscapture, desired, allowed_changes):
    """
    """
    if not isinstance(desired, SDL_AudioSpec):
        raise TypeError("desired must be a SDL_AudioSpec")
    device = byteify(device, "utf-8")
    if bool(iscapture):
        iscapture = 1
    else:
        iscapture = 0
    obtained = SDL_AudioSpec(0, 0, 0, 0, None, None)
    retval = dll.SDL_OpenAudioDevice(device, iscapture, ctypes.byref(desired),
                                     ctypes.byref(obtained), allowed_changes)
    if retval == 0:
        raise SDLError()
    return retval


@sdltype("SDL_GetAudioStatus", None, ctypes.c_int)
def get_audio_status():
    """
    """
    return dll.SDL_GetAudioStatus()


@sdltype("SDL_GetAudioDeviceStatus", [ctypes.c_uint], ctypes.c_int)
def get_audio_device_status(device):
    """
    """
    return dll.SDL_GetAudioDeviceStatus(device)


@sdltype("SDL_PauseAudio", [ctypes.c_int], None)
def pause_audio(pause_on):
    """
    """
    if bool(pause_on):
        dll.SDL_PauseAudio(1)
    else:
        dll.SDL_PauseAudio(0)


@sdltype("SDL_PauseAudioDevice", [ctypes.c_uint, ctypes.c_int], None)
def pause_audio_device(device, pause_on):
    """
    """
    if bool(pause_on):
        dll.SDL_PauseAudioDevice(device, 1)
    else:
        dll.SDL_PauseAudioDevice(device, 0)


@sdltype("SDL_LoadWAV_RW", [ctypes.POINTER(SDL_RWops), ctypes.c_int,
                            ctypes.POINTER(SDL_AudioSpec),
                            ctypes.POINTER(ctypes.POINTER(ctypes.c_ubyte)),
                            ctypes.POINTER(ctypes.c_uint)],
         ctypes.POINTER(SDL_AudioSpec))
def load_wav_rw(rwops, freesrc):
    """
    """
    if not isinstance(rwops, SDL_RWops):
        raise TypeError("rwops must be a SDL_RWops")

    spec = SDL_AudioSpec()
    audiobuf = ctypes.POINTER(ctypes.c_ubyte())
    audiolen = ctypes.c_uint()
    retval = dll.SDL_LoadWAV_RW(ctypes.byref(rwops), freesrc,
                                ctypes.byref(spec), ctypes.byref(audiobuf),
                                ctypes.byref(audiolen))
    if retval is None or not bool(retval):
        raise SDLError()
    return spec, audiobuf.contents, audiolen.value


def load_wav(filename):
    """
    """
    rwops = rw_from_file(filename, "rb")
    return load_wav_rw(rwops, 1)


@sdltype("SDL_FreeWAV", [ctypes.POINTER(ctypes.c_ubyte)], None)
def free_wav(buf):
    """
    """
    dll.SDL_FreeWAV(ctypes.byref(buf))


@sdltype("SDL_BuildAudioCVT", [ctypes.POINTER(SDL_AudioCVT), ctypes.c_ushort,
                               ctypes.c_ubyte, ctypes.c_int, ctypes.c_ushort,
                               ctypes.c_ubyte, ctypes.c_int], ctypes.c_int)
def build_audio_cvt(src_format, src_channels, src_rate, dst_format,
                    dst_channels, dst_rate):
    """
    """
    cvt = SDL_AudioCVT()
    retval = dll.SDL_BuildAudioCVT(ctypes.byref(cvt), src_format, src_channels,
                                   src_rate, dst_format, dst_channels,
                                   dst_rate)
    if retval == -1:
        raise SDLError()
    return cvt


@sdltype("SDL_ConvertAudio", [ctypes.POINTER(SDL_AudioCVT)], ctypes.c_int)
def convert_audio(cvt):
    """
    """
    if not isinstance(cvt, SDL_AudioCVT):
        raise TypeError("cvt must be a SDL_AudioCVT")
    retval = dll.SDL_ConvertAudio(ctypes.byref(cvt))
    if retval != 0:
        raise SDLError()


@sdltype("SDL_MixAudio", [ctypes.POINTER(ctypes.c_ubyte),
                          ctypes.POINTER(ctypes.c_ubyte), ctypes.c_uint,
                          ctypes.c_int], None)
def mix_audio(dst, src, length, volume):
    """
    """
    if len(dst) < length:
        raise ValueError("dst is too small")
    if len(src) < length:
        raise ValueError("src is too small")
    dll.SDL_MixAudio(ctypes.byref(dst), ctypes.byref(src), length, volume)


@sdltype("SDL_MixAudioFormat", [ctypes.POINTER(ctypes.c_ubyte),
                                ctypes.POINTER(ctypes.c_ubyte),
                                ctypes.c_ushort, ctypes.c_uint, ctypes.c_int],
         None)
def mix_audio_format(dst, src, aformat, length, volume):
    """
    """
    if len(dst) < length:
        raise ValueError("dst is too small")
    if len(src) < length:
        raise ValueError("src is too small")
    dll.SDL_MixAudio(ctypes.byref(dst), ctypes.byref(src), aformat, length,
                     volume)


@sdltype("SDL_LockAudio", None, None)
def lock_audio():
    """
    """
    dll.SDL_LockAudio()


@sdltype("SDL_LockAudioDevice", [ctypes.c_uint], None)
def lock_audio_device(device):
    """
    """
    dll.SDL_LockAudioDevice(device)


@sdltype("SDL_UnlockAudio", None, None)
def unlock_audio():
    """
    """
    dll.SDL_UnlockAudio()


@sdltype("SDL_UnlockAudioDevice", [ctypes.c_uint], None)
def unlock_audio_device(device):
    """
    """
    dll.SDL_UnlockAudioDevice(device)


@sdltype("SDL_CloseAudio", None, None)
def close_audio():
    """
    """
    dll.SDL_CloseAudio()


@sdltype("SDL_CloseAudioDevice", [ctypes.c_uint], None)
def close_audio_device(device):
    """
    """
    dll.SDL_CloseAudioDevice(device)


#@sdltype("SDL_AudioDeviceConnected", [ctypes.c_uint], None)
#def audio_device_connected(device):
#    """
#    """
#    retval = dll.SDL_AudioDeviceConnected(device)
#    if retval == -1:
#        raise SDLError()
#    return retval == 1
