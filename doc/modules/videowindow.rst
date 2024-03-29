.. module:: pygame2.video.window
   :synopsis: Window routines to manage on-screen windows

:mod:`pygame2.video.window` - Window routines to manage on-screen windows
=========================================================================

.. class:: Window(title : string, size : iterable[, \
                  position=None[, flags=None]])

   The Window class represents a visible on-screen object with an optional
   border and *title* text. It represents an area on the screen that can be
   accessed by the application for displaying graphics and receive and
   process user input.

   The position to show the Window at is undefined by default, letting
   the operating system or window manager pick the best location. The
   behaviour can be adjusted through the ``DEFAULTPOS`` class variable. ::

     Window.DEFAULTPOS = (10, 10)

   The created Window is hidden by default, which can be overriden at
   the time of creation by providing other SDL window flags through the
   *flags* parameter. The default flags for creating Window instances
   can be adjusted through the ``DEFAULTFLAGS`` class variable. ::

     Window.DEFAULTFLAGS = pygame2.sdl.video.SDL_WINDOW_SHOWN

   .. attribute:: window

      The used :class:`pygame2.sdl.video.SDL_Window`.

   .. attribute:: title

      The title of the :class:`Window`.

   .. attribute:: size

      The size of the :class:`Window`.

   .. method:: show() -> None

      Show the :class:`Window` on the display.

   .. method:: hide() -> None

      Hide the :class:`Window`.

   .. method:: maximize() -> None

      Maximizes the :class:`Window` to the display's dimensions.

   .. method:: minimize() -> None

      Minimizes the :class:`Window` to an iconified state in the system tray.

   .. method:: refresh() -> None

      Refreshes the entire :class:`Window` surface.

      .. note::

         This only needs to be called, if a SDL_Surface was acquired via
         get_surface() and is used to display contents.

   .. method:: get_surface() -> SDL_Surface

      Gets the :class:`pygame2.sdl.surface.SDL_Surface` used by the
      :class:`Window` to display 2D pixel data.

      .. note::

         Using this method will make the usage of GL operations, such as
         texture handling or the usage of SDL renderers impossible.
