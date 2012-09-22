"""User interface elements."""
from pygame2.compat import isiterable
from pygame2.ebs import Component, System, World
from pygame2.events import EventHandler
from pygame2.video.sprite import Sprite, SoftSprite
from pygame2.sdl.rect import SDL_Rect
import pygame2.sdl.pixels as pixels
import pygame2.sdl.events as events
import pygame2.sdl.mouse as mouse
import pygame2.sdl.keyboard as keyboard

__all__ = ["RELEASED", "HOVERED", "PRESSED",
           "CheckButton", "Button", "TextEntry",
           "SoftCheckButton", "SoftButton", "SoftTextEntry",
           "UIProcessor", "UIFactory"
           ]


RELEASED = 0x0000
HOVERED =  0x0001
PRESSED =  0x0002


class UIFactory(object):
    """A simple UI factory for creating GUI elements for software- or
    texture-based rendering."""
    RENDERER = 0
    SOFTWARE = 1
    def __init__(self, uitype=RENDERER, **kwargs):
        """Creates a new UIFactory.

        uitype can be RENDERER for texture-based UI elements or SOFTWARE
        for software-buffer-based UI elements.

        The additional kwargs will be stored internall and passed to the
        UI creation methods as arguments. Hence they can act as default
        arguments to be passed to each and every UI element to be
        created.
        """
        self._uitype = uitype
        if uitype == UIFactory.RENDERER:
            self.default_args = kwargs
            self._button = Button
            self._checkbutton = CheckButton
            self._textentry = TextEntry
        elif uitype == UIFactory.SOFTWARE:
            self.default_args = kwargs
            self._button = SoftButton
            self._checkbutton = SoftCheckButton
            self._textentry = SoftTextEntry
        else:
            raise ValueError("unsupported UIFactory type")

    @property
    def uitype(self):
        """The UI element type created by the factory."""
        return self._uitype

    def create_button(self, **kwargs):
        """Creates a new Button UI element."""
        args = self.default_args.copy()
        args.update(kwargs)
        return self._button(**args)

    def create_check_button(self, **kwargs):
        """Creates a new CheckButton UI element."""
        args = self.default_args.copy()
        args.update(kwargs)
        return self._checkbutton(**args)

    def create_text_entry(self, **kwargs):
        """Creates a new TextEntry UI element."""
        args = self.default_args.copy()
        args.update(kwargs)
        return self._textentry(**args)

    def __repr__(self):
        uitype = "RENDERER"
        if self.uitype == SOFTWARE:
            uitype = "SOFTWARE"
        return "UIFactory(uitype=%s, default_args=%s)" % (uitype,
                                                          self.default_args)

def _compose_button(obj):
    """Binds button attributes to the object, so it can be properly
    processed by the UIProcessor.

    Note: this is an internal helper method to avoid multiple
    inheritance and composition issues and should not be used by user
    code.
    """
    obj.state = RELEASED
    obj.motion = EventHandler(obj)
    obj.pressed = EventHandler(obj)
    obj.released = EventHandler(obj)
    obj.click = EventHandler(obj)
    obj.events = {
        events.SDL_MOUSEMOTION: obj.motion,
        events.SDL_MOUSEBUTTONDOWN: obj.pressed,
        events.SDL_MOUSEBUTTONUP: obj.released
        }


def _compose_text_entry(obj):
    """Binds text entry attributes to the object, so it can be properly
    processed by the UIProcessor.

    Note: this is an internal helper method to avoid multiple
    inheritance and composition issues and should not be used by user
    code.
    """
    obj.text = ""
    obj.motion = EventHandler(obj)
    obj.pressed = EventHandler(obj)
    obj.released = EventHandler(obj)
    obj.keydown = EventHandler(obj)
    obj.keyup = EventHandler(obj)
    obj.input = EventHandler(obj)
    obj.editing = EventHandler(obj)
    obj.events = {
        events.SDL_MOUSEMOTION: obj.motion,
        events.SDL_MOUSEBUTTONDOWN: obj.pressed,
        events.SDL_MOUSEBUTTONUP: obj.released,
        events.SDL_TEXTEDITING: obj.editing,
        events.SDL_TEXTINPUT: obj.input,
        events.SDL_KEYDOWN: obj.keydown,
        events.SDL_KEYUP: obj.keyup
        }


class Button(Sprite):
    """A Sprite object that can react on mouse events."""
    def __init__(self, *args, **kwargs):
        """Creates a new Button.

        If a source is provided, the constructor assumes it to be a
        readable buffer object or file path to load the pixel data from.
        The size and bpp will be ignored in those cases.

        If no source is provided, a size tuple containing the width and
        height of the button and a bpp value, indicating the bits per
        pixel to be used, need to be provided.
        """
        super(Button, self).__init__(*args, **kwargs)
        _compose_button(self)

    def __repr__(self):
        format, access, w, h = render.query_texture(self.texture)
        static = "True"
        if access == render.SDL_TEXTUREACCESS_STREAMING:
            static = "False"
        return "Button(format=%d, static=%s, size=%s)" % \
            (format, static, (w, h))


class SoftButton(SoftSprite):
    """A SoftSprite object that can react on mouse events."""
    def __init__(self, *args, **kwargs):
        """Creates a new Button.

        If a source is provided, the constructor assumes it to be a
        readable buffer object or file path to load the pixel data from.
        The size and bpp will be ignored in those cases.

        If no source is provided, a size tuple containing the width and
        height of the button and a bpp value, indicating the bits per
        pixel to be used, need to be provided.
        """
        super(SoftButton, self).__init__(*args, **kwargs)
        _compose_button(self)

    def __repr__(self):
        return "SoftButton(size=%s, bpp=%d)" % \
            (self.size, self.surface.format.BitsPerPixel)


class CheckButton(Button):
    """A specialised Button that retains its state."""
    def __init__(self, *args, **kwargs):
        """Creates a new CheckButton.

        If a source is provided, the constructor assumes it to be a
        readable buffer object or file path to load the pixel data from.
        The size and bpp will be ignored in those cases.

        If no source is provided, a size tuple containing the width and
        height of the button and a bpp value, indicating the bits per
        pixel to be used, need to be provided.
        """
        super(CheckButton, self).__init__(*args, **kwargs)
        self.checked = False

    def __repr__(self):
        format, access, w, h = render.query_texture(self.texture)
        static = "True"
        if access == render.SDL_TEXTUREACCESS_STREAMING:
            static = "False"
        return "CheckButton(format=%d, static=%s, size=%s)" % \
            (format, static, (w, h))


class SoftCheckButton(SoftButton):
    """A specialised SoftButton that retains its state."""
    def __init__(self, *args, **kwargs):
        """Creates a new SoftCheckButton.

        If a source is provided, the constructor assumes it to be a
        readable buffer object or file path to load the pixel data from.
        The size and bpp will be ignored in those cases.

        If no source is provided, a size tuple containing the width and
        height of the button and a bpp value, indicating the bits per
        pixel to be used, need to be provided.
        """
        super(SoftCheckButton, self).__init__(*args, **kwargs)
        self.checked = False

    def __repr__(self):
        return "SoftCheckButton(size=%s, bpp=%d)" % \
            (self.size, self.surface.format.BitsPerPixel)


class TextEntry(Sprite):
    """A Sprite object that can react on text input."""
    def __init__(self, *args, **kwargs):
        """Creates a new TextEntry.

        If a source is provided, the constructor assumes it to be a
        readable buffer object or file path to load the pixel data from.
        The size and bpp will be ignored in those cases.

        If no source is provided, a size tuple containing the width and
        height of the button and a bpp value, indicating the bits per
        pixel to be used, need to be provided.
        """
        super(TextEntry, self).__init__(*args, **kwargs)
        _compose_text_entry(self)

    def __repr__(self):
        format, access, w, h = render.query_texture(self.texture)
        static = "True"
        if access == render.SDL_TEXTUREACCESS_STREAMING:
            static = "False"
        return "TextEntry(format=%d, static=%s, size=%s)" % \
            (format, static, (w, h))


class SoftTextEntry(SoftSprite):
    """A SoftSprite object that can react on text input."""
    def __init__(self, *args, **kwargs):
        """Creates a new SoftTextEntry.

        If a source is provided, the constructor assumes it to be a
        readable buffer object or file path to load the pixel data from.
        The size and bpp will be ignored in those cases.

        If no source is provided, a size tuple containing the width and
        height of the button and a bpp value, indicating the bits per
        pixel to be used, need to be provided.
        """
        super(SoftTextEntry, self).__init__(*args, **kwargs)
        _compose_text_entry(self)

    def __repr__(self):
        return "SoftTextEntry(size=%s, bpp=%d)" % \
            (self.size, self.surface.format.BitsPerPixel)


class UIProcessor(System):
    """A processing system for user interface elements and events."""
    def __init__(self):
        """Creates a new UIProcessor."""
        super(UIProcessor, self).__init__()
        self.componenttypes = (Button, TextEntry, SoftButton, SoftTextEntry)
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

        if isinstance(component, (TextEntry, SoftTextEntry)):
            area = SDL_Rect(component.x, component.y,
                            component.size[0], component.size[1])
            keyboard.set_text_input_rect(area)
            keyboard.start_text_input()
        self._activecomponent = component

    def deactivate(self, component):
        """Deactivates the currently active control."""
        if component == self._activecomponent:
            if isinstance(self._activecomponent, (TextEntry, SoftTextEntry)):
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
            if isinstance(component, (TextEntry, SoftTextEntry)):
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
            if isinstance(component, (Button, SoftButton)):
                component.state |= HOVERED
        elif isinstance(component, (Button, SoftButton)):
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
            if isinstance(component, (Button, SoftButton)):
                component.state = PRESSED | HOVERED
                if isinstance(component, (CheckButton, SoftCheckButton)):
                    if event.button.button == mouse.SDL_BUTTON_LEFT:
                        component.checked = not component.checked
            elif isinstance(component, (TextEntry, SoftTextEntry)):
                if event.button.button == mouse.SDL_BUTTON_LEFT:
                    # Since we loop over all components, and might deactivate
                    # some, store it temporarily for later activation.
                    self._nextactive = component
        elif isinstance(component, (Button, SoftButton)):
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
            if isinstance(component, (Button, SoftButton)):
                if (component.state & PRESSED) == PRESSED:
                    # Was pressed already, now it is a click
                    component.click(event)
                component.state = RELEASED | HOVERED
        elif isinstance(component, (Button, SoftButton)):
            component.state &= ~HOVERED

    def dispatch(self, obj, event):
        """Passes an event to the given object.

        If obj is a World object, UI relevant components will receive
        the event, if they support the event type.

        If obj is a single object, obj.events MUST be a dictionary
        consisting of SDL event type identifiers and EventHandler
        instances bound to the object.
        If obj is an iterable, such as a list or set, every item within
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

    def __repr__(self):
        return "UIProcessor()"
