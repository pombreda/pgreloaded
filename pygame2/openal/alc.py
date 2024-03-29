"""
OpenAL ALC implementation
"""
import ctypes
import pygame2.array as array
from pygame2.openal.al import OpenALError
from pygame2.compat import byteify, stringify
from pygame2.openal import dll, openaltype

__all__ = ["capture_close_device", "capture_open_device", "capture_samples",
           "capture_start", "capture_stop", "close_device", "create_context",
           "destroy_context", "get_context_device", "get_current_context",
           "get_enum_value", "get_integer_v", "get_proc_address", "get_string",
           "is_extension_present", "make_context_current", "open_device",
           "process_context", "suspend_context"
           ]

ALC_FALSE = 0
ALC_TRUE =  1

ALC_FREQUENCY = 0x1007
ALC_REFRESH   = 0x1008
ALC_SYNC      = 0x1009

ALC_MONO_SOURCES =   0x1010
ALC_STEREO_SOURCES = 0x1011

ALC_NO_ERROR = ALC_FALSE
ALC_INVALID_DEVICE  = 0xA001
ALC_INVALID_CONTEXT = 0xA002
ALC_INVALID_ENUM    = 0xA003
ALC_INVALID_VALUE   = 0xA004
ALC_OUT_OF_MEMORY   = 0xA005

ALC_DEFAULT_DEVICE_SPECIFIER = 0x1004
ALC_DEVICE_SPECIFIER =         0x1005
ALC_EXTENSIONS =               0x1006

ALC_MAJOR_VERSION = 0x1000
ALC_MINOR_VERSION = 0x1001

ALC_ATTRIBUTES_SIZE = 0x1002
ALC_ALL_ATTRIBUTES =  0x1003

ALC_DEFAULT_ALL_DEVICES_SPECIFIER = 0x1012
ALC_ALL_DEVICES_SPECIFIER =         0x1013

ALC_CAPTURE_DEVICE_SPECIFIER =         0x310
ALC_CAPTURE_DEFAULT_DEVICE_SPECIFIER = 0x311
ALC_CAPTURE_SAMPLES =                  0x312


class ALCdevice(ctypes.Structure):
    """An OpenAL device used for audio operations."""
    pass


class ALCcontext(ctypes.Structure):
    """An execution context on a OpenAL device."""
    pass


_ERRMAP = {
    ALC_NO_ERROR: "No Error",
    ALC_INVALID_DEVICE: "Invalid device",
    ALC_INVALID_CONTEXT: "Invalid context",
    ALC_INVALID_ENUM: "Invalid enum",
    ALC_INVALID_VALUE: "Invalid value",
    ALC_OUT_OF_MEMORY: "Out of memory"
    }
_FASTERROR = lambda dev: _ERRMAP[dll.alcGetError(ctypes.byref(dev))]


@openaltype("alcGetError", [ctypes.POINTER(ALCdevice)], ctypes.c_int)
def get_error(device):
    """Gets the most recent error generated within the AL system for the
    specific device.
    """
    return dll.alcGetError(ctypes.byref(device))


@openaltype("alcCreateContext", [ctypes.POINTER(ALCdevice),
                                 ctypes.POINTER(ctypes.c_int)],
            ctypes.POINTER(ALCcontext))
def create_context(device, attrs=None):
    """Creates a context from the specified device."""
    ptr = None
    if attrs is not None:
        arr, size = array.to_ctypes(attrs, ctypes.c_int, len(attrs) + 1)
        arr[-1] = 0
        ptr = ctypes.cast(arr, ctypes.POINTER(ctypes.c_int))
    retval = dll.alcCreateContext(ctypes.byref(device), ptr)
    if retval is None or not bool(retval):
        raise OpenALError(_FASTERROR(device))
    return retval.contents


@openaltype("alcMakeContextCurrent", [ctypes.POINTER(ALCcontext)],
            ctypes.c_byte)
def make_context_current(context):
    """Makes the specified context the current context."""
    return dll.alcMakeContextCurrent(ctypes.byref(context)) == ALC_TRUE


@openaltype("alcProcessContext", [ctypes.POINTER(ALCcontext)], None)
def process_context(context):
    """Tells the passed context to begin processing."""
    dll.alcProcessContext(ctypes.byref(context))


@openaltype("alcSuspendContext", [ctypes.POINTER(ALCcontext)], None)
def suspend_context(context):
    """Tells the passed context to suspend processing."""
    dll.alcSuspendContext(ctypes.byref(context))


@openaltype("alcDestroyContext", [ctypes.POINTER(ALCcontext)], None)
def destroy_context(context):
    """Destroys the passed context."""
    dll.alcDestroyContext(ctypes.byref(context))


@openaltype("alcGetCurrentContext", None, ctypes.POINTER(ALCcontext))
def get_current_context():
    """Retrieves the current context."""
    retval = dll.alcGetCurrentContext()
    if retval is None or not bool(retval):
        return None
    return retval.contents


@openaltype("alcGetContextsDevice", [ctypes.POINTER(ALCcontext)],
            ctypes.POINTER(ALCdevice))
def get_context_device(context):
    """Retrieves the device used by the context."""
    retval = dll.alcGetContextsDevice(ctypes.byref(context))
    if retval is None or not bool(retval):
        raise OpenALError()
    return retval.contents


@openaltype("alcOpenDevice", [ctypes.c_char_p], ctypes.POINTER(ALCdevice))
def open_device(devicename=None):
    """Opens an OpenAL device with the specified name.

    If no devicename is passed, the default output device is opened.
    """
    if devicename is not None:
        devicename = byteify(str(devicename), "utf-8")
    retval = dll.alcOpenDevice(devicename)
    if retval is None or not bool(retval):
        return None
    return retval.contents


@openaltype("alcCloseDevice", [ctypes.POINTER(ALCdevice)], ctypes.c_byte)
def close_device(device):
    """Closes the passed OpenAL device."""
    return dll.alcCloseDevice(ctypes.byref(device)) == ALC_TRUE


@openaltype("alcIsExtensionPresent", [ctypes.POINTER(ALCdevice),
                                      ctypes.c_char_p], ctypes.c_byte)
def is_extension_present(device, extname):
    """Checks, if a certain extension is available for the passed device."""
    extname = byteify(str(extname), "utf-8")
    devptr = None
    if device is not None:
        devptr = ctypes.byref(device)
    return dll.alcIsExtensionPresent(devptr, extname) == ALC_TRUE


@openaltype("alcGetProcAddress", [ctypes.POINTER(ALCdevice), ctypes.c_char_p],
            ctypes.c_void_p)
def get_proc_address(device, funcname):
    """Retrieves the address of the specified device extension function."""
    funcname = byteify(str(funcname), "utf-8")
    return dll.alcGetProcAddress(ctypes.byref(device), funcname)


@openaltype("alcGetEnumValue", [ctypes.POINTER(ALCdevice), ctypes.c_char_p],
            ctypes.c_int)
def get_enum_value(device, enumname):
    """Retrieves the value for the specified enumeration name on the
    device.
    """
    enumname = byteify(str(enumname), "utf-8")
    return dll.alcGetEnumValue(ctypes.byref(device), enumname)


@openaltype("alcGetString", [ctypes.POINTER(ALCdevice), ctypes.c_int],
            ctypes.c_char_p)
def get_string(device, param):
    """Returns a set of strings related to the context device."""
    devptr = None
    if device is not None:
        devptr = ctypes.byref(device)
    retval = dll.alcGetString(devptr, param)
    if retval is None or not bool(retval):
        raise OpenALError(get_error(device))
    return stringify(retval, "utf-8")


@openaltype("alcGetIntegerv", [ctypes.POINTER(ALCdevice), ctypes.c_int,
                               ctypes.c_int, ctypes.POINTER(ctypes.c_int)],
            None)
def get_integer_v(device, param, size):
    """Returns a set of integers related to the context device."""
    values = (size * ctypes.c_int)()
    vptr = ctypes.cast(values, ctypes.POINTER(ctypes.c_int))
    dll.alcGetIntegerv(ctypes.byref(device), param, size, vptr)
    return values


@openaltype("alcCaptureOpenDevice", [ctypes.c_char_p, ctypes.c_uint,
                                     ctypes.c_int, ctypes.c_int],
            ctypes.POINTER(ALCdevice))
def capture_open_device(devicename, frequency, dformat, buffersize):
    """Opens an OpenAL capture device with the specified name."""
    if devicename is not None:
        devicename = byteify(str(devicename), "utf-8")
    retval = dll.alcCaptureOpenDevice(devicename, frequency, dformat,
                                      buffersize)
    if retval is None or not bool(retval):
        return None  # TODO
    return retval.contents


@openaltype("alcCaptureCloseDevice", [ctypes.POINTER(ALCdevice)],
            ctypes.c_byte)
def capture_close_device(device):
    """Closes the passed capture device."""
    return dll.alcCaptureCloseDevice(ctypes.byref(device)) == ALC_TRUE


@openaltype("alcCaptureStart", [ctypes.POINTER(ALCdevice)], None)
def capture_start(device):
    """Start a capturing operation."""
    dll.alcCaptureStart(ctypes.byref(device))


@openaltype("alcCaptureStop", [ctypes.POINTER(ALCdevice)], None)
def capture_stop(device):
    """Stops a capturing operation."""
    dll.alcCaptureStop(ctypes.byref(device))


@openaltype("alcCaptureSamples", [ctypes.POINTER(ALCdevice),
                                  ctypes.POINTER(ctypes.c_byte), ctypes.c_int],
            None)
def capture_samples(device, amount, itemsize):
    """Retrieves the audio data samples of a capture device."""
    bsize = amount * itemsize
    buf = (ctypes.c_ubyte * bsize)()
    ptr = ctypes.cast(buf, ctypes.POINTER(ctypes.c_ubyte))
    dll.alcCaptureSamples(ctypes.byref(device), ptr, bsize)
    return buf
