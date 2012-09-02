"""
A thin wrapper package around the SDL2 library.
"""
import sys
import ctypes
from pygame2.dll import DLL
from pygame2.compat import byteify, stringify

__all__ = ["init", "init_subsystem", "quit", "quit_subsystem", "was_init",
           "SDL_INIT_TIMER", "SDL_INIT_AUDIO", "SDL_INIT_VIDEO",
           "SDL_INIT_JOYSTICK", "SDL_INIT_HAPTIC", "SDL_INIT_NOPARACHUTE",
           "SDL_INIT_EVERYTHING", "get_error", "set_error", "clear_error",
           "SDLError"
           ]


dll = DLL("SDL 2", ["SDL2", "SDL2-2.0"])
sdltype = dll.get_decorator()

SDL_INIT_TIMER =       0x00000001
SDL_INIT_AUDIO =       0x00000010
SDL_INIT_VIDEO =       0x00000020
SDL_INIT_JOYSTICK =    0x00000200
SDL_INIT_HAPTIC =      0x00001000
SDL_INIT_NOPARACHUTE = 0x00100000
SDL_INIT_EVERYTHING =  0x0000FFFF

SDL_FALSE = 0
SDL_TRUE = 1


def get_dll_file():
    """Gets the file name of the loaded SDL2 library."""
    return dll.libfile


@sdltype("SDL_Init", [ctypes.c_uint], ctypes.c_int)
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
    """
    if flags is None:
        retval = dll.SDL_Init(0)
    else:
        retval = dll.SDL_Init(flags)
    return retval


@sdltype("SDL_InitSubSystem", [ctypes.c_uint], ctypes.c_int)
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
            funcptr.argtypes = [ctypes.c_void_p]
            dll.add_function("SDL_free", funcptr)
        else:
            # SDL_Free is most likely a #define for free()
            libc = None
            if sys.platform == "win32":
                libc = ctypes.cdll.msvcrt
            else:
                libc = ctypes.cdll.LoadLibrary("libc.so")
            dll.add_function("SDL_free", libc.free)
            funcptr.argtypes = [ctypes.c_void_p]
    dll.SDL_free(ctypes.cast(val, ctypes.c_void_p))


@sdltype("SDL_GetError", None, ctypes.c_char_p)
def get_error():
    """Gets the last SDL-related error message that occured."""
    retval = dll.SDL_GetError()
    return stringify(retval, "utf-8")


@sdltype("SDL_SetError", [ctypes.c_char_p], None)
def set_error(text):
    """Sets a SDL error message that can be retrieved using get_error()."""
    dll.SDL_SetError(byteify(str(text), "utf-8"))


@sdltype("SDL_ClearError", None, None)
def clear_error():
    """Clears the current error message so that get_error() will return an
    empty string.
    """
    dll.SDL_ClearError()


class SDLError(Exception):
    """A SDL specific exception class."""
    def __init__(self, msg=None):
        """Creates a new SDLError instance with the specified message.

        If no msg is provided, the message will be set to the value of
        get_error().
        """
        super(SDLError, self).__init__()
        self.msg = msg
        if msg is None:
            self.msg = get_error()

    def __str__(self):
        return repr(self.msg)
