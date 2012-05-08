"""User interface elements."""
from pygame2.compat import *
from pygame2.ebs import Component, System, World
from pygame2.events import EventHandler
from pygame2.video import Sprite
import pygame2.sdl.events as events
import pygame2.sdl.mouse as mouse

__all__ = ["Button", "UIProcessor"]


RELEASED = 0x0000
HOVERED =  0x0001
PRESSED =  0x0002


class Button(Sprite):
    """A Sprite object that can react on mouse events."""
    def __init__(self, source=None, size=(0, 0), bpp=32):
        """Creates a new Button.

        If a source is provided, the constructor assumes it to be a
        readable buffer object or file path to load the pixel data from.
        The size and bpp will be ignored in those cases.

        If no source is provided, a size tuple containing the width and
        height of the button and a bpp value, indicating the bits per
        pixel to be used, need to be provided.
        """
        super(Button, self).__init__(source, size, bpp)

        self.state = RELEASED
        self.motion = EventHandler(self)
        self.pressed = EventHandler(self)
        self.released = EventHandler(self)
        self.click = EventHandler(self)
        self.events = {
            events.SDL_MOUSEMOTION: self.motion,
            events.SDL_MOUSEBUTTONDOWN: self.pressed,
            events.SDL_MOUSEBUTTONUP: self.released
            }


class UIProcessor(System):
    """
    """
    def __init__(self):
        """Creates a new UIProcessor."""
        self.componenttypes = (Button, )
        self.handlers = {
            events.SDL_MOUSEMOTION: self.mousemotion,
            events.SDL_MOUSEBUTTONDOWN: self.mousedown,
            events.SDL_MOUSEBUTTONUP: self.mouseup,
            }

    def passevent(self, component, event):
        """Passes the event to a component without any additional checks
        or restrictions.
        """
        component.events[event.type](event)

    def mousemotion(self, component, event):
        """Checks, if the event's motion position is on the component
        and executes the component's event handlers on demand.

        If the motion event position is not within the area of the
        component, nothing will be done. In case the component is a
        Button, its state will be adjusted to reflect, if it is
        currently hovered or not.
        """
        x1, y1, x2, y2 = component.area
        if event.motion.x >= x1 and event.motion.x < x2 and \
                event.motion.y >= y1 and event.motion.y < y2:
            # Within the area of the component, raise the event on it.
            component.events[event.type](event)
            if isinstance(component, Button):
                component.state |= HOVERED
        elif isinstance(component, Button):
            # The mouse is not within the area of the button, reset the
            # state
            component.state &= ~HOVERED

    def mousedown(self, component, event):
        """Checks, if the event's button press position is on the
        component and executes the component's event handlers on demand.

        If the button press position is not within the area of the
        component, nothing will be done. In case the component is a
        Button, its state will be adjusted to reflect, if it is
        currently pressed or not.
        """
        x1, y1, x2, y2 = component.area
        if event.button.x >= x1 and event.button.x < x2 and \
                event.button.y >= y1 and event.button.y < y2:
            # Within the area of the component, raise the event on it.
            component.events[event.type](event)
            if isinstance(component, Button):
                component.state = PRESSED | HOVERED
        elif isinstance(component, Button):
            component.state &= ~PRESSED

    def mouseup(self, component, event):
        """Checks, if the event's button release position is on the
        component and executes the component's event handlers on demand.

        If the button release position is not within the area of the
        component, nothing will be done. In case the component is a
        Button, its state will be adjusted to reflect, whether it is
        hovered or not. If the button release followed a button press on
        the same component and if the button is the primary button, the
        click() event handler is invoked, if the component is a Button.
        """
        x1, y1, x2, y2 = component.area
        if event.button.x >= x1 and event.button.x < x2 and \
                event.button.y >= y1 and event.button.y < y2:
            # Within the area of the component, raise the event on it.
            component.events[event.type](event)
            if isinstance(component, Button):
                if (component.state & PRESSED) == PRESSED:
                    # Was pressed already, now it is a click
                    component.click(event)
                component.state = RELEASED | HOVERED
        elif isinstance(component, Button):
            component.state &= ~HOVERED

    def dispatch(self, obj, event):
        """Passes an event to the given object.

        If obj is a World object, UI relevant components will receive
        the event, if they support the event type.

        If obj is a single object, obj.events MUST be a dictionary
        consisting of SDL event type identifiers and EventHandler
        instances bound to the object.
        If obj is a iterable, such as a list or set, every item within
        obj MUST feature an 'events' attribute as described above.
        """
        if event is None:
            return
        if event.type not in self.handlers:
            return  # TODO - better warn or fail?

        handler = self.passevent
        if event.type in self.handlers:
            handler = self.handlers[event.type]

        if isinstance(obj, World):
            for ctype in self.componenttypes:
                items = world.get_components(ctype)
                items = [(v, e) for v in items for e in (event,)
                         if e.type in v.events]
                map(handler, items)
        elif isiterable(obj):
            items = [(v, e) for v in obj for e in (event,)
                     if e.type in v.events]
            map(handler, items)
        elif event.type in obj.events:
            handler(obj, event)

    def process(self, world, components):
        """The UIProcessor class does not implement the process() method
        by default. Instead it uses dispatch() to send events around to
        components.
        """
        pass
