.. module:: pygame2.sdl.log
   :synopsis: SDL2 logging wrapper

:mod:`pygame2.sdl.log` - SDL2 logging wrapper
=============================================

.. function:: log(text : string) -> None

   Logs a message with ``SDL_LOG_CATEGORY_APPLICATION`` and
   ``SDL_LOG_PRIORITY_INFO``.

   This wraps `SDL_Log`.

.. function:: log_critical(category : int, text : string) -> None

   Logs a message with the chosen *category* ``and SDL_LOG_PRIORITY_CRITICAL``.

   This wraps `SDL_LogCritical`.

.. function:: log_debug(category : int, text : string) -> None

   Logs a message with the chosen *category* and ``SDL_LOG_PRIORITY_DEBUG``.

   This wraps `SDL_LogDebug`.

.. function:: log_error(category : int, text : string) -> None

   Logs a message with the chosen *category* and ``SDL_LOG_PRIORITY_ERROR``.

   This wraps `SDL_LogError`.

.. function:: log_info(category : int, text : string) -> None

   Logs a message with the chosen *category* and ``SDL_LOG_PRIORITY_INFO``.

   This wraps `SDL_LogInfo`.

.. function:: log_verbose(category : int, text : string) -> None

   Logs a message with the chosen *category* and ``SDL_LOG_PRIORITY_VERBOSE``.

   This wraps `SDL_LogVerbose`.

.. function:: log_warn(category : int, text : string) -> None

   Logs a message with the chosen *category* and ``SDL_LOG_PRIORITY_WARN``.

   This wraps `SDL_LogWarn`.

.. function:: log_message(category : int, priority : int, text : string) -> None

   Logs a message with the chosen *category* and *priority*.

   This wraps `SDL_LogMessage`.

.. function:: log_reset_priorities() -> None

   Resets the priorities for all categories to their default values.

   This wraps `SDL_LogResetPriorities`.

.. function:: log_set_all_priority(priority : int) -> None

   Sets the priority of all categories to the passed value.

   This wraps `SDL_LogSetAllPriority`.

.. function:: log_get_priority(category : int) -> int

   Gets the ``SDL_LOG_PRIORITY_*`` value for a specific *category*.

   This wraps `SDL_LogGetPriority`.

.. function:: log_set_priority(category : int, priority : int) -> None

   Sets the priority value for a specific *category*.

   This wraps `SDL_LogSetPriority`.

.. todo::

   SDL_LogOutputFunction

.. function:: log_set_output_function(function : SDL_LogOutputFunction[, \
                                      userdata=None]) -> None

   Sets the output function for the logging methods to the passed
   :func:`SDL_LogOutputFunction`.

   .. note::

      You must keep a reference to the passed function to prevent it from
      getting dereferenced.

   This wraps `SDL_LogSetOutputFunction`.

.. function:: log_get_output_function() -> SDL_LogOutputFunction

   Gets the output function that is currently used for all logging methods.

   This wraps `SDL_LogGetOutputFunction`.
