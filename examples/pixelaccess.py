"""Direct pixel access examples."""
import sys
try:
    from pygame2.color import Color
    import pygame2.video as video
    import pygame2.sdl.events as sdlevents
except ImportError:
    import traceback
    traceback.print_exc()
    sys.exit(1)

BLACK = Color(0, 0, 0)
WHITE = Color(255, 255, 255)

def draw_stripes(surface, x1, x2, y1, y2):
    video.fill(surface, BLACK)
    pixelview = video.PixelView(surface)
    for y in range(y1, y2, 2):
        for x in range(x1, x2):
            pixelview[y][x] = WHITE
    del pixelview

def run():
    video.init()
    window = video.Window("Pixel Access", size=(800, 600))
    window.show()

    windowsurface = window.get_surface()
    x1 = 300
    x2 = 500
    y1 = 200
    y2 = 400

    while True:
        event = sdlevents.poll_event(True)
        if event is None:
            continue
        if event.type == sdlevents.SDL_QUIT:
            break
        if event.type == sdlevents.SDL_MOUSEBUTTONDOWN:
            draw_stripes(windowsurface, x1, x2, y1, y2)
        window.refresh()

    video.quit()
    return 0

if __name__ == "__main__":
    sys.exit(run())
