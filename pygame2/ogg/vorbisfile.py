"""
A thin wrapper package around the vorbisfile library.
"""
import ctypes
from pygame2.dll import DLL
from pygame2.ogg import OggError

__all__ = ["OggVorbis_File", "clear", "fopen", "pcm_total", "read", "info"
           ]


dll = DLL("vorbisfile", {"win32": ["libvorbisfile", "vorbisfile"],
                         "DEFAULT": ["vorbisfile"]
                         })
vfiletype = dll.get_decorator()


OV_FALSE = -1
OV_EOF =   -2
OV_HOLE =  -3

OV_EREAD =      -128
OV_EFAULT =     -129
OV_EIMPL =      -130
OV_EINVAL =     -131
OV_ENOTVORBIS = -132
OV_EBADHEADER = -133
OV_EVERSION =   -134
OV_ENOTAUDIO =  -135
OV_EBADPACKET = -136
OV_EBADLINK =   -137
OV_ENOSEEK =    -138

_ERRMAP = {OV_EREAD: "Error on reading data",
           OV_EFAULT: "Internal error",
           OV_EIMPL: "Implementation error",
           OV_EINVAL: "Invalid value",
           OV_ENOTVORBIS: "Invalid vorbis data",
           OV_EBADHEADER: "Bad bitstream header information",
           OV_EVERSION: "Vorbis version mismatch",
           OV_ENOTAUDIO: "Invalid audio data",
           OV_EBADPACKET: "Bad packet on reading",
           OV_EBADLINK: "Bad link",
           OV_ENOSEEK: "Data does not support seeking",
           }
_FASTERROR = lambda xid: _ERRMAP.get(xid, "Unkown error")

# ogg_int64_t = long long = c_longlong = c_int64
_ovread = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p, ctypes.c_int,
                           ctypes.c_int, ctypes.c_void_p)
_ovseek = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p, ctypes.c_int64,
                           ctypes.c_int)
_ovclose = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p)
_ovtell = ctypes.CFUNCTYPE(ctypes.c_long, ctypes.c_void_p)


class ov_callbacks(ctypes.Structure):
    """A callback handler structure for reading OGG-Vorbis streams."""
    _fields_ = [("read_func", _ovread),
                ("seek_func", _ovseek),
                ("close_func", _ovclose),
                ("tell_func", _ovtell)
                ]


class vorbis_info(ctypes.Structure):
    """Information about a vorbis stream."""
    _fields_ = [("version", ctypes.c_int),
                ("channels", ctypes.c_int),
                ("rate", ctypes.c_long),
                ("bitrate_upper", ctypes.c_long),
                ("bitrate_nominal", ctypes.c_long),
                ("bitrate_lower", ctypes.c_long),
                ("bitrate_window", ctypes.c_long),
                ("codec_setup, ", ctypes.c_void_p)
                ]

    def __repr__(self):
        return "vorbis_info(version=%d, channels=%d, rate=%d)" % \
            (self.version, self.channels, self.rate)


class OggVorbis_File(ctypes.Structure):
    """OggVorbis file structure."""
    pass


def get_dll_file():
    """Gets the file name of the loaded Vorbisfile library."""
    return dll.libfile


@vfiletype("ov_clear", [ctypes.POINTER(OggVorbis_File)], ctypes.c_int)
def clear(ovfilep):
    """Releases the resources held by a OggVorbis_File.

    Note: do not use the passed OggVorbis_File after calling this
    function.
    """
    retval = dll.ov_clear(ctypes.byref(ovfilep))
    if retval != 0:
        raise OggError(_FASTERROR(retval))


@vfiletype("ov_fopen", [ctypes.c_char_p, ctypes.POINTER(OggVorbis_File)],
           ctypes.c_int)
def fopen(fname):
    """Opens a file and loads it into a OggVorbis_File."""
    ovf = OggVorbis_File()
    retval = dll.ov_fopen(str(fname), ctypes.byref(ovf))
    if retval != 0:
        raise OggError(_FASTERROR(retval))
    return ovf


@vfiletype("ov_info", [ctypes.POINTER(OggVorbis_File), ctypes.c_int],
           ctypes.POINTER(vorbis_info))
def info(ovfilep, bstream=-1):
    """Retrieves the vorbis information from the OggVorbis_File."""
    # TODO: rewrite this by implementing the info() lookup code - since
    # it is a struct value of OggVorbis_File, we can create random
    # segfaults and bus errors, if the OggVorbis_File is freed in the
    # meantime.
    ovinfo = dll.ov_info(ctypes.byref(ovfilep), bstream)
    if ovinfo is None or not bool(ovinfo):
        raise OggError("invalid bitstream or file")
    return ovinfo


@vfiletype("ov_pcm_total", [ctypes.POINTER(OggVorbis_File), ctypes.c_int],
           ctypes.c_int64)
def pcm_total(ovfilep, bstream=-1):
    """Retrieves the total size in bytes of the PCM buffer of a
    OggVorbis_File.
    """
    retval = dll.ov_pcm_total(ovfilep, bstream)
    if retval < 0:
        raise OggError(_FASTERROR(retval))
    return retval


@vfiletype("ov_read", [ctypes.POINTER(OggVorbis_File),
                       ctypes.POINTER(ctypes.c_char), ctypes.c_int,
                       ctypes.c_int, ctypes.c_int, ctypes.c_int,
                       ctypes.POINTER(ctypes.c_int)], ctypes.c_int)
def read(ovfilep, length, outbuf=None, bigendian=False, word=2, signed=True):
    """Loads the PCM buffer of a OggVorbis_File."""
    if word not in (1, 2):
        raise ValueError("word must be 1 (8-bit) or 2 (16-bit samples)")
    cursection = ctypes.c_int(0)
    if not bigendian:
        bigendian = 0
    else:
        bigendian = 1
    if not signed:
        signed = 0
    else:
        signed = 1
    if outbuf is None:
        outbuf = (ctypes.c_char * length)()
    ptr = ctypes.cast(outbuf, ctypes.POINTER(ctypes.c_char))
    retval = dll.ov_read(ctypes.byref(ovfilep), ptr, length, bigendian,
                         word, signed, ctypes.byref(cursection))
    if retval == 0:
        return None
    if retval < 0:
        raise OggError(_FASTERROR(retval))
    return outbuf, retval, cursection
