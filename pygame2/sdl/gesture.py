"""
Wrapper methods around the SDL2 gesture routines.
"""
import ctypes
from pygame2.sdl.rwops import SDL_RWops
from pygame2.sdl import sdltype, dll, SDLError

__all__ = ["record_gesture", "save_all_dollar_templates",
           "save_dollar_template", "load_dollar_templates",
           ]


@sdltype("SDL_RecordGesture", [ctypes.c_longlong], ctypes.c_int)
def record_gesture(touchid):
    """Records a gesture on the specified touch.

    If touchid is -1, the gesture will be recored on all touches.
    """
    retval = dll.SDL_RecordGesture(touchid)
    if retval == -1:
        raise SDLError()


@sdltype("SDL_SaveAllDollarTemplates", [ctypes.POINTER(SDL_RWops)],
         ctypes.c_int)
def save_all_dollar_templates(src):
    """Saves all currently loaded Dollar Gesture templates."""
    if not isinstance(src, SDL_RWops):
        raise TypeError("src must be a SDL_RWops")
    retval = dll.SDL_SaveAllDollarTemplates(ctypes.byref(src))
    if retval == -1:
        raise SDLError()


@sdltype("SDL_SaveDollarTemplate", [ctypes.c_longlong,
                                    ctypes.POINTER(SDL_RWops)], ctypes.c_int)
def save_dollar_template(gestureid, src):
    """Saves a currently loaded Dollar Gesture template."""
    if not isinstance(src, SDL_RWops):
        raise TypeError("src must be a SDL_RWops")
    retval = dll.SDL_SaveDollarTemplate(gestureid, src)
    if retval == -1:
        raise SDLError()


@sdltype("SDL_LoadDollarTemplates", [ctypes.c_longlong,
                                     ctypes.POINTER(SDL_RWops)], ctypes.c_int)
def load_dollar_templates(touchid, src):
    """Loads Dollar Gesture templates from a source."""
    if not isinstance(src, SDL_RWops):
        raise TypeError("src must be a SDL_RWops")
    retval = dll.SDL_LoadDollarTemplates(touchid, src)
    if retval == -1:
        raise SDLError()
