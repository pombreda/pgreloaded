.. module:: pygame2.sdl.syswm
   :synopsis: SDL2 SysWM wrapper

:mod:`pygame2.sdl.syswm` - SDL2 SysWM wrapper
=============================================

.. class:: SDL_SysWMmsg()

   System specific window management message for
   :class:`pygame2.sdl.events.SDL_SysWMEvent`.

   This wraps `SDL_SysWMmsg`.

.. class:: SDL_SysWMinfo()

   System specific window manager information.

   This wraps `SDL_SysWMinfo`.

.. function:: get_window_wm_info(window : SDL_Window) -> SDL_SysWMinfo

   Retrieves driver-dependent window information.

   This wraps `SDL_GetWindowWMInfo`.
