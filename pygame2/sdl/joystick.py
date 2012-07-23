"""
Wrapper methods around the SDL2 joystick routines.
"""
import ctypes
from pygame2.compat import *
from pygame2.sdl import sdltype, dll, SDLError

__all__ = ["SDL_Joystick", "joystick_open", "joystick_opened",
           "joystick_close", "joystick_event_state", "joystick_get_axis",
           "joystick_get_ball", "joystick_get_button", "joystick_get_hat",
           "joystick_index", "joystick_name", "joystick_num_axes",
           "joystick_num_balls", "joystick_num_buttons", "joystick_num_hats",
           "joystick_update", "joystick_num_joysticks"
           ]


SDL_HAT_CENTERED  = 0x00
SDL_HAT_UP        = 0x01
SDL_HAT_RIGHT     = 0x02
SDL_HAT_DOWN      = 0x04
SDL_HAT_LEFT      = 0x08
SDL_HAT_RIGHTUP   = SDL_HAT_RIGHT | SDL_HAT_UP
SDL_HAT_RIGHTDOWN = SDL_HAT_RIGHT | SDL_HAT_DOWN
SDL_HAT_LEFTUP    = SDL_HAT_LEFT | SDL_HAT_UP
SDL_HAT_LEFTDOWN  = SDL_HAT_LEFT | SDL_HAT_DOWN


class _balldelta(ctypes.Structure):
    _fields_ = [("dx", ctypes.c_int), ("dy", ctypes.c_int)]


class SDL_Joystick(ctypes.Structure):
    _fields_ = [("_index", ctypes.c_ubyte),
                ("_name", ctypes.c_char_p),
                ("_naxes", ctypes.c_int),
                ("_axes", ctypes.POINTER(ctypes.c_short)),
                ("_nhats", ctypes.c_int),
                ("_hats", ctypes.POINTER(ctypes.c_ubyte)),
                ("_nballs", ctypes.c_int),
                ("_balls", ctypes.POINTER(_balldelta)),
                ("_nbuttons", ctypes.c_int),
                ("_buttons", ctypes.c_ubyte),
                ("_hwdata", ctypes.c_void_p),
                ("_ref_count", ctypes.c_int),
                ]


@sdltype("SDL_JoystickOpen", [ctypes.c_int], ctypes.POINTER(SDL_Joystick))
def joystick_open(index):
    """Opens the joystick specified by the passed index.

    If index is not an integer, a TypeError is raised. If the index is
    not in the range of joystick_num_joysticks(), a SDLError is raised.
    """
    if type(index) is not int:
        raise TypeError("index must be an int")
    retval = dll.SDL_JoystickOpen(index)
    if retval is None or not bool(retval):
        raise SDLError()
    return retval.contents


@sdltype("SDL_JoystickOpened", [ctypes.c_int], ctypes.c_int)
def joystick_opened(index):
    """Checks, if the joystick spcified by index has been opened.

    If index is not an integer, a TypeError is raised. If the index is
    not in the range of joystick_num_joysticks(), a SDLError is raised.
    """
    if type(index) is not int:
        raise TypeError("index must be an int")
    retval = dll.SDL_JoystickOpened(index)
    if retval < 0:
        raise SDLError()
    return retval == 1


@sdltype("SDL_JoystickClose", [ctypes.POINTER(SDL_Joystick)], None)
def joystick_close(joystick):
    """Closes the passed joystick."""
    if not isinstance(joystick, SDL_Joystick):
        raise TypeError("joystick must be a SDL_Joystick")
    return dll.SDL_JoystickClose(ctypes.byref(joystick))


@sdltype("SDL_JoystickEventState", [ctypes.c_int], ctypes.c_int)
def joystick_event_state(state):
    """Enables or disables joystick event polling.

    If joystick events are disabled by SDL_IGNORE, you must call
    joystick_update() yourself and check the state of the joystick, when
    you want to retrieve its current status information.

    If state is SDL_ENABLE, joystick events will be enabled and passed
    to the event queue, where you can process them through the
    pygame2.sdl.events module.

    If state is SDL_QUERY(or if you pass any other value), the current
    event handling state(SDL_IGNORE or SDL_ENABLE) will be returned.
    """
    retval = dll.SDL_JoystickEventState(state)
    if retval < 0:
        raise SDLError()
    return retval


@sdltype("SDL_JoystickGetAxis", [ctypes.POINTER(SDL_Joystick), ctypes.c_short],
         ctypes.c_short)
def joystick_get_axis(joystick, axis):
    """Gets the current state value of a joystick axis control.

    The state value will be in the range [-32768;32768]
    """
    if not isinstance(joystick, SDL_Joystick):
        raise TypeError("joystick must be a SDL_Joystick")
    if type(axis) is not int:
        raise TypeError("axis must be an int")
    ret = dll.SDL_JoystickGetAxis(ctypes.byref(joystick), axis)
    return ret


@sdltype("SDL_JoystickGetBall", [ctypes.POINTER(SDL_Joystick), ctypes.c_int,
                                 ctypes.POINTER(ctypes.c_int),
                                 ctypes.POINTER(ctypes.c_int)], ctypes.c_int)
def joystick_get_ball(joystick, ball):
    """Gets the ball axis change since the last poll."""
    if not isinstance(joystick, SDL_Joystick):
        raise TypeError("joystick must be a SDL_Joystick")
    if type(ball) is not int:
        raise TypeError("ball must be an int")
    dx = ctypes.c_int(0)
    dy = ctypes.c_int(0)
    ret = dll.SDL_JoystickGetBall(ctypes.byref(joystick), ball,
                                   ctypes.byref(dx), ctypes.byref(dy))
    if ret < 0:
        raise SDLError()
    return dx.value, dy.value


@sdltype("SDL_JoystickGetButton", [ctypes.POINTER(SDL_Joystick),
                                   ctypes.c_uint], ctypes.c_ubyte)
def joystick_get_button(joystick, button):
    """Gets the current state of a joystick button.

    Returns True, if the button is pressed, False otherwise.
    """
    if not isinstance(joystick, SDL_Joystick):
        raise TypeError("joystick must be a SDL_Joystick")
    if type(button) is not int:
        raise TypeError("button must be an int")
    ret = dll.SDL_JoystickGetButton(ctypes.byref(joystick), button)
    if ret < 0:
        raise SDLError()
    return ret == 1


@sdltype("SDL_JoystickGetHat", [ctypes.POINTER(SDL_Joystick), ctypes.c_uint],
         ctypes.c_ubyte)
def joystick_get_hat(joystick, hat):
    """Gets the current state of a joystick POV hat.

    The return value is one of the SDL_HAT_* positions.
    """
    if not isinstance(joystick, SDL_Joystick):
        raise TypeError("joystick must be a SDL_Joystick")
    if type(hat) is not int:
        raise TypeError("hat must be an int")
    return dll.SDL_JoystickGetHat(ctypes.byref(joystick), hat)


@sdltype("SDL_JoystickIndex", [ctypes.POINTER(SDL_Joystick)], ctypes.c_int)
def joystick_index(joystick):
    """Retrieves the device index of the passed joystick.

    Raises a TypeError, if the passed joystick is not a SDL_Joystick.
    """
    if not isinstance(joystick, SDL_Joystick):
        raise TypeError("joystick must be a SDL_Joystick")
    return dll.SDL_JoystickIndex(ctypes.byref(joystick))


@sdltype("SDL_JoystickName", [ctypes.c_int], ctypes.c_char_p)
def joystick_name(index):
    """Retrieves the device name of the joystick at the specific index.

    If index is not an integer, a TypeError is raised. If the index is
    not in the range of joystick_num_joysticks(), a SDLError is raised.
    """
    if type(index) is not int:
        raise TypeError("index must be an int")
    retval = dll.SDL_JoystickName(index)
    if retval is None:
        raise SDLError()
    return stringify(retval, "utf-8")


@sdltype("SDL_JoystickNumAxes", [ctypes.POINTER(SDL_Joystick)], ctypes.c_int)
def joystick_num_axes(joystick):
    """Gets the number of available axes for the joystick.

    Raises a SDLError, if an error occured.
    """
    if not isinstance(joystick, SDL_Joystick):
        raise TypeError("joystick must be a SDL_Joystick")
    ret = dll.SDL_JoystickNumAxes(ctypes.byref(joystick))
    if ret < 0:
        raise SDLError()
    return ret


@sdltype("SDL_JoystickNumBalls", [ctypes.POINTER(SDL_Joystick)], ctypes.c_int)
def joystick_num_balls(joystick):
    """Gets the number of available balls for the joystick.

    Raises a SDLError, if an error occured.
    """
    if not isinstance(joystick, SDL_Joystick):
        raise TypeError("joystick must be a SDL_Joystick")
    ret = dll.SDL_JoystickNumBalls(ctypes.byref(joystick))
    if ret < 0:
        raise SDLError()
    return ret


@sdltype("SDL_JoystickNumButtons", [ctypes.POINTER(SDL_Joystick)],
         ctypes.c_int)
def joystick_num_buttons(joystick):
    """Gets the number of available buttons for the joystick.

    Raises a SDLError, if an error occured.
    """
    if not isinstance(joystick, SDL_Joystick):
        raise TypeError("joystick must be a SDL_Joystick")
    ret = dll.SDL_JoystickNumButtons(ctypes.byref(joystick))
    if ret < 0:
        raise SDLError()
    return ret


@sdltype("SDL_JoystickNumHats", [ctypes.POINTER(SDL_Joystick)], ctypes.c_int)
def joystick_num_hats(joystick):
    """Gets the number of available hats for the joystick.

    Raises a SDLError, if an error occured.
    """
    if not isinstance(joystick, SDL_Joystick):
        raise TypeError("joystick must be a SDL_Joystick")
    ret = dll.SDL_JoystickNumHats(ctypes.byref(joystick))
    if ret < 0:
        raise SDLError()
    return ret


@sdltype("SDL_JoystickUpdate", None, None)
def joystick_update():
    """Update the current state of open joysticks.

    This is called automatically by the event loop, if any joystick
    events are enabled.
    """
    dll.SDL_JoystickUpdate()


@sdltype("SDL_NumJoysticks", None, ctypes.c_int)
def joystick_num_joysticks():
    """Retrieves the amount of available joysticks connected to the system.

    Raises a SDLError, if an error occured.
    """
    ret = dll.SDL_NumJoysticks()
    if ret < 0:
        raise SDLError()
    return ret
