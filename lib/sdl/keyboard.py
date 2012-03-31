"""
Wrapper methods around the SDL2 keyboard handling routines.
"""

import ctypes
from pygame2.compat import *
from pygame2.sdl import sdltype, dll
from pygame2.sdl.error import SDLError
import pygame2.sdl.keycode as keycode
import pygame2.sdl.scancode as scancode
from pygame2.sdl.video import SDL_Window
from pygame2.sdl.rect import SDL_Rect

class SDL_Keysym (ctypes.Structure):
    """SDL_Keysym () -> None
    
    A key symbol class.
    """
    _fields_ = [("scancode", ctypes.c_ubyte),
                ("sym", ctypes.c_int),
                ("mod", ctypes.c_ushort),
                ("_unicode", ctypes.c_uint)
                ]

    def __init__ (self, scancode=0, sym=0, mod=0, unicode='\0'):
        self.scancode = scancode
        self.sym = sym
        self.mod = mod
        self._unicode = ord(unicode)
    
    def __repr__ (self):
        return "SDL_Keysym (scancode=%d, sym=%d, mod=%d, unicode=%s)" % \
            (self.scancode, self.sym, self.mod, self.unicode)
    
    def __copy__ (self):
        return SDL_Keysym (self.scancode, self.sym, self.mod, self.unicode)

    def __deepcopy__ (self, memo):
        return SDL_Keysym (self.scancode, self.sym, self.mod, self.unicode)
        
    @property
    def unicode (self):
        """Get the unicode value of the key symbol."""
        return unichr (self._unicode)

@sdltype("SDL_GetKeyboardFocus", None, ctypes.POINTER(SDL_Window))
def get_keyboard_focus ():
    """get_keyboard_focus () -> Window

    Gets the (SDL2) window that currently has the keyboard input focus.

    If no (SDL2) window has the keyboard input focus, None will be
    returned.
    """
    val = dll.SDL_GetKeyboardFocus ()
    if bool (val):
        return val.contents
    return None

@sdltype("SDL_GetKeyboardState", [ctypes.POINTER(ctypes.c_int)],
         ctypes.POINTER(ctypes.c_ubyte))
def get_keyboard_state ():
    """get_keyboard_state () -> tuple

    Gets a snapshot of the current keyboard state. This will return a
    tuple with scancode.SDL_NUM_SCANCODES entries of either 0 or 1. For
    each available scancode, a corresponding entry in the tuple will be
    set to either 1, indicating a pressed key or 0, if the corresponding
    key is not pressed.
    """
    size = ctypes.c_int (0)
    vals = dll.SDL_GetKeyboardState (ctypes.byref(size))
    vals = tuple (vals[:size.value])
    return vals
    
@sdltype("SDL_GetKeyFromName", [ctypes.c_char_p], ctypes.c_int)
def get_key_from_name (name):
    """get_key_from_name (name) -> int

    Retrieves the key code from the passed name.

    If no matching key code could be found, SDLK_UNKNOWN will be returned.
    """
    return dll.SDL_GetKeyFromName (byteify (str (name), "utf-8"))

@sdltype("SDL_GetKeyFromScancode", [ctypes.c_ubyte], ctypes.c_int)
def get_key_from_scancode (scancode):
    """get_key_from_scancode (scancode) -> int

    Retrieves the key code from the passed scancode.

    If no matching key code could be found, SDLK_UNKNOWN will be returned.
    """
    if type (scancode) is not int:
        raise TypeError ("scancode must be an int")
    return dll.SDL_GetKeyFromScancode (scancode)

@sdltype("SDL_GetKeyName", [ctypes.c_int], ctypes.c_char_p)
def get_key_name (key):
    """get_key_name (key) -> str

    Retrieves the name of the passed key code.

    If the passed value does not have a name, an empty string is returned.
    """
    if type (key) is not int:
        raise TypeError ("key must be an int")
    retval = dll.SDL_GetKeyName (key)
    return stringify (retval, "utf-8")

@sdltype("SDL_GetModState", None, ctypes.c_ushort)
def get_mod_state ():
    """get_mod_state () -> int

    Gets the current key modifier state for the keyboard.
    """
    return dll.SDL_GetModState ()

@sdltype("SDL_GetScancodeFromKey", [ctypes.c_int], ctypes.c_ubyte)
def get_scancode_from_key (key):
    """get_scancode_from_key (key) -> int

    Retrieves the scancode for the passed key.

    If no matching scancode could be found, SDL_SCANCODE_UNKNOWN will be
    returned.
    """
    if type (key) is not int:
        raise TypeError ("key must be an int")
    return dll.SDL_GetScancodeFromKey (key)

@sdltype("SDL_GetScancodeFromName", [ctypes.c_char_p], ctypes.c_ubyte)
def get_scancode_from_name (name):
    """get_scancode_from_name (name) -> int

    Retrieves the scancode for the passed key name.
    """
    return dll.SDL_GetScancodeFromName (byteify (str(name), "utf-8"))

@sdltype("SDL_GetScancodeName", [ctypes.c_ubyte], ctypes.c_char_p)
def get_scancode_name (code):
    """get_scancode_name (code) -> int

    Retrieves the name of the passed scancode.

    If the passed value does not have a name, an empty string is returned.
    """
    if type (code) is not int:
        raise TypeError ("scancode must be an int")
    if code < 0 or code >= scancode.SDL_NUM_SCANCODES:
        raise ValueError ("invalid scancode value")
    retval = dll.SDL_GetScancodeName (code)
    return stringify (retval, "utf-8")

@sdltype("SDL_SetModState", [ctypes.c_ushort], None)
def set_mod_state (mod):
    """set_mod_state (mod) -> None
    
    Set the current key modifier state for the keyboard.

    This does not really change the keyboard state, but only the
    internally maintained flags.
    """
    dll.SDL_SetModState (mod)

@sdltype("SDL_SetTextInputRect", [ctypes.POINTER(SDL_Rect)], None)
def set_text_input_rect (rect):
    """set_text_input_rect (rect) -> None

    Sets the text input area to the specified value.
    """
    if not isinstance (rect, SDL_Rect):
        raise TypeError ("rect must be a SDL_Rect")
    dll.SDL_SetTextInputRect (ctypes.byref (rect))

@sdltype("SDL_StartTextInput", None, None)
def start_text_input ():
    """start_text_input () -> None
    """
    dll.SDL_StartTextInput ()

@sdltype("SDL_StopTextInput", None, None)
def stop_text_input ():
    """stop_text_input () -> None
    """
    dll.SDL_StopTextInput ()
