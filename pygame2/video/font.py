"""Font and text rendering routines."""
import os
import pygame2.sdl.surface as sdlsurface
from pygame2.video.sprite import SoftwareSprite

__all__ = ["BitmapFont"]


class BitmapFont(object):
    """A bitmap graphics to character mapping.

    The BitmapFont class uses an image surface to find and render font
    character glyphs for text. It requires a mapping table, which
    denotes the characters available on the image.

    The mapping table is a list of strings, where each string reflects a
    'line' of characters on the image. Each character within each line
    has the same size as specified by the size argument.

    A typical mapping table might look like

      [ '0123456789',
        'ABCDEFGHIJ',
        'KLMNOPQRST',
        'UVWXYZ    ',
        'abcdefghij',
        'klmnopqrst',
        'uvwxyz    ',
        ',;.:!?+-()' ]
    """

    DEFAULTMAP = ["0123456789",
                  "ABCDEFGHIJ",
                  "KLMNOPQRST",
                  "UVWXYZ    ",
                  "abcdefghij",
                  "klmnopqrst",
                  "uvwxyz    ",
                  ",;.:!?+-()"
                  ]

    def __init__(self, surface, size, mapping=None):
        """Creates a new BitmapFont instance from the passed image.

        Each character is expected to be of the same size (a 2-value tuple
        denoting the width and height) and to be in order of the passed
        mapping.
        """
        if mapping is None:
            self.mapping = list(BitmapFont.DEFAULTMAP)
        else:
            self.mapping = mapping
        self.offsets = {}
        if isinstance(surface, SoftwareSprite):
            self.surface = surface.surface
        #elif isinstance(surface, sprite.Sprite):
        #    TODO
        elif isinstance(surface, sdlsurface.SDL_Surface):
            self.surface = surface
        self.size = size[0], size[1]
        self._calculate_offsets()

    def _calculate_offsets(self):
        """Calculates the internal character offsets for each line."""
        self.offsets = {}
        offsets = self.offsets
        x, y = 0, 0
        w, h = self.size
        for line in self.mapping:
            x = 0
            for c in line:
                offsets[c] = (x, y, w, h)
                x += w
            y += h

    def render(self, text, bpp=None):
        """Renders the passed text on a new Sprite and returns it."""
        x, y = 0, 0
        tw, th = 0, 0
        w, h = self.size
        # TODO
        lines = text.split(os.linesep)
        for line in lines:
            tw = max(tw, sum([w for c in line]))
            th += h

        if bpp is None:
            bpp = self.surface.format.BitsPerPixel
        surface = SoftwareSprite(tw, th, bpp)
        target = surface.surface
        blit_surface = sdlsurface.blit_surface
        fontsf = self.surface
        offsets = self.offsets
        for line in lines:
            for c in line:
                blit_surface(target, (x, y), fontsf, offsets[c])
                x += w
            y += h
        return surface

    def render_on(self, surface, text, offset=(0, 0)):
        """Renders a text on the passed sprite, starting at a specific
        offset.

        The top-left start position of the text will be the passed offset and
        4-value tuple with the changed area will be returned.
        """
        x, y = offset
        w, h = self.size

        target = None
        if isinstance(surface, SoftwareSprite):
            target = surface.surface
        #elif isinstance(surface, sprite.Sprite):
        #    TODO
        elif isinstance(surface, sdlsurface.SDL_Surface):
            target = surface
        else:
            raise TypeError("unsupported surface type")

        lines = text.split(os.linesep)
        blit_surface = sdlsurface.blit_surface
        fontsf = self.surface
        offsets = self.offsets
        for line in lines:
            for c in line:
                blit_surface(target, (x, y), fontsf, offsets[c])
                x += w
            y += h
        return (offset[0], offset[1], x + w, y + h)

    def contains(self, c):
        """Checks, whether a certain character exists in the font."""
        return c in self.offsets

    def can_render(self, text):
        """Checks, whether all characters in the passed text can be rendered.
        """
        lines = text.split(os.linesep)
        has_key = self.offsets.has_key
        for line in lines:
            for c in line:
                if not has_key(c):
                    return False
        return True
