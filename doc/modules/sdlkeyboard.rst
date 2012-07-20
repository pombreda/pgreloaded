.. module:: pygame2.sdl.keyboard
   :synopsis: SDL2 keyboard wrapper

:mod:`pygame2.sdl.keyboard` - SDL2 keyboard wrapper
===================================================

.. class:: SDL_Keysym([scancode=0[, sym=0[, mod=0[, unicode='\0']]]])

   A key symbol class

   This wraps `SDL_Keysym`.

   .. attribute:: scancode

      TODO

   .. attribute:: sym

      TODO

   .. attribute:: mod

      TODO

   .. attribute:: unicode

      Gets the unicode value of the key symbol.

.. function:: get_keyboard_focus() -> SDL_Window

   Gets the :class:`pygame2.sdl.video.SDL_Window` that currently has the
   keyboard input focus. If window has the keyboard input focus, ``None`` will
   be returned.

   This wraps `SDL_GetKeyboardFocus`.

.. function:: get_keyboard_state() -> (int, int, int, ...)

   Gets a snapshot of the current keyboard state. This will return a tuple
   with :data:`pygame2.sdl.scancode.SDL_NUM_SCANCODES` entries of either
   0 or 1. For each available scancode, a corresponding entry in the tuple
   will be set to either 1, indicating a pressed key or 0, if the
   corresponding key is not pressed.

   This wraps `SDL_GetKeyboardState`.

.. function:: get_key_from_name(name : string) -> int

   Retrieves the key code from the passed name. If no matching key code could
   be found, SDLK_UNKNOWN will be returned.

   This wraps `SDL_GetKeyFromName`.

.. function:: get_key_from_scancode(code : int) -> int

   Retrieves the key code from the passed scancode. If no matching key code
   could be found, SDLK_UNKNOWN will be returned.

   This wraps `SDL_GetKeyFromScancode`.

.. function:: get_key_name(key : int) -> string

   Retrieves the name of the passed key code. If the passed value does not
   have a name, an empty string is returned.

   This wraps `SDL_GetKeyName`.

.. function:: get_mod_state() -> int

   Gets the current key modifier state for the keyboard.

   This wraps `SDL_GetModState`.

.. function:: get_scancode_from_key(key : int) -> int

   Retrieves the scancode for the passed key. If no matching scancode could
   be found, SDL_SCANCODE_UNKNOWN will be returned.

   This wraps `SDL_GetScancodeFromKey`.

.. function:: get_scancode_from_name(name : string) -> int

   Retrieves the scancode for the passed key name.

   This wraps `SDL_GetScancodeFromName`.

.. function:: get_scancode_name(code : int) -> string

   Retrieves the name of the passed scancode. If the passed value does not
   have a name, an empty string is returned.

   This wraps `SDL_GetScancodeName`.

.. function:: set_mod_state(mod : int) -> None

   Set the current key modifier state for the keyboard. This does not really
   change the keyboard state, but only the internally maintained flags.

.. function:: set_text_input_rect(rect : SDL_Rect) -> None

   Sets the text input area to the specified value.

.. function:: start_text_input() -> None

   Causes the event system to raise SDL_TEXTINPUT events on keyboard presses.

   This wraps `SDL_StartTextInput`.

.. function:: stop_text_input() -> None

   Causes the event system to stop raising SDL_TEXTINPUT events on keyboard
   presses.

   This wraps `SDL_StopTextInput`.
