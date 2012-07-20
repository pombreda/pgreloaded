.. module:: pygame2.sdl.power
   :synopsis: SDL2 power saving wrapper

:mod:`pygame2.sdl.power` - SDL2 power saving wrapper
====================================================

.. data:: SDL_POWERSTATE_UNKNOWN

   The power supply information could not be obtained.

.. data:: SDL_POWERSTATE_ON_BATTERY

   The system is running on battery.

.. data:: SDL_POWERSTATE_NO_BATTERY

   The system is not running on battery.

.. data:: SDL_POWERSTATE_CHARGING

   The system is currently charging the battery.

.. data:: SDL_POWERSTATE_CHARGED

   The system's battery is fully charged.

.. function:: get_power_info() -> (int, int, int)

   Gets the current power supply information. The returned tuple consists of
   a ``SDL_POWERSTATE_*`` value, the seconds of battery life left (or -1,
   if it can not be determined or is not running on a battery) and the
   percentage of battery life left (again -1, if it can not be determined
   or not running on a battery).

   This wraps `SDL_GetPowerInfo`.
