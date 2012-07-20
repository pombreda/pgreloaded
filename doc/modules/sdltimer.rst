.. module:: pygame2.sdl.timer
   :synopsis: SDL2 timer wrapper

:mod:`pygame2.sdl.timer` - SDL2 timer wrapper
=============================================

.. function:: get_ticks() -> int

   Gets the number of milliseconds since the underlying SDL library was
   initialized.

   .. note::

      This value wraps if the program runs for more than ~49 days.

   This wraps `SDL_GetTicks`.

.. function:: get_performance_counter() -> int

   Gets the current value of the high resolution counter.

   This wraps `SDL_GetPerformanceCounter`.

.. function:: get_performance_frequency() -> int

   Gets the count per second of the high resolution counter.

   This wraps `SDL_GetPerformanceFrequency`.

.. function:: delay(ms : int) -> None

   Wait a specified number of milliseconds before continuing.

   This wraps `SDL_Delay`.

SDL_TimerCallback

.. function:: add_timer(interval : int, callback : SDL_TimerCallback[, \
                        param=None]) -> int

   Adds a new timer to the pool of timers already running. This returns a
   unique id for the timer or raises a :exc:`pygame2.sdl.SDLError` on error.

   .. note::

      You must keep a reference to the passed callback to prevent it from
      being dereferenced.

   This wraps `SDL_AddTimer`.

.. function:: remove_timer(timerid : int) -> bool

   Removes a timer. This will return whether the removal was successful or not.

   This wraps `SDL_RemoveTimer`.
