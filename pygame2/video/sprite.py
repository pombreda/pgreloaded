"""Sprite, texture and pixel surface routines."""
import abc
from pygame2.compat import *
from pygame2.color import convert_to_color
from pygame2.ebs import Component, System
from pygame2.video.window import Window
from pygame2.video.image import load_image
import pygame2.sdl.surface as sdlsurface
from pygame2.sdl.rect import SDL_Rect, SDL_Point
import pygame2.sdl.video as video
import pygame2.sdl.pixels as pixels
import pygame2.sdl.render as render
import pygame2.sdl.rwops as rwops

__all__ = ["Sprite", "SoftwareSprite", "TextureSprite", "SpriteFactory",
           "SoftwareSpriteRenderer", "SpriteRenderer",
           "TextureSpriteRenderer", "RenderContext", "TEXTURE", "SOFTWARE"]

TEXTURE = 0
SOFTWARE = 1


class RenderContext(object):
    """SDL2-based rendering context for windows and sprites."""
    def __init__(self, target, index=-1,
                 flags=render.SDL_RENDERER_ACCELERATED):
        """Creates a new RenderContext for the given target.

        If target is a Window or SDL_Window, index and flags are passed
        to the relevant sdl.render.create_renderer() call. If target is
        a SoftwareSprite or SDL_Surface, the index and flags arguments are
        ignored.
        """
        self.renderer = None
        self.rendertaget = None
        if isinstance(target, Window):
            self.renderer = render.create_renderer(target.window, index, flags)
            self.rendertarget = target.window
        elif isinstance(target, video.SDL_Window):
            self.renderer = render.create_renderer(target, index, flags)
            self.rendertarget = target
        elif isinstance(target, SoftwareSprite):
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
        """The drawing color of the RenderContext."""
        return convert_to_color(render.get_render_draw_color(self.renderer))

    @color.setter
    def color(self, value):
        """The drawing color of the RenderContext."""
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

    def present(self):
        """TODO"""
        render.render_present(self.renderer)

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


class Sprite(Component):
    """A simple 2D object."""
    __metaclass__ = abc.ABCMeta

    def __init__(self):
        """Creates a new Sprite."""
        super(Sprite, self).__init__()
        self.x = 0
        self.y = 0
        self.depth = 0

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
    @abc.abstractmethod
    def size(self):
        """The size of the Sprite as tuple."""
        return

    @property
    def area(self):
        """The rectangular area occupied by the Sprite."""
        w, h = self.size
        return (self.x, self.y, self.x + w, self.y + h)


class SoftwareSprite(Sprite):
    """A simple, visible, pixel-based 2D object using software buffers."""
    def __init__(self, surface, free):
        """Creates a new SoftwareSprite."""
        super(SoftwareSprite, self).__init__()
        self.free = free
        if not isinstance(surface, sdlsurface.SDL_Surface):
            raise TypeError ("surface must be a SDL_Surface")
        self.surface = surface

    def __del__(self):
        """Releases the bound SDL_Surface, if it was created by the
        SoftwareSprite.
        """
        surface = getattr(self, "surface", None)
        if self.free and surface is not None:
            sdlsurface.free_surface(surface)
        self.surface = None

    @property
    def size(self):
        """The size of the SoftwareSprite as tuple."""
        return self.surface.size

    def __repr__(self):
        return "SoftwareSprite(size=%s, bpp=%d)" % \
            (self.size, self.surface.format.BitsPerPixel)


class TextureSprite(Sprite):
    """A simple, visible, texture-based 2D object, using a renderer."""
    def __init__(self, texture):
        """Creates a new TextureSprite."""
        super(TextureSprite, self).__init__()
        self.texture = texture
        self._size = render.query_texture(texture)[2:]

    def __del__(self):
        """Releases the bound SDL_Texture."""
        if self.texture is not None:
            render.destroy_texture(self.texture)
        self.texture = None

    @property
    def size(self):
        """The size of the TextureSprite as tuple."""
        return self._size

    def __repr__(self):
        tformat, access, w, h = render.query_texture(self.texture)
        static = "True"
        if access == render.SDL_TEXTUREACCESS_STREAMING:
            static = "False"
        return "TextureSprite(format=%d, static=%s, size=%s)" % \
            (tformat, static, (w, h))


class SpriteFactory(object):
    """A factory class for creating Sprite objects."""
    def __init__(self, sprite_type=TEXTURE, **kwargs):
        """Creates a new SpriteFactory.

        The SpriteFactory can create TextureSprite or SoftwareSprite
        instances, depending on the sprite_type being passed to it,
        which can be SOFTWARE or TEXTURE. The additional kwargs are used
        as default arguments for creating sprites within the factory
        methods.
        """
        if sprite_type == TEXTURE:
            if "renderer" not in kwargs:
                raise ValueError("you have to provide a renderer= argument")
        elif sprite_type != SOFTWARE:
            raise ValueError("stype must be TEXTURE or SOFTWARE")
        self._spritetype = sprite_type
        self.default_args = kwargs

    @property
    def sprite_type(self):
        """The sprite type created by the factory."""
        return self._spritetype

    def __repr__(self):
        stype = "TEXTURE"
        if self.sprite_type == SOFTWARE:
            stype = "SOFTWARE"
        return "SpriteFactory(sprite_type=%s, default_args=%s)" % \
            (stype, self.default_args)

    def create_sprite_renderer(self, *args, **kwargs):
        """Creates a new SpriteRenderer.

        For TEXTURE mode, the passed args and kwargs are ignored and the
        RenderContext or SDL_Renderer passed to the SpriteFactory is used.
        """
        if self.sprite_type == TEXTURE:
            return TextureSpriteRenderer(self.default_args["renderer"])
        else:
            return SoftwareSpriteRenderer(*args, **kwargs)

    def from_image(self, fname):
        """Creates a Sprite from the passed image file."""
        return self.from_surface(load_image(fname), True)

    def from_surface(self, surface, free=False):
        """Creates a Sprite from the passed SDL_Surface.

        If free is set to True, the passed surface will be freed
        automatically.
        """
        if self.sprite_type == TEXTURE:
            renderer = self.default_args["renderer"]
            texture = render.create_texture_from_surface(renderer.renderer,
                                                         surface)
            s = TextureSprite(texture)
            if free:
                sdlsurface.free_surface(surface)
        elif self.sprite_type == SOFTWARE:
            s = SoftwareSprite(surface, free)
        return s

    def from_object(self, obj):
        """Creates a Sprite from an arbitrary object."""
        if self.sprite_type == TEXTURE:
            rw = rwops.rw_from_object(obj)
            # TODO: support arbitrary objects.
            surface = sdlsurface.load_bmp_rw(rw, True)
            s = self.from_surface(surface, True)
        elif self.sprite_type == SOFTWARE:
            rw = rwops.rw_from_object(obj)
            s = SoftwareSprite(sdlsurface.load_bmp_rw(rw, True), True)
        return s

    def from_color(self, color, size=(0, 0), bpp=32, masks=None):
        """Creates a sprite with a certain color.
        """
        color = convert_to_color(color)
        if masks:
            rmask, gmask, bmask, amask = masks
        else:
            rmask = gmask = bmask = amask = 0
        sf = sdlsurface.create_rgb_surface(size[0], size[1], bpp, rmask, gmask,
                                           bmask, amask)
        fmt = sf.format
        if fmt.Amask != 0:
            # Target has an alpha mask
            c = pixels.map_rgba(fmt, color.r, color.g, color.b, color.a)
        else:
            c = pixels.map_rgb(fmt, color.r, color.g, color.b)
        sdlsurface.fill_rect(sf, None, c)
        return self.from_surface(sf, True)

    def create_sprite(self, **kwargs):
        """Creates an empty Sprite.

        This will invoke create_software_sprite() or
        create_texture_sprite() with the passed arguments and the set
        default arguments.
        """
        args = self.default_args.copy()
        args.update(kwargs)

        if self.sprite_type == TEXTURE:
            return self.create_texture_sprite(**args)
        else:
            return self.create_software_sprite(**args)

    def create_software_sprite(self, size=(0, 0), bpp=32, masks=None):
        """Creates a software sprite.

        A size tuple containing the width and height of the sprite and a
        bpp value, indicating the bits per pixel to be used, need to be
        provided.
        """
        if masks:
            rmask, gmask, bmask, amask = masks
        else:
            rmask = gmask = bmask = amask = 0
        surface = sdlsurface.create_rgb_surface(size[0], size[1],
                                                bpp, rmask, gmask,
                                                bmask, amask)
        return SoftwareSprite(surface, True)

    def create_texture_sprite(self, renderer, size=(0, 0),
                              pformat=pixels.SDL_PIXELFORMAT_RGBA8888,
                              static=True):
        """Creates a texture sprite.

        A size tuple containing the width and height of the sprite needs
        to be provided.

        TextureSprite objects are assumed to be static by default,
        making it impossible to access their pixel buffer in favour for
        faster copy operations. If you need to update the pixel data
        frequently, static can be set to False to allow a streaming
        access on the underlying texture pixel buffer.
        """
        if isinstance(renderer, render.SDL_Renderer):
            sdlrenderer = renderer
        elif isinstance(renderer, RenderContext):
            sdlrenderer = renderer.renderer
        else:
            raise TypeError("renderer must be a Renderer or SDL_Renderer")
        access = render.SDL_TEXTUREACCESS_STATIC
        if not static:
            access = render.SDL_TEXTUREACCESS_STREAMING
        texture = render.create_texture(sdlrenderer, pformat, access,
                                        size[0], size[1])
        return TextureSprite(texture)


class SpriteRenderer(System):
    """A rendering system for Sprite components.

    This is a base class for rendering systems capable of drawing and
    displaying Sprite-based objects. Inheriting classes need to
    implement the rendering capability by overriding the render()
    method.
    """
    def __init__(self):
        super(SpriteRenderer, self).__init__()
        self.componenttypes = (Sprite, )
        self._sortfunc = lambda e: e.depth

    def render(self, sprites):
        """Renders the passed sprites.

        This is a no-op function and needs to be implemented by inheriting
        classes.
        """
        pass

    def process(self, world, components):
        """Draws the passed SoftSprite objects on the Window's surface."""
        self.render(sorted(components, key=self._sortfunc))

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


class SoftwareSpriteRenderer(SpriteRenderer):
    """A rendering system for SoftwareSprite components.

    The SoftwareSpriteRenderer class uses a Window as drawing device to
    display Sprite surfaces. It uses the Window's internal SDL surface as
    drawing context, so that GL operations, such as texture handling or
    using SDL renderers is not possible.
    """
    def __init__(self, window):
        """Creates a new SoftSpriteRenderer for a specific Window."""
        super(SoftwareSpriteRenderer, self).__init__()
        if isinstance(window, Window):
            self.window = window.window
        elif isinstance(window, video.SDL_Window):
            self.window = window
        else:
            raise TypeError("unsupported window type")
        self.surface = video.get_window_surface(self.window)
        self.componenttypes = (SoftwareSprite, )

    def render(self, sprites, x=None, y=None):
        """Draws the passed sprites (or sprite) on the Window's surface.

        x and y are optional arguments that can be used as relative
        drawing location for sprites. If set to None, the location
        information of the sprites are used. If set and sprites is an
        iterable, such as a list of SoftwareSprite objects, x and y are relative
        location values that will be added to each individual sprite's
        position. If sprites is a single SoftwareSprite, x and y denote the
        absolute position of the SoftwareSprite, if set.
        """
        r = SDL_Rect(0, 0, 0, 0)
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
            r.x = x or sprites.x
            r.y = y or sprites.y
            sdlsurface.blit_surface(sprites.surface, None, self.surface, r)
        video.update_window_surface(self.window)


class TextureSpriteRenderer(SpriteRenderer):
    """A rendering system for TextureSprite components.

    The TextureSpriteRenderer class uses a SDL_Renderer as drawing
    device to display TextureSprite objects.
    """
    def __init__(self, target):
        """Creates a new TextureSpriteRenderer.

        target can be a Window, SDL_Window, RenderContext or SDL_Renderer.
        If it is a Window or SDL_Window instance, a RenderContext will be
        created to acquire the SDL_Renderer.
        """
        super(TextureSpriteRenderer, self).__init__()
        if isinstance(target, (Window, video.SDL_Window)):
            # Create a Renderer for the window and use that one.
            target = RenderContext(target)

        if isinstance(target, RenderContext):
            self._renderer = target  # Used to prevent GC
            sdlrenderer = target.renderer
        elif isinstance(target, render.SDL_Renderer):
            sdlrenderer = target
        else:
            raise TypeError("unsupported object type")
        self.sdlrenderer = sdlrenderer
        self.componenttypes = (TextureSprite, )

    def render(self, sprites, x=None, y=None):
        """Draws the passed sprites (or sprite).

        x and y are optional arguments that can be used as relative
        drawing location for sprites. If set to None, the location
        information of the sprites are used. If set and sprites is an
        iterable, such as a list of TextureSprite objects, x and y are
        relative location values that will be added to each individual
        sprite's position. If sprites is a single TextureSprite, x and y
        denote the absolute position of the TextureSprite, if set.
        """
        r = SDL_Rect(0, 0, 0, 0)
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
