.. module:: pygame2.sdl.mouse
   :synopsis: SDL2 mouse wrapper

:mod:`pygame2.sdl.mouse` - SDL2 mouse wrapper
=============================================


.. function:: SDL_BUTTON(x : int) -> int

   Creates a bitmask for the ``SDL_BUTTON_`` constants.

   This wraps `SDL_BUTTON`.

.. class:: SDL_Curosr()

   TODO

.. function:: create_color_cursor(surface : SDL_Surface, hotx : int, hoty : int) -> SDL_Cursor

   Creates a cursor from the passed *surface*. If the cursor could not be
   created, a :exc:`pygame2.sdl.SDLError` is raised.

   This wraps `SDL_CreateColorCursor`.

.. function:: create_cursor(data : bytes, mask : bytes, w : int, h : int, \
                            hotx : int, hoty : int) -> SDL_Cursor

   Creates a cursor from the passed black/white *data* and alpha *mask*.

   This wraps `SDL_CreateCursor`.

.. function:: free_cursor(cursor : SDL_Cursor) -> None

   Releases the resources hold by the passed *cursor*.

   This wraps `SDL_FreeCursor`.

.. function:: get_cursor() -> SDL_Cursor

   Retrieves the currently used :class:`SDL_Cursor`.

   This wraps `SDL_GetCursor`.

.. function:: set_cursor(cursor : SDL_Cursor) -> None

   Sets the :class:`SDL_Cursor` to be used by the mouse input device.

   This wraps `SDL_SetCursor`.

.. function:: get_mouse_focus() -> SDL_Window

   Gets the :class:`pygame2.sdl.video.SDL_Window` that currently has the mouse
   input focus.

   This wraps `SDL_GetMouseFocus`.

.. function:: get_mouse_state() -> (int, int, int)

   This retrieves the current mouse button state and its x and y coordinates
   on the currently focused :class:`pygame2.sdl.video.SDL_Window`.
   The mouse button state is a bitmask, which can be tested with
   :func:`SDL_BUTTON()`.

   This wraps `SDL_GetMouseState`.

.. function:: get_relative_mouse_mode() -> bool

   Checks, whether the relative mouse mode is enabled or not.

   This wraps `SDL_GetRelativeMouseMode`.

.. function:: get_relative_mouse_state() -> (int, int, int)

   The current button state is returned as a button bitmask, which can
   be tested using :func:`SDL_BUTTON()`, and x and y are set to the mouse
   deltas since the last call to :func:`get_relative_mouse_state()`.

   This wraps `SDL_GetRelativeMouseState`.

.. function:: set_relative_mouse_mode(enabled : bool) -> None

   Enables or disables the relative mouse mode. While the mouse is in
   relative mode, the cursor is hidden, and the driver will try to report
   continuous motion in the current window. Only relative motion events will
   be delivered, the mouse position will not change.

   .. note::

      This function will flush any pending mouse motion.

   This wraps `SDL_SetRelativeMouseMode`.

.. function:: show_cursor(show : int) -> bool

   Shows, hides or queries the state of the mouse cursor. If *show* is 1
   or ``True``, the cursor will be shown, if it is 0 or ``False``, the
   cursor will be hidden. If *show* is -1, the state of the cursor
   (shown or hidden) will be returned as boolean flag.

   This will always return a bool, indicating whether the cursor is
   shown or hidden.

   This wraps `SDL_ShowCursor`.

.. function:: warp_mouse_in_window(window : SDL_Window, x : int, y : int) -> None

   Moves the mouse to the given position in the specified *window*. If
   *window* is ``None``, the mouse will be moved to the position in the SDL
   window, which currently has the input focus.

   This wraps `SDL_WarpMouseInWindow`.
