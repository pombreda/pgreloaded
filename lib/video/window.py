"""window routines to manage on-screen windows."""
import pygame2.sdl.video as video


class Window(object):
    """The Window class represents a visible on-screen object with an
    optional border and title text.

    It represents an area on the screen that can be accessed by the
    application for displaying graphics and receive and process user
    input.
    """
    DEFAULTFLAGS = video.SDL_WINDOW_HIDDEN

    def __init__(self, title, size, position=(0, 0), flags=None):
        """Creates a Window with a specific size and title.

        TODO
        """
        if flags is None:
            flags = self.DEFAULTFLAGS
        self.window = video.create_window(title, position[0], position[1],
                                          size[0], size[1], flags)

    def show(self):
        """Show the window on the display."""
        video.show_window(self.window)

    def hide(self):
        """Hides the window."""
        video.hide_window(self.window)

    def maximize(self):
        """Maximizes the window to the display's dimensions."""
        video.maximize_window(self.window)

    def minimize(self):
        """Minimizes the window to an iconified state in the system tray."""
        video.minimize_window(self.window)

    def refresh(self):
        """Refreshes the entire window surface."""
        video.update_window_surface(self.window)
