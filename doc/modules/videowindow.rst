.. module:: pygame2.video.window
   :synopsis: Window routines to manage on-screen windows

:mod:`pygame2.video.window` - Window routines to manage on-screen windows
=========================================================================

.. class:: Window(title : string, size : iterable[, \
                  position=(0, 0)[, flags=None]])
   
   The Window class represents a visible on-screen object with an optional
   border and *title* text. It represents an area on the screen that can be
   accessed by the application for displaying graphics and receive and
   process user input.
   
   The created Window is hidden by default, which can be overriden at the
   time of creation by providing other SDL window flags through the *flags*
   parameter. The default flags for creating Window instances can be
   adjusted through the ``DEFAULTFLAGS`` class variable. ::

     Window.DEFAULTFLAGS = pygame2.sdl.video.SDL_WINDOW_SHOWN

   .. attribute:: window
   
      The used :class:`pygame2.sdl.video.SDL_Window`.
      
   .. attribute:: title
   
      The title of the :class:`Window`.
   
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
   
   .. method:: get_surface() -> SDL_Surface
   
      Gets the :class:`pygame2.sdl.surface.SDL_Surface` used by the
      :class:`Window` to display 2D pixel data.
      
      .. note::
         
         Using this method will make the usage of GL operations, such as
         texture handling or the usage of SDL renderers impossible.
