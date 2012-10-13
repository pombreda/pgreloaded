"""
Wrapper methods around the SDL2 haptic routines.
"""
import ctypes
from pygame2.compat import stringify
from pygame2.sdl.joystick import SDL_Joystick
from pygame2.sdl import sdltype, dll, SDL_TRUE, SDLError

__all__ = ["SDL_Haptic", "SDL_HapticDirection", "SDL_HapticConstant",
           "SDL_HapticPeriodic", "SDL_HapticCondition", "SDL_HapticRamp",
           "SDL_HapticCustom", "SDL_HapticEffect",
           "num_haptics", "haptic_name", "haptic_open",
           "haptic_opened", "haptic_index", "mouse_is_haptic",
           "haptic_open_from_mouse", "joystick_is_haptic",
           "haptic_open_from_joystick", "haptic_close", "haptic_num_effects",
           "haptic_num_effects_playing", "haptic_query", "haptic_num_axes",
           "haptic_effect_supported", "haptic_new_effect",
           "haptic_update_effect", "haptic_run_effect", "haptic_stop_effect",
           "haptic_destroy_effect", "haptic_get_effect_status",
           "haptic_set_gain", "haptic_set_autocenter", "haptic_pause",
           "haptic_unpause", "haptic_stop_all", "haptic_rumble_supported",
           "haptic_rumble_init", "haptic_rumble_play", "haptic_rumble_stop",

           "SDL_HAPTIC_CONSTANT", "SDL_HAPTIC_SINE", "SDL_HAPTIC_SQUARE",
           "SDL_HAPTIC_TRIANGLE", "SDL_HAPTIC_SAWTOOTHUP",
           "SDL_HAPTIC_SAWTOOTHDOWN", "SDL_HAPTIC_RAMP", "SDL_HAPTIC_SPRING",
           "SDL_HAPTIC_DAMPER", "SDL_HAPTIC_INERTIA", "SDL_HAPTIC_FRICTION",
           "SDL_HAPTIC_CUSTOM", "SDL_HAPTIC_GAIN", "SDL_HAPTIC_AUTOCENTER",
           "SDL_HAPTIC_STATUS", "SDL_HAPTIC_PAUSE", "SDL_HAPTIC_POLAR",
           "SDL_HAPTIC_CARTESIAN", "SDL_HAPTIC_SPHERICAL",
           "SDL_HAPTIC_INFINITY"
           ]

SDL_HAPTIC_CONSTANT =     1 << 0
SDL_HAPTIC_SINE =         1 << 1
SDL_HAPTIC_SQUARE =       1 << 2
SDL_HAPTIC_TRIANGLE =     1 << 3
SDL_HAPTIC_SAWTOOTHUP =   1 << 4
SDL_HAPTIC_SAWTOOTHDOWN = 1 << 5
SDL_HAPTIC_RAMP =         1 << 6
SDL_HAPTIC_SPRING =       1 << 7
SDL_HAPTIC_DAMPER =       1 << 8
SDL_HAPTIC_INERTIA =      1 << 9
SDL_HAPTIC_FRICTION =     1 << 10
SDL_HAPTIC_CUSTOM =       1 << 11

SDL_HAPTIC_GAIN =       1 << 12
SDL_HAPTIC_AUTOCENTER = 1 << 13
SDL_HAPTIC_STATUS =     1 << 14
SDL_HAPTIC_PAUSE =      1 << 15

SDL_HAPTIC_POLAR =     0
SDL_HAPTIC_CARTESIAN = 1
SDL_HAPTIC_SPHERICAL = 2

SDL_HAPTIC_INFINITY = 4294967295


class SDL_Haptic(ctypes.Structure):
    """A haptic-enabled device."""
    pass


class SDL_HapticDirection(ctypes.Structure):
    """The direction a haptic effect comes from."""
    _fields_ = [("type", ctypes.c_ubyte), ("dir", ctypes.c_int * 3)]


class SDL_HapticConstant(ctypes.Structure):
    """A constant effect that does not change while running."""
    _fields_ = [("type", ctypes.c_ushort),
                ("direction", SDL_HapticDirection),
                ("length", ctypes.c_uint),
                ("delay", ctypes.c_ushort),
                ("button", ctypes.c_ushort),
                ("interval", ctypes.c_ushort),
                ("level", ctypes.c_short),
                ("attack_length", ctypes.c_ushort),
                ("attack_level", ctypes.c_ushort),
                ("fade_length", ctypes.c_ushort),
                ("fade_level", ctypes.c_ushort),
                ]


class SDL_HapticPeriodic(ctypes.Structure):
    """A periodic effect."""
    _fields_ = [("type", ctypes.c_ushort),
                ("direction", SDL_HapticDirection),
                ("length", ctypes.c_uint),
                ("delay", ctypes.c_ushort),
                ("button", ctypes.c_ushort),
                ("interval", ctypes.c_ushort),
                ("period", ctypes.c_ushort),
                ("magnitude", ctypes.c_short),
                ("offset", ctypes.c_short),
                ("phase", ctypes.c_ushort),
                ("attack_length", ctypes.c_ushort),
                ("attack_level", ctypes.c_ushort),
                ("fade_length", ctypes.c_ushort),
                ("fade_level", ctypes.c_ushort),
                ]


class SDL_HapticCondition(ctypes.Structure):
    """A conditionally running effect."""
    _fields_ = [("type", ctypes.c_ushort),
                ("direction", SDL_HapticDirection),
                ("length", ctypes.c_uint),
                ("delay", ctypes.c_ushort),
                ("button", ctypes.c_ushort),
                ("interval", ctypes.c_ushort),
                ("right_sat", ctypes.c_ushort * 3),
                ("left_sat", ctypes.c_ushort * 3),
                ("right_coeff", ctypes.c_short * 3),
                ("left_coeff", ctypes.c_short * 3),
                ("deadband", ctypes.c_ushort * 3),
                ("center", ctypes.c_short * 3),
                ]


class SDL_HapticRamp(ctypes.Structure):
    """A ramp-like effect."""
    _fields_ = [("type", ctypes.c_ushort),
                ("direction", SDL_HapticDirection),
                ("length", ctypes.c_uint),
                ("delay", ctypes.c_ushort),
                ("button", ctypes.c_ushort),
                ("interval", ctypes.c_ushort),
                ("start", ctypes.c_short),
                ("end", ctypes.c_short),
                ("attack_length", ctypes.c_ushort),
                ("attack_level", ctypes.c_ushort),
                ("fade_length", ctypes.c_ushort),
                ("fade_level", ctypes.c_ushort),
                ]


class SDL_HapticCustom(ctypes.Structure):
    """A custom effect."""
    _fields_ = [("type", ctypes.c_ushort),
                ("direction", SDL_HapticDirection),
                ("length", ctypes.c_uint),
                ("delay", ctypes.c_ushort),
                ("button", ctypes.c_ushort),
                ("interval", ctypes.c_ushort),
                ("channels", ctypes.c_ubyte),
                ("period", ctypes.c_ushort),
                ("samples", ctypes.c_ushort),
                ("data", ctypes.POINTER(ctypes.c_ushort)),
                ("attack_length", ctypes.c_ushort),
                ("attack_level", ctypes.c_ushort),
                ("fade_length", ctypes.c_ushort),
                ("fade_level", ctypes.c_ushort),
                ]


class SDL_HapticEffect(ctypes.Union):
    """A generic haptic effect, containing the concrete haptic effect."""
    _fields_ = [("type", ctypes.c_ushort),
                ("constant", SDL_HapticConstant),
                ("periodic", SDL_HapticPeriodic),
                ("condition", SDL_HapticCondition),
                ("ramp", SDL_HapticRamp),
                ("custom", SDL_HapticCustom),
                ]


@sdltype("SDL_NumHaptics", None, None)
def num_haptics():
    """Gets the number of haptic-aware joysticks attached."""
    return dll.SDL_NumHaptics()


@sdltype("SDL_HapticName", [ctypes.c_int], ctypes.c_char_p)
def haptic_name(index):
    """Gets device name for a specific haptic device."""
    retval = dll.SDL_HapticName(index)
    if retval is not None:
        return stringify(retval, "utf-8")
    raise SDLError()


@sdltype("SDL_HapticOpen", [ctypes.c_int], ctypes.POINTER(SDL_Haptic))
def haptic_open(index):
    """Opens a haptic device."""
    retval = dll.SDL_HapticOpen(index)
    if retval is not None:
        return retval.contents
    raise SDLError()


@sdltype("SDL_HapticOpened", [ctypes.c_int], ctypes.c_int)
def haptic_opened(index):
    """Checks, if a haptic device has been opened."""
    return dll.SDL_HapticOpened(index) == 1


@sdltype("SDL_HapticIndex", [ctypes.POINTER(SDL_Haptic)], ctypes.c_int)
def haptic_index(haptic):
    """Gets the index of the haptic device."""
    retval = dll.SDL_HapticIndex(ctypes.byref(haptic))
    if retval == -1:
        raise SDLError()
    return retval


@sdltype("SDL_MouseIsHaptic", None, ctypes.c_int)
def mouse_is_haptic():
    """Checks, if the currently used mouse has haptic capabilities."""
    return dll.SDL_MouseIsHaptic() == SDL_TRUE


@sdltype("SDL_HapticOpenFromMouse", None, ctypes.POINTER(SDL_Haptic))
def haptic_open_from_mouse():
    """Tries to open the mouse as haptic device."""
    retval = dll.SDL_HapticOpenFromMouse()
    if retval is None or not bool(retval):
        raise SDLError()
    return retval.contents


@sdltype("SDL_JoystickIsHaptic", [ctypes.POINTER(SDL_Joystick)], ctypes.c_int)
def joystick_is_haptic(joystick):
    """Checks, if the passed SDL_Joystick has haptic capabilities."""
    retval = dll.SDL_JoystickIsHaptic(ctypes.byref(joystick))
    if retval == -1:
        raise SDLError()
    return retval == 1


@sdltype("SDL_HapticOpenFromJoystick", [ctypes.POINTER(SDL_Joystick)],
         ctypes.POINTER(SDL_Haptic))
def haptic_open_from_joystick(joystick):
    """Tries to open the passed SDL_Joystick as haptic device."""
    retval = dll.SDL_HapticOpenFromJoystick(ctypes.byref(joystick))
    if retval is None or not bool(retval):
        raise SDLError()
    return retval.contents


@sdltype("SDL_HapticClose", [ctypes.POINTER(SDL_Haptic)], None)
def haptic_close(haptic):
    """Closes an open SDL_Haptic device."""
    dll.SDL_HapticClose(ctypes.byref(haptic))


@sdltype("SDL_HapticNumEffects", [ctypes.POINTER(SDL_Haptic)], ctypes.c_int)
def haptic_num_effects(haptic):
    """Returns the number of effects the device can store."""
    retval = dll.SDL_HapticNumEffects(ctypes.byref(haptic))
    if retval == -1:
        raise SDLError()
    return retval


@sdltype("SDL_HapticNumEffectsPlaying", [ctypes.POINTER(SDL_Haptic)],
         ctypes.c_int)
def haptic_num_effects_playing(haptic):
    """Returns the number of effects the device can play at the same time."""
    retval = dll.SDL_HapticNumEffectsPlaying(ctypes.byref(haptic))
    if retval == -1:
        raise SDLError()
    return retval


@sdltype("SDL_HapticQuery", [ctypes.POINTER(SDL_Haptic)], ctypes.c_uint)
def haptic_query(haptic):
    """Gets the features supported by the haptic device."""
    return dll.SDL_HapticQuery(ctypes.byref(haptic))


@sdltype("SDL_HapticNumAxes", [ctypes.POINTER(SDL_Haptic)], ctypes.c_int)
def haptic_num_axes(haptic):
    """Gets the number of axes of the haptic device."""
    return dll.SDL_HapticNumAxes(ctypes.byref(haptic))


@sdltype("SDL_HapticEffectSupported", [ctypes.POINTER(SDL_Haptic),
                                       ctypes.POINTER(SDL_HapticEffect)],
         ctypes.c_int)
def haptic_effect_supported(haptic, effect):
    """Checks, if the specified effect is supported by the haptic device."""
    retval = dll.SDL_HapticEffectSupported(ctypes.byref(haptic),
                                           ctypes.byref(effect))
    if retval == -1:
        raise SDLError()
    return retval == SDL_TRUE


@sdltype("SDL_HapticNewEffect", [ctypes.POINTER(SDL_Haptic),
                                 ctypes.POINTER(SDL_HapticEffect)],
         ctypes.c_int)
def haptic_new_effect(haptic, effect):
    """Creates a new effect on the device."""
    retval = dll.SDL_HapticNewEffect(ctypes.byref(haptic),
                                     ctypes.byref(effect))
    if retval == -1:
        raise SDLError()
    return retval


@sdltype("SDL_HapticUpdateEffect", [ctypes.POINTER(SDL_Haptic), ctypes.c_int,
                                    ctypes.POINTER(SDL_HapticEffect)],
         ctypes.c_int)
def haptic_update_effect(haptic, effectid, effect):
    """Updates an effect on the device."""
    retval = dll.SDL_HapticNewEffect(ctypes.byref(haptic), effectid,
                                     ctypes.byref(effect))
    if retval == -1:
        raise SDLError()
    return retval


@sdltype("SDL_HapticRunEffect", [ctypes.POINTER(SDL_Haptic), ctypes.c_int,
                                 ctypes.c_uint], ctypes.c_int)
def haptic_run_effect(haptic, effectid, iterations):
    """Runs an effect on the haptic device.

    If iterations is SDL_HAPTIC_INFINITY, the effect will be run forever.
    """
    retval = dll.SDL_HapticRunEffect(ctypes.byref(haptic), effectid,
                                     iterations)
    if retval == -1:
        raise SDLError()


@sdltype("SDL_HapticStopEffect", [ctypes.POINTER(SDL_Haptic), ctypes.c_int],
         ctypes.c_int)
def haptic_stop_effect(haptic, effectid):
    """Stops a haptic effect."""
    retval = dll.SDL_HapticStopEffect(ctypes.byref(haptic), effectid)
    if retval == -1:
        raise SDLError()


@sdltype("SDL_HapticDestroyEffect", [ctypes.POINTER(SDL_Haptic), ctypes.c_int],
         None)
def haptic_destroy_effect(haptic, effectid):
    """Destroys a haptic effect."""
    dll.SDL_HapticDestroyEffect(ctypes.byref(haptic), effectid)


@sdltype("SDL_HapticGetEffectStatus", [ctypes.POINTER(SDL_Haptic),
                                       ctypes.c_int], ctypes.c_int)
def haptic_get_effect_status(haptic, effectid):
    """Gets the status of a haptic effect."""
    retval = dll.SDL_HapticGetEffectStatus(ctypes.byref(haptic), effectid)
    if retval == -1:
        raise SDLError()
    return retval


@sdltype("SDL_HapticSetGain", [ctypes.POINTER(SDL_Haptic), ctypes.c_int],
         ctypes.c_int)
def haptic_set_gain(haptic, gain):
    """Sets the global gain of the haptic device."""
    retval = dll.SDL_HapticSetGain(ctypes.byref(haptic), gain)
    if retval == -1:
        raise SDLError()


@sdltype("SDL_HapticSetAutocenter", [ctypes.POINTER(SDL_Haptic), ctypes.c_int],
         ctypes.c_int)
def haptic_set_autocenter(haptic, autocenter):
    """Sets the global autocenter of the haptic device."""
    retval = dll.SDL_HapticSetAutocenter(ctypes.byref(haptic), autocenter)
    if retval == -1:
        raise SDLError()


@sdltype("SDL_HapticPause", [ctypes.POINTER(SDL_Haptic)], ctypes.c_int)
def haptic_pause(haptic):
    """Pauses a haptic device."""
    retval = dll.SDL_HapticPause(ctypes.byref(haptic))
    if retval == -1:
        raise SDLError()


@sdltype("SDL_HapticUnpause", [ctypes.POINTER(SDL_Haptic)], ctypes.c_int)
def haptic_unpause(haptic):
    """Unpauses a haptic device."""
    retval = dll.SDL_HapticUnpause(ctypes.byref(haptic))
    if retval == -1:
        raise SDLError()


@sdltype("SDL_HapticStopAll", [ctypes.POINTER(SDL_Haptic)], ctypes.c_int)
def haptic_stop_all(haptic):
    """Stops all currently playing effects on a haptic device."""
    retval = dll.SDL_HapticStopAll(ctypes.byref(haptic))
    if retval == -1:
        raise SDLError()


@sdltype("SDL_HapticRumbleSupported", [ctypes.POINTER(SDL_Haptic)],
         ctypes.c_int)
def haptic_rumble_supported(haptic):
    """Checks, if rumble is supported on the haptic device."""
    retval = dll.SDL_HapticRumbleSupported(ctypes.byref(haptic))
    if retval == -1:
        raise SDLError()
    return retval == SDL_TRUE


@sdltype("SDL_HapticRumbleInit", [ctypes.POINTER(SDL_Haptic)], ctypes.c_int)
def haptic_rumble_init(haptic):
    """Initialises a haptic device for rumble playback."""
    retval = dll.SDL_HapticRumbleInit(ctypes.byref(haptic))
    if retval == -1:
        raise SDLError()


@sdltype("SDL_HapticRumblePlay", [ctypes.POINTER(SDL_Haptic), ctypes.c_float,
                                  ctypes.c_uint], ctypes.c_int)
def haptic_rumble_play(haptic, strength, length):
    """Plays a rumble on the haptic device."""
    if float(strength) < 0 or float(strength) > 1:
        raise ValueError("strength must be in the range [0, 1]")
    retval = dll.SDL_HapticRumblePlay(ctypes.byref(haptic), strength, length)
    if retval == -1:
        raise SDLError()


@sdltype("SDL_HapticRumbleStop", [ctypes.POINTER(SDL_Haptic)], ctypes.c_int)
def haptic_rumble_stop(haptic):
    """Stops the rumble playback on a haptic device."""
    retval = dll.SDL_HapticRumbleStop(ctypes.byref(haptic))
    if retval == -1:
        raise SDLError()
