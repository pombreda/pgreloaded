"""User interface examples."""
import sys

# Import the Color class, so we can create RGBA color values.
from pygame2.color import Color

# Try to import the video system and event system. Since pygame2.video makes
# use of pygame2.sdl, the import might fail, if the SDL DLL could not be
# loaded. In that case, just print the error and exit with a proper
# error code.
try:
    import pygame2.video as video
    import pygame2.sdl.events as sdlevents
except ImportError:
    import traceback
    traceback.print_exc()
    sys.exit(1)

WHITE = Color(255, 255, 255)


def onmotion(button, event):
    print("Mouse moves over the button!")


def onclick(button, event):
    print("Button was clicked!")


def run():
    # You know those from the helloworld.py example.
    # Initialize the video subsystem, create a window and make it visible.
    video.init()
    window = video.Window("Pixel Access", size=(800, 600))
    window.show()

    # Create a simple Button sprite, which reacts on mouse movements and
    # button presses and fill it with a white color. The Button class inherits
    # directly from the Sprite class, so everything you can do with the Sprite
    # class is also possible for the Button class.
    button = video.Button(size=(100, 100))
    video.fill(button, WHITE)
    button.position = 50, 50

    # Bind some actions to the button's event handlers. Whenever a click
    # (combination of a mouse button press and mouse button release), the
    # onclick() function will be called.
    # Whenever the mouse moves around in the area occupied by the button, the
    # onmotion() function will be called.
    # The event handlers receive the issuer of the event as first argument
    # (the button is the issuer of that event) and the SDL event data as second
    # argument for further processing, if necessary.
    button.click += onclick
    button.motion += onmotion

    # Since buttons are sprites, we can use the SpriteRenderer class, we
    # learned about in helloworld.py, to draw the button on the Window
    renderer = video.SpriteRenderer(window)
    renderer.render(button)

    #
    #
    uiprocessor = video.UIProcessor()

    while True:
        event = sdlevents.poll_event(True)
        if event is None:
            continue
        if event.type == sdlevents.SDL_QUIT:
            break
        uiprocessor.dispatch(button, event)
        window.refresh()

    video.quit()
    return 0

if __name__ == "__main__":
    sys.exit(run())