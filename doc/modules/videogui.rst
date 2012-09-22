.. module:: pygame2.video.gui
   :synopsis: User interface elements

:mod:`pygame2.video.gui` - user interface elements
==================================================

.. inheritance-diagram:: pygame2.video.gui
   :parts: 1

.. data:: RELEASED

   Indicates that the UI element is released.

.. data:: HOVERED

   Indicates that the mouse pointer is currently hovering the UI element.

.. data:: PRESSED

   Indicates that a mouse button is pressed on the UI element.

.. class:: Button(*args, **kwargs)

   A :class:`pygame2.video.sprite.Sprite` object that can react on mouse
   events.

   *args* and *kwargs* are passed to the
   :class:`pygame2.video.sprite.Sprite` constructor.

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

.. class:: CheckButton(*args, **kwargs)

   A specialised :class:`Button` that retains its state.

   .. attribute:: checked

      Indicates, if the :class:`CheckButton` is checked or not.

.. class:: TextEntry(*args, **kwargs)

   A :class:`pygame2.video.sprite.Sprite` object that can react on text
   input.

   *args* and *kwargs* are passed to the
   :class:`pygame2.video.sprite.Sprite` constructor.

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

.. class:: SoftButton(*args, **kwargs)

   A :class:`pygame2.video.sprite.SoftSprite` object that can react on
   mouse events.

   *args* and *kwargs* are passed to the
   :class:`pygame2.video.sprite.SoftSprite` constructor.

   .. attribute:: state

      The current state of the button. This can be a value of
      ``RELEASED``, ``HOVERED`` or ``PRESSED``

   .. attribute:: motion

      A :class:`pygame2.events.EventHandler` that is invoked, if the mouse
      moves around while being over the :class:`SoftButton`.

   .. attribute:: pressed

      A :class:`pygame2.events.EventHandler` that is invoked, if a mouse button
      is pressed on the :class:`SoftButton`.

   .. attribute:: released

      A :class:`pygame2.events.EventHandler` that is invoked, if a mouse button
      is released on the :class:`SoftButton`.

   .. attribute:: click

      A :class:`pygame2.events.EventHandler` that is invoked, if a mouse
      button is pressed and released on the :class:`SoftButton`.

   .. attribute:: events

      A dict containing the mapping of SDL2 events to the available
      :class:`pygame2.events.EventHandler` bindings of the :class:`SoftButton`.

.. class:: SoftCheckButton(*args, **kwargs)

   A specialised :class:`SoftButton` that retains its state.

   .. attribute:: checked

      Indicates, if the :class:`SoftCheckButton` is checked or not.

.. class:: TextEntry(*args, **kwargs)

   A :class:`pygame2.video.sprite.SoftSprite` object that can react on
   text input.

   *args* and *kwargs* are passed to the
   :class:`pygame2.video.sprite.SoftSprite` constructor.

   .. attribute:: motion

      A :class:`pygame2.events.EventHandler` that is invoked, if the mouse
      moves around while being over the :class:`SoftTextEntry`.

   .. attribute:: pressed

      A :class:`pygame2.events.EventHandler` that is invoked, if a mouse button
      is pressed on the :class:`SoftTextEntry`.

   .. attribute:: released

      A :class:`pygame2.events.EventHandler` that is invoked, if a mouse button
      is released on the :class:`SoftTextEntry`.

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
      :class:`pygame2.events.EventHandler` bindings of the
      :class:`SoftTextEntry`.

   .. attribute:: text

      The text of the :class:`SoftTextEntry`.

.. class:: UIFactory(uitype=UIFactory.RENDERER[, **kwargs])

   A factory class for creating UI elements. The :class:`UIFactory`
   allows you to create any UI element for either software-based
   :class:`pygame2.video.sprite.SoftSprite` or hardware-accelerated
   :class:`pygame2.video.sprite.Sprite` objects.

   Depending on the *uitype*, the factory will create either the one or
   the other. Since the constructors of both sprite types differ, a set
   of *kwargs* can be provided, which will be used as default arguments
   to pass to the factory methods.

   .. data:: RENDERER

      Indicates that :class:`pygame2.video.sprite.Sprite` based UI
      elements should be created.

   .. data:: SOFTWARE

      Indicates that :class:`pygame2.video.sprite.SoftSprite` based UI
      elements should be created.

   .. attribute:: default_args

      A dictionary containing the default arguments to be passed to the
      factory methods.

   .. attribute:: uitype

      The creation type of the :class:`UIFactory`. This will be either
      :data:`RENDERER` or :data:`SOFTWARE`.

   .. method:: create_button(**kwargs) -> Button or SoftButton

      Creates a new button UI element, either of type :class:`Button` or
      :class:`SoftButton`. *kwargs* can be used to provide additional
      arguments to the constructor and to overridethe
      :attr:`default_args`.

   .. method:: create_check_button(**kwargs) -> CheckButton or SoftCheckButton

      Creates a new checkbutton UI element, either of type
      :class:`CheckButton` or :class:`SoftCheckButton`. *kwargs* can be
      used to provide additional arguments to the constructor and to
      overridethe :attr:`default_args`.

   .. method:: create_text_entry(**kwargs) -> TextEntry or SoftTextEntry

      Creates a new textentry UI element, either of type
      :class:`TextEntry` or :class:`SoftTextEntry`. *kwargs* can be used
      to provide additional arguments to the constructor and to
      overridethe :attr:`default_args`.

.. class:: UIProcessor()

   A processing system for user interface elements and events.

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

   .. method:: mouseup(self, component, event) -> None

      Checks, if the event's button release position is on the *component* and
      executes the component's event handlers on demand. If the button release
      position is not within the area of the component, nothing will be done.

      In case the component is a :class:`Button`, its :attr:`Button.state`
      will be adjusted to reflect, whether it is hovered or not.

      If the button release followed a button press on the same component and
      if the button is the primary button, the click() event handler is invoked,
      if the component is a :class:`Button`.

   .. method:: dispatch(obj : object, event : SDL_Event) -> None

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
