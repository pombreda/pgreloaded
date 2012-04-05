"""
A thin wrapper package around the SDL2 library.
"""
import os
import sys
import ctypes
from ctypes.util import find_library
from pygame2 import get_dll_path

__all__ = ["init", "init_subsystem", "quit", "quit_subsystem", "was_init",
           "SDL_INIT_TIMER", "SDL_INIT_AUDIO", "SDL_INIT_VIDEO",
           "SDL_INIT_JOYSTICK", "SDL_INIT_HAPTIC", "SDL_INIT_NOPARACHUTE",
           "SDL_INIT_EVERYTHING"
           ]


_LIBNAME = None
if sys.platform == "win32":
    _LIBNAME = "SDL2.dll"
elif sys.platform == "darwin":
    _LIBNAME = "SDL2"
else:
    _LIBNAME = "libSDL2.so"


class _DLL(object):
    """Function wrapper around the different DLL functions. Do not use or
    instantiate this one directly from your user code.
    """
    def __init__(self):
        self._dll = None
        path = get_dll_path()
        if path:
            # Explicit path provided by the user or Win32
            global _LIBNAME
            _LIBNAME = os.path.join(path, _LIBNAME)
        else:
            _LIBNAME = find_library("SDL2")
            if not _LIBNAME:
                _LIBNAME = find_library("SDL2-2.0")
        self._dll = ctypes.CDLL(_LIBNAME)

    def has_dll_function(self, name):
        """Checks, if a function identified by name exists in the bound dll.
        """
        return hasattr(self._dll, name)

    def get_dll_function(self, name):
        """Tries to retrieve the function identified by name from the bound
        dll.
        """
        func = getattr(self._dll, name)
        return func

    def add_function(self, name, func):
        """Adds the passed function to the _DLL instance.

        The function will be identified by the passed name, so that a
        invocation of mydll.name (...) will invoke the bound function.
        """
        self.__dict__[name] = func


dll = _DLL()


class sdltype(object):
    """Decorator class used to wrap SDL2 related functions.

    You should not use this decorator in user code.
    """
    def __init__(self, funcname=None, args=None, returns=None):
        func = dll.get_dll_function(funcname)
        func.argtype = args
        func.restype = returns
        dll.add_function(funcname, func)

    def __call__(self, func):
        return func

SDL_INIT_TIMER =       0x00000001
SDL_INIT_AUDIO =       0x00000010
SDL_INIT_VIDEO =       0x00000020
SDL_INIT_JOYSTICK =    0x00000200
SDL_INIT_HAPTIC =      0x00001000
SDL_INIT_NOPARACHUTE = 0x00100000
SDL_INIT_EVERYTHING =  0x0000FFFF

SDL_FALSE = 0
SDL_TRUE = 1


@sdltype("SDL_Init", [ctypes.c_uint], ctypes.c_uint)
def init(flags=None):
    """Initializes the SDL library.

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

        flags = init(SDL_INIT_TIMER|SDL_INIT_VIDEO)
        if flags != SDL_INIT_TIMER|SDL_INIT_VIDEO:
            print(pygame2.error.get_error())
    """
    return dll.SDL_Init(flags)


@sdltype("SDL_InitSubSystem", [ctypes.c_uint], ctypes.c_uint)
def init_subsystem(flags):
    """Similar to init(), but can be called to explicitly initialize a certain
    module. init() needs to be called beforehand.
    """
    return dll.SDL_InitSubSystem(flags)


@sdltype("SDL_QuitSubSystem", [ctypes.c_uint], None)
def quit_subsystem(flags):
    """Quits a specific module of SDL, leaving the rest intact.

    Example:

        quit_subsystem(SDL_INIT_AUDIO) # Deactivate the audio subsystem
    """
    dll.SDL_QuitSubSystem(flags)


@sdltype("SDL_WasInit", [ctypes.c_uint], ctypes.c_uint)
def was_init(flags):
    """Returns a bitmask of the subsystems that were previously initialized.

    Example:

        init(SDL_INIT_VIDEO)
        ...
        if(was_init(SDL_INIT_VIDEO) & SDL_INIT_VIDEO):
            print("Video subsystem was initialized properly")
    """
    return dll.SDL_WasInit(flags)


@sdltype("SDL_Quit", None, None)
def quit():
    """Shuts down the SDL library and releases all resources hold by it.

    Calling SDL related methods after quit() will wake the dragons, so
    do not do it.
    """
    dll.SDL_Quit()


def free(val):
    """Frees memory hold by a SDL resource."""
    if not hasattr(dll, "SDL_free"):
        # Bind it on the first time, the function is called.
        if dll.has_dll_function("SDL_free"):
            funcptr = dll.get_dll_function("SDL_free")
            dll.add_function("SDL_free", funcptr)
        else:
            # SDL_Free is most likely a #define for free()
            libc = None
            if sys.platform == "win32":
                libc = ctypes.cdll.msvcrt
            else:
                libc = ctypes.cdll.LoadLibrary("libc.so")
            dll.add_function("SDL_free", libc.free)
    dll.SDL_free(ctypes.cast(val, ctypes.c_void_p))
