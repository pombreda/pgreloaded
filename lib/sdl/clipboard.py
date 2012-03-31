"""
Wrapper methods around the SDL2 clipboard routines.
"""
import copy
import ctypes
from pygame2.compat import *
from pygame2.sdl import sdltype, dll, free, SDL_TRUE
from pygame2.sdl.error import SDLError

@sdltype("SDL_GetClipboardText", None, ctypes.POINTER(ctypes.c_char))
def get_clipboard_text ():
    """get_clipboard_text () -> str
    
    Retrieves text from the OS clipboard, if available.
    """
    retval =  dll.SDL_GetClipboardText ()
    if retval is None:
        raise SDLError ()
    # cast to get the whole content
    val = ctypes.cast (retval, ctypes.c_char_p) 
    # 'copy' to a new location, so we can free retval safely
    v2 = ctypes.c_char_p (val.value)
    free (retval)
    return stringify (v2.value, "utf-8")

@sdltype("SDL_HasClipboardText", None, ctypes.c_int)
def has_clipboard_text ():
    """has_clipboard_text () -> bool
    
    Checks, if text is available on the OS clipboard.
    """
    return dll.SDL_HasClipboardText () == SDL_TRUE

@sdltype("SDL_SetClipboardText", [ctypes.c_char_p], ctypes.c_int)
def set_clipboard_text (text):
    """set_clipboard_text (text) -> None
    
    Puts text on the OS clipboard.
    
    This raises a SDLError, if the operation was not successful.
    """
    ptr = str (text)
    ret = dll.SDL_SetClipboardText (byteify (ptr, "utf-8"))
    if ret < 0:
        raise SDLError ()
