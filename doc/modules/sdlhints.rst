.. module:: pygame2.sdl.hints
   :synopsis: SDL2 hinting wrapper

:mod:`pygame2.sdl.hints` - SDL2 hinting wrapper
===============================================

.. function:: clear_hints() -> None

   Clears all set hints.

   This wraps `SDL_ClearHints`.

.. function:: get_hint(name : string) -> string

   Gets the currently set value for the passed hint.

   This wraps `SDL_GetHint`.

.. function:: set_hint(name : string, value : string) -> int

   Sets the value of a specific hint.

   This wraps `SDL_SetHint`.

.. function:: set_hint_with_priority(name : string, value : string, \
                                     priority : int) -> int

   Sets the value of a specific hint using a priority override. The hint
   priority can be one of

   * SDL_HINT_DEFAULT
   * SDL_HINT_NORMAL
   * SDL_HINT_OVERRIDE

   This wraps `SDL_SetHintWithPriority`.
