"""
Wrapper methods around the SDL2 platform routines.
"""
import ctypes
from pygame2.compat import stringify
from pygame2.sdl import sdltype, dll

__all__ = ["get_platform"]


@sdltype("SDL_GetPlatform", None, ctypes.c_char_p)
def get_platform():
    """Gets the platform, the used SDL2 library was built on."""
    retval = dll.SDL_GetPlatform()
    return stringify(retval, "utf-8")
