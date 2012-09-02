"""
Wrapper methods around the SDL2 log handling routines.
"""
import ctypes
from pygame2.compat import byteify
from pygame2.sdl import sdltype, dll

__all__ = ["log", "log_critical", "log_debug", "log_error", "log_info",
           "log_verbose", "log_warn", "log_message", "log_reset_priorities",
           "log_set_all_priority", "log_get_priority", "log_set_priority",
           "SDL_LogOutputFunction", "log_set_output_function",
           "log_get_output_function"
           ]

SDL_LOG_CATEGORY_APPLICATION = 0
SDL_LOG_CATEGORY_ERROR       = 1
SDL_LOG_CATEGORY_SYSTEM      = 2
SDL_LOG_CATEGORY_AUDIO       = 3
SDL_LOG_CATEGORY_VIDEO       = 4
SDL_LOG_CATEGORY_RENDER      = 5
SDL_LOG_CATEGORY_INPUT       = 6
# 10 reserved ones
SDL_LOG_CATEGORY_CUSTOM      = 17
_ALLOWED_CATEGORIES = (
    SDL_LOG_CATEGORY_APPLICATION,
    SDL_LOG_CATEGORY_ERROR,
    SDL_LOG_CATEGORY_SYSTEM,
    SDL_LOG_CATEGORY_AUDIO,
    SDL_LOG_CATEGORY_VIDEO,
    SDL_LOG_CATEGORY_RENDER,
    SDL_LOG_CATEGORY_INPUT,
    SDL_LOG_CATEGORY_CUSTOM
    )

SDL_LOG_PRIORITY_VERBOSE  = 1
SDL_LOG_PRIORITY_DEBUG    = 2
SDL_LOG_PRIORITY_INFO     = 3
SDL_LOG_PRIORITY_WARN     = 4
SDL_LOG_PRIORITY_ERROR    = 5
SDL_LOG_PRIORITY_CRITICAL = 6
_ALLOWED_PRIORITIES = (
    SDL_LOG_PRIORITY_VERBOSE,
    SDL_LOG_PRIORITY_DEBUG,
    SDL_LOG_PRIORITY_INFO,
    SDL_LOG_PRIORITY_WARN,
    SDL_LOG_PRIORITY_ERROR,
    SDL_LOG_PRIORITY_CRITICAL
)


@sdltype("SDL_Log", [ctypes.c_char_p], None)
def log(text):
    """Logs a message with SDL_LOG_CATEGORY_APPLICATION and
    SDL_LOG_PRIORITY_INFO.
    """
    dll.SDL_Log(byteify(str(text), "utf-8"))
SDL_log = log


@sdltype("SDL_LogCritical", [ctypes.c_int, ctypes.c_char_p], None)
def log_critical(category, text):
    """Logs a message with the chosen category and SDL_LOG_PRIORITY_CRITICAL.
    """
    if type(category) is not int:
        raise TypeError("category must be a valid SDL_LOG_CATEGORY value")
    if category not in _ALLOWED_CATEGORIES:
        raise ValueError("category must be a valid SDL_LOG_CATEGORY value")
    dll.SDL_LogCritical(category, byteify(str(text), "utf-8"))


@sdltype("SDL_LogDebug", [ctypes.c_int, ctypes.c_char_p], None)
def log_debug(category, text):
    """Logs a message with the chosen category and SDL_LOG_PRIORITY_DEBUG."""
    if type(category) is not int:
        raise TypeError("category must be a valid SDL_LOG_CATEGORY value")
    if category not in _ALLOWED_CATEGORIES:
        raise ValueError("category must be a valid SDL_LOG_CATEGORY value")
    dll.SDL_LogDebug(category, byteify(str(text), "utf-8"))


@sdltype("SDL_LogError", [ctypes.c_int, ctypes.c_char_p], None)
def log_error(category, text):
    """Logs a message with the chosen category and SDL_LOG_PRIORITY_ERROR."""
    if type(category) is not int:
        raise TypeError("category must be a valid SDL_LOG_CATEGORY value")
    if category not in _ALLOWED_CATEGORIES:
        raise ValueError("category must be a valid SDL_LOG_CATEGORY value")
    dll.SDL_LogError(category, byteify(str(text), "utf-8"))


@sdltype("SDL_LogInfo", [ctypes.c_int, ctypes.c_char_p], None)
def log_info(category, text):
    """Logs a message with the chosen category and SDL_LOG_PRIORITY_INFO."""
    if type(category) is not int:
        raise TypeError("category must be a valid SDL_LOG_CATEGORY value")
    if category not in _ALLOWED_CATEGORIES:
        raise ValueError("category must be a valid SDL_LOG_CATEGORY value")
    dll.SDL_LogInfo(category, byteify(str(text), "utf-8"))


@sdltype("SDL_LogVerbose", [ctypes.c_int, ctypes.c_char_p], None)
def log_verbose(category, text):
    """Logs a message with the chosen category and SDL_LOG_PRIORITY_VERBOSE.
    """
    if type(category) is not int:
        raise TypeError("category must be a valid SDL_LOG_CATEGORY value")
    if category not in _ALLOWED_CATEGORIES:
        raise ValueError("category must be a valid SDL_LOG_CATEGORY value")
    dll.SDL_LogVerbose(category, byteify(str(text), "utf-8"))


@sdltype("SDL_LogWarn", [ctypes.c_int, ctypes.c_char_p], None)
def log_warn(category, text):
    """Logs a message with the chosen category and SDL_LOG_PRIORITY_WARN."""
    if type(category) is not int:
        raise TypeError("category must be a valid SDL_LOG_CATEGORY value")
    if category not in _ALLOWED_CATEGORIES:
        raise ValueError("category must be a valid SDL_LOG_CATEGORY value")
    dll.SDL_LogWarn(category, byteify(str(text), "utf-8"))


@sdltype("SDL_LogMessage", [ctypes.c_int, ctypes.c_int, ctypes.c_char_p], None)
def log_message(category, priority, text):
    """Logs a message with the chosen category and priority."""
    if type(category) is not int:
        raise TypeError("category must be a valid SDL_LOG_CATEGORY value")
    if category not in _ALLOWED_CATEGORIES:
        raise ValueError("category must be a valid SDL_LOG_CATEGORY value")
    if type(priority) is not int:
        raise TypeError("priority must be a valid SDL_LOG_PRIORITY value")
    if priority not in _ALLOWED_PRIORITIES:
        raise ValueError("priority must be a valid SDL_LOG_PRIORITY value")
    dll.SDL_LogMessage(category, priority, byteify(str(text), "utf-8"))


@sdltype("SDL_LogResetPriorities", None, None)
def log_reset_priorities():
    """Resets the priorities for all categories to their default values."""
    dll.SDL_LogResetPriorities()


@sdltype("SDL_LogSetAllPriority", [ctypes.c_int], None)
def log_set_all_priority(priority):
    """Sets the priority of all categories to the passed value."""
    if type(priority) is not int:
        raise TypeError("priority must be a valid SDL_LOG_PRIORITY value")
    if priority not in _ALLOWED_PRIORITIES:
        raise ValueError("priority must be a valid SDL_LOG_PRIORITY value")
    dll.SDL_LogSetAllPriority(priority)


@sdltype("SDL_LogGetPriority", [ctypes.c_int], ctypes.c_int)
def log_get_priority(category):
    """Gets the SDL_LOG_PRIORITY_* value for a specific category."""
    if type(category) is not int:
        raise TypeError("category must be a valid SDL_LOG_CATEGORY value")
    if category not in _ALLOWED_CATEGORIES:
        raise ValueError("category must be a valid SDL_LOG_CATEGORY value")
    return dll.SDL_LogGetPriority(category)


@sdltype("SDL_LogSetPriority", [ctypes.c_int, ctypes.c_int], None)
def log_set_priority(category, priority):
    """Sets the priority value for a specific category."""
    if type(category) is not int:
        raise TypeError("category must be a valid SDL_LOG_CATEGORY value")
    if category not in _ALLOWED_CATEGORIES:
        raise ValueError("category must be a valid SDL_LOG_CATEGORY value")
    if type(priority) is not int:
        raise TypeError("priority must be a valid SDL_LOG_PRIORITY value")
    if priority not in _ALLOWED_PRIORITIES:
        raise ValueError("priority must be a valid SDL_LOG_PRIORITY value")
    dll.SDL_LogSetPriority(category, priority)


SDL_LogOutputFunction = ctypes.CFUNCTYPE(None, ctypes.py_object, ctypes.c_int,
                                         ctypes.c_int, ctypes.c_char_p)


@sdltype("SDL_LogSetOutputFunction", [SDL_LogOutputFunction, ctypes.py_object],
         None)
def log_set_output_function(function, userdata=None):
    """Sets the output function for the logging methods to the passed
    SDL_LogOutputFunction.

    NOTE: You must keep a reference to the passed function to prevent
    it from getting dereferenced.
    """
    if userdata is not None:
        userdata = ctypes.py_object(userdata)
    if function is not None:
        # Preserve the pointer, so it does not get GC'd
        function._userdata = userdata
    else:
        function = SDL_LogOutputFunction()
    dll.SDL_LogSetOutputFunction(function, userdata)


@sdltype("SDL_LogGetOutputFunction", [ctypes.POINTER(SDL_LogOutputFunction),
                                      ctypes.POINTER(ctypes.py_object)], None)
def log_get_output_function():
    """Gets the output function that is currently used for all logging methods.
    """
    obj = ctypes.py_object()
    function = SDL_LogOutputFunction()
    dll.SDL_LogGetOutputFunction(ctypes.byref(function), ctypes.byref(obj))
    if not bool(obj):
        return function, None
    return function, obj.value
