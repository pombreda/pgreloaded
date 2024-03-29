"""
Wrapper methods around the SDL2 hint routines.
"""
from ctypes import c_char_p, c_int, c_uint
from pygame2.compat import stringify, byteify
from pygame2.sdl import sdltype, dll

__all__ = ["clear_hints", "get_hint", "set_hint", "set_hint_with_priority",
           "SDL_HINT_DEFAULT", "SDL_HINT_NORMAL", "SDL_HINT_OVERRIDE",
           "SDL_HINT_FRAMEBUFFER_ACCELERATION", "SDL_HINT_IDLE_TIMER_DISABLED",
           "SDL_HINT_ORIENTATIONS", "SDL_HINT_RENDER_DRIVER",
           "SDL_HINT_RENDER_OPENGL_SHADERS", "SDL_HINT_RENDER_SCALE_QUALITY",
           "SDL_HINT_RENDER_VSYNC", "SDL_HINT_VIDEO_X11_XVIDMODE",
           "SDL_HINT_VIDEO_X11_XINERAMA", "SDL_HINT_VIDEO_X11_XRANDR"
           ]


SDL_HINT_DEFAULT  = 0
SDL_HINT_NORMAL   = 1
SDL_HINT_OVERRIDE = 2
_SUPPORTED_HINTS = (SDL_HINT_DEFAULT, SDL_HINT_NORMAL, SDL_HINT_OVERRIDE)

SDL_HINT_FRAMEBUFFER_ACCELERATION = "SDL_FRAMEBUFFER_ACCELERATION"
SDL_HINT_IDLE_TIMER_DISABLED      = "SDL_IOS_IDLE_TIMER_DISABLED"
SDL_HINT_ORIENTATIONS             = "SDL_IOS_ORIENTATIONS"
SDL_HINT_RENDER_DRIVER            = "SDL_RENDER_DRIVER"
SDL_HINT_RENDER_OPENGL_SHADERS    = "SDL_RENDER_OPENGL_SHADERS"
SDL_HINT_RENDER_SCALE_QUALITY     = "SDL_RENDER_SCALE_QUALITY"
SDL_HINT_RENDER_VSYNC             = "SDL_RENDER_VSYNC"
SDL_HINT_VIDEO_X11_XVIDMODE       = "SDL_VIDEO_X11_XVIDMODE"
SDL_HINT_VIDEO_X11_XINERAMA       = "SDL_VIDEO_X11_XINERAMA"
SDL_HINT_VIDEO_X11_XRANDR         = "SDL_VIDEO_X11_XRANDR"


@sdltype("SDL_ClearHints", None, None)
def clear_hints():
    """Clears all set hints."""
    dll.SDL_ClearHints()


@sdltype("SDL_GetHint", [c_char_p], c_char_p)
def get_hint(name):
    """Gets the currently set value for the passed hint."""
    retval = dll.SDL_GetHint(byteify(str(name), "utf-8"))
    if retval is not None:
        return stringify(retval, "utf-8")
    return None


@sdltype("SDL_SetHint", [c_char_p, c_char_p], c_int)
def set_hint(name, value):
    """Sets the value of a specific hint."""
    return dll.SDL_SetHint(byteify(str(name), "utf-8"),
                           byteify(str(value), "utf-8"))


@sdltype("SDL_SetHintWithPriority", [c_char_p, c_char_p, c_uint], c_int)
def set_hint_with_priority(name, value, priority):
    """Sets the value of a specific hint using a priority override.

    The hint priority can be one of
    * SDL_HINT_DEFAULT
    * SDL_HINT_NORMAL
    * SDL_HINT_OVERRIDE
    """
    if priority not in _SUPPORTED_HINTS:
        raise ValueError("unsupported priority")
    return dll.SDL_SetHintWithPriority(byteify(str(name), "utf-8"),
                                       byteify(str(value), "utf-8"), priority)
