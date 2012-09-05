.. module:: pygame2.sdl.haptic
   :synopsis: SDL2 haptic wrapper

:mod:`pygame2.sdl.haptic` - SDL2 haptic wrapper
===============================================

.. class:: SDL_Haptic

   TODO

   This wraps `SDL_Haptic`.

.. class:: SDL_HapticCondition

   TODO

   This wraps `SDL_HapticCondition`.

.. class:: SDL_HapticConstant

   TODO

   This wraps `SDL_HapticConstant`.

.. class:: SDL_HapticCustom

   TODO

   This wraps `SDL_HapticCustom`.

.. class:: SDL_HapticDirection

   TODO

   This wraps `SDL_HapticDirection`.

.. class:: SDL_HapticPeriodic

   TODO

   This wraps `SDL_HapticPeriodic`.

.. class:: SDL_HapticRamp

   TODO

   This wraps `SDL_HapticRamp`.

.. class:: SDL_HapticEffect

   TODO

   This wraps `SDL_HapticEffect`.

.. function:: haptic_close(haptic : SDL_Haptic) -> None

   Closes an open SDL_Haptic device.

   This wraps `SDL_HapticClose`.

.. function:: haptic_destroy_effect(haptic : SDL_Haptic, effectid : int) \
   -> None

   Destroys a haptic effect.

   This wraps `SDL_HapticDestroyEffect`.

.. function:: haptic_effect_supported(haptic : SDL_Haptic, \
   effect : SDL_HapticEffectg) -> bool

   Checks, if the specified effect is supported by the haptic device.

   This wraps `SDL_HapticEffectSupported`.

.. function:: haptic_get_effect_status(haptic : SDL_Haptic, \
   effectid : int) -> int

   Gets the status of a haptic effect.

   This wraps `SDL_HapticGetEffectStatus`.

.. function:: haptic_index(haptic : SDL_Haptic) -> int

   Gets the index of the haptic device

   This wraps `SDL_HapticIndex`.

.. function:: haptic_name(haptic : SDL_Haptic) -> str

   Gets the device name for a specific haptic device.

   This wraps `SDL_HapticName`.

.. function:: haptic_num_axes(haptic : SDL_Haptic) -> int

   Gets the number of axes of the haptic device.

   This wraps `SDL_HapticNumAxes`.

.. function:: haptic_num_effects(haptic : SDL_Haptic) -> int

   Returns the number of effectrs the device can store.

   This wraps `SDL_HapticNumEffects`.

.. function:: haptic_num_effects_playing(haptic : SDL_Haptic) -> int

   Returns the number of effects the device can play at the same time.

   This wraps `SDL_HapticNumEffectsPlaying`.

.. function:: haptic_open(index : int) -> SDL_Haptic

   Opens a haptic device.

   This wraps `SDL_HapticOpen`.

.. function:: haptic_open_from_joystick(joystick : SDL_Joystick) -> SDL_Haptic

   Tries to open the passed :class:`pygame2.sdl.joystick.SDL_Joystick`
   as haptic device.

   This wraps `SDL_HapticOpenFromJoystick`.

.. function:: haptic_open_from_mouse() -> SDL_Haptic

   Tries to open the mouse as haptic device.

   This wraps `SDL_HapticOpenFromMouse`.

.. function:: haptic_opened(index : int) -> bool

   Checks, if a haptic device has been opened.

   This wraps `SDL_HapticOpened`.

.. function:: haptic_pause(haptic : SDL_Haptic) -> None

   Pauses a haptic device.

   This wraps `SDL_HapticPause`.

.. function:: haptic_query(haptic : SDL_Haptic) -> int

   Gets the features supported by the haptic device.

   This wraps `SDL_HapticQuery`.

.. function:: haptic_rumble_init(haptic : SDL_Haptic) -> None

   Initialises a haptic device for rumble playback.

   This wraps `SDL_HapticRumbleInit`.

.. function:: haptic_rumble_play(haptic : SDL_Haptic, strength : float, \
   length : int) -> None

   Plays a rumble on the haptic device.

   This wraps `SDL_HapticRumblePlay`.

.. function:: haptic_rumble_stop(haptic : SDL_Haptic) -> None

   Stops the rumble playback on a haptic device.

   This wraps `SDL_HapticRumbleStop`.

.. function:: haptic_rumble_supported(haptic : SDL_Haptic) -> bool

   Checks, if rumble is supported on the haptic device.

   This wraps `SDL_HapticRumbleSupported`.

.. function:: haptic_run_effect(haptic : SDL_Haptic, effectid : int, \
   iterations : int) -> None

   Runs an effect on the haptic device. If *iterations* is
   `SDL_HAPTIC_INFINITY`, the effect will be run forever.

   This wraps `SDL_HapticRunEffect`.

.. function:: haptic_set_autocenter(haptic : SDL_Haptic, \
   autocenter : int) -> None

   Sets the global autocenter of the haptic device

   This wraps `SDL_HapticAutocenter`.

.. function:: haptic_set_gain(haptic : SDL_Haptic, gain : int) -> None

   Sets the global gain of the haptic device.

   This wraps `SDL_HapticSetGain`.

.. function:: haptic_stop_all(haptic : SDL_Haptic) -> None

   Stops all currently playing effects on a haptic device.

   This wraps `SDL_HapticStopAll`.

.. function:: haptic_stop_effect(haptic : SDL_Haptic, effectid : int) -> None

   Stops a haptic effect.

   This wraps `SDL_HapticStopEffect`.

.. function:: haptic_unpause(haptic : SDL_Haptic) -> None

   Unpauses a haptic device

   This wraps `SDL_HapticUnpause`.

.. function:: joystick_is_haptic(joystick : SDL_Joystick) -> bool

   Checks, if the passed :class:`pygame2.sdl.joystick.SDL_Joystick` has
   haptic capabilities.

   This wraps `SDL_JoystickIsHaptic`.

.. function:: mouse_is_haptic() -> bool

   Checks, if the currently used mouse has haptic capabilities.

   This wraps `SDL_MouseIsHaptic`.

.. function:: num_haptics() -> int

   Gets the number of haptic-aware joysticks attached.

   This wraps `SDL_NumHaptics`.
