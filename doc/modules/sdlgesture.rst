.. module:: pygame2.sdl.gesture
   :synopsis: SDL2 gesture wrapper

:mod:`pygame2.sdl.gesture` - SDL2 gesture wrapper
=================================================

.. function:: record_gesture(touchid : int) -> None

   Records a gesture on the specified touch. If *touchid* is -1, the
   gesture will be recored on all touches.

   This wraps `SDL_RecordGesture`.

.. function:: save_all_dollar_templates(src : SDL_RWops) -> None

   Saves all currently loaded Dollar Gesture templates.

   This wraps `SDL_SaveAllDollarTemplates`.

.. function:: save_dollar_template(gestureid : int, src : SDL_RWops) -> None

   Saves a currently loaded Dollar Gesture template.

   This wraps `SDL_SaveDollarTemplate`.

.. function:: load_dollar_templates(touchid : int, src : SDL_RWops) -> None

    Loads Dollar Gesture templates from a source.

    This wraps `SDL_LoadDollarTemplates`.
