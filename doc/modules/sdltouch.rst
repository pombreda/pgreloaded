.. module:: pygame2.sdl.touch
   :synopsis: SDL2 touch wrapper

:mod:`pygame2.sdl.touch` - SDL2 touch wrapper
=============================================

.. class:: SDL_Finger

   TODO

   This wraps `SDL_Finger`.

.. class:: SDL_Touch

   TODO

   This wraps `SDL_Touch`.

.. function:: get_touch(tid : int) -> SDL_Touch

   Gets the touch object at the given id.

   This wraps `SDL_GetTouch`.

.. function:: get_finger(touch : SDL_Touch, fid : int) -> SDL_Finger

   Gets the finger object of the given touch at the given id.
