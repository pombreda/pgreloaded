.. module:: pygame2.video.gui
   :synopsis: User interface elements
.. currentmodule:: pygame2.video

:mod:`pygame2.video.gui` - user interface elements
==================================================

.. data:: RELEASED

   Indicates that the UI element is released.

.. data:: HOVERED

   Indicates that the mouse pointer is currently hovering the UI element.

.. data:: PRESSED

   Indicates that a mouse button is pressed on the UI element.

.. class:: Button(source=None, size=(0, 0), bpp=32, freesf=False)

   A :class:`Sprite` object that can react on mouse events.

   If a *source* is provided, the constructor assumes it to be a readable
   buffer object or file path to load the pixel data from. The *size* and
   *bpp* will be ignored in those cases.

   If no *source* is provided, a *size* tuple containing the width and
   height of the button and a *bpp* value, indicating the bits per
   pixel to be used, need to be provided.

   *freesf* denotes, if the passed *source* shall be freed automatically on
   garbage-collecting the :class:`Button`.

   .. attribute:: state

      The current state of the button. This can be a value of
      ``RELEASED``, ``HOVERED`` or ``PRESSED``

   .. attribute:: motion

      A :class:`pygame2.events.EventHandler` that is invoked, if the mouse
      moves around while being over the :class:`Button`.

   .. attribute:: pressed

      A :class:`pygame2.events.EventHandler` that is invoked, if a mouse button
      is pressed on the :class:`Button`.

   .. attribute:: released

      A :class:`pygame2.events.EventHandler` that is invoked, if a mouse button
      is released on the :class:`Button`.

   .. attribute:: click

      A :class:`pygame2.events.EventHandler` that is invoked, if a mouse
      button is pressed and released on the :class:`Button`.

   .. attribute:: events

      A dict containing the mapping of SDL2 events to the available
      :class:`pygame2.events.EventHandler` bindings of the :class:`Button`.

.. class:: TextEntry(source=None, size=(0, 0), bpp=32, freesf=False)

   A :class:`Sprite` object that can react on text input.

   If a *source* is provided, the constructor assumes it to be a readable
   buffer object or file path to load the pixel data from. The *size* and
   *bpp* will be ignored in those cases.

   If no *source* is provided, a *size* tuple containing the width and
   height of the button and a *bpp* value, indicating the bits per
   pixel to be used, need to be provided.

   *freesf* denotes, if the passed *source* shall be freed automatically on
   garbage-collecting the :class:`TextEntry`.

   .. attribute:: motion

      A :class:`pygame2.events.EventHandler` that is invoked, if the mouse
      moves around while being over the :class:`TextEntry`.

   .. attribute:: pressed

      A :class:`pygame2.events.EventHandler` that is invoked, if a mouse button
      is pressed on the :class:`TextEntry`.

   .. attribute:: released

      A :class:`pygame2.events.EventHandler` that is invoked, if a mouse button
      is released on the :class:`TextEntry`.

   .. attribute:: keydown

      A :class:`pygame2.events.EventHandler` that is invoked on pressing a key.

   .. attribute:: keyup

      A :class:`pygame2.events.EventHandler` that is invoked on releasing a key.

   .. attribute:: input

      A :class:`pygame2.events.EventHandler` that is invoked on text input
      events.

   .. attribute:: editing

      A :class:`pygame2.events.EventHandler` that is invoked on text editing
      events.

   .. attribute:: events

      A dict containing the mapping of SDL2 events to the available
      :class:`pygame2.events.EventHandler` bindings of the :class:`TextEntry`.

   .. attribute:: text

      The text of the :class:`TextEntry`.

.. class:: UIProcessor()

   TODO

   .. attribute:: handlers

      A dict containing the mapping of SDL2 events to the available
      :class:`pygame2.events.EventHandler` bindings of the
      :class:`UIProcessor`.

   .. method:: activate(component : Component) -> None

      Activates a UI control to receive text input.

   .. method:: deactivate(component : Component) -> None

      Deactivate the currently active UI control.

   .. method:: passevent(component : Component, event : SDL_Event) -> None

      Passes the *event* to a *component* without any additional checks or
      restrictions.

   .. method:: mousemotion(component : Component, event : SDL_Event) -> None

      Checks, if the event's motion position is on the *component* and
      executes the component's event handlers on demand. If the motion event
      position is not within the area of the *component*, nothing will be
      done. In case the component is a :class:`Button`, its
      :attr:`Button.state` will be adjusted to reflect, if it is
      currently hovered or not.

   .. method:: mousedown(component : Component, event : SDL_Event) -> None

      Checks, if the event's button press position is on the *component* and
      executes the component's event handlers on demand. If the button press
      position is not within the area of the component, nothing will be done.

      In case the component is a :class:`Button`, its :attr:`Button.state`
      will be adjusted to reflect, if it is currently pressed or not.

      In case the component is a :class:`TextEntry` and the pressed button is
      the primary mouse button, the component will be marked as the next
      control to activate for text input.

   .. method:: mouseup(self, component, event):

    Checks, if the event's button release position is on the *component* and
    executes the component's event handlers on demand. If the button release
    position is not within the area of the component, nothing will be done.

    In case the component is a :class:`Button`, its :attr:`Button.state`
    will be adjusted to reflect, whether it is hovered or not.

    If the button release followed a button press on the same component and
    if the button is the primary button, the click() event handler is invoked,
    if the component is a :class:`Button`.

   .. method:: dispatch(obj : object, event : SDL_Event):

      Passes an event to the given object. If *obj* is a
      :class:`pygame2.ebs.World` object, UI relevant components will receive
      the event, if they support the event type. If *obj* is a single object,
      ``obj.events`` **must** be a dict consisting of SDL event type
      identifiers and :class:`pygame2.events.EventHandler` instances bound
      to the object. If *obj* is a iterable, such as a list or set, every
      item within *obj* **must** feature an ``events`` attribute as
      described above.

   .. method:: process(world : World, components : iterable) -> None

      The :class:`UIProcessor` class does not implement the process()``
      method by default. Instead it uses :meth:`dispatch()` to send events
      around to components. :meth:`process()` does nothing.
