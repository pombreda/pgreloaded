"""
Wrapper methods around the SDL2 power management routines.
"""
import ctypes
from pygame2.sdl import sdltype, dll

__all__ = ["get_power_info", "SDL_POWERSTATE_UNKNOWN",
           "SDL_POWERSTATE_ON_BATTERY", "SDL_POWERSTATE_NO_BATTERY",
           "SDL_POWERSTATE_CHARGING", "SDL_POWERSTATE_CHARGED"
           ]

SDL_POWERSTATE_UNKNOWN    = 0
SDL_POWERSTATE_ON_BATTERY = 1
SDL_POWERSTATE_NO_BATTERY = 2
SDL_POWERSTATE_CHARGING   = 3
SDL_POWERSTATE_CHARGED    = 4


@sdltype("SDL_GetPowerInfo", [ctypes.POINTER(ctypes.c_int),
                              ctypes.POINTER(ctypes.c_int)], ctypes.c_int)
def get_power_info():
    """Gets the current power supply information.

    The returned tuple consists of a SDL_POWERSTATE_* value, the seconds
    of battery life left (or -1, if it can not be determined or is not
    running on a battery) and the percentage of battery life left (again
    -1, if it can not be determined or not running on a battery).
    """
    psec = ctypes.c_int(0)
    ppct = ctypes.c_int(0)
    state = dll.SDL_GetPowerInfo(ctypes.byref(psec), ctypes.byref(ppct))
    return (state, psec.value, ppct.value)
