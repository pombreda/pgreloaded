"""
Wrapper methods around the SDL2 timer routines.
"""
import ctypes
from pygame2.compat import *
from pygame2.sdl import sdltype, dll, SDL_TRUE

@sdltype("SDL_GetTicks", None, ctypes.c_uint)
def get_ticks ():
    """get_ticks () -> int
    
    Gets the number of milliseconds since the underlying SDL library was
    initialized.
    
    NOTE: This value wraps if the program runs for more than ~49 days.
    """
    return dll.SDL_GetTicks ()

@sdltype("SDL_GetPerformanceCounter", None, ctypes.c_ulonglong)
def get_performance_counter ():
    """get_performance_counter () -> int
    
    Gets the current value of the high resolution counter.
    """
    return dll.SDL_GetPerformanceCounter ()

@sdltype("SDL_GetPerformanceFrequency", None, ctypes.c_ulonglong)
def get_performance_frequency ():
    """get_performance_frequency () -> int
    
    Gets the count per second of the high resolution counter.
    """
    return dll.SDL_GetPerformanceFrequency ()

@sdltype("SDL_Delay", [ctypes.c_uint], None)
def delay (ms):
    """delay (ms) -> None
    
    Wait a specified number of milliseconds before continuing.
    """
    if ms < 0:
        raise ValueError ("ms must not be smaller than 0")
    dll.SDL_Delay (ms)

SDL_TimerCallback = ctypes.CFUNCTYPE(ctypes.c_uint, ctypes.c_uint,
                                     ctypes.py_object)
    
@sdltype("SDL_AddTimer", [ctypes.c_uint, SDL_TimerCallback, ctypes.py_object],
         ctypes.c_int)
def add_timer (interval, callback, param=None):
    """add_timer (interval, callback, param=None) -> int
    
    Adds a new timer to the pool of timers already running.
    
    This returns a unique id for the timer or raises a SDLError on error.
    
    NOTE: You must keep a reference to the passed callback to prevent
    it from being dereferenced.
    """
    if interval < 0:
        raise ValueError ("interval must not be smaller than 0")

    if not hasattr (callback, "_param"):
        callback._param = {}
    val = ctypes.py_object (param)
    timerid = dll.SDL_AddTimer (interval, callback, val)
    if timerid == 0 or not bool (timerid):
        raise SDLError ()
    callback._param[timerid] = val # Preserve the parameter
    return timerid

@sdltype("SDL_RemoveTimer", [ctypes.c_int], ctypes.c_int)
def remove_timer (timerid):
    """remove_timer (timerid) -> bool
    
    Removes a timer.
    
    This will return, whether the removal was successful or not.
    """
    return dll.SDL_RemoveTimer (timerid) == SDL_TRUE
