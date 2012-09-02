"""
Wrapper methods around the SDL2 clipboard routines.
"""
import ctypes
from pygame2.compat import stringify, byteify
from pygame2.sdl import sdltype, dll, free, SDL_TRUE, SDLError

__all__ = ["get_clipboard_text", "has_clipboard_text", "set_clipboard_text"]


@sdltype("SDL_GetClipboardText", None, ctypes.POINTER(ctypes.c_char))
def get_clipboard_text():
    """Retrieves text from the OS clipboard, if available.

    NOTE: this might leak memory.
    """
    retval = dll.SDL_GetClipboardText()
    if retval is None or not bool(retval):
        raise SDLError()
    # cast to get the whole content, then 'copy' to a new location,
    # so we can free retval safely
    val = stringify(ctypes.cast(retval, ctypes.c_char_p).value, "utf-8")
    free(retval)
    return val


@sdltype("SDL_HasClipboardText", None, ctypes.c_int)
def has_clipboard_text():
    """Checks, if text is available on the OS clipboard."""
    return dll.SDL_HasClipboardText() == SDL_TRUE


@sdltype("SDL_SetClipboardText", [ctypes.c_char_p], ctypes.c_int)
def set_clipboard_text(text):
    """Puts text on the OS clipboard.

    This raises a SDLError, if the operation was not successful.
    """
    ptr = str(text)
    ret = dll.SDL_SetClipboardText(byteify(ptr, "utf-8"))
    if ret < 0:
        raise SDLError()
