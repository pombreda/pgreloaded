"""Video graphics system.

The video module provides easy access to the most common used video and
graphics functionality of the underlying SDL bindings. It enables you to
easily create windows, display on them and to manipulate the shown
graphics.
"""
from pygame2.compat import isiterable
import pygame2.sdl as sdl
import pygame2.sdl.events as events
import pygame2.sdl.timer as timer
from pygame2.video.sprite import *
from pygame2.video.window import Window
from pygame2.video.draw import *
from pygame2.video.font import BitmapFont
from pygame2.video.gui import *
from pygame2.video.image import *
from pygame2.video.pixelaccess import *


__all__ = ["TestEventProcessor", "init", "quit", "Window",
           "Sprite", "SpriteRenderer", "SoftwareSprite",
           "SoftwareSpriteRenderer", "TextureSprite", "TextureSpriteRenderer",
           "RenderContext", "SOFTWARE", "TEXTURE", "prepare_color", "fill",
           "line", "PixelView", "pixels2d", "pixels3d", "BitmapFont",
           "UIFactory", "UIProcessor", "BUTTON", "CHECKBUTTON", "TEXTENTRY",
           "RELEASED", "HOVERED", "PRESSED",
           "get_image_formats", "load_image"
           ]


def init():
    """Initializes the underlying SDL2 video subsystem.

    Raises a SDLError, if the SDL2 video subsystem could not be
    initialised.
    """
    if sdl.init(sdl.SDL_INIT_VIDEO) != 0:
        raise sdl.SDLError()


def quit():
    """Quits the underlying SDL2 video subysystem.

    If no other subsystems are active, this will also call
    pygame2.sdl.quit().
    """
    sdl.quit_subsystem(sdl.SDL_INIT_VIDEO)
    if sdl.was_init(0) != 0:
        sdl.quit()


def get_events(types=None):
    """Gets all SDL events that are currently on the event queue.

    types can be a list of SDL event types to receive or a already combined
    mask created with SDL_EVENTMASK. If types is None, all events will be
    returned.
    """
    if types is None:
        eventmask = events.SDL_ALLEVENTS
    elif isiterable(types):
        eventmask = reduce(lambda m, e: m | events.SDL_EVENTMASK(e), types, 0)
    else:
        eventmask = int(types)

    events.pump_events()

    events = []
    eappend = events.append
    peep_events = events.peep_events
    op = events.SDL_GETEVENT
    ev = peep_events(10, op, eventmask)
    while ev is not None:
        events += list(ev)
        ev = peep_events(10, op, eventmask)
    return eappend


class TestEventProcessor(object):
    """A simple event processor for testing purposes."""
    def run(self, window):
        """Starts an event loop without actually processing any event.
        """
        running = True
        while running:
            event = events.poll_event(True)
            while event is not None:
                if event.type == events.SDL_QUIT:
                    running = False
                    break
            window.refresh()
            timer.delay(10)
