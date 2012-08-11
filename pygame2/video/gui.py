"""User interface elements."""
from pygame2.compat import *
from pygame2.ebs import Component, System, World
from pygame2.events import EventHandler
from pygame2.video import Sprite
from pygame2.sdl.rect import SDL_Rect
import pygame2.sdl.events as events
import pygame2.sdl.mouse as mouse
import pygame2.sdl.keyboard as keyboard

__all__ = ["RELEASED", "HOVERED", "PRESSED",
           "CheckButton", "Button", "TextEntry",
           "UIProcessor"
           ]


RELEASED = 0x0000
HOVERED =  0x0001
PRESSED =  0x0002


class Button(Sprite):
    """A Sprite object that can react on mouse events."""
    def __init__(self, source=None, size=(0, 0), bpp=32, freesf=False):
        """Creates a new Button.

        If a source is provided, the constructor assumes it to be a
        readable buffer object or file path to load the pixel data from.
        The size and bpp will be ignored in those cases.

        If no source is provided, a size tuple containing the width and
        height of the button and a bpp value, indicating the bits per
        pixel to be used, need to be provided.
        """
        super(Button, self).__init__(source, size, bpp, freesf)
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


class CheckButton(Button):
    """A specialised Button that retains its state."""
    def __init__(self, source=None, size=(0, 0), bpp=32, freesf=False):
        """Creates a new CheckButton.

        If a source is provided, the constructor assumes it to be a
        readable buffer object or file path to load the pixel data from.
        The size and bpp will be ignored in those cases.

        If no source is provided, a size tuple containing the width and
        height of the button and a bpp value, indicating the bits per
        pixel to be used, need to be provided.
        """
        super(CheckButton, self).__init__(source, size, bpp, freesf)
        self.checked = False


class TextEntry(Sprite):
    """A Sprite object that can react on text input."""
    def __init__(self, source=None, size=(0, 0), bpp=32, freesf=False):
        """Creates a new TextEntry.

        If a source is provided, the constructor assumes it to be a
        readable buffer object or file path to load the pixel data from.
        The size and bpp will be ignored in those cases.

        If no source is provided, a size tuple containing the width and
        height of the button and a bpp value, indicating the bits per
        pixel to be used, need to be provided.
        """
        super(TextEntry, self).__init__(source, size, bpp, freesf)
        self.text = ""
        self.motion = EventHandler(self)
        self.pressed = EventHandler(self)
        self.released = EventHandler(self)
        self.keydown = EventHandler(self)
        self.keyup = EventHandler(self)
        self.input = EventHandler(self)
        self.editing = EventHandler(self)
        self.events = {
            events.SDL_MOUSEMOTION: self.motion,
            events.SDL_MOUSEBUTTONDOWN: self.pressed,
            events.SDL_MOUSEBUTTONUP: self.released,
            events.SDL_TEXTEDITING: self.editing,
            events.SDL_TEXTINPUT: self.input,
            events.SDL_KEYDOWN: self.keydown,
            events.SDL_KEYUP: self.keyup
            }


class UIProcessor(System):
    """A processing system for user interface elements and events.

    TODO
    """
    def __init__(self):
        """Creates a new UIProcessor."""
        super(UIProcessor, self).__init__()
        self.componenttypes = (Button, TextEntry)
        self._nextactive = None
        self._activecomponent = None
        self.handlers = {
            events.SDL_MOUSEMOTION: self.mousemotion,
            events.SDL_MOUSEBUTTONDOWN: self.mousedown,
            events.SDL_MOUSEBUTTONUP: self.mouseup,
            events.SDL_TEXTINPUT: self.textinput
            }

    def activate(self, component):
        """Activates a control to receive input."""
        if self._activecomponent != component:
            self.deactivate(self._activecomponent)

        if isinstance(component, TextEntry):
            area = SDL_Rect(component.x, component.y,
                            component.size[0], component.size[1])
            keyboard.set_text_input_rect(area)
            keyboard.start_text_input()
        self._activecomponent = component

    def deactivate(self, component):
        """Deactivates the currently active control."""
        if component == self._activecomponent:
            if isinstance(self._activecomponent, TextEntry):
                keyboard.stop_text_input()
            self._activecomponent = None

    def passevent(self, component, event):
        """Passes the event to a component without any additional checks
        or restrictions.
        """
        component.events[event.type](event)

    def textinput(self, component, event):
        """Checks, if an active component is available and matches the
        passed component and passes the event on to that component."""
        if self._activecomponent == component:
            if isinstance(component, TextEntry):
                component.text += event.text.text
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
        currently pressed or not. In case the component is a TextEntry and
        the pressed button is the primary mouse button, the component will
        be marked as the next control to activate for text input.
        """
        x1, y1, x2, y2 = component.area
        if event.button.x >= x1 and event.button.x < x2 and \
                event.button.y >= y1 and event.button.y < y2:
            # Within the area of the component, raise the event on it.
            component.events[event.type](event)
            if isinstance(component, Button):
                component.state = PRESSED | HOVERED
                if isinstance(component, CheckButton):
                    if event.button.button == mouse.SDL_BUTTON_LEFT:
                        component.checked = not component.checked
            elif isinstance(component, TextEntry):
                if event.button.button == mouse.SDL_BUTTON_LEFT:
                    # Since we loop over all components, and might deactivate
                    # some, store it temporarily for later activation.
                    self._nextactive = component
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

        handler = self.handlers.get(event.type, self.passevent)
        if isinstance(obj, World):
            for ctype in self.componenttypes:
                items = obj.get_components(ctype)
                items = [(v, e) for v in items for e in (event,)
                         if e.type in v.events]
                if len(items) > 0:
                    arg1, arg2 = zip(*items)
                    map(handler, arg1, arg2)
        elif isiterable(obj):
            items = [(v, e) for v in obj for e in (event,)
                     if e.type in v.events]
            if len(items) > 0:
                arg1, arg2 = zip(*items)
                map(handler, arg1, arg2)
        elif event.type in obj.events:
            handler(obj, event)
        if self._nextactive is not None:
            self.activate(self._nextactive)
            self._nextactive = None

    def process(self, world, components):
        """The UIProcessor class does not implement the process() method
        by default. Instead it uses dispatch() to send events around to
        components.
        """
        pass
