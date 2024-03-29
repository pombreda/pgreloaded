"""Direct pixel access examples."""
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

# Define black and white as global values, so we can access them throughout
# the code.
BLACK = Color(0, 0, 0)
WHITE = Color(255, 255, 255)


# This function will use a rectangular area and fill each second horizontal
# line with a white color on the passed surface.
def draw_horizontal_stripes(surface, x1, x2, y1, y2):
    # Fill the entire surface with a black color. In contrast to
    # colorpalettes.py we use a Color() value here, just to demonstrate that
    # it really works.
    video.fill(surface, BLACK)

    # Create a 2D view that allows us to directly access each individual pixel
    # of the surface. The PixelView class is quite slow, since it uses an non-
    # optimised read-write access to each individual pixel and offset. It works
    # on every platform, though.
    pixelview = video.PixelView(surface)

    # Loop over the area bounds, considering each fourth line and every column
    # on the 2D view. The PixelView uses a y-x alignment to access pixels.
    # This mkeans that the first accessible dimension of the PixelView denotes
    # the horizontal lines of an image, and the second the vertical lines.
    for y in range(y1, y2, 4):
        for x in range(x1, x2):
            # Change the color of each individual pixel. We can assign any
            # color-like value here, since the assignment method of the
            # PixelView will implicitly check and convert the value to a
            # matching color for its target surface.
            pixelview[y][x] = WHITE

    # Explicitly delete the PixelView. Some surface types need to be locked
    # in order to access their pixels directly. The PixelView will do that
    # implicitly at creation time. Once we are done with all necessary
    # operations, we need to unlock the surface, which will be done
    # automatically at the time the PixelView is garbage-collected.
    del pixelview

# as draw_horizontal_stripes(), but vertical
def draw_vertical_stripes(surface, x1, x2, y1, y2):
    video.fill(surface, BLACK)
    pixelview = video.PixelView(surface)
    for x in range(x1, x2, 4):
        for y in range(y1, y2):
            pixelview[y][x] = WHITE
    del pixelview


def run():
    # You know those from the helloworld.py example.
    # Initialize the video subsystem, create a window and make it visible.
    video.init()
    window = video.Window("Pixel Access", size=(800, 600))
    window.show()

    # As in colorpalettes.py, explicitly acquire the window's surface to
    # draw on.
    windowsurface = window.get_surface()

    # We implement the functionality as it was done in colorpalettes.py and
    # utilise a mapping table to look up the function to be executed, together
    # with the arguments they should receive
    functions = ((draw_horizontal_stripes, (windowsurface, 300, 500, 200, 400)),
                 (draw_vertical_stripes, (windowsurface, 300, 500, 200, 400)),
                 )

    # A storage variable for the function we are currently on, so that we know
    # which function to execute next.
    curindex = 0

    # The event loop is nearly the same as we used in colorpalettes.py. If you
    # do not know, what happens here, take a look at colorpalettes.py for a
    # detailled description.
    running = True
    while running:
        events = video.get_events()
        for event in events:
            if event.type == sdlevents.SDL_QUIT:
                running = False
                break
            if event.type == sdlevents.SDL_MOUSEBUTTONDOWN:
                curindex += 1
                if curindex >= len(functions):
                    curindex = 0
                # In contrast to colorpalettes.py, our mapping table consists
                # of functions and their arguments. Thus, we get the currently
                # requested function and argument tuple and execute the
                # function with the arguments.
                func, args = functions[curindex]
                func(*args)
                break
        window.refresh()
    video.quit()
    return 0

if __name__ == "__main__":
    sys.exit(run())
