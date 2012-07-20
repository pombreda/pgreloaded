.. module:: pygame2.sdl.joystick
   :synopsis: SDL2 joystick wrapper

:mod:`pygame2.sdl.joystick` - SDL2 joystick wrapper
===================================================

.. class:: SDL_Joystick()

   TODO

.. function:: joystick_open(index : int) -> SDL_Joystick

   Opens the joystick specified by the passed *index*. If the *index* is not
   in the range of :func:`joystick_num_joysticks()`, a
   :exc:`pygame2.sdl.SDLError` is raised.

   This wraps `SDL_JoystickOpen`.

.. function:: joystick_opened(index : int) -> bool

   Checks, if the joystick spcified by *index* has been opened.

   If *index* is not an integer, a TypeError is raised. If the *index*
   is not in the range of :func:`joystick_num_joysticks()`, a
   :exc:`pygame2.sdl.SDLError` is raised.

   This wraps `SDL_JoystickOpened`.

.. function:: joystick_close(joystick : SDL_Joystick) -> None

   Closes the passed joystick.

   This wraps `SDL_JoystickClose`.

.. function:: joystick_event_state(state : int) -> int

   Enables or disables joystick event polling.

   If joystick events are disabled by ``SDL_IGNORE``, you must call
   :func:`joystick_update()` yourself and check the state of the joystick, when
   you want to retrieve its current status information.

   If state is ``SDL_ENABLE``, joystick events will be enabled and passed
   to the event queue, where you can process them through the
   :mod:`pygame2.sdl.events` module.

   If state is ``SDL_QUERY`` (or if you pass any other value), the current
   event handling state (``SDL_IGNORE`` or ``SDL_ENABLE``) will be returned.

   This wraps `SDL_JoystickEventState`.

.. function:: joystick_get_axis(joystick : SDL_Joystick, axis : int) -> int

   Gets the current state value of a joystick axis control. The state value
   will be in the range [-32768;32768].

   This wraps `SDL_JoystickGetAxis`.

.. function:: joystick_get_ball(joystick : SDL_Joystick, ball : int) -> (int, int)

   Gets the ball axis change since the last poll.

   This wraps `SDL_JoystickGetBall`.

.. function:: joystick_get_button(joystick : SDL_Joystick, button : int) -> bool

   Gets the current state of a joystick button. Returns ``True``, if the
   button is pressed, ``False`` otherwise.

   This wraps `SDL_JoystickGetButton`.

.. function:: joystick_get_hat(joystick : SDL_Joystick, hat : int) -> int

   Gets the current state of a joystick POV hat. The return value is one of
   the ``SDL_HAT_*`` positions.

   This wraps `SDL_JoystickGetHat`.

.. function:: joystick_index(joystick : SDL_Joystick) -> int

   Retrieves the device index of the passed joystick.

   This wraps `SDL_JoystickIndex`.

.. function:: joystick_name(index : int) -> string

   Retrieves the device name of the joystick at the specific index. If the
   *index* is not in the range of :func:`joystick_num_joysticks()`, a
   :exc:`pygame2.sdl.SDLError` is raised.

   This wraps `SDL_JoystickName`.

.. function:: joystick_num_axes(joystick : SDL_Joystick) -> int

   Gets the number of available axes for the joystick.

   This wraps `SDL_JoystickNumAxes`.

.. function:: joystick_num_balls(joystick : SDL_Joystick) -> int

   Gets the number of available balls for the joystick.

   This wraps `SDL_JoystickNumBalls`.

.. function:: joystick_num_buttons(joystick : SDL_Joystick) -> int

   Gets the number of available buttons for the joystick.

   This wraps `SDL_JoystickNumButtons`.

.. function:: joystick_num_hats(joystick : SDL_Joystick) -> int

   Gets the number of available hats for the joystick.

   This wraps `SDL_JoystickNumHats`.

.. function:: joystick_update() -> None

   Update the current state of open joysticks. This is called automatically by
   the event loop, if any joystick events are enabled.

   This wraps `SDL_JoystickUpdate`.

.. function:: joystick_num_joysticks() -> int

   Retrieves the amount of available joysticks connected to the system.

   This wraps `SDL_NumJoysticks`.
