"""
Wrapper methods around the SDL2 video management routines.
"""
import ctypes
from pygame2.compat import *
from pygame2.sdl import sdltype, dll, SDL_TRUE
import pygame2.sdl.array as array
from pygame2.sdl.surface import SDL_Surface
from pygame2.sdl.rect import SDL_Rect
from pygame2.sdl.error import SDLError

SDL_BLENDMODE_NONE  = 0x00000000
SDL_BLENDMODE_BLEND = 0x00000001
SDL_BLENDMODE_ADD   = 0x00000002
SDL_BLENDMODE_MOD   = 0x00000004

SDL_GL_RED_SIZE                 = 0
SDL_GL_GREEN_SIZE               = 1
SDL_GL_BLUE_SIZE                = 2
SDL_GL_ALPHA_SIZE               = 3
SDL_GL_BUFFER_SIZE              = 4
SDL_GL_DOUBLEBUFFER             = 5
SDL_GL_DEPTH_SIZE               = 6
SDL_GL_STENCIL_SIZE             = 7
SDL_GL_ACCUM_RED_SIZE           = 8
SDL_GL_ACCUM_GREEN_SIZE         = 9
SDL_GL_ACCUM_BLUE_SIZE          = 10
SDL_GL_ACCUM_ALPHA_SIZE         = 11
SDL_GL_STEREO                   = 12
SDL_GL_MULTISAMPLEBUFFERS       = 13
SDL_GL_MULTISAMPLESAMPLES       = 14
SDL_GL_ACCELERATED_VISUAL       = 15
SDL_GL_RETAINED_BACKING         = 16
SDL_GL_CONTEXT_MAJOR_VERSION    = 17
SDL_GL_CONTEXT_MINOR_VERSION    = 18
SDL_GL_CONTEXT_FLAGS            = 19
SDL_GL_CONTEXT_PROFILE_MASK     = 20

SDL_GL_CONTEXT_PROFILE_CORE           = 0x0001
SDL_GL_CONTEXT_PROFILE_COMPATIBILITY  = 0x0002
SDL_GL_CONTEXT_PROFILE_ES2            = 0x0004

SDL_GL_CONTEXT_DEBUG_FLAG              = 0x0001
SDL_GL_CONTEXT_FORWARD_COMPATIBLE_FLAG = 0x0002
SDL_GL_CONTEXT_ROBUST_ACCESS_FLAG      = 0x0004

SDL_WINDOW_FULLSCREEN       = 0x00000001
SDL_WINDOW_OPENGL           = 0x00000002
SDL_WINDOW_SHOWN            = 0x00000004
SDL_WINDOW_HIDDEN           = 0x00000008
SDL_WINDOW_BORDERLESS       = 0x00000010
SDL_WINDOW_RESIZABLE        = 0x00000020
SDL_WINDOW_MINIMIZED        = 0x00000040
SDL_WINDOW_MAXIMIZED        = 0x00000080
SDL_WINDOW_INPUT_GRABBED    = 0x00000100
SDL_WINDOW_INPUT_FOCUS      = 0x00000200
SDL_WINDOW_MOUSE_FOCUS      = 0x00000400
SDL_WINDOW_FOREIGN          = 0x00000800

SDL_WINDOWEVENT_NONE            = 0
SDL_WINDOWEVENT_SHOWN           = 1
SDL_WINDOWEVENT_HIDDEN          = 2
SDL_WINDOWEVENT_EXPOSED         = 3
SDL_WINDOWEVENT_MOVED           = 4
SDL_WINDOWEVENT_RESIZED         = 5
SDL_WINDOWEVENT_SIZE_CHANGED    = 6
SDL_WINDOWEVENT_MINIMIZED       = 7
SDL_WINDOWEVENT_MAXIMIZED       = 8
SDL_WINDOWEVENT_RESTORED        = 9
SDL_WINDOWEVENT_ENTER           = 10
SDL_WINDOWEVENT_LEAVE           = 11
SDL_WINDOWEVENT_FOCUS_GAINED    = 12
SDL_WINDOWEVENT_FOCUS_LOST      = 13
SDL_WINDOWEVENT_CLOSE           = 14

SDL_WINDOWPOS_UNDEFINED_MASK = 0x1FFF0000
def SDL_WINDOWPOS_UNDEFINED_DISPLAY (x):
    """
    """
    return (SDL_WINDOWPOS_UNDEFINED_MASK | x)

SDL_WINDOWPOS_UNDEFINED = SDL_WINDOWPOS_UNDEFINED_DISPLAY (0)
def SDL_WINDOWPOS_ISUNDEFINED (x):
    """
    """
    return (x & 0xFFFF0000) == SDL_WINDOWPOS_UNDEFINED_MASK

SDL_WINDOWPOS_CENTERED_MASK = 0x2FFF0000
def SDL_WINDOWPOS_CENTERED_DISPLAY (x):
    """
    """
    return (SDL_WINDOWPOS_CENTERED_MASK | x)

SDL_WINDOWPOS_CENTERED = SDL_WINDOWPOS_CENTERED_DISPLAY (0)
def SDL_WINDOWPOS_ISCENTERED (x):
    """
    """
    return (x & 0xFFFF0000) == SDL_WINDOWPOS_CENTERED_MASK

class SDL_DisplayMode (ctypes.Structure):
    """SDL_DisplayMode (format=0, w=0, h=0, refresh_rate=0) -> SDL_DisplayMode
    
    TODO
    """
    _fields_ = [("format", ctypes.c_uint),
                ("w", ctypes.c_int),
                ("h", ctypes.c_int),
                ("refresh_rate", ctypes.c_int),
                ("_driverdata", ctypes.c_void_p)
                ]
    def __init__ (self, format=0, w=0, h=0, refresh_rate=0):
        self.format = format
        self.w = w
        self.h = h
        self.refresh_rate = refresh_rate

    def __repr__ (self):
        return "SDL_DisplayMode (format=%d, w=%d, h=%d, refresh_rate=%d)" % \
            (self.format, self.w, self.h, self.refresh_rate)

    def __eq__ (self, mode):
        return self.format == mode.format and self.w == mode.w and \
            self.h == mode.h and self.refresh_rate == mode.refresh_rate

    def __ne__ (self, mode):
        return self.format != mode.format or self.w != mode.w or \
            self.h != mode.h or self.refresh_rate != mode.refresh_rate
    
class SDL_Window (ctypes.Structure):
    """
    """
    @property
    def position (self):
        return get_window_position (self)
    
    @property
    def size (self):
        return get_window_size (self)

    @property
    def flags (self):
        return get_window_flags (self)

    @property
    def title (self):
        return get_window_title (self)
    
    @property
    def id (self):
        return get_window_id (self)
    
    def __repr__ (self):
        return "SDL_Window (id=%d, title=%s, position=%s, size=%s)" % \
            (self.id, self.title, self.position, self.size)
    
SDL_Window._fields_ = [("_magic", ctypes.c_void_p),
                       ("_id", ctypes.c_uint),
                       ("_title", ctypes.c_char_p),
                       ("_x", ctypes.c_int),
                       ("_y", ctypes.c_int),
                       ("_w", ctypes.c_int),
                       ("_h", ctypes.c_int),
                       ("_flags", ctypes.c_uint),
                       ("_windowed", SDL_Rect),
                       ("_fullscreen_mode", SDL_DisplayMode),
                       ("_brightness", ctypes.c_float),
                       ("_gamma", ctypes.POINTER(ctypes.c_ushort)),
                       ("_saved_gamma", ctypes.POINTER(ctypes.c_ushort)),
                       ("_surface", ctypes.POINTER (SDL_Surface)),
                       ("_surface_valid", ctypes.c_int),
                       # TODO: wrap SDL_WindowShaper?
                       ("_shaper", ctypes.c_void_p), 
                       # TODO: wrap SDL_WindowUserData?
                       ("_data", ctypes.c_void_p), 
                       ("_driverdata", ctypes.c_void_p),
                       ("_prev", ctypes.POINTER(SDL_Window)),
                       ("_next", ctypes.POINTER(SDL_Window)),
                        ]
    
    
@sdltype("SDL_CreateWindow", [ctypes.c_char_p, ctypes.c_int, ctypes.c_int,
                              ctypes.c_int, ctypes.c_int, ctypes.c_uint],
         ctypes.POINTER(SDL_Window))
def create_window (title, x, y, w, h, flags):
    """create_window (title, x, y, w, h, flags) -> SDL_Window

    Creates a new SDL window with the specified dimensions and title.
    
    TODO
    """
    title = byteify (str(title), "utf-8")
    retval = dll.SDL_CreateWindow (title, x, y, w, h, flags)
    if retval is None or not bool(retval):
        raise SDLError ()
    return retval.contents

@sdltype("SDL_CreateWindowFrom", [ctypes.c_void_p], ctypes.POINTER(SDL_Window))
def create_window_from (data):
    """
    """
    retval = dll.SDL_CreateWindowFrom (ctypes.byref (data))
    if retval is None or not bool(retval):
        raise SDLError ()
    return retval.contents

@sdltype("SDL_DestroyWindow", [ctypes.POINTER(SDL_Window)], None)
def destroy_window (window):
    """destroy_window (window) -> None

    Destroys the passed SDL_Window.

    Calling methods on a destroyed window 
    """
    if not isinstance (window, SDL_Window):
        raise TypeError ("window must be a SDL_Window")
    dll.SDL_DestroyWindow (ctypes.byref (window))
    
@sdltype("SDL_DisableScreenSaver", None, None)
def disable_screensaver ():
    """disable_screensaver () -> None

    Prevents the screen from being blanked by a screensaver.
    """
    dll.SDL_DisableScreenSaver ()

@sdltype("SDL_EnableScreenSaver", None, None)
def enable_screensaver ():
    """enable_screensaver () -> None

    Allows the screen to be blanked by a screensaver.
    """
    dll.SDL_EnableScreenSaver ()
    
@sdltype("SDL_IsScreenSaverEnabled", None, ctypes.c_int)
def is_screensaver_enabled ():
    """is_screensaver_enabled () -> bool

    Returns whether the scrensaver is currently enabled.
    """
    return dll.SDL_IsScreenSaverEnabled () == SDL_TRUE

@sdltype("SDL_GetClosestDisplayMode", [ctypes.c_int,
                                       ctypes.POINTER(SDL_DisplayMode),
                                       ctypes.POINTER(SDL_DisplayMode)],
         ctypes.POINTER(SDL_DisplayMode))
def get_closest_display_mode (displayindex, mode):
    """get_closest_display_mode (displayindex, mode) -> SDL_DisplayMode
    
    Get the closest match to the requested display mode.
    
    The available display modes are scanned and the closest mode matching the
    requested mode and returned. The mode format and refresh_rate default to
    the desktop mode if they are 0 in the passed mode. The modes are  scanned
    with size being first priority, format being second priority, and finally
    checking the refresh_rate. If no mode could be found, a SDLError is raised.
    """
    if type (displayindex) is not int:
        raise TypeError ("displayindex must be an int")
    if not isinstance (mode, SDL_DisplayMode):
        raise TypeError ("mode must be a SDL_DisplayMode")
    
    closest = SDL_DisplayMode ()
    retval = dll.SDL_GetClosestDisplayMode (displayindex, ctypes.byref (mode),
                                            ctypes.byref (closest))
    if retval is None or not bool (retval):
        return None
    return closest

@sdltype("SDL_GetCurrentDisplayMode", [ctypes.c_int,
                                       ctypes.POINTER(SDL_DisplayMode)],
         ctypes.c_int)
def get_current_display_mode (displayindex):
    """get_current_display_mode (displayindex) -> SDL_DisplayMode
    
    Gets the currently active display mode.
    
    Raises a SDLError, if an error occured.
    """
    if type (displayindex) is not int:
        raise TypeError ("displayindex must be an int")
    current = SDL_DisplayMode ()
    retval = dll.SDL_GetCurrentDisplayMode (displayindex,
                                            ctypes.byref (current))
    if retval < 0:
        raise SDLError ()
    return current

@sdltype("SDL_GetDesktopDisplayMode", [ctypes.c_int,
                                       ctypes.POINTER(SDL_DisplayMode)],
         ctypes.c_int)
def get_desktop_display_mode (displayindex):
    """get_desktop_display_mode (displayindex) -> SDL_DisplayMode
    
    Gets the currently used desktop display mode.
    
    Raises a SDLError, if an error occured.
    """
    if type (displayindex) is not int:
        raise TypeError ("displayindex must be an int")
    desktop = SDL_DisplayMode ()
    retval = dll.SDL_GetDesktopDisplayMode (displayindex,
                                            ctypes.byref (desktop))
    if retval < 0:
        raise SDLError ()
    return desktop

@sdltype("SDL_GetDisplayBounds", [ctypes.c_int, ctypes.POINTER(SDL_Rect)],
         ctypes.c_int)
def get_display_bounds (displayindex):
    """get_display_bounds (displayindex) -> SDL_Rect
    
    Gets the visible dimensions for a display and its currently used mode.
    
    Raises a SDLError, if an error occured.    
    """
    if type (displayindex) is not int:
        raise TypeError ("displayindex must be an int")
    rect = SDL_Rect ()
    retval = dll.SDL_GetDisplayBounds (displayindex, ctypes.byref (rect))
    if retval < 0:
        raise SDLError ()
    return rect

@sdltype("SDL_GetDisplayMode", [ctypes.c_int, ctypes.c_int,
                                ctypes.POINTER(SDL_DisplayMode)],
         ctypes.c_int)
def get_display_mode (displayindex, modeindex):
    """get_display_mode (displayindex, modeindex) -> SDL_DisplayMode
    
    Retrieves the display mode for a specific display.
    
    Raises a SDLError, if an error occured.
    """
    if type (displayindex) is not int or type (modeindex) is not int:
        raise TypeError ("displayindex and modeindex must be int values")
    displaymode = SDL_DisplayMode ()
    retval = dll.SDL_GetDisplayMode (displayindex, modeindex,
                                     ctypes.byref (displaymode))
    if retval < 0:
        raise SDLError ()
    return displaymode
    
@sdltype("SDL_GetNumDisplayModes", [ctypes.c_int], ctypes.c_int)
def get_num_display_modes (displayindex):
    """get_num_display_modes (displayindex) -> int
    
    Retrieves the number of available display modes for a specific display.
    
    Raises a SDLError, if an error occured.
    """
    if type (displayindex) is not int:
        raise TypeError ("displayindex must be an int")
    retval = dll.SDL_GetNumDisplayModes (displayindex)
    if retval < 0:
        raise SDLError ()
    return retval

@sdltype("SDL_GetNumVideoDisplays", None, ctypes.c_int)
def get_num_video_displays ():
    """get_num_video_displays () -> int
    
    Retrieves the number of available video displays.
    
    Raises a SDLError, if an error occured.
    """
    retval = dll.SDL_GetNumVideoDisplays ()
    if retval < 0:
        raise SDLError ()
    return retval

@sdltype("SDL_GetNumVideoDrivers", None, ctypes.c_int)
def get_num_video_drivers ():
    """get_num_video_drivers () -> int
    
    Retrieves the number of available video drivers.
    """
    retval = dll.SDL_GetNumVideoDrivers ()
    if retval < 0:
        raise SDLError ()
    return retval

@sdltype("SDL_GetVideoDriver", [ctypes.c_int], ctypes.c_char_p)
def get_video_driver (displayindex):
    """get_video_driver (displayindex) -> str
    
    Gets the video driver used by a specific display.
    
    If the video driver for the display could not be determined, or if an
    invalid display index is used, a SDLError is raised.
    """
    if type (displayindex) is not int:
        raise TypeError ("displayindex must be an int")
    retval = dll.SDL_GetVideoDriver (displayindex)
    if retval is None:
        raise SDLError ()
    return stringify (retval, "utf-8")

@sdltype("SDL_GetCurrentVideoDriver", None, ctypes.c_char_p)
def get_current_video_driver ():
    """get_current_video_driver () -> str
    
    Gets the currently used video driver.
    """
    retval = dll.SDL_GetCurrentVideoDriver ()
    return stringify (retval, "utf-8")

@sdltype("SDL_VideoInit", [ctypes.c_char_p], None)
def init (drivername=None):
    """init (drivername=None) -> None
    
    Initializes the SDL video subsystem.
    
    Initializes the SDL video subsystem with an optionally choosable driver to
    use. This is basically the same as calling
    
        pygame2.sdl.init (pygame2.sdl.SDL_INIT_VIDEO)
    
    but lets you choose a video driver instead of using the default driver for
    the platform your application is running on
    """
    if drivername is not None:
        drivername = byteify (str (drivername), "utf-8")
    dll.SDL_VideoInit (drivername)

@sdltype ("SDL_VideoQuit", None, None)
def quit ():
    """quit () -> None
    
    Quits the SDL video subsystem.
    
    This is similar to calling
    pygame2.sdl.quit_subsystem (pygame2.sdl.SDL_INIT_VIDEO)
    """
    dll.SDL_VideoQuit ()

@sdltype("SDL_GetWindowDisplay", [ctypes.POINTER(SDL_Window)], ctypes.c_int)
def get_window_display (window):
    """get_window_display (window) -> int
    
    Gets the index of the display, the SDL_window is currently shown on.
    
    If the display could not determined, a SDLError is raised.
    """
    if not isinstance (window, SDL_Window):
        raise TypeError ("window must be a SDL_Window")
    retval = dll.SDL_GetWindowDisplay (ctypes.byref (window))
    if retval == -1:
        raise SDLError ()
    return retval

@sdltype("SDL_SetWindowDisplayMode", [ctypes.POINTER(SDL_Window),
                                      ctypes.POINTER(SDL_DisplayMode)],
         ctypes.c_int)
def set_window_display_mode (window, mode=None):
    """set_window_display_mode (window, mode=None) -> None
    
    Sets the display mode to be used, if the window is shown in a fullscreen
    mode.
    
    If mode is omitted, the default display mode for the window is used, which
    usually is the window's dimensions and the desktop format and refresh rate.
    Since certain dimensions cannot be used in fullscreen on a display, the
    default mode for the window might be the lowest or highest (or something in
    between) mode of the display itself.
    """
    if not isinstance (window, SDL_Window):
        raise TypeError ("window must be a SDL_Window")
    if mode and not isinstance (mode, SDL_DisplayMode):
        raise TypeError ("mode must be a SDL_DisplayMode")
    val = None
    if mode:
        val = ctypes.byref (mode)
    retval = dll.SDL_SetWindowDisplayMode (ctypes.byref (window), val)
    if retval == -1:
        raise SDLError ()

@sdltype("SDL_GetWindowDisplayMode", [ctypes.POINTER(SDL_Window),
                                      ctypes.POINTER(SDL_DisplayMode)],
         ctypes.c_int)
def get_window_display_mode (window):
    """get_window_display_mode (window) -> SDL_DisplayMode
    
    Gets the currently used SDL_DisplayMode for a SDL_Window.
    
    If the display mode for the window could not be determined, a SDLError is
    raised.
    """
    if not isinstance (window, SDL_Window):
        raise TypeError ("window must be a SDL_Window")
    mode = SDL_DisplayMode ()
    retval = dll.SDL_GetWindowDisplayMode (ctypes.byref (window),
                                           ctypes.byref (mode))
    if retval == -1:
        raise SDLError ()
    return mode

@sdltype ("SDL_GetWindowPixelFormat", [ctypes.POINTER(SDL_Window)],
          ctypes.c_uint)
def get_window_pixelformat (window):
    """get_window_pixelformat (window) -> int
    
    Retrieves the pixel format associated with the window.
    """
    if not isinstance (window, SDL_Window):
        raise TypeError ("window must be a SDL_Window")
    format = dll.SDL_GetWindowPixelFormat (ctypes.byref(window))
    if format == 0:
        raise SDLError ()
    return format

@sdltype ("SDL_GetWindowID", [ctypes.POINTER(SDL_Window)], ctypes.c_int)
def get_window_id (window):
    """get_window_id (window) -> int
    
    Gets the id of the SDL_Window.
    """
    if not isinstance (window, SDL_Window):
        raise TypeError ("window must be a SDL_Window")
    id = dll.SDL_GetWindowID (ctypes.byref(window))
    if id == 0:
        raise SDLError ()
    return id

@sdltype ("SDL_GetWindowFromID", [ctypes.c_uint], ctypes.POINTER(SDL_Window))
def get_window_from_id (id):
    """get_window_from_id (id) -> SDL_Window
    
    Get a SDL_Window from a stored id.
    
    If no SDL_Window could be found for the passed id, a SDLError is raised.
    """
    if type (id) is not int:
        raise TypeError ("id must be an int")
    window = dll.SDL_GetWindowFromID (id)
    if window is None:
        raise SDLError ()
    return window.contents

@sdltype ("SDL_GetWindowFlags", [ctypes.POINTER(SDL_Window)], ctypes.c_uint)
def get_window_flags (window):
    """get_window_flags (window) -> int
    
    Retrieves the currently applied flags for a specific window.
    """
    if not isinstance (window, SDL_Window):
        raise TypeError ("window must be a SDL_Window")
    return dll.SDL_GetWindowFlags (ctypes.byref(window))

@sdltype ("SDL_GetWindowTitle", [ctypes.POINTER(SDL_Window)], ctypes.c_char_p)
def get_window_title (window):
    """get_window_title (window) -> str
    
    Retrieves the title of a SDL_Window.
    
    Raises a SDLError, if the title could not be retrieved.
    """
    if not isinstance (window, SDL_Window):
        raise TypeError ("window must be a SDL_Window")
    retval = dll.SDL_GetWindowTitle (ctypes.byref(window))
    if retval is None or not bool (retval):
        raise SDLError ()
    return stringify (retval, "utf-8")

@sdltype ("SDL_SetWindowTitle", [ctypes.POINTER(SDL_Window), ctypes.c_char_p],
          None)
def set_window_title (window, title):
    """set_window_title (window, title) -> None
    
    Sets the title to be used by a SDL_Window.
    """
    if not isinstance (window, SDL_Window):
        raise TypeError ("window must be a SDL_Window")
    title = byteify (str (title), "utf-8")
    dll.SDL_SetWindowTitle (ctypes.byref(window), title)

@sdltype("SDL_SetWindowIcon", [ctypes.POINTER(SDL_Window),
                               ctypes.POINTER(SDL_Surface)], None)
def set_window_icon (window, icon):
    """
    """
    if not isinstance (window, SDL_Window):
        raise TypeError ("window must be a SDL_Window")
    if not isinstance (icon, SDL_Surface):
        raise TypeError ("icon must be a SDL_Surface")
    dll.SDL_SetWindowIcon (ctypes.byref(window), ctypes.byref(icon))

@sdltype("SDL_SetWindowData", [ctypes.POINTER(SDL_Window), ctypes.c_char_p,
                               ctypes.py_object], ctypes.c_void_p)
def set_window_data (window, name, data):
    """set_window_data (window, name, data) -> object

    Associate arbitrary content with a window.

    The passed data will be identified by the specified name.

    Note: you must preserve a 
    This will return the previous value 
    """
    if not isinstance (window, SDL_Window):
        raise TypeError ("window must be a SDL_Window")
    name = byteify (str (name), "utf-8")
    ptr = ctypes.py_object(data)
    retval = dll.SDL_SetWindowData (ctypes.byref (window), name, ptr)
    retval = ctypes.cast (retval, ctypes.py_object)
    if retval is None or not bool (retval):
        return None
    return retval.value

@sdltype("SDL_GetWindowData", [ctypes.POINTER(SDL_Window), ctypes.c_char_p],
         ctypes.c_void_p)
def get_window_data (window, name):
    """get_window_data (window, name) -> object

    Gets associated content from the window.
    
    The data to be retrieved is identified by the specified name. If there is
    no data found for name, None will be returned.
    """
    if not isinstance (window, SDL_Window):
        raise TypeError ("window must be a SDL_Window")
    name = byteify (str (name), "utf-8")
    retval = dll.SDL_GetWindowData (ctypes.byref(window), name)
    retval = ctypes.cast (retval, ctypes.py_object)
    if retval is None or not bool(retval):
        return None
    return retval.value

@sdltype("SDL_SetWindowPosition", [ctypes.POINTER(SDL_Window), ctypes.c_int,
                                   ctypes.c_int], None)
def set_window_position (window, x, y):
    """set_window_position (window, x, y) -> None

    Sets the position of the top-left corner of the passed SDL_Window.
    """
    if not isinstance (window, SDL_Window):
        raise TypeError ("window must be a SDL_Window")
    if type (x) is not int or type (y) is not int:
        raise TypeError ("x and y must be integer values")
    dll.SDL_SetWindowPosition (ctypes.byref (window), x, y)

@sdltype("SDL_GetWindowPosition", [ctypes.POINTER(SDL_Window),
                                   ctypes.POINTER(ctypes.c_int),
                                   ctypes.POINTER(ctypes.c_int)], None)
def get_window_position (window):
    """get_window_position (window) -> int, int

    Gets the current top-left position of the passed SDL_Window
    """
    if not isinstance (window, SDL_Window):
        raise TypeError ("window must be a SDL_Window")
    x = ctypes.c_int (0)
    y = ctypes.c_int (0)
    dll.SDL_GetWindowPosition (ctypes.byref(window), ctypes.byref(x),
                               ctypes.byref(y))
    return x.value, y.value

@sdltype("SDL_SetWindowSize", [ctypes.POINTER(SDL_Window), ctypes.c_int,
                               ctypes.c_int], None)
def set_window_size (window, w, h):
    """set_window_size (window, w, h) -> None

    Sets the size of the passed SDL_Window.
    """
    if not isinstance (window, SDL_Window):
        raise TypeError ("window must be a SDL_Window")
    if type (w) is not int or type (h) is not int:
        raise TypeError ("w and h must be integer values")
    dll.SDL_SetWindowSize (ctypes.byref (window), w, h)

@sdltype("SDL_GetWindowSize", [ctypes.POINTER(SDL_Window),
                               ctypes.POINTER(ctypes.c_int),
                               ctypes.POINTER(ctypes.c_int)], None)
def get_window_size (window):
    """get_window_size (window) -> int, int

    Gets the size of the passed SDL_window.
    """
    if not isinstance (window, SDL_Window):
        raise TypeError ("window must be a SDL_Window")
    w = ctypes.c_int (0)
    h = ctypes.c_int (0)
    dll.SDL_GetWindowSize (ctypes.byref(window), ctypes.byref(w),
                           ctypes.byref(h))
    return w.value, h.value

@sdltype("SDL_ShowWindow", [ctypes.POINTER(SDL_Window)], None)
def show_window (window):
    """show_window (window) -> None

    Shows the passed SDL_Window.
    """
    if not isinstance (window, SDL_Window):
        raise TypeError ("window must be a SDL_Window")
    dll.SDL_ShowWindow (ctypes.byref(window))

@sdltype("SDL_HideWindow", [ctypes.POINTER(SDL_Window)], None)
def hide_window (window):
    """hide_window (window) -> None

    Hides the passed SDL_Window.
    """
    if not isinstance (window, SDL_Window):
        raise TypeError ("window must be a SDL_Window")
    dll.SDL_HideWindow (ctypes.byref(window))

@sdltype("SDL_RaiseWindow", [ctypes.POINTER(SDL_Window)], None)
def raise_window (window):
    """raise_window (window) -> None

    Raises the passed window above other windows.
    """
    if not isinstance (window, SDL_Window):
        raise TypeError ("window must be a SDL_Window")
    dll.SDL_RaiseWindow (ctypes.byref(window))

@sdltype("SDL_MaximizeWindow", [ctypes.POINTER(SDL_Window)], None)
def maximize_window (window):
    """maximize_window (window) -> None

    Tries to maximize the window size to the display extents, but at
    least as large as possible.
    """
    if not isinstance (window, SDL_Window):
        raise TypeError ("window must be a SDL_Window")
    dll.SDL_MaximizeWindow (ctypes.byref(window))

@sdltype("SDL_MinimizeWindow", [ctypes.POINTER(SDL_Window)], None)
def minimize_window (window):
    """minimize_window (window) -> None

    Minimizes a window to an iconic representation.
    """
    if not isinstance (window, SDL_Window):
        raise TypeError ("window must be a SDL_Window")
    dll.SDL_MinimizeWindow (ctypes.byref(window))

@sdltype("SDL_RestoreWindow", [ctypes.POINTER(SDL_Window)], None)
def restore_window (window):
    """restore_window (window) -> None

    Restores the size and position of a minimized or maximized window.
    """
    if not isinstance (window, SDL_Window):
        raise TypeError ("window must be a SDL_Window")
    dll.SDL_RestoreWindow (ctypes.byref(window))

@sdltype("SDL_SetWindowFullscreen", [ctypes.POINTER(SDL_Window), ctypes.c_int],
         ctypes.c_int)
def set_window_fullscreen (window, fullscreen):
    """set_window_fullscreen (window, fullscreen) -> None

    Sets a window's fullscreen state.
    """
    if not isinstance (window, SDL_Window):
        raise TypeError ("window must be a SDL_Window")
    fscreen = None
    if not fullscreen:
        fscreen = ctypes.c_int (0)
    else:
        fscreen = ctypes.c_int (1)
    retval = dll.SDL_SetWindowFullscreen (ctypes.byref(window), fscreen)
    if retval == -1:
        raise SDLError ()

@sdltype("SDL_GetWindowSurface", [ctypes.POINTER(SDL_Window)],
    ctypes.POINTER(SDL_Surface))
def get_window_surface (window):
    """get_window_surface (window) -> SDL_Surface

    Gets the SDL_Surface associated with the passed SDL_Window.

    A new surface will be created with the optimal format for the
    window, if necessary. This surface will be freed when the window is
    destroyed.

    NOTE: You may not combine this with 3D or the rendering API on this
    window.
    """
    if not isinstance (window, SDL_Window):
        raise TypeError ("window must be a SDL_Window")
    surface = dll.SDL_GetWindowSurface (ctypes.byref(window))
    if surface is None or not bool (surface):
        raise SDLError ()
    return surface.contents

@sdltype("SDL_UpdateWindowSurface", [ctypes.POINTER(SDL_Window)], None)
def update_window_surface (window):
    """update_window_surface (window) -> None

    Copies the window surface to the screen.

    Raises a SDLError, if an error occured.
    """
    if not isinstance (window, SDL_Window):
        raise TypeError ("window must be a SDL_Window")
    retval = dll.SDL_UpdateWindowSurface (ctypes.byref(window))
    if retval == -1:
        raise SDLError ()

@sdltype("SDL_UpdateWindowSurfaceRects", [ctypes.POINTER(SDL_Window),
                                          ctypes.POINTER(SDL_Rect),
                                          ctypes.c_int], ctypes.c_int)
def update_window_surface_rects (window, rects):
    """update_window_surface_rects (window, rects) -> None

    Copies a set of areas of the window surface to the screen.

    The rects argument must be a sequence of SDL_Rect instances.

    Raises a SDLError, if an error occured.
    """
    if not isinstance (window, SDL_Window):
        raise TypeError ("window must be a SDL_Window")
    rptr, count = array.to_ctypes (rects, SDL_Rect)
    retval = dll.SDL_UpdateWindowSurfaceRects (ctypes.byref(window), rptr,
                                               count)
    if retval == -1:
        raise SDLError ()

@sdltype("SDL_SetWindowGrab", [ctypes.POINTER(SDL_Window), ctypes.c_int], None)
def set_window_grab (window, grabbed):
    """set_window_grab (window, grabbed) -> None

    Sets a window's input grab mode.

    If grabbed is True, the window will grab the input, otherwise, it
    will release the grab.
    """
    if not isinstance (window, SDL_Window):
        raise TypeError ("window must be a SDL_Window")
    if not grabbed:
        grab = ctypes.c_int (0)
    else:
        grab = ctypes.c_int (1)
    dll.SDL_SetWindowGrab (ctypes.byref(window), grab)

@sdltype("SDL_GetWindowGrab", [ctypes.POINTER(SDL_Window)], ctypes.c_int)
def get_window_grab (window):
    """get_window_grab (window) -> bool

    Checks, if input is currently grabbed by the window.
    """
    if not isinstance (window, SDL_Window):
        raise TypeError ("window must be a SDL_Window")
    return dll.SDL_GetWindowGrab (ctypes.byref(window)) == SDL_TRUE

@sdltype("SDL_SetWindowBrightness", [ctypes.POINTER(SDL_Window),
                                     ctypes.c_float], ctypes.c_int)
def set_window_brightness (window, brightness):
    """set_window_brightness (windown, brightness) -> float

    Sets the brightness (gamma correction) for the passed window.

    Raises a SDLError, if an error occured.
    """
    if not isinstance (window, SDL_Window):
        raise TypeError ("window must be a SDL_Window")
    bright = ctypes.c_float (float (brightness))
    retval = dll.SDL_SetWindowBrightness (ctypes.byref(window), bright)
    if retval == -1:
        raise SDLError ()

@sdltype("SDL_GetWindowBrightness", [ctypes.POINTER(SDL_Window)],
         ctypes.c_float)
def get_window_brightness (window):
    """get_window_brightness (window) -> float

    Gets the brightness (gamma correction) of the window.
    """
    if not isinstance (window, SDL_Window):
        raise TypeError ("window must be a SDL_Window")
    return dll.SDL_GetWindowBrightness (ctypes.byref(window))

@sdltype("SDL_SetWindowGammaRamp", [ctypes.POINTER(SDL_Window),
                                    ctypes.POINTER(ctypes.c_ushort),
                                    ctypes.POINTER(ctypes.c_ushort),
                                    ctypes.POINTER(ctypes.c_ushort)],
         ctypes.c_int)
def set_window_gamma_ramp (window, red, green, blue):
    """
    """
    if not isinstance (window, SDL_Window):
        raise TypeError ("window must be a SDL_Window")
    rptr, size = array.to_ctypes (red, ctypes.c_ushort)
    if size != 256:
        raise ValueError ("red gamma table must contain 256 values")
    gptr, size = array.to_ctypes (green, ctypes.c_ushort)
    if size != 256:
        raise ValueError ("green gamma table must contain 256 values")
    bptr, size = array.to_ctypes (blue, ctypes.c_ushort)
    if size != 256:
        raise ValueError ("blue gamma table must contain 256 values")
    retval = dll.SDL_SetWindowGammaRamp (ctypes.byref(window), rptr, gptr, bptr)
    if retval == -1:
        raise SDLError ()

@sdltype("SDL_GetWindowGammaRamp", [ctypes.POINTER(SDL_Window),
                                    ctypes.POINTER(ctypes.c_ushort),
                                    ctypes.POINTER(ctypes.c_ushort),
                                    ctypes.POINTER(ctypes.c_ushort)],
         ctypes.c_int)
def get_window_gamma_ramp (window):
    """
    """
    if not isinstance (window, SDL_Window):
        raise TypeError ("window must be a SDL_Window")
    rtable = (256 * ctypes.c_ushort)()
    gtable = (256 * ctypes.c_ushort)()
    btable = (256 * ctypes.c_ushort)()
    retval = dll.SDL_GetWindowGammaRamp (ctypes.byref(window),
        ctypes.byref(rtable), ctypes.byref(gtable), ctypes.byref(btable))
    if retval == -1:
        raise SDLError ()
    return rtable, gtable, btable

@sdltype("SDL_GL_LoadLibrary", [ctypes.c_char_p], ctypes.c_int)
def gl_load_library (path=None):
    """gl_load_library (path=None) -> bool
    
    Dynamically loads the passed OpenGL library.
    
    if path is None, the default OpenGL library will be loaded.
    """
    if path is not None:
        path = byteify (str (path), "utf-8")
        retval = dll.SDL_GL_LoadLibrary (path)
    else:
        retval = dll.SDL_GL_LoadLibrary (None)
    if retval == -1:
        raise SDLError ()
    return retval == 0

@sdltype("SDL_GL_GetProcAddress", [ctypes.c_char_p], ctypes.c_void_p)
def gl_get_proc_address (proc):
    """
    """
    proc = byteify (str (proc), "utf-8")
    return dll.SDL_GL_GetProcAddress (proc)

@sdltype("SDL_GL_UnloadLibrary", None, None)
def gl_unload_library ():
    """gl_unload_library () -> None
    
    Unloads the library previously loaded with gl_load_library().
    """
    dll.SDL_GL_UnloadLibrary ()

@sdltype("SDL_GL_ExtensionSupported", [ctypes.c_char_p], ctypes.c_int)
def gl_extension_supported (extension):
    """gl_extension_supported (extension) -> bool
    
    Checks, if the passed OpenGL extension is supported by the currently loaded
    OpenGL library.
    """
    extension = byteify (str (extension), "utf-8")
    return dll.SDL_GL_ExtensionSupported (extension) == SDL_TRUE

@sdltype("SDL_GL_SetAttribute", [ctypes.c_int, ctypes.c_int], ctypes.c_int)
def gl_set_attribute (attr, value):
    """gl_set_attribute (attr, value) -> None
    
    Sets an OpenGL attribute for SDL.
    
    The passed attr must be a valid SDL_GL_* constant.
    
    Raises a SDLError, if the attribute could not be set.
    """
    if type (attr) is not int or type (value) is not int:
        raise TypeError ("attr and value must be integer values")
    retval = dll.SDL_GL_SetAttribute (attr, value)
    if retval == -1:
        raise SDLError ()

@sdltype("SDL_GL_GetAttribute", [ctypes.c_int, ctypes.POINTER(ctypes.c_int)],
    ctypes.c_int)
def gl_get_attribute (attr):
    """gl_get_attribute (attr) -> int
    
    Gets the current value for the passed OpenGL attribute.
    
    Raises a SDLError, if an invalid attribute is passed or an error occured.
    """
    if type (attr) is not int:
        raise TypeError ("attr must be an int")
    value = ctypes.c_int (0)
    retval = dll.SDL_GL_GetAttribute (attr, ctypes.byref(value))
    if retval < 0:
        raise SDLError ()
    return value.value

@sdltype("SDL_GL_CreateContext", [ctypes.POINTER(SDL_Window)], ctypes.c_void_p)
def gl_create_context (window):
    """gl_create_context (window) -> ctypes.c_void_p
    
    Creates a new OpenGL context for the specified SDL_Window.

    The SDL_Window must have been created with the SDL_WINDOW_OPENGL flag.

    On failure, a SDLError is raised.
    """
    if not isinstance (window, SDL_Window):
        raise TypeError ("window must be a SDL_Window")
    retval = dll.SDL_GL_CreateContext (ctypes.byref(window))
    if retval is None or not bool (retval):
        raise SDLError ()
    return retval

@sdltype("SDL_GL_DeleteContext", [ctypes.c_void_p], None)
def gl_delete_context (context):
    """gl_delete_context (context) -> None

    Deletes a previously created OpenGL context.
    """
    context = ctypes.c_void_p (context)
    dll.SDL_GL_DeleteContext (context)

@sdltype("SDL_GL_MakeCurrent", [ctypes.POINTER(SDL_Window), ctypes.c_void_p],
    ctypes.c_int)
def gl_make_current (window, context):
    """gl_make_current (window, context) -> None

    Sets up an OpenGL context for rendering into the passed OpenGL window.

    The SDL_Window must have been created with the SDL_WINDOW_OPENGL
    flag.  The passed OpenGL context must have been created with a
    compatible window.

    On failure, a SDLError is raised
    """
    if not isinstance (window, SDL_Window):
        raise TypeError ("window must be a SDL_Window")
    context = ctypes.c_void_p (context)
    retval = dll.SDL_GL_MakeCurrent (ctypes.byref(window), context)
    if retval < 0:
        raise SDLError ()

@sdltype("SDL_GL_SetSwapInterval", [ctypes.c_int], ctypes.c_int)
def gl_set_swap_interval (interval):
    """
    """
    if interval not in (0, 1):
        raise ValueError ("interval must be either 0 or 1")
    retval = dll.SDL_GL_SetSwapInterval (interval)
    if retval == -1:
        raise SDLError ()

@sdltype("SDL_GL_GetSwapInterval", None, ctypes.c_int)
def gl_get_swap_interval (interval):
    """
    """
    retval = dll.SDL_GL_GetSwapInterval ()
    if retval == -1:
        raise SDLError ()
    return retval

@sdltype("SDL_GL_SwapWindow", [ctypes.POINTER(SDL_Window)], None)
def gl_swap_window (window):
    """
    """
    if not isinstance (window, SDL_Window):
        raise TypeError ("window must be a SDL_Window")
    dll.SDL_GL_SwapWindow (ctypes.byref(window))
