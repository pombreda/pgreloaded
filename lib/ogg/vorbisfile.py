"""
A thin wrapper package around the vorbisfile library.
"""
import sys
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
    _fields_ = [("read_func", _ovread),
                ("seek_func", _ovseek),
                ("close_func", _ovclose),
                ("tell_func", _ovtell)
                ]


class vorbis_info(ctypes.Structure):
    _fields_ = [("version", ctypes.c_int),
                ("channels", ctypes.c_int),
                ("rate", ctypes.c_long),
                ("bitrate_upper", ctypes.c_long),
                ("bitrate_nominal", ctypes.c_long),
                ("bitrate_lower", ctypes.c_long),
                ("bitrate_window", ctypes.c_long),
                ("codec_setup, ", ctypes.c_void_p)
                ]


class OggVorbis_File(ctypes.Structure):
    pass


def get_dll_file():
    """Gets the file name of the loaded Vorbisfile library."""
    return dll.libfile

    
@vfiletype("ov_clear", [ctypes.POINTER(OggVorbis_File)], ctypes.c_int)
def clear(ovfilep):
    """x"""
    if not isinstance(ovfilep, OggVorbis_File):
        raise TypeError("ovfilep must be an OggVorbis_File")
    retval = dll.ov_clear(ctypes.byref(ovfilep))
    if retval != 0:
        raise OggVorbisError(_FASTERROR(retval))


@vfiletype("ov_fopen", [ctypes.c_char_p, ctypes.POINTER(OggVorbis_File)],
           ctypes.c_int)
def fopen(fname):
    """x"""
    ovf = OggVorbis_File()
    retval = dll.ov_fopen(fname, ctypes.byref(ovf))
    if retval != 0:
        raise OggVorbisError(_FASTERROR(retval))
    return ovf


@vfiletype("ov_info", [ctypes.POINTER(OggVorbis_File), ctypes.c_int],
           ctypes.POINTER(vorbis_info))
def info(ovfilep, bstream=-1):
    """x"""
    if not isinstance(ovfilep, OggVorbis_File):
        raise TypeError("ovfilep must be an OggVorbis_File")
    info = dll.ov_info(ctypes.byref(ovfilep), bstream)
    if info is None or not bool(info):
        raise OggVorbisError("invalid bitstream or file")
    return info.contents


@vfiletype("ov_pcm_total", [ctypes.POINTER(OggVorbis_File), ctypes.c_int],
           ctypes.c_int64)
def pcm_total(ovfilep, bstream=-1):
    """x"""
    if not isinstance(ovfilep, OggVorbis_File):
        raise TypeError("ovfilep must be an OggVorbis_File")
    retval = dll.ov_pcm_total(ovfilep, bstream)
    if retval < 0:
        raise OggVorbisError(_FASTERROR(retval))
    return retval


@vfiletype("ov_read", [ctypes.POINTER(OggVorbis_File),
                       ctypes.POINTER(ctypes.c_char), ctypes.c_int,
                       ctypes.c_int, ctypes.c_int, ctypes.c_int,
                       ctypes.POINTER(ctypes.c_int)], ctypes.c_int)
def read(ovfilep, length, outbuf=None, bigendian=False, word=2, signed=True):
    """x"""
    if not isinstance(ovfilep, OggVorbis_File):
        raise TypeError("ovfilep must be an OggVorbis_File")
    if word not in (1, 2):
        raise ValueError("word must be 1 (8-bit) or 2 (16-bit samples)")
    cursection = ctypes.c_int()
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
    retval = dll.ov_read(ctypes.byref(ovfilep), ctypes.byref(outbuf), length,
                         bigendian, word, signed, ctypes.byref(cursection))
    if retval == 0:
        return None
    if retval < 0:
        raise OggVorbisError(_FASTERROR(retval))
    return outbuf, retval, cursection
