"""
A thin wrapper package around the SDL2 library.
"""
import os
import sys
import ctypes
from ctypes.util import find_library
from pygame2 import get_dll_path

_libname = None
if sys.platform == "win32":
    _libname = "SDL2.dll"
elif sys.platform == "darwin":
    _libname = "SDL2.dylib"
else:
    _libname = "libSDL2.so"

class _DLL (object):
    """_DLL () -> _DLL
    
    Function wrapper around the different DLL functions. Do not use or
    instantiate this one directly from your user code.
    """
    def __init__ (self):
        self._dll = None
        path = get_dll_path ()
        if path:
            # Explicit path provided by the user or Win32
            global _libname
            _libname = os.path.join (path, _libname)
        else:
            _libname = find_library ("SDL2")
            if not _libname:
                _libname = find_library ("SDL2-2.0")
        self._dll = ctypes.CDLL (_libname)

    def get_function (self, name):
        func = getattr (self._dll, name)
        return func

    def add_function (self, name, func):
        self.__dict__[name] = func

dll = _DLL ()

class sdltype (object):
    """sdltype (funcname=None, args=None, returns=None) -> sdltype

    Decorator class used to wrap SDL2 related functions.

    You should not use this decorator in user code.
    """
    def __init__ (self, funcname=None, args=None, returns=None):
        func = dll.get_function (funcname)
        func.argtype = args
        func.restype = returns
        dll.add_function (funcname, func)

    def __call__ (self, func):
        return func

SDL_INIT_TIMER =        0x00000001
SDL_INIT_AUDIO =        0x00000010
SDL_INIT_VIDEO =        0x00000020
SDL_INIT_JOYSTICK =     0x00000200
SDL_INIT_HAPTIC =       0x00001000
SDL_INIT_NOPARACHUTE =  0x00100000
SDL_INIT_EVERYTHING =   0x0000FFFF

SDL_FALSE = 0
SDL_TRUE = 1

@sdltype("SDL_Init", [ctypes.c_uint], ctypes.c_uint)
def init (flags=None):
    """init (flags) -> int

    Initializes the SDL library.

    Initializes the SDL library using the passed bit-wise combination of
    SDL subsystems defined through the SDL_INIT_ constants.

    Legal values are:
    
    SDL_INIT_TIMER - Initializes the timer module
    SDL_INIT_AUDIO - Initializes the audio module
    SDL_INIT_VIDEO - Initializes the video module
    SDL_INIT_JOYSTICK - Initializes the joystick module
    SDL_INIT_HAPTIC - Initializes force-feedback support for joysticks
    SDL_INIT_EVERYTHING - Initializes all modules from above
    SDL_INIT_NOPARACHUTE - Deactivates the interrupt wrappers
                           (e.g. for SIGINT, SIGSEGV, etc.)

    Example:

    flags = init (SDL_INIT_TIMER|SDL_INIT_VIDEO)
    if flags != SDL_INIT_TIMER|SDL_INIT_VIDEO:
        print (pygame2.error.get_error ())
    """
    return dll.SDL_Init (flags)

@sdltype("SDL_InitSubSystem", [ctypes.c_uint], ctypes.c_uint)
def init_subsystem (flags):
    """init_subsystem (flags) -> int

    Similar to init(), but can be called to explicitly initialize a certain
    module. init() needs to be called beforehand.
    """
    return dll.SDL_InitSubSystem (flags)

@sdltype("SDL_QuitSubSystem", [ctypes.c_uint], None)
def quit_subsystem (flags):
    """quit_subsystem (flags) -> None

    Quits a specific module of SDL, leaving the rest intact.

    Example:
    
    quit_subsystem (SDL_INIT_AUDIO) # Deactivate the audio subsystem
    """
    dll.SDL_QuitSubSystem (flags)

@sdltype("SDL_WasInit", [ctypes.c_uint], ctypes.c_uint)
def was_init (flags):
    """was_init (flags) -> int
    
    Returns a bitmask of the subsystems that were previously initialized.

    Example:

    init (SDL_INIT_VIDEO)
    ...
    if (was_init (SDL_INIT_VIDEO) & SDL_INIT_VIDEO):
        print ("Video subsystem was initialized properly")
    """
    return dll.SDL_WasInit (flags)

@sdltype("SDL_Quit", None, None)
def quit ():
    """quit () -> None

    Shuts down the SDL library and releases all resources hold by it.

    Calling SDL related methods after quit() will wake the dragons, so
    do not do it.
    """
    dll.SDL_Quit ()

def free (val):
    """free (val) -> None
    
    Frees memory hold by a SDL resource.
    """
    if not hasattr (dll, "SDL_free"):
        # Bind it on the first time, the function is called.
        try:
            funcptr = dll.get_function ("SDL_free")
            dll.add_function ("SDL_free", funcptr)
        except:
            # SDL_Free might be a #define to free()
            libc = None
            if sys.platform == "win32":
                libc = ctypes.cdll.msvcrt
            else:
                libc = ctypes.cdll.LoadLibrary ("libc.so")
            dll.add_function ("SDL_free", libc.free)
    dll.SDL_free (val)
