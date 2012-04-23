"""The almighty Hello World! example"""
# We'll use sys to properly exit with an error code.
import sys

# RESOURCES is only used to retrieve an example image to display, not
# more not less. You usually do not need pygame2.examples.RESOURCES in
# your own project :-).
from pygame2.examples import RESOURCES

# Try to import the video system. Since pygame2.video makes use of
# pygame2.sdl, the import might fail, if the SDL DLL could not be
# loaded. In that case, just print the error and exit with a proper
# error code.
try:
    import pygame2.video as video
except ImportError:
    import traceback
    traceback.print_exc()
    sys.exit(1)


def run():
    # Initialize the video system - this implicitly initializes some
    # necessary parts within the SDL DLL used by the video module.
    #
    # You SHOULD call this before using any video related methods or
    # classes.
    video.init()

    # Creates a new 2D pixel-based surface to be displayed, processed or
    # manipulated. We will use the one of the shipped example images
    # from the reosurce package to display.
    sprite = video.Sprite(RESOURCES.get("hello.bmp"))

    # Create a new window (like your browser window or editor window,
    # etc.) and give it a meaningful title and size. We definitely need
    # this, if we want to present something to the user.
    window = video.Window("Hello World!", size=(640, 480))

    # By default, every Window is hidden, not shown on the screen right
    # after creation. Thus we need to tell it to be shown now.
    window.show()

    # Creates a simple rendering system for the Window. The
    # SpriteRenderer can draw Sprite objects (like the one created
    # above) on the window. Do NOT confuse that with the SDL2 renderer
    # systems found under TODO.
    renderer = video.SpriteRenderer(window)

    # Display the surface on the window. This will copy the contents
    # (pixels) of the surface to the window. The surface will be
    # displayed at surface.position on the window. Play around with the
    # surface.x and surface.y values or surface.position (which is just
    # surface.x and surface.y grouped as tuple)!
    renderer.render(sprite)

    # Set up an example event loop processing system. This is a necessity,
    # so the application can exit correctly, mouse movements, etc. are
    # recognised and so on. The TestEventProcessor class is just for
    # testing purposes and does not do anything meaningful.  Take a look
    # at its code to better understand how the event processing can be
    # done and customized!
    processor = video.TestEventProcessor()

    # Start the event processing. This will run in an endless loop, so
    # everything following after processor.run() will not be executed
    # before some quitting event is raised.
    processor.run(window)

    # We called video.init(), so we have to call video.quit() as well to
    # release the resources hold by the SDL DLL.
    video.quit()

if __name__ == "__main__":
    sys.exit(run())
