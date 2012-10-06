"""
Wrapper methods around the SDL2 touch routines.
"""
import ctypes
from pygame2.sdl import sdltype, dll, SDLError
from pymgae2.sdl.window import SDL_Window

__all__ = ["SDL_Finger", "SDL_Touch", "get_touch", "get_finger"]


class SDL_Finger(ctypes.Structure):
    """Finger gesture information."""
    _fields_ = [("id", ctypes.c_longlong),
                ("x", ctypes.c_ushort),
                ("y", ctypes.c_ushort),
                ("pressure", ctypes.c_ushort),
                ("xdelta", ctypes.c_ushort),
                ("ydelta", ctypes.c_ushort),
                ("last_x", ctypes.c_ushort),
                ("last_y", ctypes.c_ushort),
                ("last_pressure", ctypes.c_ushort),
                ("down", ctypes.c_int),
                ]


class SDL_Touch(ctypes.Structure):
    """Touch gesture information."""
    _fields_ = [("FreeTouch", ctypes.c_void_p),
                ("pressure_max", ctypes.c_float),
                ("pressure_min", ctypes.c_float),
                ("x_max", ctypes.c_float),
                ("x_min", ctypes.c_float),
                ("y_max", ctypes.c_float),
                ("y_min", ctypes.c_float),
                ("xres", ctypes.c_ushort),
                ("yres", ctypes.c_ushort),
                ("pressureres", ctypes.c_ushort),
                ("native_xres", ctypes.c_ushort),
                ("native_yres", ctypes.c_ushort),
                ("native_pressureres", ctypes.c_ushort),
                ("tilt_x", ctypes.c_float),
                ("tilt_y", ctypes.c_float),
                ("rotation", ctypes.c_float),
                ("id", ctypes.c_longlong),
                ("focus", ctypes.POINTER(SDL_Window)),
                ("name", ctypes.c_char_p),
                ("buttonstate", ctypes.c_ubyte),
                ("relative_mode", ctypes.c_int),
                ("flush_motion", ctypes.c_int),
                ("num_fingers", ctypes.c_int),
                ("max_fingers", ctypes.c_int),
                ("fingers", ctypes.POINTER(ctypes.POINTER(SDL_Finger))),
                ("driverdata", ctypes.c_void_p),
                ]


@sdltype("SDL_GetTouch", [ctypes.c_longlong], ctypes.POINTER(SDL_Touch))
def get_touch(tid):
    """Get the touch object at the given id."""
    retval = dll.SDL_GetTouch(tid)
    if retval is None or not bool(retval):
        raise SDLError()
    return retval.contents


@sdltype("SDL_GetFinger", [ctypes.POINTER(SDL_Touch), ctypes.c_longlong],
         ctypes.POINTER(SDL_Finger))
def get_finger(touch, fid):
    """Gets the finger object of the given touch at the given id."""
    retval = dll.SDL_GetFinger(ctypes.byref(touch), fid)
    if retval is None or not bool(retval):
        raise SDLError()
    return retval.contents
