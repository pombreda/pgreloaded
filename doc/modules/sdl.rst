.. module:: pygame2.sdl
   :synopsis: SDL2 library wrapper

:mod:`pygame2.sdl` - SDL2 library wrapper
=========================================

The :mod:`pygame2.sdl` module is a :mod:`ctypes`-based wrapper around
the SDL2 library. It wraps nearly all publicly accessible structures and
functions of the SDL2 library to be accessible from Python code.

A detailled documentation about the behaviour of the different functions
can found within the SDL2 documentation. The API documentation of
:mod:`pygame2.sdl` will focus on a brief description and outlines
noteworthy specialities or - where necessary - differences for Python.


Submodules
----------

.. toctree::
   :maxdepth: 1

   sdlaudio.rst
   sdlclipboard.rst
   sdlcpuinfo.rst
   sdlendian.rst
   sdlevents.rst
   sdlhints.rst
   sdljoystick.rst
   sdlkeyboard.rst
   sdllog.rst
   sdlmouse.rst
   sdlpixels.rst
   sdlplatform.rst
   sdlpower.rst
   sdlrect.rst
   sdlrender.rst
   sdlshape.rst
   sdlsurface.rst
   sdltimer.rst
   sdlversion.rst
   sdlvideo.rst

SDL2 API
--------

.. function:: get_dll_file() -> string

   Gets the name of the loaded SDL2 dll file.

.. function:: init(flags=None) -> int

   Initializes the SDL library using the passed bit-wise combination of
   SDL subsystems defined through the ``SDL_INIT_`` constants.

   Legal values are:

   * ``SDL_INIT_TIMER`` - Initializes the timer module
   * ``SDL_INIT_AUDIO`` - Initializes the audio module
   * ``SDL_INIT_VIDEO`` - Initializes the video module
   * ``SDL_INIT_JOYSTICK`` - Initializes the joystick module
   * ``SDL_INIT_HAPTIC`` - Initializes force-feedback support for joysticks
   * ``SDL_INIT_EVERYTHING`` - Initializes all modules from above
   * ``SDL_INIT_NOPARACHUTE`` - Deactivates the interrupt wrappers (e.g. for SIGINT, SIGSEGV, etc.)

   This wraps :c:func:`SDL_Init()`.

.. function:: init_subsystem(flags : int) -> int

    Similar to init(), but can be called to explicitly initialize a certain
    module. init() needs to be called beforehand.

    This wraps :c:func:`SDL_InitSubSystem()`.

.. function:: quit_subsystem(flags : int) -> None

   Quits a specific module of SDL, leaving the rest intact.

   This wraps :c:func:`SDL_QuitSubSystem()`.

.. function:: was_init(flags : int) -> int

   Returns a bitmask of the subsystems that were previously initialized.

   This wraps :c:func:`SDL_WasInit()`.

.. function:: quit() -> None

   Shuts down the SDL library and releases all resources hold by it.

   .. note::

      Calling SDL related methods after quit() will wake the dragons, so
      do not do it.

   This wraps :c:func:`SDL_Quit()`.

.. function:: free(val : object) -> None

   Frees memory hold by a SDL resource.

   This wraps :c:func:`SDL_Free()`.

.. function:: get_error() -> string

   Gets the last SDL-related error message that occured.

   This wraps :c:func:`SDL_GetError()`.

.. function:: set_error(text : string) -> None

   Sets a SDL error message that can be retrieved using :func:`get_error()`.
   This wraps :c:func:`SDL_SetError`.

.. function:: clear_error() -> None

   Clears the current error message so that :func:`get_error()` will return an
   empty string.

   This wraps :c:func:`SDL_ClearError()`.

.. exception:: SDLError(msg=None)

   A SDL specific exception class. If no msg is provided, the message
   will be set to the value of :func:`get_error()`.
