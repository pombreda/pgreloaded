"""Window routines to manage on-screen windows."""
import pygame2.sdl.video as sdlvideo

__all__ = ["Window"]


class Window(object):
    """The Window class represents a visible on-screen object with an
    optional border and title text.

    It represents an area on the screen that can be accessed by the
    application for displaying graphics and receive and process user
    input.
    """
    DEFAULTFLAGS = sdlvideo.SDL_WINDOW_HIDDEN

    def __init__(self, title, size, position=(0, 0), flags=None):
        """Creates a Window with a specific size and title.

        The created Window is hidden by default, which can be overriden
        at the time of creation by providing other SDL window flags
        through the flags parameter.

        The default flags for creating Window instances can be adjusted
        through the DEFAULTFLAGS class variable. Example:

            Window.DEFAULTFLAGS = pygame2.sdl.video.SDL_WINDOW_SHOWN
        """
        if flags is None:
            flags = self.DEFAULTFLAGS
        self.window = sdlvideo.create_window(title, position[0], position[1],
                                             size[0], size[1], flags)

    def __del__(self):
        """Releases the resources of the Window, implicitly destroying the
        underlying SDL2 window."""
        if getattr(self, "window", None):
            sdlvideo.destroy_window(self.window)
            self.window = None

    @property
    def title(self):
        """The title of the window."""
        return sdlvideo.get_window_title(self.window)

    @title.setter
    def title(self, value):
        """The title of the window."""
        sdlvideo.set_window_title(self.window, value)

    @property
    def size(self):
        """The size of the window."""
        return sdlvideo.get_window_size(self.window)

    def show(self):
        """Show the window on the display."""
        sdlvideo.show_window(self.window)

    def hide(self):
        """Hides the window."""
        sdlvideo.hide_window(self.window)

    def maximize(self):
        """Maximizes the window to the display's dimensions."""
        sdlvideo.maximize_window(self.window)

    def minimize(self):
        """Minimizes the window to an iconified state in the system tray."""
        sdlvideo.minimize_window(self.window)

    def refresh(self):
        """Refreshes the entire window surface."""
        sdlvideo.update_window_surface(self.window)

    def get_surface(self):
        """Gets the SDL_Surface used by the Window to display 2D pixel
        data.

        Using this method will make the usage of GL operations, such
        as texture handling, or using SDL renderers impossible.
        """
        return sdlvideo.get_window_surface(self.window)
