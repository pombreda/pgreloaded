"""Video graphics system.

The video module provides easy access to the most common used video and
graphics functionality of the underlying SDL bindings. It enables you to
easily create windows, display on them and to manipulate the shown
graphics.
"""
import pygame2.sdl as sdl
import pygame2.sdl.events as events
import pygame2.sdl.timer as timer
from pygame2.video.sprite import Sprite, SpriteRenderer
from pygame2.video.window import Window

__all__ = ["Window", "Sprite", "SpriteRenderer", "TestEventProcessor",
           "init", "quit"]


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


class TestEventProcessor(object):
    """A simple event processor for testing purposes."""
    def run(self, window):
        """Starts an event loop without actually processing any event.
        """
        while True:
            event = events.poll_event(True)
            if event is None:
                timer.delay(10)
            elif event.type == events.SDL_QUIT:
                return
            else:
                window.refresh()
