"""A simple example for filling rectangular areas."""
import sys

# Import the pre-defined color palettes
import pygame2.colorpalettes as colorpalettes

# Try to import the video system. Since pygame2.video makes use of
# pygame2.sdl, the import might fail, if the SDL DLL could not be
# loaded. In that case, just print the error and exit with a proper
# error code.
try:
    import pygame2.video as video
    import pygame2.sdl.events as sdlevents
except ImportError:
    import traceback
    traceback.print_exc()
    sys.exit(1)


# This function will draw the passed palette colors onto the window surface.
# The function does not require the window surface itself, any surface is fine,
# since the window surface acquired in run() does not differ from any other
# surface (not entirely true, but it offers and supports the same
# functionality).
def draw_palette(surface, palette):
    # Fill the entire surface with a black color. This is done by simply
    # passing a 0 value to the fill argument. We could also create a
    # Color(0, 0, 0) instance here, but this would be the same.
    video.fill(surface, 0)

    # Calculate the average width (roughly cut) to be used for each palette
    # value. When running the example, you will notice a black gap on the
    # right for some palettes. This s caused by the implicit cut behaviour
    # of the // operator. Since we can only operate pixel-wise, there are
    # no fractions to be used.
    width, height = surface.size
    rw = width // len(palette)

    # Create the area to be filled with the palette values. we always start
    # at the top-left corner, use the calculated width and the entire height
    # of the window surface. As you will see below, we then only advance
    # horizontically by the calculated width to draw stripes.
    # Play around with different height values and start offsets to see what
    # happens
    rect = [0, 0, rw, height]

    # Loop over all colors and fill a portion of the surface with them. As
    # above, we use fill() to fill the surface with the palette color, but now
    # we provide an area (the third argument) to avoid filling the whole
    # surface. Instead, the provided area makes sure, that we only fill a
    # certain part.
    for color in palette:
        video.fill(surface, color, rect)
        rect[0] += rw


def run():
    # You know those from the helloworld.py example.
    # Initialize the video subsystem, create a window and make it visible.
    video.init()
    window = video.Window("Color Palettes", size=(800, 600))
    window.show()

    # Explicitly acquire the window's surface to draw on. We used the
    # SpriteRenderer class in helloworld.py, which did the drawing magic for
    # us. Now we will do it ourselves, so we have to get a surface to draw on.
    # NOTE: if you intend to use textures or the SDL renderers, you must not
    # use the method.
    windowsurface = window.get_surface()

    # A simple mapping table for the builtin color palettes. We will use
    # the table to look up the color palette to draw an the title to set below.
    palettes = (
        ("Mono Palette", colorpalettes.MONOPALETTE),
        ("2-bit Gray Palette", colorpalettes.GRAY2PALETTE),
        ("4-bit Gray Palette", colorpalettes.GRAY4PALETTE),
        ("8-bit Gray Palette", colorpalettes.GRAY8PALETTE),
        ("3-bit RGB Palette", colorpalettes.RGB3PALETTE),
        ("CGA Palette", colorpalettes.CGAPALETTE),
        ("EGA Palette", colorpalettes.EGAPALETTE),
        ("VGA Palette", colorpalettes.VGAPALETTE),
        ("Web Palette", colorpalettes.WEBPALETTE),
        )

    # A storage variable for the palette we are currently on, so that we know
    # which palette to draw next.
    curindex = 0

    # Since it is not that nice to have a black window right at the start of
    # the application, we will set the window's title to the first entry
    # of our mapping tables. Afterwards, we will draw the matching palette
    # to the window surface.
    window.title = palettes[0][0]
    draw_palette(windowsurface, palettes[0][1])

    # The event loop. In helloworld.py we used the TestEventProcessor class,
    # since there was not much to do. Now however, we want to react on the user
    # input. Every time the user clicks around in our window, we want to
    # show the next palette. Once we reached the last palette within the
    # mapping table, we will start again with the first one.
    while True:
        # This will check for any events that piled up since the last check.
        # If an event was found (such as a click, a mouse movement, keyboard
        # input, etc.), we will retrieve it. By passing True to poll_event(),
        # also will let the system know that it does not need to keep the
        # event anymore. If we'd just want to inspect the events, without
        # actually doing anything with them, we would pass False to it, so
        # that a next call to poll_event() can receive tha specific event, too.
        event = sdlevents.poll_event(True)

        # In case there was no event, we do not need to do anything. This
        # might happen, if  e.g. the user works with another application. Since
        # poll_event() does not wait for an event to occur (that'd mean your
        # application blocks until there is an event), we have to handle
        # this.
        if event is None:
            # delay
            continue

        # The received event can contain different information. There might
        # be mouse movements, clicks, keyboard hits and many more. All of
        # those carry different information. A mouse movement will contain
        # the mouse cursor position, while a keyoard hit will contain the key
        # that was pressed. Depending on that, we need to handle the occured
        # event in a different way, which is done here.
        #
        # In case of a special QUIT event, the user wants to quit the
        # application, just as you are used to closing an editor.
        # If the user wants to quit the application, we should let him do so.
        # This is done by breaking out of the while True: loop.
        if event.type == sdlevents.SDL_QUIT:
            break

        # We received a mouse button press event. As you can see from the type,
        # the user pressed the mouse button, but did not necesarily release
        # it. As such, it is not a typical click, but only 50% of it, which
        # is sufficient for our case here.
        if event.type == sdlevents.SDL_MOUSEBUTTONDOWN:
            # If the user pressed the button, we want to draw the next palette
            # and update the window title accordingly. We do this by increasing
            # the storage variable and - in case it reached the last entry, set
            # it back to the first entry.
            curindex += 1
            if curindex >= len(palettes):
                curindex = 0
            window.title = palettes[curindex][0]
            draw_palette(windowsurface, palettes[curindex][1])

        # On each occured event, we will refresh the window, since it might
        # have happened that the user moved the window around, pressed a button
        # or did something else. In all those cases, we want the palettes
        # to be shown, so we need to refresh the window. This will cause the
        # window internally to copy its surface information (those we used to
        # draw the palette on) to the screen, where the window currently is
        # placed on.
        # Comment this line out to see what happens!
        window.refresh()

    # As for helloworld.py, we have to call video.quit(), since we also
    # called video.init().
    video.quit()
    return 0

if __name__ == "__main__":
    sys.exit(run())
