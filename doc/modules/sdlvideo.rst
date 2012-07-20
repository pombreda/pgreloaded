.. module:: pygame2.sdl.video
   :synopsis: SDL2 video wrapper

:mod:`pygame2.sdl.video` - SDL2 video wrapper
=============================================

.. function:: SDL_WINDOWPOS_UNDEFINED_DISPLAY(x : int) -> int

   TODO

   This wraps `SDL_WINDOWPOS_UNDEFINED_DISPLAY`.

.. function:: SDL_WINDOWPOS_ISUNDEFINED(x : int) -> bool

   TODO

   This wraps `SDL_WINDOWPOS_ISUNDEFINED`.

.. function:: SDL_WINDOWPOS_CENTERED_DISPLAY(x) -> int

   TODO

   This wraps `SDL_WINDOWPOS_CENTERED_DISPLAY`.

.. function:: SDL_WINDOWPOS_ISCENTERED(x : int) -> bool

   TODO

   This wraps `SDL_WINDOWPOS_ISCENTERED`.

.. class:: SDL_DisplayMode(format_=0, w=0, h=0, refresh_rate=0)

   TODO

   .. attribute:: format

      TODO

   .. attribute:: w

      TODO

   .. attribute:: h

      TODO

   .. attribute:: refresh_rate

      TODO

.. class:: SDL_Window()

   TODO

.. function:: create_window(title : string, x : int, y : int, w : int, \
                            h : int, flags : int) -> SDL_Window

   Creates a new SDL window with the specified dimensions and title.

   This wraps `SDL_CreateWindow`.

.. function:: create_window_from(data : ctypes.c_void_p) -> SDL_Window

   TODO

   This wraps `SDL_CreateWindowFrom`.

.. function:: destroy_window(window : SDL_Window) -> None

   Destroys the passed :class:`SDL_Window`.

   This wraps `SDL_DestroyWindow`.

.. function:: disable_screensaver() -> None

   Prevents the screen from being blanked by a screensaver.

   This wraps `SDL_DisableScreenSaver`.

.. function:: enable_screensaver() -> None

   Allows the screen to be blanked by a screensaver.

   This wraps `SDL_EnableScreenSaver`.

.. function:: is_screensaver_enabled() -> bool

   Returns whether the scrensaver is currently enabled.

   This wraps `SDL_IsScreenSaverEnabled`.

.. function:: get_closest_display_mode(displayindex : int, \
                                       mode : SDL_DisplayMode) -> SDL_DisplayMode

   Get the closest match to the requested display mode. The available display
   modes are scanned and the closest mode matching the requested mode and
   returned. The mode format and refresh_rate default to the desktop mode if
   they are 0 in the passed mode. The modes are scanned with size being first
   priority, format being second priority, and finally checking the
   refresh_rate. If no mode could be found, a :exc:`pygame2.sdl.SDLError` is
   raised.

   This wraps `SDL_GetClosestDisplayMode`.

.. function:: get_current_display_mode(displayindex : int) -> SDL_DisplayMode

   Gets the currently active display mode.

   This wraps `SDL_GetCurrentDisplayMode`.

.. function:: get_desktop_display_mode(displayindex : int) -> SDL_DisplayMode

   Gets the currently used desktop display mode.

   This wraps `SDL_GetDesktopDisplayMode`.

.. function:: get_display_bounds(displayindex : int) -> SDL_Rect

   Gets the visible dimensions for a display and its currently used mode.

   This wraps `SDL_GetDisplayBounds`.

.. function:: get_display_mode(displayindex : int, \
                               modeindex : int) -> SDL_DisplayMode

   Retrieves the display mode for a specific display.

   This wraps `SDL_GetDisplayMode`.

.. function:: get_num_display_modes(displayindex : int) -> int

   Retrieves the number of available display modes for a specific display.

   This wraps `SDL_GetNumDisplayModes`.

.. function:: get_num_video_displays() -> int

   Retrieves the number of available video displays.

   This wraps `SDL_GetNumVideoDisplays`.

.. function:: get_num_video_drivers() -> int

   Retrieves the number of available video drivers.

   This wraps `SDL_GetNumVideoDrivers`.

.. function:: get_video_driver(displayindex : int) -> string

   Gets the video driver used by a specific display. If the video driver for
   the display could not be determined, or if an invalid display index is
   used, a :exc:`pygame2.sdl.SDLError` is raised.

   This wraps `SDL_GetVideoDriver`.

.. function:: get_current_video_driver() -> string

   Gets the currently used video driver.

   This wraps `SDL_GetCurrentVideoDriver`.

.. function:: init(drivername=None) -> None

   Initializes the SDL video subsystem with an optionally choosable driver to
   use. This is basically the same as calling ::

     >>> pygame2.sdl.init(pygame2.sdl.SDL_INIT_VIDEO)

   but lets you choose a video driver instead of using the default driver for
   the platform your application is running on.

   This wraps `SDL_VideoInit`.

.. function:: quit() -> None

   Quits the SDL video subsystem. This is similar to calling ::

     >>> pygame2.sdl.quit_subsystem(pygame2.sdl.SDL_INIT_VIDEO)

   This wraps `SDL_VideoQuit`.

.. function:: get_window_display(window : SDL_Window) -> int

   Gets the index of the display, the :class:`SDL_window` is currently shown on.
   If the display could not determined, a :class:`pygame2.sdl.SDLError` is
   raised.

   This wraps `SDL_GetWindowDisplay`.

.. function:: set_window_display_mode(window : SDL_Window[, mode=None]) -> None

   Sets the display mode to be used, if the window is shown in a fullscreen
   mode. If *mode* is omitted, the default display mode for the window is
   used, which usually is the window's dimensions and the desktop format and
   refresh rate. Since certain dimensions cannot be used in fullscreen on a
   display, the default mode for the window might be the lowest or highest
   (or something in between) mode of the display itself.

   This wraps `SDL_SetWindowDisplayMode`.

.. function:: get_window_display_mode(window : SDL_Window) -> SDL_DisplayMode

   Gets the currently used :class:`SDL_DisplayMode` for a *window*. If the
   display mode for the window could not be determined, a
   :exc:`pygame2.sdl.SDLError` is raised.

   This wraps `SDL_GetWindowDisplayMode`.

.. function:: get_window_pixelformat(window : SDL_Window) -> int

   Retrieves the pixel format associated with the window.

   This wraps `SDL_GetWindowPixelFormat`.

.. function:: get_window_id(window : SDL_Window) -> int

   Gets the id of the window.

   This wraps `SDL_GetWindowID`.

.. function:: get_window_from_id(id : int) -> SDL_Window

   Get a SDL_Window from a stored id. If no SDL_Window could be found for the
   passed id, a SDLError is raised.

   This wraps `SDL_GetWindowFromID`.

.. function:: get_window_flags(window : SDL_Window) -> int

   Retrieves the currently applied flags for a specific window.

   This wraps `SDL_GetWindowFlags`.

.. function:: get_window_title(window : SDL_Window) -> string

   Retrieves the title of a SDL_Window.

   This wraps `SDL_GetWindowTitle`.

.. function:: set_window_title(window : SDL_Window, title : string) -> None

   Sets the title to be used by a SDL_Window.

   This wraps `SDL_SetWindowTitle`.

.. function:: set_window_icon(window : SDL_Window, icon : SDL_Surface) -> None

   Sets the icon for the window.

   This wraps `SDL_SetWindowIcon`.

.. function:: set_window_data(window : SDL_Window, name : string, data : object) -> object

   Associate arbitrary content with a window. The passed data will be
   identified by the specified *name*. This will return the previous value.

   .. note::

      You must keep a reference to the passed data to prevent it from being
      GC'd.

   This wraps `SDL_SetWindowData`.

.. function:: get_window_data(window : SDL_Window, name : string) -> object

   Gets associated content from the window. The data to be retrieved is
   identified by the specified name. If there is no data found for *name*,
   ``None`` will be returned.

   This wraps `SDL_GetWindowData`.

.. function:: set_window_position(window : SDL_Window, x : int, y : int) -> None

   Sets the position of the top-left corner of the passed SDL_Window.

   This wraps `SDL_SetWindowPosition`.

.. function:: get_window_position(window) -> int, int

   Gets the current top-left position of the passed SDL_Window as two-value
    tuple.

   This wraps `SDL_GetWindowPosition`.

.. function:: set_window_size(window, w, h) -> None

   Sets the size of the passed SDL_Window.

   This wraps `SDL_SetWindowSize`.

.. function:: get_window_size(window) -> int, int

   Gets the size of the passed SDL_window as two-value tuple.

   This wraps `SDL_GetWindowSize`.

.. function:: show_window(window) -> None

   Shows the passed SDL_Window.

   This wraps `SDL_ShowWindow`.

.. function:: hide_window(window) -> None

   Hides the passed SDL_Window.

   This wraps `SDL_HideWindow`.

.. function:: raise_window(window) -> None

   Raises the passed window above other windows.

   This wraps `SDL_RaiseWindow`.

.. function:: maximize_window(window) -> None

   Tries to maximize the window size to the display extents, but at least
    as large as possible.

   This wraps `SDL_MaximizeWindow`.

.. function:: minimize_window(window) -> None

   Minimizes a window to an iconic representation.

   This wraps `SDL_MinimizeWindow`.

.. function:: restore_window(window) -> None

   Restores the size and position of a minimized or maximized window.

   This wraps `SDL_RestoreWindow`.

.. function:: set_window_fullscreen(window, fullscreen) -> None

   Sets a window's fullscreen state.

   This wraps `SDL_SetWindowFullscreen`.

.. function:: get_window_surface(window) -> SDL_Surface

   Gets the SDL_Surface associated with the passed SDL_Window.

    A new surface will be created with the optimal format for the
    window, if necessary. This surface will be freed when the window is
    destroyed.

    NOTE: You may not combine this with 3D or the rendering API on this
    window.

   This wraps `SDL_GetWindowSurface`.

.. function:: update_window_surface(window) -> None

   Copies the window surface to the screen.

   This wraps `SDL_UpdateWindowSurface`.

.. function:: update_window_surface_rects(window, rects) -> None

   Copies a set of areas of the window surface to the screen.

    The rects argument must be a sequence of SDL_Rect instances.

   This wraps `SDL_UpdateWindowSurfaceRects`.

.. function:: set_window_grab(window, grabbed) -> None

   Sets a window's input grab mode.

    If grabbed is True, the window will grab the input, otherwise, it will
    release the grab.

   This wraps `SDL_SetWindowGrab`.

.. function:: get_window_grab(window) -> bool

   Checks, if input is currently grabbed by the window.

   This wraps `SDL_GetWindowGrab`.

.. function:: set_window_brightness(window, brightness) -> None

   Sets the brightness(gamma correction) for the passed window.

   This wraps `SDL_SetWindowBrightness`.

.. function:: get_window_brightness(window) -> float

   Gets the brightness(gamma correction) of the window.

   This wraps `SDL_GetWindowBrightness`.

.. function:: set_window_gamma_ramp(window, red, green, blue) -> None

   TODO

   This wraps `SDL_SetWindowGammaRamp`.

.. function:: get_window_gamma_ramp(window) -> XX

   TODO

   This wraps `SDL_GetWindowGammaRamp`.

.. function:: gl_load_library(path=None) -> bool

   Dynamically loads the passed OpenGL library.

    if path is None, the default OpenGL library will be loaded.

   This wraps `SDL_GL_LoadLibrary`.

.. function:: gl_get_proc_address(proc) -> ctypes.c_void_p



   This wraps `SDL_GL_GetProcAddress`.

.. function:: gl_unload_library() -> None

   Unloads the library previously loaded with gl_load_library().

   This wraps `SDL_GL_UnloadLibrary`.

.. function:: gl_extension_supported(extension) -> bool

   Checks, if the passed OpenGL extension is supported by the currently
    loaded OpenGL library.

   This wraps `SDL_GL_ExtensionSupported`.

.. function:: gl_set_attribute(attr, value) -> None

   Sets an OpenGL attribute for SDL.

    The passed attr must be a valid SDL_GL_* constant.

   This wraps `SDL_GL_SetAttribute`.

.. function:: gl_get_attribute(attr) -> int

   Gets the current value for the passed OpenGL attribute.

   This wraps `SDL_GL_GetAttribute`.

.. function:: gl_create_context(window) -> ctypes.c_void_p

   Creates a new OpenGL context for the specified SDL_Window.

    The SDL_Window must have been created with the SDL_WINDOW_OPENGL flag.

    On failure, a SDLError is raised.

   This wraps `SDL_GL_CreateContext`.

.. function:: gl_delete_context(context) -> None

   Deletes a previously created OpenGL context.

    Multiple invocations with the same context can lead to undefined
    behaviur, so make sure, you call it only once per context.

   This wraps `SDL_GL_DeleteContext`.

.. function:: gl_make_current(window, context) -> None

   Sets up an OpenGL context for rendering into the passed OpenGL window.

    The SDL_Window must have been created with the SDL_WINDOW_OPENGL
    flag.  The passed OpenGL context must have been created with a
    compatible window.

    On failure, a SDLError is raised

   This wraps `SDL_GL_MakeCurrent`.

.. function:: gl_set_swap_interval(interval) -> None

   Set the swap interval for the current OpenGL context.

    interval can be either 0 for immediate updates or 1 for updates
    synchronized with the vertical retrace.

    Raises a SDLError, if setting the swap interval is not supported.

   This wraps `SDL_GL_SetSwapInterval`.

.. function:: gl_get_swap_interval() -> int

   Gets the swap interval for the current OpenGL context.

    This returns either 0 for immediate updates or 1 if the updates are
    synchronized with the vertical retrace. If getting the swap interval
    is not supported, a SDLError is raised.

   This wraps `SDL_GL_GetSwapInterval`.

.. function:: gl_swap_window(window) -> None

   Swaps the OpenGL buffers for a window, if double-buffering is supported.

   This wraps `SDL_GL_SwapWindow`.
