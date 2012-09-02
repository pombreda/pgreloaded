"""
Wrapper methods around the SDL2 syswm routines.
"""
import ctypes
from pygame2.sdl import sdltype, dll, SDLError, SDL_FALSE
from pygame2.sdl.version import SDL_version, SDL_VERSION
from pygame2.sdl.video import SDL_Window

__all__ = ["SDL_SYSWM_UNKNOWN", "SDL_SYSWM_WINDOWS", "SDL_SYSWM_X11",
           "SDL_SYSWM_DIRECTFB", "SDL_SYSWM_COCOA", "SDL_SYSWM_UIKIT",
           "SDL_SysWMmsg", "SDL_SysWMinfo", "get_window_wm_info"
           ]


SDL_SYSWM_UNKNOWN  = 0
SDL_SYSWM_WINDOWS  = 1
SDL_SYSWM_X11      = 2
SDL_SYSWM_DIRECTFB = 3
SDL_SYSWM_COCOA    = 4
SDL_SYSWM_UIKIT    = 5
_SYSWMNAMES = ("unknown", "windows", "x11", "directfb", "cocoa", "uikit")


# FIXME: Hack around the ctypes "_type_ 'v' not supported" bug - remove
# once this has been fixed properly in Python 2.7+
HWND = ctypes.c_void_p
UINT = ctypes.c_uint
if ctypes.sizeof(ctypes.c_long) == ctypes.sizeof(ctypes.c_void_p):
    WPARAM = ctypes.c_ulong
    LPARAM = ctypes.c_long
elif ctypes.sizeof(ctypes.c_longlong) == ctypes.sizeof(ctypes.c_void_p):
    WPARAM = ctypes.c_ulonglong
    LPARAM = ctypes.c_longlong
# FIXME: end


class _winmsg(ctypes.Structure):
    """TODO"""
    _fields_ = [("hwnd", HWND),
                ("msg", UINT),
                ("wParam", WPARAM),
                ("lParam", LPARAM),
                ]


class _x11msg(ctypes.Structure):
    """TODO"""
    _fields_ = [("event", ctypes.c_void_p)]


class _dfbmsg(ctypes.Structure):
    """TODO"""
    _fields_ = [("event", ctypes.c_void_p)]


class _cocoamsg(ctypes.Structure):
    """TODO"""
    pass


class _uikitmsg(ctypes.Structure):
    """TODO"""
    pass


class _msg(ctypes.Union):
    """TODO"""
    _fields_ = [("win", _winmsg),
                ("x11", _x11msg),
                ("dfb", _dfbmsg),
                ("cocoa", _cocoamsg),
                ("uikit", _uikitmsg),
                ("dummy", ctypes.c_int)
                ]


class SDL_SysWMmsg(ctypes.Structure):
    """TODO"""
    _fields_ = [("version", SDL_version),
                ("subsystem", ctypes.c_int),
                ("msg", _msg)
                ]


class _wininfo(ctypes.Structure):
    """TODO"""
    _fields_ = [("window", HWND)]


class _x11info(ctypes.Structure):
    """TODO"""
    _fields_ = [("display", ctypes.c_void_p),
                ("window", ctypes.c_ulong)]


class _dfbinfo(ctypes.Structure):
    """TODO"""
    _fields_ = [("dfb", ctypes.c_void_p),
                ("window", ctypes.c_void_p),
                ("surface", ctypes.c_void_p)]


class _cocoainfo(ctypes.Structure):
    """TODO"""
    _fields_ = [("window", ctypes.c_void_p)]


class _uikitinfo(ctypes.Structure):
    """TODO"""
    _fields_ = [("window", ctypes.c_void_p)]


class _info(ctypes.Union):
    """TODO"""
    _fields_ = [("win", _wininfo),
                ("x11", _x11info),
                ("dfb", _dfbinfo),
                ("cocoa", _cocoainfo),
                ("uikit", _uikitinfo),
                ("dummy", ctypes.c_int)
                ]


class SDL_SysWMinfo(ctypes.Structure):
    """TODO"""
    _fields_ = [("version", SDL_version),
                ("subsystem", ctypes.c_int),
                ("info", _info)
                ]

    def __repr__(self):
        return "SDL_SysWMinfo(version=%s, subsystem=%s, ...)" \
            % (self.version, _SYSWMNAMES[self.subsystem])


@sdltype("SDL_GetWindowWMInfo", [ctypes.POINTER(SDL_Window),
                                 ctypes.POINTER(SDL_SysWMinfo)], ctypes.c_int)
def get_window_wm_info(window):
    """Retrieves driver-dependent window information."""
    if not isinstance(window, SDL_Window):
        raise TypeError("window must be a SDL_Window")
    wminfo = SDL_SysWMinfo()
    SDL_VERSION(wminfo.version)
    ret = dll.SDL_GetWindowWMInfo(ctypes.byref(window), ctypes.byref(wminfo))
    if ret == SDL_FALSE:
        raise SDLError()
    return wminfo
