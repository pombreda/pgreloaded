"""
Pygame2 OpenAL wrapper.
"""
import ctypes
import pygame2.array as array
from pygame2.compat import byteify, stringify
from pygame2.openal import dll, openaltype

__all__ = ["get_error", "OpenALError", "enable", "disable", "is_enabled",
           "get_string", "get_boolean_v", "get_integer_v", "get_float_v",
           "get_double_v", "get_boolean", "get_integer", "get_float",
           "get_double", "is_extension_present", "get_proc_address",
           "get_enum_value", "listener_f", "listener_3f", "listener_fv",
           "listener_i", "listener_3i", "listener_iv", "get_listener_f",
           "get_listener_3f", "get_listener_fv", "get_listener_i",
           "get_listener_3i", "get_listener_iv", "gen_sources",
           "delete_sources", "is_source", "source_f", "source_3f",
           "source_fv", "source_i", "source_3i", "source_iv", "get_source_f",
           "get_source_3f", "get_source_fv", "get_source_i", "get_source_3i",
           "get_source_iv", "source_play_v", "source_stop_v",
           "source_rewind_v", "source_pause_v", "source_play", "source_stop",
           "source_rewind", "source_pause", "source_queue_buffers",
           "source_unqueue_buffers", "gen_buffers", "delete_buffers",
           "is_buffer", "buffer_data", "buffer_f", "buffer_3f", "buffer_fv",
           "buffer_i", "buffer_3i", "buffer_iv", "get_buffer_f",
           "get_buffer_3f", "get_buffer_fv", "get_buffer_i", "get_buffer_3i",
           "get_buffer_iv", "doppler_factor", "doppler_velocity",
           "speed_of_source", "distance_model"
           ]

AL_INVALID = -1
AL_NONE = 0

AL_FALSE = 0
AL_TRUE =  1

AL_SOURCE_RELATIVE = 0x202

AL_CONE_INNER_ANGLE = 0x1001
AL_CONE_OUTER_ANGLE = 0x1002
AL_PITCH =            0x1003
AL_POSITION =         0x1004
AL_DIRECTION =        0x1005
AL_VELOCITY =         0x1006
AL_LOOPING =          0x1007
AL_BUFFER =           0x1009
AL_GAIN =             0x100A
AL_MIN_GAIN =         0x100D
AL_MAX_GAIN =         0x100E
AL_ORIENTATION =      0x100F

AL_CHANNEL_MASK = 0x3000

AL_SOURCE_STATE =      0x1010
AL_INITIAL =           0x1011
AL_PLAYING =           0x1012
AL_PAUSED =            0x1013
AL_STOPPED =           0x1014
AL_BUFFERS_QUEUED =    0x1015
AL_BUFFERS_PROCESSED = 0x1016

AL_SEC_OFFSET =    0x1024
AL_SAMPLE_OFFSET = 0x1025
AL_BYTE_OFFSET =   0x1026
AL_SOURCE_TYPE =   0x1027
AL_STATIC =        0x1028
AL_STREAMING =     0x1029
AL_UNDETERMINED =  0x1030

AL_FORMAT_MONO8 =    0x1100
AL_FORMAT_MONO16 =   0x1101
AL_FORMAT_STEREO8 =  0x1102
AL_FORMAT_STEREO16 = 0x1103

AL_REFERENCE_DISTANCE = 0x1020
AL_ROLLOFF_FACTOR =     0x1021
AL_CONE_OUTER_GAIN =    0x1022
AL_MAX_DISTANCE =       0x1023

AL_FREQUENCY = 0x2001
AL_BITS =      0x2002
AL_CHANNELS =  0x2003
AL_SIZE =      0x2004

AL_UNUSED =    0x2010
AL_PENDING =   0x2011
AL_PROCESSED = 0x2012

AL_NO_ERROR = AL_FALSE
AL_INVALID_NAME =      0xA001
AL_ILLEGAL_ENUM =      0xA002
AL_INVALID_ENUM =      0xA002
AL_INVALID_VALUE =     0xA003
AL_ILLEGAL_COMMAND =   0xA004
AL_INVALID_OPERATION = 0xA004
AL_OUT_OF_MEMORY =     0xA005

AL_VENDOR =     0xB001
AL_VERSION =    0xB002
AL_RENDERER =   0xB003
AL_EXTENSIONS = 0xB004

AL_DOPPLER_FACTOR =   0xC000
AL_DOPPLER_VELOCITY = 0xC001
AL_SPEED_OF_SOUND =   0xC003

AL_DISTANCE_MODEL =            0xD000
AL_INVERSE_DISTANCE =          0xD001
AL_INVERSE_DISTANCE_CLAMPED =  0xD002
AL_LINEAR_DISTANCE =           0xD003
AL_LINEAR_DISTANCE_CLAMPED =   0xD004
AL_EXPONENT_DISTANCE =         0xD005
AL_EXPONENT_DISTANCE_CLAMPED = 0xD006


_ERRMAP = {
    AL_NO_ERROR: "No Error",
    AL_INVALID_NAME: "Invalid name",
    AL_INVALID_ENUM: "Invalid enum",
    AL_INVALID_VALUE: "Invalid value",
    AL_INVALID_OPERATION: "Invalid operation",
    AL_OUT_OF_MEMORY: "Out of memory"
    }

def _clear_error():
    get_error()


def _raise_error_or_continue():
    errcode = get_error()
    if errcode == AL_NO_ERROR:
        return
    if errcode in _ERRMAP:
        raise OpenALError(_ERRMAP[errcode])
    else:
        raise OpenALError("Error code [%d]" % errcode)


@openaltype("alGetError", None, ctypes.c_int)
def get_error():
    """Gets the most recent error generated within the AL system."""
    return dll.alGetError()


class OpenALError(Exception):
    """An OpenAL specific exception class."""
    def __init__(self, msg=None):
        """Creates a new OpenALError instance with the specified message.

        If no msg is provided, the message will be set a mapped value of
        get_error().
        """
        super(OpenALError, self).__init__(self)
        self.msg = msg
        if msg is None:
            errcode = get_error()
            if errcode in _ERRMAP:
                self.msg = _ERRMAP[errcode]
            else:
                self.msg = "Error code [%d]" % errcode

    def __str__(self):
        return repr(self.msg)


@openaltype("alEnable", [ctypes.c_int], None)
def enable(capability):
    """Enables a feature of the OpenAL driver."""
    dll.alEnable(capability)
    _raise_error_or_continue()


@openaltype("alDisable", [ctypes.c_int], None)
def disable(capability):
    """Disables a feature of the OpenAL driver."""
    dll.alDisable(capability)
    _raise_error_or_continue()


@openaltype("alIsEnabled", [ctypes.c_int], ctypes.c_byte)
def is_enabled(capability):
    """Checks, if a feature of the OpenAL driver is currently enabled."""
    return dll.alIsEnabled(capability) == AL_TRUE
    _raise_error_or_continue()


@openaltype("alGetString", [ctypes.c_int], ctypes.c_char_p)
def get_string(param):
    """Retrieves an OpenAL string property."""
    retval = dll.alGetString(param)
    _raise_error_or_continue()
    return retval

@openaltype("alGetBooleanv", [ctypes.c_int, ctypes.POINTER(ctypes.c_byte)],
            None)
def get_boolean_v(param):
    """Retrieves an OpenAL boolean state."""
    val = ctypes.c_byte(0)
    dll.alGetBooleanv(param, ctypes.byref(val))
    _raise_error_or_continue()
    return val.value


@openaltype("alGetIntegerv", [ctypes.c_int, ctypes.POINTER(ctypes.c_int)],
            None)
def get_integer_v(param):
    """Retrieves an OpenAL integer state."""
    val = ctypes.c_int(0)
    dll.alGetIntegerv(param, ctypes.byref(val))
    _raise_error_or_continue()
    return val.value


@openaltype("alGetFloatv", [ctypes.c_int, ctypes.POINTER(ctypes.c_float)],
            None)
def get_float_v(param):
    """Retrieves an OpenAL float state."""
    val = ctypes.c_float(0)
    dll.alGetFloatv(param, ctypes.byref(val))
    _raise_error_or_continue()
    return val.value


@openaltype("alGetDoublev", [ctypes.c_int, ctypes.POINTER(ctypes.c_double)],
            None)
def get_double_v(param):
    """Retrieves an OpenAL double state."""
    val = ctypes.c_double(0)
    dll.alGetDoublev(param, ctypes.byref(val))
    _raise_error_or_continue()
    return val.value


@openaltype("alGetBoolean", [ctypes.c_int], ctypes.c_byte)
def get_boolean(param):
    """Returns an OpenAL boolean state."""
    val = dll.alGetBoolean(param)
    _raise_error_or_continue()
    return val


@openaltype("alGetInteger", [ctypes.c_int], ctypes.c_int)
def get_integer(param):
    """Returns an OpenAL integer state."""
    val = dll.alGetInteger(param)
    _raise_error_or_continue()
    return val


@openaltype("alGetFloat", [ctypes.c_int], ctypes.c_float)
def get_float(param):
    """Returns an OpenAL float state."""
    val = dll.alGetFloat(param)
    _raise_error_or_continue()
    return val


@openaltype("alGetDouble", [ctypes.c_int], ctypes.c_double)
def get_double(param):
    """Returns an OpenAL double state."""
    val = dll.alGetDouble(param)
    _raise_error_or_continue()
    return val


@openaltype("alIsExtensionPresent", [ctypes.c_char_p], ctypes.c_byte)
def is_extension_present(extname):
    """Tests if the specified extension is available for the OpenAL driver."""
    extname = byteify(extname, "utf-8")
    return dll.alIsExtensionPresent(extname) == AL_TRUE


@openaltype("alGetProcAddress", [ctypes.c_char_p], ctypes.c_void_p)
def get_proc_address(fname):
    """Returns the address of an OpenAL extension function."""
    fname = byteify(fname, "utf-8")
    return dll.alGetProcAddress(fname)


@openaltype("alGetEnumValue", [ctypes.c_char_p], ctypes.c_int)
def get_enum_value(ename):
    """Returns the enumeration value of an OpenAL enum."""
    ename = byteify(ename, "utf-8")
    return dll.alGetEnumValue(ename)


@openaltype("alListenerf", [ctypes.c_int, ctypes.c_float], None)
def listener_f(param, value):
    """Sets a floating point property for the listener."""
    dll.alListenerf(param, value)
    _raise_error_or_continue()


@openaltype("alListener3f", [ctypes.c_int, ctypes.c_float, ctypes.c_float,
                             ctypes.c_float], None)
def listener_3f(param, value1, value2, value3):
    """Sets a floating point property for the listener."""
    dll.alListener3f(param, value1, value2, value3)
    _raise_error_or_continue()


@openaltype("alListenerfv", [ctypes.c_int, ctypes.POINTER(ctypes.c_float)],
            None)
def listener_fv(param, values):
    """Sets a floating point-vector property for the listener """
    values, size = array.to_ctypes(values, ctypes.c_float)
    ptr = ctypes.cast(values, ctypes.POINTER(ctypes.c_float))
    dll.alListenerfv(param, ptr)
    _raise_error_or_continue()


@openaltype("alListeneri", [ctypes.c_int, ctypes.c_int], None)
def listener_i(param, value):
    """Sets an integer property for the listener."""
    dll.alListeneri(param, value)
    _raise_error_or_continue()


@openaltype("alListener3i", [ctypes.c_int, ctypes.c_int, ctypes.c_int,
                             ctypes.c_int], None)
def listener_3i(param, value1, value2, value3):
    """Sets an integer property for the listener."""
    dll.alListener3i(param, value1, value2, value3)
    _raise_error_or_continue()


@openaltype("alListeneriv", [ctypes.c_int, ctypes.POINTER(ctypes.c_int)], None)
def listener_iv(param, values):
    """Sets an integer-vector property for the listener."""
    values, size = array.to_ctypes(values, ctypes.c_int)
    ptr = ctypes.cast(values, ctypes.POINTER(ctypes.c_int))
    dll.alListeneriv(param, ptr)
    _raise_error_or_continue()


@openaltype("alGetListenerf", [ctypes.c_int, ctypes.POINTER(ctypes.c_float)],
            None)
def get_listener_f(param):
    """Gets a floating point property for the listener."""
    val = ctypes.c_float(0)
    dll.alGetListenerf(param, ctypes.byref(val))
    _raise_error_or_continue()
    return val.value


@openaltype("alGetListener3f", [ctypes.c_int, ctypes.POINTER(ctypes.c_float),
                                ctypes.POINTER(ctypes.c_float),
                                ctypes.POINTER(ctypes.c_float)], None)
def get_listener_3f(param):
    """Gets a floating point property for the listener and returns it
    as tuple.
    """
    val1 = ctypes.c_float(0)
    val2 = ctypes.c_float(0)
    val3 = ctypes.c_float(0)
    dll.alGetListener3f(param, ctypes.byref(val1), ctypes.byref(val2),
                        ctypes.byref(val3))
    _raise_error_or_continue()
    return (val1.value, val2.value, val3.value)


@openaltype("alGetListenerfv", [ctypes.c_int, ctypes.POINTER(ctypes.c_float)],
            None)
def get_listener_fv(param, size):
    """Gets a floating point-vector property for the listener and
    returns it as tuple.
    """
    val = (ctypes.c_float * size)()
    dll.alGetListenerfv(param, ctypes.byref(val))
    _raise_error_or_continue()
    return val


@openaltype("alGetListeneri", [ctypes.c_int, ctypes.POINTER(ctypes.c_int)],
            None)
def get_listener_i(param):
    """Gets an integer property for the listener."""
    val = ctypes.c_int(0)
    dll.alGetListeneri(param, ctypes.byref(val))
    _raise_error_or_continue()
    return val.value


@openaltype("alGetListener3i", [ctypes.c_int, ctypes.POINTER(ctypes.c_int),
                                ctypes.POINTER(ctypes.c_int),
                                ctypes.POINTER(ctypes.c_int)], None)
def get_listener_3i(param):
    """Gets an integer property for the listener and returns it as
    tuple.
    """
    val1 = ctypes.c_int(0)
    val2 = ctypes.c_int(0)
    val3 = ctypes.c_int(0)
    dll.alGetListener3i(param, ctypes.byref(val1), ctypes.byref(val2),
                        ctypes.byref(val3))
    _raise_error_or_continue()
    return (val1.value, val2.value, val3.value)


@openaltype("alGetListeneriv", [ctypes.c_int, ctypes.POINTER(ctypes.c_int)],
            None)
def get_listener_iv(param, size):
    """Gets an integer-vector property for the listener and returns it
    as tuple.
    """
    val = (ctypes.c_int * size)()
    dll.alGetListeneriv(param, ctypes.byref(val))
    _raise_error_or_continue()
    return val


@openaltype("alGenSources", [ctypes.c_int, ctypes.POINTER(ctypes.c_uint)],
            None)
def gen_sources(size):
    """Generates one or more sources and returns their ids as tuple."""
    sources = (ctypes.c_uint * size)()
    ptr = ctypes.cast(sources, ctypes.POINTER(ctypes.c_uint))
    dll.alGenSources(size, ptr)
    _raise_error_or_continue()
    return sources


@openaltype("alDeleteSources", [ctypes.c_int, ctypes.POINTER(ctypes.c_uint)],
            None)
def delete_sources(sources):
    """Deletes one or more sources."""
    sources, size = array.to_ctypes(sources, ctypes.c_uint)
    ptr = ctypes.cast(sources, ctypes.POINTER(ctypes.c_uint))
    dll.alDeleteSources(size, ptr)
    _raise_error_or_continue()


@openaltype("alIsSource", [ctypes.c_uint], ctypes.c_byte)
def is_source(sid):
    """Tests if the passed sid is a valid source identifier."""
    val = dll.alIsSource(sid) == AL_TRUE
    _raise_error_or_continue()
    return val


@openaltype("alSourcef", [ctypes.c_uint, ctypes.c_int, ctypes.c_float], None)
def source_f(sid, param, value):
    """Sets a floating point property of a source."""
    dll.alSourcef(sid, param, value)
    _raise_error_or_continue()


@openaltype("alSource3f", [ctypes.c_uint, ctypes.c_int, ctypes.c_float,
                           ctypes.c_float, ctypes.c_float], None)
def source_3f(sid, param, value1, value2, value3):
    """Sets a floating point property of a source."""
    dll.alSource3f(sid, param, value1, value2, value3)
    _raise_error_or_continue()


@openaltype("alSourcefv", [ctypes.c_uint, ctypes.c_int,
                           ctypes.POINTER(ctypes.c_float)], None)
def source_fv(sid, param, values):
    """Sets a floating point-vector property of a source."""
    values, size = array.to_ctypes(values, ctypes.c_float)
    ptr = ctypes.cast(values, ctypes.POINTER(ctypes.c_float))
    dll.alSourcefv(sid, param, ptr)
    _raise_error_or_continue()


@openaltype("alSourcei", [ctypes.c_uint, ctypes.c_int, ctypes.c_int], None)
def source_i(sid, param, value):
    """Sets an integer property of a source."""
    dll.alSourcei(sid, param, value)
    _raise_error_or_continue()


@openaltype("alSource3i", [ctypes.c_uint, ctypes.c_int, ctypes.c_int,
                           ctypes.c_int, ctypes.c_int], None)
def source_3i(sid, param, value1, value2, value3):
    """Sets an integer property of a source."""
    dll.alSource3i(sid, param, value1, value2, value3)
    _raise_error_or_continue()


@openaltype("alSourceiv", [ctypes.c_uint, ctypes.c_int,
                           ctypes.POINTER(ctypes.c_int)], None)
def source_iv(sid, param, values):
    """Sets an integer-vector property of a source."""
    values, size = array.to_ctypes(values, ctypes.c_int)
    ptr = ctypes.cast(values, ctypes.POINTER(ctypes.c_int))
    dll.alSourceiv(sid, param, ptr)
    _raise_error_or_continue()


@openaltype("alGetSourcef", [ctypes.c_uint, ctypes.c_int,
                             ctypes.POINTER(ctypes.c_float)], None)
def get_source_f(sid, param):
    """Gets a floating point property of a source."""
    val = ctypes.c_float(0)
    dll.alGetSourcef(sid, param, ctypes.byref(val))
    _raise_error_or_continue()
    return val.value


@openaltype("alGetSource3f", [ctypes.c_uint, ctypes.c_int,
                              ctypes.POINTER(ctypes.c_float),
                              ctypes.POINTER(ctypes.c_float),
                              ctypes.POINTER(ctypes.c_float)], None)
def get_source_3f(sid, param):
    """Gets a floating point property of a source and returns it as
    tuple.  """
    val1 = ctypes.c_float(0)
    val2 = ctypes.c_float(0)
    val3 = ctypes.c_float(0)
    dll.alGetSource3f(sid, param, ctypes.byref(val1), ctypes.byref(val2),
                      ctypes.byref(val3))
    _raise_error_or_continue()
    return (val1.value, val2.value, val3.value)


@openaltype("alGetSourcefv", [ctypes.c_uint, ctypes.c_int,
                              ctypes.POINTER(ctypes.c_float)], None)
def get_source_fv(sid, param, size):
    """Gets a floating point-vector property of a source."""
    val = (ctypes.c_float * size)()
    dll.alGetSourcefv(sid, param, ctypes.byref(val))
    _raise_error_or_continue()
    return val


@openaltype("alGetSourcei", [ctypes.c_uint, ctypes.c_int,
                             ctypes.POINTER(ctypes.c_int)], None)
def get_source_i(sid, param):
    """Gets an integer property of a source."""
    val = ctypes.c_int(0)
    dll.alGetSourcei(sid, param, ctypes.byref(val))
    _raise_error_or_continue()
    return val.value


@openaltype("alGetSource3i", [ctypes.c_uint, ctypes.c_int,
                              ctypes.POINTER(ctypes.c_int),
                              ctypes.POINTER(ctypes.c_int),
                              ctypes.POINTER(ctypes.c_int)], None)
def get_source_3i(sid, param):
    """Gets an integer property of a source."""
    val1 = ctypes.c_int(0)
    val2 = ctypes.c_int(0)
    val3 = ctypes.c_int(0)
    dll.alGetSource3i(sid, param, ctypes.byref(val1), ctypes.byref(val2),
                      ctypes.byref(val3))
    _raise_error_or_continue()
    return (val1.value, val2.value, val3.value)


@openaltype("alGetSourceiv", [ctypes.c_uint, ctypes.c_int,
                              ctypes.POINTER(ctypes.c_int)], None)
def get_source_iv(sid, param, size):
    """Gets an integer-vector property of a source."""
    val = (ctypes.c_int * size)()
    dll.alGetSourceiv(sid, param, ctypes.byref(val))
    _raise_error_or_continue()
    return val


@openaltype("alSourcePlayv", [ctypes.c_int, ctypes.POINTER(ctypes.c_uint)],
            None)
def source_play_v(sids):
    """Plays a set of sources."""
    sids, size = array.to_ctypes(sids)
    ptr = ctypes.cast(sids, ctypes.POINTER(ctypes.c_uint))
    dll.alSourcePlayv(size, ptr)
    _raise_error_or_continue()


@openaltype("alSourceStopv", [ctypes.c_int, ctypes.POINTER(ctypes.c_uint)],
            None)
def source_stop_v(sids):
    """Stops a set of sources.O"""
    sids, size = array.to_ctypes(sids)
    ptr = ctypes.cast(sids, ctypes.POINTER(ctypes.c_uint))
    dll.alSourceStopv(size, ptr)
    _raise_error_or_continue()


@openaltype("alSourceRewindv", [ctypes.c_int, ctypes.POINTER(ctypes.c_uint)],
            None)
def source_rewind_v(sids):
    """Rewinds a set of sources."""
    sids, size = array.to_ctypes(sids)
    ptr = ctypes.cast(sids, ctypes.POINTER(ctypes.c_uint))
    dll.alSourceRewindv(size, ptr)
    _raise_error_or_continue()


@openaltype("alSourcePausev", [ctypes.c_int, ctypes.POINTER(ctypes.c_uint)],
            None)
def source_pause_v(sids):
    """Pauses a set of sources."""
    sids, size = array.to_ctypes(sids)
    ptr = ctypes.cast(sids, ctypes.POINTER(ctypes.c_uint))
    dll.alSourcePausev(size, ptr)
    _raise_error_or_continue()


@openaltype("alSourcePlay", [ctypes.c_uint], None)
def source_play(sid):
    """Plays a source."""
    dll.alSourcePlay(sid)
    _raise_error_or_continue()


@openaltype("alSourceStop", [ctypes.c_uint], None)
def source_stop(sid):
    """Stops a source."""
    dll.alSourceStop(sid)
    _raise_error_or_continue()


@openaltype("alSourceRewind", [ctypes.c_uint], None)
def source_rewind(sid):
    """Rewinds a source."""
    dll.alSourceRewind(sid)
    _raise_error_or_continue()


@openaltype("alSourcePause", [ctypes.c_uint], None)
def source_pause(sid):
    """Pauses a source."""
    dll.alSourcePause(sid)
    _raise_error_or_continue()


@openaltype("alSourceQueueBuffers", [ctypes.c_uint, ctypes.c_int,
                                     ctypes.POINTER(ctypes.c_uint)], None)
def source_queue_buffers(sid, bids):
    """Queues a set of buffers on a source.

    All buffers attached to a source will be played in sequence and the
    number of buffers played can be retrieved using a source_i() call to
    retrieve AL_BUFFERS_PROCESSED.
    """
    bufs, size = array.to_ctypes(bids, ctypes.c_uint)
    dll.alSourceQueueBuffers(sid, size, bufs)
    _raise_error_or_continue()


@openaltype("alSourceUnqueueBuffers", [ctypes.c_uint, ctypes.c_int,
                                       ctypes.POINTER(ctypes.c_uint)], None)
def source_unqueue_buffers(sid, bids):
    """Unqueues a set off buffers attached to a source."""
    bufs, size = array.to_ctypes(bids, ctypes.c_uint)
    dll.alSourceUnqueueBuffers(sid, size, bufs)
    _raise_error_or_continue()


@openaltype("alGenBuffers", [ctypes.c_int, ctypes.POINTER(ctypes.c_uint)],
            None)
def gen_buffers(count):
    """Generates one or more buffers, which contain audio data."""
    buffers = (count * ctypes.c_uint)()
    ptr = ctypes.cast(buffers, ctypes.POINTER(ctypes.c_uint))
    dll.alGenBuffers(count, ptr)
    _raise_error_or_continue()
    return buffers


@openaltype("alDeleteBuffers", [ctypes.c_int, ctypes.POINTER(ctypes.c_uint)],
            None)
def delete_buffers(buffers):
    """Deletes one or more buffers, freeing the resources used by them."""
    buffers, size = array.to_ctypes(buffers, ctypes.c_uint)
    ptr = ctypes.cast(buffers, ctypes.POINTER(ctypes.c_uint))
    dll.alDeleteBuffers(size, ptr)
    _raise_error_or_continue()


@openaltype("alIsBuffer", [ctypes.c_uint], ctypes.c_byte)
def is_buffer(bid):
    """Tests if the passed bid is a valid buffer identifier."""
    return dll.alIsBuffer(bid) == AL_TRUE


@openaltype("alBufferData", [ctypes.c_uint, ctypes.c_int,
                             ctypes.POINTER(ctypes.c_ubyte), ctypes.c_int,
                             ctypes.c_int], None)
def buffer_data(bid, bformat, data, freq):
    """Fille a buffer with audio data.

    The predefined formats expect tha data to be valid PCM data,
    extension functions might load other data types as well."""
    datap = data
    size = len(data)
    if isinstance(data, array.CTypesView):
        datap = data.to_bytes()
        size = data.bytesize
    else:
        size = len(data)
        datap = (ctypes.c_ubyte * size).from_buffer_copy(data)
    datap = ctypes.cast(datap, ctypes.POINTER(ctypes.c_ubyte))
    dll.alBufferData(bid, bformat, datap, size, freq)
    _raise_error_or_continue()


@openaltype("alBufferf", [ctypes.c_uint, ctypes.c_int, ctypes.c_float], None)
def buffer_f(bid, param, value):
    """Sets a floating point property of the buffer."""
    dll.alBufferf(bid, param, value)
    _raise_error_or_continue()


@openaltype("alBuffer3f", [ctypes.c_uint, ctypes.c_int, ctypes.c_float,
                           ctypes.c_float, ctypes.c_float], None)
def buffer_3f(bid, param, value1, value2, value3):
    """Sets a floating point property of the buffer."""
    dll.alBuffer3f(bid, param, value1, value2, value3)
    _raise_error_or_continue()


@openaltype("alBufferfv", [ctypes.c_uint, ctypes.c_int,
                           ctypes.POINTER(ctypes.c_float)], None)
def buffer_fv(bid, param, values):
    """Sets a floating point-vector property of the buffer."""
    values, size = array.to_ctypes(values, ctypes.c_float)
    ptr = ctypes.cast(values, ctypes.POINTER(ctypes.c_float))
    dll.alBufferfv(bid, param, ptr)
    _raise_error_or_continue()


@openaltype("alBufferi", [ctypes.c_uint, ctypes.c_int, ctypes.c_int], None)
def buffer_i(bid, param, value):
    """Sets an integer property of the buffer."""
    dll.alBufferi(bid, param, value)
    _raise_error_or_continue()


@openaltype("alBuffer3i", [ctypes.c_uint, ctypes.c_int, ctypes.c_int,
                           ctypes.c_int, ctypes.c_int], None)
def buffer_3i(bid, param, value1, value2, value3):
    """Sets an integer property of the buffer."""
    dll.alBuffer3i(bid, param, value1, value2, value3)
    _raise_error_or_continue()


@openaltype("alBufferiv", [ctypes.c_uint, ctypes.c_int,
                           ctypes.POINTER(ctypes.c_int)], None)
def buffer_iv(bid, param, values):
    """Sets an integer-vector property of the buffer."""
    values, size = array.to_ctypes(values, ctypes.c_int)
    ptr = ctypes.cast(values, ctypes.POINTER(ctypes.c_int))
    dll.alBufferiv(bid, param, ptr)
    _raise_error_or_continue()


@openaltype("alGetBufferf", [ctypes.c_uint, ctypes.POINTER(ctypes.c_float)],
            None)
def get_buffer_f(bid, param):
    """Gets a floating point property of the buffer."""
    val = ctypes.c_float(0)
    dll.alGetBufferf(bid, param, ctypes.byref(val))
    _raise_error_or_continue()
    return val.value


@openaltype("alGetBuffer3f", [ctypes.c_uint, ctypes.c_int,
                              ctypes.POINTER(ctypes.c_float),
                              ctypes.POINTER(ctypes.c_float),
                              ctypes.POINTER(ctypes.c_float)], None)
def get_buffer_3f(bid, param):
    """Gets a floating point property of the buffer."""
    val1 = ctypes.c_float(0)
    val2 = ctypes.c_float(0)
    val3 = ctypes.c_float(0)
    dll.alGetBuffer3f(bid, param, ctypes.byref(val1), ctypes.byref(val2),
                      ctypes.byref(val3))
    _raise_error_or_continue()
    return (val1.value, val2.value, val3.value)


@openaltype("alGetBufferfv", [ctypes.c_uint, ctypes.c_int,
                              ctypes.POINTER(ctypes.c_float)], None)
def get_buffer_fv(bid, param, size):
    """Gets a floating point-vector property of the buffer."""
    val = (ctypes.c_float * size)()
    dll.alGetBufferfv(bid, param, ctypes.byref(val))
    _raise_error_or_continue()
    return val


@openaltype("alGetBufferi", [ctypes.c_uint, ctypes.POINTER(ctypes.c_int)],
            None)
def get_buffer_i(bid, param):
    """Gets an integer property of the buffer."""
    val = ctypes.c_int(0)
    dll.alGetBufferi(bid, param, ctypes.byref(val))
    _raise_error_or_continue()
    return val.value


@openaltype("alGetBuffer3i", [ctypes.c_uint, ctypes.c_int,
                              ctypes.POINTER(ctypes.c_int),
                              ctypes.POINTER(ctypes.c_int),
                              ctypes.POINTER(ctypes.c_int)], None)
def get_buffer_3i(sid, param):
    """Gets an integer property of the buffer."""
    val1 = ctypes.c_int(0)
    val2 = ctypes.c_int(0)
    val3 = ctypes.c_int(0)
    dll.alGetBuffer3i(sid, param, ctypes.byref(val1), ctypes.byref(val2),
                      ctypes.byref(val3))
    _raise_error_or_continue()
    return (val1.value, val2.value, val3.value)


@openaltype("alGetBufferiv", [ctypes.c_uint, ctypes.c_int,
                              ctypes.POINTER(ctypes.c_int)], None)
def get_buffer_iv(sid, param, size):
    """Gets an integer-vector property of the buffer."""
    val = (ctypes.c_int * size)()
    dll.alGetBufferiv(sid, param, ctypes.byref(val))
    _raise_error_or_continue()
    return val


@openaltype("alDopplerFactor", [ctypes.c_float], None)
def doppler_factor(value):
    """Sets the OpenAL doppler factor value."""
    dll.alDopplerFactor(value)


@openaltype("alDopplerVelocity", [ctypes.c_float], None)
def doppler_velocity(value):
    """Sets the speed of sound to be used in Doppler calculations.

    NOTE: this is a legacy function from OpenAL 1.0 and should not be
    used anymore. Use speed_of_source() instead.
    """
    dll.alDopplerVelocity(value)


@openaltype("alSpeedOfSound", [ctypes.c_float], None)
def speed_of_source(value):
    """Sets the speed of sound to be used in Doppler calculuations."""
    dll.alSpeedOfSound(value)


@openaltype("alDistanceModel", [ctypes.c_int], None)
def distance_model(value):
    """Sets the OpenAL distance model."""
    dll.alDistanceModel(value)
