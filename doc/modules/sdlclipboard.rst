.. module:: pygame2.sdl.clipboard
   :synopsis: SDL2 Clipboard wrapper

:mod:`pygame2.sdl.clipboard` - SDL2 Clipboard wrapper
=====================================================

.. function:: get_clipboard_text() -> string

   Retrieves text from the OS clipboard, if available.

   .. note::

      This might leak memory.

   This wraps :c:func:`SDL_GetClipboardText`.

.. function:: has_clipboard_text() -> bool

   Checks, if text is available on the OS clipboard.

   This wraps :c:func:`SDL_HasClipboardText`.

.. function:: set_clipboard_text(text : string) -> None

   Puts text on the OS clipboard. This raises a
   :exc:`pygame2.sdl.SDLError`, if the operation was not successful.

   This wraps :c:func:`SDL_SetClipboardText`.
