"""
Wrapper methods around the SDL2 error handling routines.
"""
from ctypes import c_char_p, create_string_buffer
from pygame2.compat import *
from pygame2.sdl import sdltype, dll

__all__ = ["get_error", "set_error", "clear_error", "SDLError"]


@sdltype("SDL_GetError", None, c_char_p)
def get_error():
    """Gets the last SDL-related error message that occured."""
    retval = dll.SDL_GetError()
    return stringify(retval, "utf-8")


@sdltype("SDL_SetError", [c_char_p], None)
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

        If the passed msg argument is None, the error message will be set
        to the value of get_error().
        """
        self.msg = msg
        if not msg:
            self.msg = get_error()

    def __str__(self):
        return repr(self.msg)
