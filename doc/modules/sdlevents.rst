.. module:: pygame2.sdl.events
   :synopsis: SDL2 system events wrapper

:mod:`pygame2.sdl.events` - SDL2 system events wrapper
======================================================

.. class:: SDL_WindowEvent()

   .. attribute:: type

      The type identifier of the event.

   .. attribute:: timestamp

      The exact time at which the event occured.

   .. attribute:: windowid

      The id of the SDL window, for which the event occured.

   .. attribute:: event

      TODO

   .. attribute:: data1

      TODO

   .. attribute:: data2

      TODO

.. class:: SDL_KeyboardEvent()

   .. attribute:: type

      The type identifier of the event.

   .. attribute:: timestamp

      The exact time at which the event occured.

   .. attribute:: windowid

      The id of the SDL window, for which the event occured.

   .. attribute:: state

      The keyboard state.

   .. attribute:: repeat

      TODO

.. class:: SDL_TextEditingEvent()

   .. attribute:: type

      The type identifier of the event.

   .. attribute:: timestamp

      The exact time at which the event occured.

   .. attribute:: windowid

      The id of the SDL window, for which the event occured.

   .. attribute:: text

      The edited text.

   .. attribute::  start

      The start offset of the editing operation.

   .. attribute:: length

      The length of the edited text portion.

.. class:: SDL_TextInputEvent()

   .. attribute:: type

      The type identifier of the event.

   .. attribute:: timestamp

      The exact time at which the event occured.

   .. attribute:: windowid

      The id of the SDL window, for which the event occured.

   .. attribute:: text

      The text input.

.. class:: SDL_MouseMotionEvent()

   .. attribute:: type

      The type identifier of the event.

   .. attribute:: timestamp

      The exact time at which the event occured.

   .. attribute:: windowid

      The id of the SDL window, for which the event occured.

   .. attribute:: state

      The mouse state.

   .. attribute:: x

      The x position of the mouse.

   .. attribute:: y

      The y position of the mouse.

   .. attribute:: xrel

      The relative x movement since the last event.

   .. attribute:: yrel

      The relative y movement since the last event.

.. class:: SDL_MouseButtonEvent()

   .. attribute:: type

      The type identifier of the event.

   .. attribute:: timestamp

      The exact time at which the event occured.

   .. attribute:: windowid

      The id of the SDL window, for which the event occured.

   .. attribute:: button

      The mouse button(s).

   .. attribute:: state

      The mouse state.

   .. attribute:: x

      The x position of the mouse.

   .. attribute:: y

      The y position of the mouse.

.. class:: SDL_MouseWheelEvent()

   .. attribute:: type

      The type identifier of the event.

   .. attribute:: timestamp

      The exact time at which the event occured.

   .. attribute:: windowid

      The id of the SDL window, for which the event occured.

   .. attribute:: x

      The wheel movement over the x axis.

   .. attribute:: y

       The wheel movement over the y axis.

.. class:: SDL_JoyAxisEvent()

   .. attribute:: type

      The type identifier of the event.

   .. attribute:: timestamp

      The exact time at which the event occured.

   .. attribute:: which

      TODO

   .. attribute:: axis

      TODO

   .. attribute:: value

      TODO

.. class:: SDL_JoyBallEvent()

   .. attribute:: type

      The type identifier of the event.

   .. attribute:: timestamp

      The exact time at which the event occured.

   .. attribute:: which

      TODO

   .. attribute:: vall

      TODO

   .. attribute:: xrel

      TODO

   .. attribute:: yrel

      TODO

.. class:: SDL_JoyHatEvent()

   .. attribute:: type

      The type identifier of the event.

   .. attribute:: timestamp

      The exact time at which the event occured.

   .. attribute:: which

      TODO

   .. attribute:: hat

      TODO

   .. attribute:: value

      TODO

.. class:: SDL_JoyButtonEvent()

   .. attribute:: type

      The type identifier of the event.

   .. attribute:: timestamp

      The exact time at which the event occured.

   .. attribute:: which

      TODO

   .. attribute:: button

      TODO

   .. attribute:: state

      TODO

.. class:: SDL_TouchFingerEvent()

   .. attribute:: type

      The type identifier of the event.

   .. attribute:: timestamp

      The exact time at which the event occured.

   .. attribute:: windowid

      The id of the SDL window, for which the event occured.

   .. attribute:: touchid

      TODO

   .. attribute:: fingerid

      TODO

   .. attribute:: state

      TODO

   .. attribute:: x

      TODO

   .. attribute:: y

      TODO

   .. attribute:: dx

      TODO

   .. attribute:: dy

      TODO

   .. attribute:: pressure

      TODO

.. class:: SDL_TouchButtonEvent()

   .. attribute:: type

      The type identifier of the event.

   .. attribute:: timestamp

      The exact time at which the event occured.

   .. attribute:: windowid

      The id of the SDL window, for which the event occured.

   .. attribute:: touchid

      TODO

   .. attribute:: state

      TODO

   .. attribute:: button

      TODO

.. class:: SDL_MultiGestureEvent()

   .. attribute:: type

      The type identifier of the event.

   .. attribute:: timestamp

      The exact time at which the event occured.

   .. attribute:: windowid

      The id of the SDL window, for which the event occured.

   .. attribute:: touchid

      TODO

   .. attribute:: dtheta

      TODO

   .. attribute:: ddist

      TODO

   .. attribute:: x

      TODO

   .. attribute:: y

      TODO

   .. attribute:: numfingers

      TODO

.. class:: SDL_DollarGestureEvent()

   .. attribute:: type

      The type identifier of the event.

   .. attribute:: timestamp

      The exact time at which the event occured.

   .. attribute:: windowid

      The id of the SDL window, for which the event occured.

   .. attribute:: touchid

      TODO

   .. attribute:: gestureid

      TODO

   .. attribute:: numfingers

      TODO

   .. attribute:: error

      TODO

   .. attribute:: x

      TODO

   .. attribute:: y

      TODO

.. class:: SDL_DropEvent()

   .. attribute:: type

      The type identifier of the event.

   .. attribute:: timestamp

      The exact time at which the event occured.

   .. attribute:: windowid

      The id of the SDL window, for which the event occured.

   .. attribute:: file

      TODO

.. class:: SDL_QuitEvent()

   .. attribute:: type

      The type identifier of the event.

   .. attribute:: timestamp

      The exact time at which the event occured.

.. class:: SDL_UserEvent()

   .. attribute:: type

      The type identifier of the event.

   .. attribute:: timestamp

      The exact time at which the event occured.

   .. attribute:: windowid

      The id of the SDL window, for which the event occured.

   .. attribute:: code

      TODO

   .. attribute:: data1

      TODO

   .. attribute:: data2

      TODO

.. class:: SDL_SysWMEvent()

   .. attribute:: type

      The type identifier of the event.

   .. attribute:: timestamp

      The exact time at which the event occured.

   .. attribute:: msg

      The exact :class:`pygame2.sdl.syswm.SDL_SysWMmsg`.

.. class:: SDL_Event()

   .. attribute:: type

      The type identifier of the event.

   .. attribute:: window

      The exact :class:`SDL_WindowEvent`.

   .. attribute:: key

      The exact :class:`SDL_KeyboardEvent`.

   .. attribute:: text

      The exact :class:`SDL_TextEditingEvent`.

   .. attribute:: input

      The exact :class:`SDL_TextInputEvent`.

   .. attribute:: motion

      The exact :class:`SDL_MouseMotionEvent`.

   .. attribute:: button

      The exact :class:`SDL_MouseButtonEvent`.

   .. attribute:: wheel

      The exact :class:`SDL_MouseWheelEvent`.

   .. attribute:: jaxis

      The exact :class:`SDL_JoyAxisEvent`.

   .. attribute:: jball

      The exact :class:`SDL_JoyBallEvent`.

   .. attribute:: jhat

      The exact :class:`SDL_JoyHatEvent`.

   .. attribute:: jbutton

      The exact :class:`SDL_JoyButtonEvent`.

   .. attribute:: quit

      The exact :class:`SDL_QuitEvent`.

   .. attribute:: user

      The exact :class:`SDL_UserEvent`.

   .. attribute:: syswm

      The exact :class:`SDL_SysWMEvent`.

   .. attribute:: tfinger

      The exact :class:`SDL_TouchFingerEvent`.

   .. attribute:: tbutton

      The exact :class:`SDL_TouchButtonEvent`.

   .. attribute:: mgesture

      The exact :class:`SDL_MultiGestureEvent`.

   .. attribute:: dgesture

      The exact :class:`SDL_DollarGestureEvent`.

   .. attribute:: drop

      The exact :class:`SDL_DropEvent`.

.. class:: SDL_EventFilter(callback)

   TODO


.. function:: add_event_watch(efilter : SDL_EventFilter[, \
                              userdata=None]) -> None

   Adds a filter callback function to the event system. The filter will
   be called everytime a new event is pushed to the event queue.

   The same filter function can be added multiple times with different
   ``userdata`` values. Each filter function will be invoked with the
   data passed at the time of addition.


   This wraps :c:func:`SDL_AddEventWatch`.

.. function:: del_event_watch(efilter : SDL_EventFilter[, \
                              userdata=None]) -> None

   Removes a filter callback function from the event system. If the same
   filter function was added multiple times with different (or
   identical) ``userdata``, only that specific filter(or the first
   occurance of it) will be removed.

   This wraps :c:func:`SDL_DelEventWatch`.

.. function:: event_state(etype : int, state : int) -> int

   Influences the processing behaviour for certain events. If *state* is
   set to ``SDL_IGNORE``, events with the specific type will be
   automatically dropped from the event queue and not be filtered or
   processed. If *state* is set to ``SDL_ENABLE``, events with the
   specific type will be processed normally. If *state* is set to
   ``SDL_QUERY``, the current processing state for the specific event
   type will be returned.

   This wraps :c:func:`SDL_EventState`.

.. function:: get_event_state(etype : int) -> int

   Queries the processing behaviour for a specific event type.
   This is a shortcut handler for ``event_state(type, SDL_QUERY)``.

   This wraps :c:func:`SDL_GetEventState`.

.. function:: filter_events(efilter : SDL_EventFilter[, userdata=None]) -> None

   Executes the passed filter callback on the current event queue. Every
   event, for which the filter returns 0, will be removed from the
   queue.

   This wraps :c:func:`SDL_FilterEvents`.

.. function:: flush_event(etype : int) -> None

   Removes all events of the specific type from the event queue.

   This wraps :c:func:`SDL_FlushEvent`.

.. function:: flush_events(mintype : int, maxtype : int) -> None

   Removes all events, which types are between *mintype* and *maxtype*,
   from the event queue.

   This wraps :c:func:`SDL_FlushEvents`.

.. function:: get_event_filter() -> SDL_EventFilter

   Retrieves the currently set event filter callback and its user data.

   This wraps :c:func:`SDL_GetEventFilter`.

.. function:: set_event_filter(efilter : SDL_EventFilter[, \
                               userdata=None]) -> None

   Sets up a filter callback to process all events before they are put
   into the event queue.

   If the filter returns 1, the event will be added to the queue. If it
   returns 0, the event will be dropped from the queue.

   .. note::
      The filter function might run in a different thread, so be
      very careful with what you are doing within the function.

    There is one caveat when dealing with the ``SDL_QUITEVENT`` event
    type.  The event filter is only called when the window manager
    desires to close the application window. If the event filter returns
    1, then the window will be closed, otherwise the window will remain
    open if possible.

    If the quit event is generated by an interrupt signal, it will
    bypass the internal queue and be delivered to the application at the
    next event poll.

   This wraps :c:func:`SDL_SetEventFilter`.

.. function:: has_event(etype : int) -> bool

   Checks, if there are any events of the specific type in the event
   queue.

   This wraps :c:func:`SDL_HasEvent`.

.. function:: has_events(mintype : int, maxtype : int) -> bool

   Checks, if there are any events, which types are between *mintype* and
   *maxtype*, in the event queue.

   This wraps :c:func:`SDL_HasEvents`.

.. function:: peep_events(events, numevents, action, mintype, maxtype) \
              -> (int, (SDL_Event, SDL_Event, ...))

   Checks the event queue for messages and optionally returns them.

   If *action* is ``SDL_ADDEVENT``, up to *numevents* events will be
   added to the back of the event queue. A sequence of at least
   *numevent* SDL_Event items has to be provided then.

   If *action* is ``SDL_PEEKEVENT``, up to *numevents* events at the
   front of the event queue, within the specified minimum and maximum
   type, will be returned and will not be removed from the queue. The
   *events* argument will be ignored by the function.

   If *action* is ``SDL_GETEVENT``, up to *numevents* events at the
   front of the event queue, within the specified minimum and maximum
   type, will be returned and will be removed from the queue. The *events*
   argument will be ignored by the function.

   This wraps :c:func:`SDL_PeepEvents`.

.. function:: poll_event(getevent=False) -> SDL_Event

   Polls for currently pending events. If *getevent* is ``True``, the
   next event (if any) is removed from the queue and returned. Otherwise
   a bool is returned, indicating, if there are any pending events.

   This wraps :c:func:`SDL_PollEvent`.

.. function:: pump_events() -> None

   Pumps the event loop, gathering events from the input devices.

   .. note::

      This should only be run in the thread that sets the video mode.

   This wraps :c:func:`SDL_PumpEvents`.

.. function:: push_event(event : SDL_Event) -> bool

   Adds the passed *event* to the event queue. Returns ``True`` on
   success, or ``False``, if the event was filtered. If some error
   occured, a :exc:`pygame2.sdl.SDLError` is raised.

   This wraps :c:func:`SDL_PushEvent`.

.. function:: register_events(numevents : int) -> int

   Allocates a set of user-defined events and returns the beginning
   event type number for that set. If there are not enough types left, a
   :exc:`pygame2.sdl.SDLError` is raised.

   This wraps :c:func:`SDL_RegisterEvents`.

.. function:: wait_event() -> SDL_Event

   Waits indefinitely for the next available event. If an error occurs,
   a :exc:`pygame2.sdl.SDLError` is raised.

   This wraps :c:func:`SDL_WaitEvent`.

.. function:: wait_event_timeout(timeout : int) -> SDL_Event

   Waits until the specified *timeout* (in milliseconds) for the next event.

   This wraps :c:func:`SDL_WaitEventTimeout`.

.. function:: quit_requested() -> bool

   Checks, if quitting the application was requested.

   This wraps :c:func:`SDL_QuitRequested`.
