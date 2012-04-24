"""A simple example for filing rectangular areas."""
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
    import pygame2.sdl.surface as sdlsurface
    import pygame2.sdl.pixels as sdlpixels
    import pygame2.sdl.rect as sdlrect
except ImportError:
    import traceback
    traceback.print_exc()
    sys.exit(1)


def draw_palette(surface, palette):
    sdlsurface.fill_rect(surface, None, 0) # Black
    width, height = surface.size
    rw = width // len(palette)
    rect = sdlrect.SDL_Rect(0, 0, rw, height)
    for color in palette:
        cval = video.prepare_color(color, surface)
        sdlsurface.fill_rect(surface, rect, cval)
        rect.x += rw


def run():
    video.init()
    window = video.Window("Color Palettes", size=(800, 600))
    window.show()
    windowsurface = window.get_surface()

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

    curindex = 0
    window.title = palettes[0][0]
    draw_palette(windowsurface, palettes[0][1])

    while True:
        event = sdlevents.poll_event(True)
        if event is None:
            # delay
            continue
        if event.type == sdlevents.SDL_QUIT:
            break
        if event.type == sdlevents.SDL_MOUSEBUTTONDOWN:
            curindex += 1
            if curindex >= len(palettes):
                curindex = 0
            window.title = palettes[curindex][0]
            draw_palette(windowsurface, palettes[curindex][1])
        window.refresh()

    video.quit()

if __name__ == "__main__":
    sys.exit(run())
