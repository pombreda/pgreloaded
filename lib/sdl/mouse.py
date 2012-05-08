"""
Wrapper methods around the SDL2 mouse routines.
"""
import ctypes
from pygame2.sdl import sdltype, dll, SDL_FALSE, SDL_TRUE, SDLError
from pygame2.sdl.surface import SDL_Surface
from pygame2.sdl.video import SDL_Window

__all__ = ["SDL_BUTTON", "SDL_Cursor", "create_color_cursor", "create_cursor",
           "free_cursor", "get_cursor", "set_cursor", "get_mouse_focus",
           "get_mouse_state", "get_relative_mouse_mode", "show_cursor",
           "get_relative_mouse_state", "set_relative_mouse_mode",
           "warp_mouse_in_window"
           ]


def SDL_BUTTON(x):
    """Creates a bitmask for the SDL_BUTTON_ constants."""
    return (1 << (x - 1))

SDL_BUTTON_LEFT   = 1
SDL_BUTTON_MIDDLE = 2
SDL_BUTTON_RIGHT  = 3
SDL_BUTTON_X1     = 4
SDL_BUTTON_X2     = 5

SDL_BUTTON_LMASK  = SDL_BUTTON(SDL_BUTTON_LEFT)
SDL_BUTTON_MMASK  = SDL_BUTTON(SDL_BUTTON_MIDDLE)
SDL_BUTTON_RMASK  = SDL_BUTTON(SDL_BUTTON_RIGHT)
SDL_BUTTON_X1MASK = SDL_BUTTON(SDL_BUTTON_X1)
SDL_BUTTON_X2MASK = SDL_BUTTON(SDL_BUTTON_X2)


class SDL_Cursor(ctypes.Structure):
    pass


SDL_Cursor._fields_ = [("next", ctypes.POINTER(SDL_Cursor)),
                       ("_driverdata", ctypes.c_void_p)
                       ]


@sdltype("SDL_CreateColorCursor", [ctypes.POINTER(SDL_Surface), ctypes.c_int,
                                   ctypes.c_int], ctypes.POINTER(SDL_Cursor))
def create_color_cursor(surface, hotx, hoty):
    """Creates a cursor from the passed surface.

    If the cursor could not be created, a SDLError is raised.
    """
    if not isinstance(surface, SDL_Surface):
        raise TypeError("surface must be a SDL_Surface")
    cursor = dll.SDL_CreateColorCursor(ctypes.byref(surface), hotx, hoty)
    if cursor is None or not bool(cursor):
        raise SDLError()
    return cursor.contents


@sdltype("SDL_CreateCursor", [ctypes.POINTER(ctypes.c_ubyte),
                              ctypes.POINTER(ctypes.c_ubyte), ctypes.c_int,
                              ctypes.c_int, ctypes.c_int, ctypes.c_int],
         ctypes.POINTER(SDL_Cursor))
def create_cursor(data, mask, w, h, hotx, hoty):
    """Creates a cursor from the passed black/white data and alpha mask.

    TODO
    """
    cursor = dll.SDL_CreateCursor(ctypes.byref(data), ctypes.byref(mask),
                                  w, h, hotx, hoty)
    if cursor is None:
        raise SDLError()
    return cursor


@sdltype("SDL_FreeCursor", [ctypes.POINTER(SDL_Cursor)], None)
def free_cursor(cursor):
    """Releases the resources hold by the passed SDL_Cursor."""
    if not isinstance(cursor, SDL_Cursor):
        raise TypeError("cursor must be a SDL_Cursor")
    dll.SDL_FreeCursor(ctypes.byref(cursor))


@sdltype("SDL_GetCursor", None, ctypes.POINTER(SDL_Cursor))
def get_cursor():
    """Retrieves the currently used SDL_Cursor."""
    val = dll.SDL_GetCursor()
    if val is None or not bool(val):
        raise SDLError()
    return val.contents


@sdltype("SDL_SetCursor", [ctypes.POINTER(SDL_Cursor)], None)
def set_cursor(cursor):
    """Sets the SDL_Cursor to be used by the mouse input device."""
    if not isinstance(cursor, SDL_Cursor):
        raise TypeError("cursor must be a SDL_Cursor")
    dll.SDL_SetCursor(ctypes.byref(cursor))


@sdltype("SDL_GetMouseFocus", None, ctypes.POINTER(SDL_Window))
def get_mouse_focus():
    """Gets the SDL window that currently has the mouse input focus."""
    retval = dll.SDL_GetMouseFocus()
    if retval is None or not bool(retval):
        raise SDLError()
    return retval.contents


@sdltype("SDL_GetMouseState", [ctypes.POINTER(ctypes.c_int),
                               ctypes.POINTER(ctypes.c_int)], ctypes.c_ubyte)
def get_mouse_state():
    """Retrieves the current mouse state.

    This retrieves the current mouse button state and its x and y coordinates
    on the currently focused SDL window.
    The mouse button state is a bitmask, which can be tested with SDL_BUTTON().
    """
    x = ctypes.c_int(0)
    y = ctypes.c_int(0)
    state = dll.SDL_GetMouseState(ctypes.byref(x), ctypes.byref(y))
    return(state.value, x.value, y.value)


@sdltype("SDL_GetRelativeMouseMode", None, ctypes.c_int)
def get_relative_mouse_mode():
    """Checks, whether the relative mouse mode is enabled or not."""
    return dll.SDL_GetRelativeMouseMode() == SDL_TRUE


@sdltype("SDL_GetRelativeMouseState", [ctypes.POINTER(ctypes.c_int),
                                       ctypes.POINTER(ctypes.c_int)],
         ctypes.c_ubyte)
def get_relative_mouse_state():
    """Retrieves the relative state of the mouse.

    The current button state is returned as a button bitmask, which can
    be tested using SDL_BUTTON(), and x and y are set to the mouse deltas
    since the last call to get_relative_mouse_state().
    """
    x = ctypes.c_int(0)
    y = ctypes.c_int(0)
    state = dll.SDL_GetRelativeMouseState(ctypes.byref(x), ctypes.byref(y))
    return(state.value, x.value, y.value)


@sdltype("SDL_SetRelativeMouseMode", [ctypes.c_int], ctypes.c_int)
def set_relative_mouse_mode(enabled):
    """Enables or disables the relative mouse mode.

    While the mouse is in relative mode, the cursor is hidden, and the
    driver will try to report continuous motion in the current window.
    Only relative motion events will be delivered, the mouse position
    will not change.

    NOTE: This function will flush any pending mouse motion.
    """
    setval = ctypes.c_int(1)
    ret = 0
    if bool(enabled):
        ret = dll.SDL_SetRelativeMouseMode(SDL_TRUE)
    else:
        ret = dll.SDL_SetRelativeMouseMode(SDL_FALSE)
    if ret < 0:
        raise SDLError()


@sdltype("SDL_ShowCursor", [ctypes.c_int], ctypes.c_int)
def show_cursor(show):
    """Shows, hides or queries the state of the mouse cursor.

    If show is 1, the cursor will be shown, if it is 0, the cursor will be
    hidden. If show is -1, the state of the cursor(shown or hidden) will be
    returned as boolean flag.

    This will always return a bool, indicating whether the cursor is shown or
    hidden.
    """
    if type(show) is not int:
        raise TypeError("show must be an int")
    return dll.SDL_ShowCursor(show) == 1


@sdltype("SDL_WarpMouseInWindow", [ctypes.POINTER(SDL_Window), ctypes.c_int,
                                   ctypes.c_int], None)
def warp_mouse_in_window(window, x, y):
    """Moves the mouse to the given position in the specified window.

    If window is None, the mouse will be moved to the position in the SDL
    window, which currently has the input focus.
    """
    if not isinstance(window, SDL_Window):
        raise TypeError("window must be a SDL_Window")
    if window is None:
        dll.SDL_WarpMouseInWindow(None, x, y)
    else:
        dll.SDL_WarpMouseInWindow(ctypes.byref(window), x, y)
