.. module:: pygame2.sdl.shape
   :synopsis: SDL2 shaping wrapper

:mod:`pygame2.sdl.shape` - SDL2 shaping wrapper
===============================================

.. function:: SDL_SHAPEMODEALPHA(mode) -> bool

   Checks, if the passed shape mode supports alpha transparency.

   This wraps `SDL_SHAPEMODEALPHA`.

.. class:: SDL_WindowShapeParams()

   TODO

   .. attribute:: binarizationCutoff

      TODO

   .. attribute:: colorKey

      TODO

.. class:: SDL_WindowShapeMode()

   TODO

   .. attribute:: mode

      TODO

   .. attribute:: parameters

      TODO

.. function:: create_shaped_window(title : string, x : int, y : int, \
                                   w : int, h : int, flags : int) -> SDL_Window

   Create a window that can be shaped with the specified position, dimension
   and flags.

   TODO

   This wraps `SDL_CreateShapedWindow`.

.. function:: is_shaped_window(window : SDL_Window) -> bool

   Checks if the passed *window* is a shaped window.

   This wraps `SDL_IsShapedWindow`.

.. function:: set_window_shape(window : SDL_Window, surface : SDL_Surface, \
                               shapemode : SDL_WindowShapeMode) -> None

   Sets the shape parameters of a shaped window.

   This wraps `SDL_SetWindowShape`.

.. function:: get_shaped_window_mode(window : SDL_Window) -> SDL_WindowShapeMode

   Gets the shape parameters from a shaped window.

   This wraps `SDL_GetShapedWindowMode`.
