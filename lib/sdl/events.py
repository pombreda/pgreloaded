"""
Wrapper methods around the SDL2 event routines.
"""
import ctypes
from pygame2.sdl import sdltype, dll, SDL_FALSE, SDL_TRUE, get_error, SDLError

__all__ = ["SDL_WindowEvent", "SDL_KeyboardEvent", "SDL_TextEditingEvent",
           "SDL_TextInputEvent", "SDL_MouseMotionEvent",
           "SDL_MouseButtonEvent", "SDL_MouseWheelEvent", "SDL_JoyAxisEvent",
           "SDL_JoyBallEvent", "SDL_JoyHatEvent", "SDL_JoyButtonEvent",
           "SDL_TouchFingerEvent", "SDL_TouchButtonEvent",
           "SDL_MultiGestureEvent", "SDL_DollarGestureEvent", "SDL_DropEvent",
           "SDL_QuitEvent", "SDL_UserEvent", "SDL_SysWMEvent", "SDL_Event",
           "SDL_EventFilter", "add_event_watch", "del_event_watch",
           "event_state", "get_event_state", "filter_events", "flush_event",
           "flush_events", "get_event_filter", "set_event_filter", "has_event",
           "has_events", "peep_events", "poll_event", "pump_events",
           "push_event", "register_events", "wait_event", "wait_event_timeout",
           "quit_requested"
           ]

SDL_RELEASED = 0
SDL_PRESSED  = 1

SDL_FIRSTEVENT          = 0
SDL_QUIT                = 0x100
SDL_WINDOWEVENT         = 0x200
SDL_SYSWMEVENT          = 0x201
SDL_KEYDOWN             = 0x300
SDL_KEYUP               = 0x301
SDL_TEXTEDITING         = 0x302
SDL_TEXTINPUT           = 0x303
SDL_MOUSEMOTION         = 0x400
SDL_MOUSEBUTTONDOWN     = 0x401
SDL_MOUSEBUTTONUP       = 0x402
SDL_MOUSEWHEEL          = 0x403
SDL_INPUTMOTION         = 0x500
SDL_INPUTBUTTONDOWN     = 0x501
SDL_INPUTBUTTONUP       = 0x502
SDL_INPUTWHEEL          = 0x503
SDL_INPUTPROXIMITYIN    = 0x504
SDL_INPUTPROXIMITYOUT   = 0x505
SDL_JOYAXISMOTION       = 0x600
SDL_JOYBALLMOTION       = 0x601
SDL_JOYHATMOTION        = 0x602
SDL_JOYBUTTONDOWN       = 0x603
SDL_JOYBUTTONUP         = 0x604
SDL_FINGERDOWN          = 0x700
SDL_FINGERUP            = 0x701
SDL_FINGERMOTION        = 0x702
SDL_TOUCHBUTTONDOWN     = 0x703
SDL_TOUCHBUTTONUP       = 0x704
SDL_DOLLARGESTURE       = 0x800
SDL_DOLLARRECORD        = 0x801
SDL_MULTIGESTURE        = 0x802
SDL_CLIPBOARDUPDATE     = 0x900
SDL_DROPFILE            = 0x1000
SDL_USEREVENT           = 0x8000
SDL_LASTEVENT           = 0xFFFF

ALL_EVENTS = (
    SDL_QUIT,
    SDL_WINDOWEVENT,
    SDL_SYSWMEVENT,
    SDL_KEYDOWN,
    SDL_KEYUP,
    SDL_TEXTEDITING,
    SDL_TEXTINPUT,
    SDL_MOUSEMOTION,
    SDL_MOUSEBUTTONDOWN,
    SDL_MOUSEBUTTONUP,
    SDL_MOUSEWHEEL,
    SDL_INPUTMOTION,
    SDL_INPUTBUTTONDOWN,
    SDL_INPUTBUTTONUP,
    SDL_INPUTWHEEL,
    SDL_INPUTPROXIMITYIN,
    SDL_INPUTPROXIMITYOUT,
    SDL_JOYAXISMOTION,
    SDL_JOYBALLMOTION,
    SDL_JOYHATMOTION,
    SDL_JOYBUTTONDOWN,
    SDL_JOYBUTTONUP,
    SDL_FINGERDOWN,
    SDL_FINGERUP,
    SDL_FINGERMOTION,
    SDL_TOUCHBUTTONDOWN,
    SDL_TOUCHBUTTONUP,
    SDL_DOLLARGESTURE,
    SDL_DOLLARRECORD,
    SDL_MULTIGESTURE,
    SDL_CLIPBOARDUPDATE,
    SDL_DROPFILE,
    SDL_USEREVENT,
    )
    

SDL_TEXTEDITINGEVENT_TEXT_SIZE = 32
SDL_TEXTINPUTEVENT_TEXT_SIZE   = 32

SDL_ADDEVENT  = 0
SDL_PEEKEVENT = 1
SDL_GETEVENT  = 2

SDL_QUERY   = -1
SDL_IGNORE  = 0
SDL_DISABLE = 0
SDL_ENABLE  = 1


class SDL_WindowEvent(ctypes.Structure):
    _fields_ = [("type", ctypes.c_uint),
                ("timestamp", ctypes.c_uint),
                ("windowid", ctypes.c_uint),
                ("event", ctypes.c_ubyte),
                ("_padding1", ctypes.c_ubyte),
                ("_padding2", ctypes.c_ubyte),
                ("_padding3", ctypes.c_ubyte),
                ("data1", ctypes.c_int),
                ("data2", ctypes.c_int),
                ]


class SDL_KeyboardEvent(ctypes.Structure):
    _fields_ = [("type", ctypes.c_uint),
                ("timestamp", ctypes.c_uint),
                ("windowid", ctypes.c_uint),
                ("state", ctypes.c_ubyte),
                ("repeat", ctypes.c_ubyte),
                ("_padding2", ctypes.c_ubyte),
                ("_padding3", ctypes.c_ubyte),
                ("keysym", ctypes.c_int),
                ]


class SDL_TextEditingEvent(ctypes.Structure):
    _fields_ = [("type", ctypes.c_uint),
                ("timestamp", ctypes.c_uint),
                ("windowid", ctypes.c_uint),
                ("text", (ctypes.c_char * SDL_TEXTEDITINGEVENT_TEXT_SIZE)),
                ("start", ctypes.c_int),
                ("length", ctypes.c_int),
                ]


class SDL_TextInputEvent(ctypes.Structure):
    _fields_ = [("type", ctypes.c_uint),
                ("timestamp", ctypes.c_uint),
                ("windowid", ctypes.c_uint),
                ("text", (ctypes.c_char * SDL_TEXTINPUTEVENT_TEXT_SIZE)),
                ]


class SDL_MouseMotionEvent(ctypes.Structure):
    _fields_ = [("type", ctypes.c_uint),
                ("timestamp", ctypes.c_uint),
                ("windowid", ctypes.c_uint),
                ("state", ctypes.c_ubyte),
                ("_padding1", ctypes.c_ubyte),
                ("_padding2", ctypes.c_ubyte),
                ("_padding3", ctypes.c_ubyte),
                ("x", ctypes.c_int),
                ("y", ctypes.c_int),
                ("xrel", ctypes.c_int),
                ("yrel", ctypes.c_int)
                ]


class SDL_MouseButtonEvent(ctypes.Structure):
    _fields_ = [("type", ctypes.c_uint),
                ("timestamp", ctypes.c_uint),
                ("windowid", ctypes.c_uint),
                ("button", ctypes.c_ubyte),
                ("state", ctypes.c_ubyte),
                ("_padding1", ctypes.c_ubyte),
                ("_padding2", ctypes.c_ubyte),
                ("x", ctypes.c_int),
                ("y", ctypes.c_int),
                ]


class SDL_MouseWheelEvent(ctypes.Structure):
    _fields_ = [("type", ctypes.c_uint),
                ("timestamp", ctypes.c_uint),
                ("windowid", ctypes.c_uint),
                ("x", ctypes.c_int),
                ("y", ctypes.c_int),
                ]


class SDL_JoyAxisEvent(ctypes.Structure):
    _fields_ = [("type", ctypes.c_uint),
                ("timestamp", ctypes.c_uint),
                ("which", ctypes.c_ubyte),
                ("axis", ctypes.c_ubyte),
                ("_padding1", ctypes.c_ubyte),
                ("_padding2", ctypes.c_ubyte),
                ("value", ctypes.c_int),
                ]


class SDL_JoyBallEvent(ctypes.Structure):
    _fields_ = [("type", ctypes.c_uint),
                ("timestamp", ctypes.c_uint),
                ("which", ctypes.c_ubyte),
                ("vall", ctypes.c_ubyte),
                ("_padding1", ctypes.c_ubyte),
                ("_padding2", ctypes.c_ubyte),
                ("xrel", ctypes.c_int),
                ("yrel", ctypes.c_int),
                ]


class SDL_JoyHatEvent(ctypes.Structure):
    _fields_ = [("type", ctypes.c_uint),
                ("timestamp", ctypes.c_uint),
                ("which", ctypes.c_ubyte),
                ("hat", ctypes.c_ubyte),
                ("value", ctypes.c_ubyte),
                ("_padding1", ctypes.c_ubyte),
                ]


class SDL_JoyButtonEvent(ctypes.Structure):
    _fields_ = [("type", ctypes.c_uint),
                ("timestamp", ctypes.c_uint),
                ("which", ctypes.c_ubyte),
                ("button", ctypes.c_ubyte),
                ("state", ctypes.c_ubyte),
                ("_padding1", ctypes.c_ubyte),
                ]


class SDL_TouchFingerEvent(ctypes.Structure):
    _fields_ = [("type", ctypes.c_uint),
                ("timestamp", ctypes.c_uint),
                ("windowid", ctypes.c_uint),
                ("touchid", ctypes.c_ulong),
                ("fingerid", ctypes.c_ulong),
                ("state", ctypes.c_ubyte),
                ("_padding1", ctypes.c_ubyte),
                ("_padding2", ctypes.c_ubyte),
                ("_padding3", ctypes.c_ubyte),
                ("x", ctypes.c_ushort),
                ("y", ctypes.c_ushort),
                ("dx", ctypes.c_short),
                ("dy", ctypes.c_short),
                ("pressure", ctypes.c_ushort),
                ]


class SDL_TouchButtonEvent(ctypes.Structure):
    _fields_ = [("type", ctypes.c_uint),
                ("timestamp", ctypes.c_uint),
                ("windowid", ctypes.c_uint),
                ("touchid", ctypes.c_ulong),
                ("state", ctypes.c_ubyte),
                ("button", ctypes.c_ubyte),
                ("_padding1", ctypes.c_ubyte),
                ("_padding2", ctypes.c_ubyte),
                ]


class SDL_MultiGestureEvent(ctypes.Structure):
    _fields_ = [("type", ctypes.c_uint),
                ("timestamp", ctypes.c_uint),
                ("windowid", ctypes.c_uint),
                ("touchid", ctypes.c_ulong),
                ("dtheta", ctypes.c_float),
                ("ddist", ctypes.c_float),
                ("x", ctypes.c_float),
                ("y", ctypes.c_float),
                ("numfingers", ctypes.c_ushort),
                ("_padding", ctypes.c_ushort),
                ]


class SDL_DollarGestureEvent(ctypes.Structure):
    _fields_ = [("type", ctypes.c_uint),
                ("timestamp", ctypes.c_uint),
                ("windowid", ctypes.c_uint),
                ("touchid", ctypes.c_ulong),
                ("gestureid", ctypes.c_ulong),
                ("numfingers", ctypes.c_uint),
                ("error", ctypes.c_float),
                ("x", ctypes.c_float),
                ("y", ctypes.c_float),
                ]


class SDL_DropEvent(ctypes.Structure):
    _fields_ = [("type", ctypes.c_uint),
                ("timestamp", ctypes.c_uint),
                ("file", ctypes.c_char_p)
                ]


class SDL_QuitEvent(ctypes.Structure):
    _fields_ = [("type", ctypes.c_uint),
                ("timestamp", ctypes.c_uint),
                ]


class SDL_UserEvent(ctypes.Structure):
    _fields_ = [("type", ctypes.c_uint),
                ("timestamp", ctypes.c_uint),
                ("windowid", ctypes.c_uint),
                ("code", ctypes.c_int),
                ("data1", ctypes.c_void_p),
                ("data2", ctypes.c_void_p),
                ]


class SDL_SysWMEvent(ctypes.Structure):
    _fields_ = [("type", ctypes.c_uint),
                ("timestamp", ctypes.c_uint),
                # TODO: create a capsule for SDL_SysWMmsg?
                ("msg", ctypes.c_void_p),
                ]


class SDL_Event(ctypes.Union):
    _fields_ = [("type", ctypes.c_uint),
                ("window", SDL_WindowEvent),
                ("key", SDL_KeyboardEvent),
                ("text", SDL_TextEditingEvent),
                ("input", SDL_TextInputEvent),
                ("motion", SDL_MouseMotionEvent),
                ("button", SDL_MouseButtonEvent),
                ("wheel", SDL_MouseWheelEvent),
                ("jaxis", SDL_JoyAxisEvent),
                ("jball", SDL_JoyBallEvent),
                ("jhat", SDL_JoyHatEvent),
                ("jbutton", SDL_JoyButtonEvent),
                ("quit", SDL_QuitEvent),
                ("user", SDL_UserEvent),
                ("syswm", SDL_SysWMEvent),
                ("tfinger", SDL_TouchFingerEvent),
                ("tbutton", SDL_TouchButtonEvent),
                ("mgesture", SDL_MultiGestureEvent),
                ("dgesture", SDL_DollarGestureEvent),
                ("drop", SDL_DropEvent),
                ]


SDL_EventFilter = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.py_object,
                                   ctypes.POINTER(SDL_Event))


@sdltype("SDL_AddEventWatch", [SDL_EventFilter, ctypes.py_object], None)
def add_event_watch(filter, userdata=None):
    """Adds a filter callback function to the event system.

    The filter will be called everytime a new event is pushed to the
    event queue.

    The same filter function can be added multiple times with different
    userdata values. Each filter function will be invoked with the data
    passed at the time of addition.
    """
    if not hasattr(filter, "_userdata"):
        filter._userdata = []
    val = ctypes.py_object(userdata)
    # Preserve the userdata, so it does not get GC'd
    filter._userdata.append(val)
    dll.SDL_AddEventWatch(filter, val)


@sdltype("SDL_DelEventWatch", [SDL_EventFilter, ctypes.py_object], None)
def del_event_watch(filter, userdata=None):
    """Removes a filter callback function from the event system.

    If the same filter function was added multiple times with different
   (or identical) userdata, only that specific filter(or the first
    occurance of it) will be removed.
    """
    # Resembles SDL2's implementation for checking for the userdata.
    if not hasattr(filter, "_userdata"):
        return
    for val in filter._userdata:
        if val.value == userdata:
            filter._userdata.remove(val)
            dll.SDL_DelEventWatch(filter, val)
            break


@sdltype("SDL_EventState", [ctypes.c_uint, ctypes.c_int], ctypes.c_ubyte)
def event_state(type, state):
    """Influences the processing behaviour for certain events.

    If state is set to SDL_IGNORE, events with the specific type will be
    automatically dropped from the event queue and not be filtered or
    processed.

    If state is set to SDL_ENABLE, events with the specific type will be
    processed normally.

    If state is set to SDL_QUERY, the current processing state for the
    specific event type will be returned.
    """
    ret = dll.SDL_EventState(type, state)
    if get_error() != "":
        raise SDLError()
    return ret


def get_event_state(type):
    """Queries the processing behaviour for a specific event type.

    This is a shortcut handler for event_state(type, SDL_QUERY).
    """
    return event_state(type, SDL_QUERY)


@sdltype("SDL_FilterEvents", [SDL_EventFilter, ctypes.py_object], None)
def filter_events(filter, userdata=None):
    """Executes the passed filter callback on the current event queue.

    Every event, for which the filter returns 0, will be removed from
    the queue.
    """
    ptr = ctypes.py_object(userdata)
    # Preserve the pointer for multi-threaded event queues
    filter._userdata = ptr
    dll.SDL_FilterEvents(filter, ptr)


@sdltype("SDL_FlushEvent", [ctypes.c_uint], None)
def flush_event(type):
    """Removes all events of the specific type from the event queue."""
    dll.SDL_FlushEvent(type)


@sdltype("SDL_FlushEvents", [ctypes.c_uint, ctypes.c_uint], None)
def flush_events(mintype, maxtype):
    """Removes all events, which types are between mintype and maxtype,
    from the event queue.
    """
    dll.SDL_FlushEvents(mintype, maxtype)


@sdltype("SDL_GetEventFilter", [ctypes.POINTER(SDL_EventFilter),
                                ctypes.POINTER(ctypes.py_object)],
         ctypes.c_int)
def get_event_filter():
    """Retrieves the currently set event filter callback and its user data.
    """
    filter = SDL_EventFilter()
    data = ctypes.py_object()
    ret = dll.SDL_GetEventFilter(ctypes.byref(filter), ctypes.byref(data))
    if ret.value == SDL_FALSE:
        if get_error() != "":
            raise SDLError()
        return None, None
    if bool(data):
        return filter, data
    return filter, None


@sdltype("SDL_SetEventFilter", [SDL_EventFilter, ctypes.py_object], None)
def set_event_filter(filter, userdata=None):
    """Sets up a filter callback to process all events before they are put
    into the event queue.


    If the filter returns 1, the event will be added to the queue. If it
    returns 0, the event will be dropped from the queue.

    NOTE: The filter function might run in a different thread, so be
    very careful with what you are doing within the function.

    There is one caveat when dealing with the SDL_QUITEVENT event type.
    The event filter is only called when the window manager desires to
    close the application window. If the event filter returns 1, then
    the window will be closed, otherwise the window will remain open if
    possible.

    If the quit event is generated by an interrupt signal, it will
    bypass the internal queue and be delivered to the application at the
    next event poll.
    """
    ptr = ctypes.py_object(userdata)
    # Preserve the pointer for multi-threaded event queues
    filter._userdata = ptr
    dll.SDL_SetEventFilter(filter, ptr)


@sdltype("SDL_HasEvent", [ctypes.c_uint], ctypes.c_int)
def has_event(type):
    """Checks, if there are any events of the specific type in the event queue.
    """
    return dll.SDL_HasEvent(type) == SDL_TRUE


@sdltype("SDL_HasEvents", [ctypes.c_uint, ctypes.c_uint], None)
def has_events(mintype, maxtype):
    """Checks, if there are any events, which types are between mintype and
    maxtype, in the event queue.
    """
    return dll.SDL_HasEvents(mintype, maxtype) == SDL_TRUE


@sdltype("SDL_PeepEvents", [ctypes.POINTER(SDL_Event), ctypes.c_int,
                            ctypes.c_int, ctypes.c_uint, ctypes.c_uint],
         ctypes.c_int)
def peep_events(events, numevents, action, mintype, maxtype):
    """Checks the event queue for messages and optionally returns them.

    If action is SDL_ADDEVENT, up to numevents events will be added to
    the back of the event queue. A sequence of at least numevent
    SDL_Event items has to be provided then.

    If action is SDL_PEEKEVENT, up to numevents events at the front
    of the event queue, within the specified minimum and maximum type,
    will be returned and will not be removed from the queue. The events
    argument will be ignored by the function.

    If action is SDL_GETEVENT, up to numevents events at the front
    of the event queue, within the specified minimum and maximum type,
    will be returned and will be removed from the queue. The events
    argument will be ignored by the function.
    """
    if numevents < 1:
        raise ValueError("numevents must be greater than 0")
    if action == SDL_ADDEVENT:
        # If the user wants to add something, it has to match the passed
        # sequence.
        if len(events) < numevents:
            raise ValueError("events must contain at least numevents values")
    else:
        # ignore whatever was passed
        events = (numevents * SDL_Event)()
    ret = dll.SDL_PeepEvents(ctypes.byref(events), numevents, action,
                             mintype, maxtype)
    if ret < 0:
        raise SDLError()
    return ret, events


@sdltype("SDL_PollEvent", [ctypes.POINTER(SDL_Event)], ctypes.c_int)
def poll_event(getevent=False):
    """Polls for currently pending events.

    if getevent is True, the next event(if any) is removed from the
    queue and returned. Otherwise a bool is returned, indicating, if
    there are any pending events.
    """
    if not getevent:
        return dll.SDL_PollEvent(None) == 1
    else:
        event = SDL_Event()
        ret = dll.SDL_PollEvent(ctypes.byref(event))
        if ret == 1:
            return event
        return None


@sdltype("SDL_PumpEvents", None, None)
def pump_events():
    """Pumps the event loop, gathering events from the input devices.

    NOTE: This should only be run in the thread that sets the video
    mode.
    """
    dll.SDL_PumpEvents()


@sdltype("SDL_PushEvent", [ctypes.POINTER(SDL_Event)], ctypes.c_int)
def push_event(event):
    """Adds the passed event to the event queue.

    Returns True on success, or False, if the event was filtered. If
    some error occured, a SDLError is raised.
    """
    ret = dll.SDL_PushEvent(ctypes.byref(event))
    if ret < 0:
        raise SDLError()
    return ret == 1


@sdltype("SDL_RegisterEvents", None, ctypes.c_int)
def register_events(numevents):
    """Allocates a set of user-defined events and returns the beginning
    event type number for that set.

    If there are not enough types left, a SDLError is raised.
    """
    ret = dll.SDL_RegisterEvents(numevents)
    if ret == (0xFFFFFFFF - 1):
        raise SDLError()
    return ret


@sdltype("SDL_WaitEvent", [ctypes.POINTER(SDL_Event)], ctypes.c_int)
def wait_event():
    """Waits indefinitely for the next available event.

    If an error occurs, a SDLError is raised.
    """
    event = SDL_Event()
    ret = dll.SDL_WaitEvent(ctypes.byref(event))
    if ret == 0:
        raise SDLError()
    return event


@sdltype("SDL_WaitEventTimeout", [ctypes.POINTER(SDL_Event), ctypes.c_int],
    ctypes.c_int)
def wait_event_timeout(timeout):
    """Waits until the specified timeout(in milliseconds) for the next event.
    """
    event = SDL_Event()

    ret = dll.SDL_WaitEventTimeout(ctypes.byref(event), timeout)
    if ret == 0:
        raise SDLError()
    return event


def quit_requested():
    """Checks, if quitting the application was requested."""
    pump_events()
    return peep_events(None, 0, SDL_PEEKEVENT, SDL_QUIT, SDL_QUIT) > 0
