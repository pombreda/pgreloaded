"""Sprite, texture and pixel surface routines."""
import os
from pygame2.compat import isiterable, experimental
from pygame2.ebs import Component, System
import pygame2.sdl.surface as sdlsurface
import pygame2.sdl.rect as rect
import pygame2.sdl.video as video
import pygame2.sdl.pixels as pixels
import pygame2.sdl.render as render
import pygame2.sdl.rwops as rwops
from pygame2.video.window import Window

__all__ = ["SoftSpriteRenderer", "SoftSprite", "SpriteRenderer", "Sprite",
           "Renderer"]


class SoftSpriteRenderer(System):
    """A rendering system for SoftSprite components.

    The SoftSpriteRenderer class uses a Window as drawing device to display
    Sprite surfaces. It uses the Window's intenal SDL surface as
    drawing context, so that GL operations, such as texture handling or
    using SDL renderers is not possible.
    """
    def __init__(self, window):
        """Creates a new SoftSpriteRenderer for a specific Window."""
        super(SoftSpriteRenderer, self).__init__()
        if isinstance(window, Window):
            self.window = window.window
        elif isinstance(window, video.SDL_Window):
            self.window = window
        else:
            raise TypeError("unsupported window type")

        self.surface = video.get_window_surface(self.window)
        self._sortfunc = lambda e1, e2: cmp(e1.depth, e2.depth)
        self.componenttypes = (SoftSprite, )

    def render(self, sprites, x=None, y=None):
        """Draws the passed sprites (or sprite) on the Window's surface.

        x and y are optional arguments that can be used as relative
        drawing location for sprites. If set to None, the location
        information of the sprites are used. If set and sprites is an
        iterable, such as a list of SoftSprite objects, x and y are relative
        location values that will be added to each individual sprite's
        position. If sprites is a single SoftSprite, x and y denote the
        absolute position of the SoftSprite, if set.
        """
        r = rect.SDL_Rect(0, 0, 0, 0)
        if isiterable(sprites):
            blit_surface = sdlsurface.blit_surface
            surface = self.surface
            x = x or 0
            y = y or 0
            for sp in sprites:
                r.x = x + sp.x
                r.y = y + sp.y
                blit_surface(sp.surface, None, surface, r)
        else:
            if x is None or y is None:
                x = sprites.x
                y = sprites.y
            sdlsurface.blit_surface(sprites.surface, None, self.surface, r)
        video.update_window_surface(self.window)

    def process(self, world, components):
        """Draws the passed SoftSprite objects on the Window's surface."""
        self.render(sorted(components, self._sortfunc))

    @property
    def sortfunc(self):
        """Sort function for the component processing order.

        The default sort order is based on the depth attribute of every
        sprite. Lower depth values will cause sprites to be drawn below
        sprites with higher depth values.
        """
        return self._sortfunc

    @sortfunc.setter
    def sortfunc(self, value):
        """Sort function for the component processing order.

        The default sort order is based on the depth attribute of every
        sprite. Lower depth values will cause sprites to be drawn below
        sprites with higher depth values.
        """
        if not callable(value):
            raise TypeError("sortfunc must be callable")
        self._sortfunc = value


class SoftSprite(Component):
    """A simple, visible, pixel-based 2D object using software buffers."""
    def __init__(self, source=None, size=(0, 0), bpp=32, masks=None,
                 freesf=False):
        """Creates a new SoftSprite.

        If a source is provided, the constructor assumes it to be a
        readable buffer object or file path to load the pixel data from.
        The size and bpp will be ignored in those cases.

        If no source is provided, a size tuple containing the width and
        height of the sprite and a bpp value, indicating the bits per
        pixel to be used, need to be provided.
        """
        super(SoftSprite, self).__init__()
        self._freesf = True
        self.surface = None
        if source is not None:
            if isinstance(source, sdlsurface.SDL_Surface):
                self.surface = source
                self._freesf = freesf
            elif type(source) is str:
                if os.path.exists(source):
                    # Load from file
                    self.surface = sdlsurface.load_bmp(source)
                else:
                    raise ValueError("source string is not a path")
            else:
                rw = rwops.rw_from_object(source)
                self.surface = sdlsurface.load_bmp_rw(rw, True)
        else:
            if masks:
                rmask, gmask, bmask, amask = masks
            else:
                rmask = gmask = bmask = amask = 0
            self.surface = sdlsurface.create_rgb_surface(size[0], size[1],
                                                         bpp, rmask, gmask,
                                                         bmask, amask)
        self.depth = 0
        self.x = 0
        self.y = 0

    def __del__(self):
        """Releases the bound SDL_Surface, if it was created by the
        SoftSprite.
        """
        if self._freesf and self.surface is not None:
            sdlsurface.free_surface(self.surface)
        self.surface = None

    @property
    def size(self):
        """The size of the SoftSprite as tuple."""
        return self.surface.size

    @property
    def position(self):
        """The top-left position of the SoftSprite as tuple."""
        return self.x, self.y

    @position.setter
    def position(self, value):
        """The top-left position of the SoftSprite as tuple."""
        self.x = value[0]
        self.y = value[1]

    @property
    def area(self):
        """The rectangular area occupied by the SoftSprite."""
        w, h = self.size
        return (self.x, self.y, self.x + w, self.y + h)

    def __repr__(self):
        return "SoftSprite(size=%s, bpp=%d)" % \
            (self.size, self.surface.format.BitsPerPixel)


class SpriteRenderer(System):
    """A rendering system for Sprite components.

    The SpriteRenderer class uses a SDL_Renderer as drawing device to display
    Sprite textures.
    """
    def __init__(self, renderer):
        """Creates a new SpriteRenderer.

        obj can be a Window, SDL_Window or SDL_Renderer. If it is a Window
        instance, Window.create_renderer() will be called to acquire the
        SDL_Renderer. If it is a SDL_Window, it will try to create a
        SDL_Renderer with hardeware acceleration.
        """
        super(SpriteRenderer, self).__init__()
        if isinstance(renderer, Renderer):
            self._renderer = renderer  # Used to prevent GC
            sdlrenderer = renderer.renderer
        elif isinstance(renderer, render.SDL_Renderer):
            sdlrenderer = renderer
        else:
            raise TypeError("unsupported object type")
        self.sdlrenderer = sdlrenderer
        self._sortfunc = lambda e1, e2: cmp(e1.depth, e2.depth)
        self.componenttypes = (Sprite, )

    def render(self, sprites, x=None, y=None):
        """Draws the passed sprites (or sprite).

        x and y are optional arguments that can be used as relative
        drawing location for sprites. If set to None, the location
        information of the sprites are used. If set and sprites is an
        iterable, such as a list of Sprite objects, x and y are relative
        location values that will be added to each individual sprite's
        position. If sprites is a single Sprite, x and y denote the
        absolute position of the Sprite, if set.
        """
        r = rect.SDL_Rect(0, 0, 0, 0)
        if isiterable(sprites):
            rcopy = render.render_copy
            renderer = self.sdlrenderer
            x = x or 0
            y = y or 0
            for sp in sprites:
                r.x = x + sp.x
                r.y = y + sp.y
                r.w, r.h = sp.size
                rcopy(renderer, sp.texture, None, r)
        else:
            if x is None or y is None:
                r.x = sprites.x
                r.y = sprites.y
                r.w, r.h = sprites.size
            render.render_copy(self.sdlrenderer, sprites.texture, None, r)
        render.render_present(self.sdlrenderer)

    def process(self, world, components):
        """Draws the passed Sprite objects."""
        self.render(sorted(components, self._sortfunc))

    @property
    def sortfunc(self):
        """Sort function for the component processing order.

        The default sort order is based on the depth attribute of every
        sprite. Lower depth values will cause sprites to be drawn below
        sprites with higher depth values.
        """
        return self._sortfunc

    @sortfunc.setter
    def sortfunc(self, value):
        """Sort function for the component processing order.

        The default sort order is based on the depth attribute of every
        sprite. Lower depth values will cause sprites to be drawn below
        sprites with higher depth values.
        """
        if not callable(value):
            raise TypeError("sortfunc must be callable")
        self._sortfunc = value


class Sprite(Component):
    """A simple, visible, pixel-based 2D object, using a renderer."""
    def __init__(self, renderer, source=None, size=(0, 0),
                 pformat=pixels.SDL_PIXELFORMAT_RGBA8888, static=True):
        """Creates a new Sprite.

        If a source is provided, the constructor assumes it to be a
        readable buffer object or file path to load the pixel data from.
        The size will be ignored in those cases.

        If no source is provided, a size tuple containing the width and
        height of the sprite needs to be provided.

        Sprite objects are assumed to be static by default, making it
        impossible to access their pixel buffer in favour for faster copy
        operations. If you need to update the pixel data frequently, static
        can be set to False to allow a streaming access on the underlying
        texture pixel buffer.
        """
        super(Sprite, self).__init__()
        self.texture = None
        sf = None
        if isinstance(renderer, Renderer):
            sdlrenderer = renderer.renderer
        elif isinstance(renderer, render.SDL_Renderer):
            sdlrenderer = renderer
        else:
            raise TypeError("renderer must be a Renderer or SDL_Renderer")

        if source is not None:
            dontfree = False
            if isinstance(source, sdlsurface.SDL_Surface):
                sf = surface
                dontfree = True
            elif type(source) is str:
                if os.path.exists(source):
                    # Load from file
                    sf = sdlsurface.load_bmp(source)
                else:
                    raise ValueError("source string is not a path")
            else:
                rw = rwops.rw_from_object(source)
                sf = sdlsurface.load_bmp_rw(rw, True)
            self.texture = render.create_texture_from_surface(sdlrenderer, sf)
            if not dontfree:
                sdlsurface.free_surface(sf)
        else:
            access = render.SDL_TEXTUREACCESS_STATIC
            if not static:
                access = render.SDL_TEXTUREACCESS_STREAMING
            self.texture = render.create_texture(sdlrenderer, pformat, access,
                                                 size[0], size[1])

        # Store the size for faster access on rendering operations
        self._size = render.query_texture(self.texture)[2:]
        self.depth = 0
        self.x = 0
        self.y = 0

    def __del__(self):
        """Releases the bound SDL_Texture."""
        if self.texture is not None:
            render.destroy_texture(self.texture)
        self.texture = None

    @property
    def size(self):
        """The size of the Sprite as tuple."""
        return self._size

    @property
    def position(self):
        """The top-left position of the Sprite as tuple."""
        return self.x, self.y

    @position.setter
    def position(self, value):
        """The top-left position of the Sprite as tuple."""
        self.x = value[0]
        self.y = value[1]

    @property
    def area(self):
        """The rectangular area occupied by the Sprite."""
        w, h = self.size
        return (self.x, self.y, self.x + w, self.y + h)

    def __repr__(self):
        format, access, w, h = render.query_texture(self.texture)
        static = "True"
        if access == render.SDL_TEXTUREACCESS_STREAMING:
            static = "False"
        return "Sprite(format=%d, static=%s, size=%s)" % \
            (format, static, (w, h))


class Renderer(object):
    """SDL2-based rendering context for windows and sprites."""
    def __init__(self, target, index=-1,
                 flags=render.SDL_RENDERER_ACCELERATED):
        """Creates a new Renderer for the given target.

        If target is a Window or SDL_Window, index and flags are passed
        to the relevant sdl.render.create_renderer() call. If target is
        a SoftSprite or SDL_Surface, the index and flags arguments are
        ignored.
        """
        self.renderer = None
        self.rendertaget = None
        if isinstance(target, Window):
            self.renderer = render.create_renderer(target.window, index, flags)
            self.rendertarget = target.window
        elif isinstance(target, sdlvideo.SDL_Window):
            self.renderer = render.create_renderer(window, index, flags)
            self.rendertarget = window
        elif isinstance(target, SoftSprite):
            self.renderer = render.create_software_renderer(target.surface)
            self.rendertarget = target.surface
        elif isinstance(target, sdlsurface.SDL_Surface):
            self.renderer = render.create_software_renderer(target)
            self.rendertarget = target
        else:
            raise TypeError("unsupported target type")

    def __del__(self):
        if self.renderer:
            render.destroy_renderer(self.renderer)
        self.rendertarget = None

    @property
    def color(self):
        """The drawing color of the Renderer."""
        return Color(render.get_render_draw_color(self.renderer))

    @color.setter
    def color(self, value):
        """The drawing color of the Renderer."""
        c = convert_to_color(value)
        render.set_render_draw_color(self.renderer, c.r, c.g, c.b, c.a)

    @property
    def blendmode(self):
        """The blend mode used for drawing operations (fill and line)."""
        return render.get_render_draw_blend_mode(self.renderer)

    @blendmode.setter
    def blendmode(self, value):
        """The blend mode used for drawing operations (fill and line)."""
        render.set_render_draw_blend_mode(self.renderer, value)

    def clear(self, color=None):
        """Clears the rendering context with the currently set or passed
        color."""
        if color:
            tmp = self.color
            self.color = color
        try:
            render.render_clear(self.renderer)
        finally:
            if color:
                self.color = tmp

    def copy(self, src, srcrect=None, dstrect=None):
        """TODO"""
        pass

    def draw_line(self, points, color=None):
        """Draws one or multiple lines on the rendering context."""
        # (x1, y1, x2, y2, ...)
        pcount = len(points)
        if (pcount % 4) != 0:
            raise ValueError("points does not contain a valid set of points")
        if pcount == 4:
            if color:
                tmp = self.color
                self.color = color
            try:
                x1, y1, x2, y2 = points
                render.render_draw_line(self.renderer, x1, y1, x2, y2)
            finally:
                if color:
                    self.color = tmp
        else:
            x = 0
            ptlist = []
            while x < pcount:
                ptlist.append(SDL_Point(points[x], points[x+1]))
                x += 2
            if color:
                tmp = self.color
                self.color = color
            try:
                render.render_draw_lines(self.renderer, ptlist)
            finally:
                if color:
                    self.color = tmp

    def draw_point(self, points, color=None):
        """Draws one or multiple points on the rendering context."""
        # (x1, y1, x2, y2, ...)
        pcount = len(points)
        if (pcount % 2) != 0:
            raise ValueError("points does not contain a valid set of points")
        if pcount == 2:
            if color:
                tmp = self.color
                self.color = color
            try:
                x, y = points
                render.render_draw_point(self.renderer, x, y)
            finally:
                if color:
                    self.color = tmp
        else:
            x = 0
            ptlist = []
            while x < pcount:
                ptlist.append(SDL_Point(points[x], points[x+1]))
                x += 2
            if color:
                tmp = self.color
                self.color = color
            try:
                render.render_draw_points(self.renderer, ptlist)
            finally:
                if color:
                    self.color = tmp

    def draw_rect(self, rects, color=None):
        """Draws one or multiple rectangles on the rendering context."""
        # ((x, y, w, h), ...)
        rcount = len(rects)
        if type(rects[0]) == int:
            # single rect
            if color:
                tmp = self.color
                self.color = color
            try:
                x, y, w, h = rects
                render.render_draw_rect(self.renderer, x, y, w, h)
            finally:
                if color:
                    self.color = tmp
        else:
            x = 0
            rlist = []
            for r in rects:
                rlist.append(SDL_Rect(r[0], r[1], r[2], r[3]))
            if color:
                tmp = self.color
                self.color = color
            try:
                render.render_draw_rects(self.renderer, rlist)
            finally:
                if color:
                    self.color = tmp

    def fill(self, rects, color=None):
        """Fills one or multiple rectangular areas on the rendering
        context."""
        # ((x, y, w, h), ...)
        rcount = len(rects)
        if type(rects[0]) == int:
            # single rect
            if color:
                tmp = self.color
                self.color = color
            try:
                x, y, w, h = rects
                render.render_fill_rect(self.renderer, x, y, w, h)
            finally:
                if color:
                    self.color = tmp
        else:
            x = 0
            rlist = []
            for r in rects:
                rlist.append(SDL_Rect(r[0], r[1], r[2], r[3]))
            if color:
                tmp = self.color
                self.color = color
            try:
                render.render_fill_rects(self.renderer, rlist)
            finally:
                if color:
                    self.color = tmp
