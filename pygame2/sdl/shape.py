"""
Wrapper methods around the SDL2 shape routines.
"""
import ctypes
from pygame2.compat import byteify
from pygame2.sdl import sdltype, dll, SDL_TRUE, SDLError
from pygame2.sdl.video import SDL_Window
from pygame2.sdl.pixels import SDL_Color
from pygame2.sdl.surface import SDL_Surface

__all__ = ["SDL_SHAPEMODEALPHA", "SDL_WindowShapeParams",
           "SDL_WindowShapeMode", "create_shaped_window", "is_shaped_window",
           "set_window_shape", "get_shaped_window_mode"
           ]


SDL_NONSHAPEABLE_WINDOW    = -1
SDL_INVALID_SHAPE_ARGUMENT = -2
SDL_WINDOW_LACKS_SHAPE     = -3

ShapeModeDefault              = 0
ShapeModeBinarizeAlpha        = 1
ShapeModeReverseBinarizeAlpha = 2
ShapeModeColorKey             = 3


def SDL_SHAPEMODEALPHA(mode):
    """Checks, if the passed shape mode supports alpha transparency.
    """
    return mode == ShapeModeDefault or mode == ShapeModeBinarizeAlpha or \
        mode == ShapeModeReverseBinarizeAlpha


class SDL_WindowShapeParams(ctypes.Union):
    """TODO"""
    _fields_ = [("binarizationCutoff", ctypes.c_ubyte),
                ("colorKey", SDL_Color)
                ]


class SDL_WindowShapeMode(ctypes.Structure):
    """TODO"""
    _fields_ = [("mode", ctypes.c_int),
                ("parameters", SDL_WindowShapeParams)
                ]


@sdltype("SDL_CreateShapedWindow", [ctypes.c_char_p, ctypes.c_uint,
                                    ctypes.c_uint, ctypes.c_uint,
                                    ctypes.c_uint, ctypes.c_uint],
         ctypes.POINTER(SDL_Window))
def create_shaped_window(title, x, y, w, h, flags):
    """Create a window that can be shaped with the specified position,
    dimension and flags.

    TODO
    """
    title = byteify(str(title), "utf-8")
    retval = dll.SDL_CreateShapedWindow(title, x, y, w, h, flags)
    if retval is None or not bool(retval):
        raise SDLError()
    return retval.contents


@sdltype("SDL_IsShapedWindow", [ctypes.POINTER(SDL_Window)], ctypes.c_int)
def is_shaped_window(window):
    """Checks if the passed window is a shaped window.
    """
    return dll.SDL_IsShapedWindow(ctypes.byref(window)) == SDL_TRUE


@sdltype("SDL_SetWindowShape", [ctypes.POINTER(SDL_Window),
                                ctypes.POINTER(SDL_Surface),
                                ctypes.POINTER(SDL_WindowShapeMode)],
         ctypes.c_int)
def set_window_shape(window, surface, shapemode):
    """Sets the shape parameters of a shaped window.
    """
    retval = dll.SDL_SetWindowShape(ctypes.byref(window),
                                    ctypes.byref(surface),
                                    ctypes.byref(shapemode))
    if retval != 0:
        # The shape functions in SDL2 do not set any error.
        if retval == SDL_WINDOW_LACKS_SHAPE:
            raise SDLError("window has no shape")
        elif retval == SDL_NONSHAPEABLE_WINDOW:
            raise SDLError("window is not shapeable")
        elif retval == SDL_INVALID_SHAPE_ARGUMENT:
            raise SDLError("invalid shape argument")
        else:
            raise SDLError()


@sdltype("SDL_GetShapedWindowMode", [ctypes.POINTER(SDL_Window),
                                     ctypes.POINTER(SDL_WindowShapeMode)],
         ctypes.c_int)
def get_shaped_window_mode(window):
    """Gets the shape parameters from a shaped window
    """
    mode = SDL_WindowShapeMode()
    retval = dll.SDL_GetShapedWindowMode(ctypes.byref(window),
                                         ctypes.byref(mode))
    if retval != 0:
        # The shape functions in SDL2 do not set any error.
        if retval == SDL_WINDOW_LACKS_SHAPE:
            raise SDLError("window has no shape")
        elif retval == SDL_NONSHAPEABLE_WINDOW:
            raise SDLError("window is not shapeable")
        else:
            raise SDLError()
    return mode
