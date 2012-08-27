Pygame2 for Pygamers
====================

Care to move to a newer SDL with your Pygame knowledge? Then you should
know one thing or two about Pygame2 before hacking code, since it is
completely different from Pygame. Do not let that fact scare you away,
the basics with graphics and sound are still the same (as they are
fundamental), but you will not find many similarities to the Pygame API
within Pygame2.

.. todo::

   More details, examples, etc.

Conceptual differences
----------------------
TODO


API differences
---------------

pygame
^^^^^^
======================= =================================================
pygame                  Pygame2
======================= =================================================
``init()``              :func:`pygame2.sdl.init()` where appropriate
``quit()``              :func:`pygame2.sdl.quit()` where appropriate
``error``               No equivalent - there are different exception
                        types in Pygame2
``get_error()``         :func:`pygame2.sdl.get_error()`
``set_error()``         :func:`pygame2.sdl.set_error()`
``get_sdl_version()``   :func:`pygame2.sdl.version.get_version()`
``get_sdl_byteorder()`` :data:`pygame2.sdl.endian.SDL_BYTEORDER`
``register_quit()``     No equivalent planned
``encode_string()``     Encoding anddecoding strings is done implicitly,
                        where necessary
``encode_file_path()``  Encoding anddecoding strings is done implicitly,
                        where necessary
======================= =================================================

pygame.cdrom
^^^^^^^^^^^^
Pygame2 does not feature any CD-ROM related interfaces. They were
removed in SDL2 and Pygame2 does not provide its own facilities.

pygame.Color
^^^^^^^^^^^^
You can find a similar class in :class:`pygame2.color.Color`. It does
not feature a ``set_length()`` or ``correct_gamma()`` method, though.

pygame.cursors
^^^^^^^^^^^^^^
Pygame2 does not feature any pre-defined cursor settings at the moment.

pygame.display
^^^^^^^^^^^^^^
======================= =================================================
pygame.display          Pygame2
======================= =================================================
``init()``              :func:`pygame2.video.init()`
``quit()``              :func:`pygame2.video.quit()`
``get_init()``          :func:`pygame2.sdl.was_init()`
``set_mode()``          :class:`pygame2.video.Window`
``get_surface()``       :meth:`pygame2.video.Window.get_surface()`
``flip()``              :meth:`pygame2.video.Window.refresh()`
``update()``            :meth:`pygame2.sdl.video.update_window_surface_rects()`
``get_driver()``        :func:`pygame2.sdl.video.get_current_video_driver()`
``Info``                No equivalent yet
``get_wm_info()``       No equivalent yet
``list_modes()``        :func:`pygame2.sdl.video.get_num_display_modes()`
``mode_ok()``           :func:`pygame2.sdl.video.get_closest_display_mode()`
``gl_get_attribute()``  :func:`pygame2.sdl.video.gl_get_attribute()`
``gl_set_attribute()``  :func:`pygame2.sdl.video.gl_set_attribute()`
``get_active()``        No equivalent yet
``iconify()``           :meth:`pygame2.video.Window.minimize()`
``toggle_fullscreen()`` :func:`pygame2.sdl.video.set_window_fullscreen()`
``set_gamma()``         :func:`pygame2.sdl.video.set_window_brightness()`
``set_gamma_ramp()``    :func:`pygame2.sdl.video.set_window_gamma_ramp()`
``set_icon()``          :func:`pygame2.sdl.video.set_window_icon()`
``set_caption()``       :attr:`pygame2.video.Window.title`
``get_caption()``       :attr:`pygame2.video.Window.title`
``set_palette()``       :func:`pygame2.sdl.surface.set_surface_palette()`
======================= =================================================

pygame.draw
^^^^^^^^^^^
============== =================================================
pygame.draw    Pygame2
============== =================================================
``rect()``     :func:`pygame2.sdl.render.render_draw_rect()`
``polygon()``  No equivalent yet
``circle()``   No equivalent yet
``ellipse()``  No equivalent yet
``arc()``      No equivalent yet
``lines()``    :func:`pygame2.sdl.render.render_draw_lines()`
``aaline()``   No equivalent yet
``aalines()``  No equivalent yet
============== =================================================

pygame.event
^^^^^^^^^^^^
================= =================================================
pygame.event      Pygame2
================= =================================================
``pump()``        :func:`pygame2.sdl.events.pump_events()`
``get()``         :func:`pygame2.sdl.events.poll_event()`
``poll()``        :func:`pygame2.sdl.events.poll_event()`
``wait()``        :func:`pygame2.sdl.events.wait_event()`
``peek()``        :func:`pygame2.sdl.events.peep_events()`
``clear()``       :func:`pygame2.sdl.events.flush_events()`
``event_name()``  No equivalent planned
``set_blocked()`` :func:`pygame2.sdl.events.event_state()`
``get_blocked()`` :func:`pygame2.sdl.events.event_state()`
``set_allowed()`` :func:`pygame2.sdl.events.event_state()`
``set_grab()``    :func:`pygame2.sdl.video.set_window_grab()`
``get_grab()``    :func:`pygame2.sdl.video.get_window_grab()`
``post()``        :func:`pygame2.sdl.events.peep_events()`
``Event``         :class:`pygame2.sdl.events.SDL_Event`
================= =================================================

pygame.font
^^^^^^^^^^^
====================== =================================================
pygame.font            Pygame2
====================== =================================================
``init()``             :func:`pygame2.sdlttf.init()`
``quit()``             :func:`pygame2.sdlttf.quit()`
``get_init()``         No equivalent planned
``get_default_font()`` No equivalent planned
``get_fonts()``        :func:`pygame2.font.get_fonts()`
``match_font()``       :func:`pygame2.font.get_font()`
``SysFont``            No equivalent planned
``Font``               No equivalent yet
====================== =================================================

pygame.freetype
^^^^^^^^^^^^^^^
Pygame2 does not feature direct FreeType support at the moment.

pygame.gfxdraw
^^^^^^^^^^^^^^
Pygame2 does not feature SDL_gfx support at the moment.

pygame.image
^^^^^^^^^^^^
================== =================================================
pygame.image       Pygame2
================== =================================================
``load()``         :func:`pygame2.sdlimage.load()`
``save()``         :func:`pygame2.sdl.surface.save_bmp()`
``get_extended()`` :func:`pygame2.sdlimage.is_bmp()` et al.
``tostring()``     No equivalent yet
``fromstring()``   No equivalent yet
``frombuffer()``   No equivalent yet
================== =================================================

pygame.joystick
^^^^^^^^^^^^^^^
================== ========================================================
pygame.joystick    Pygame2
================== ========================================================
``init()``         :func:`pygame2.sdl.init()`
``quit()``         :func:`pygame2.sdl.quit()`
``get_init()``     :func:`pygame2.sdl.was_init()`
``get_count()``    :func:`pygame2.sdl.joystick.joystick_num_joysticks()`
``Joystick()``     :class:`pygame2.sdl.joystick.SDL_Joystick` and related
                   functions
================== ========================================================

pygame.key
^^^^^^^^^^
================== ========================================================
pygame.key         Pygame2
================== ========================================================
``get_focused()``  :func:`pygame2.sdl.keyboard.get_keyboard_focus()`
``get_pressed()``  :func:`pygame2.sdl.keyboard.get_keyboard_state()`
``get_mods()``     :func:`pygame2.sdl.keyboard.get_mod_state()`
``set_mods()``     :func:`pygame2.sdl.keyboard.set_mod_state()`
``set_repeat()``   Based on the OS/WM settings now
``get_repeat()``   Based on the OS/WM settings now
``name()``         :func:`pygame2.sdl.keyboard.get_key_name()`
================== ========================================================

pygame.locals
^^^^^^^^^^^^^
Constants in Pygame2 are spread across the different packages and
modules, depending on where they originate from.

pygame.mixer
^^^^^^^^^^^^
SDL_mixer is currently not supported by Pygame2. The focus is set on
OpenAL usage through :mod:`pygame2.openal` and :mod:`pygame2.audio`.

====================== ====================================================
pygame.mixer           Pygame2
====================== ====================================================
``init()``             No necessity to explicitly initialize
``quit()``             No necessity to explicitly quit
``get_init()``         No necessity to explicitly initialize
``stop()``             No equivalent yet
``pause()``            No equivalent yet
``unpause()``          No equivalent yet
``fadeout()``          No equivalent yet
``set_num_channels()`` Depends on the :class:`pygame2.audio.SoundSink`
                       device and bound
                       :class:`pygame2.audio.SoundSource` instances.
``get_num_channels()`` Depends on the :class:`pygame2.audio.SoundSink`
                       device and bound
                       :class:`pygame2.audio.SoundSource` instances.
``set_reserved()``     Depends on the :class:`pygame2.audio.SoundSink`
                       device and bound
                       :class:`pygame2.audio.SoundSource` instances.
``find_channel()``     No equivalent planned
``get_busy()``         No equivalent yet
``Sound``              :class:`pygame2.audio.SoundData` for the buffer,
                       :class:`pygame2.audio.SoundSource` for the volume
                       settings and playback
``Channel``            :class:`pygame2.audio.SoundSource`
====================== ====================================================

pygame.mixer.music
^^^^^^^^^^^^^^^^^^
See `pygame.mixer`_.


pygame.mouse
^^^^^^^^^^^^
================= ====================================================
pygame.mouse      Pygame2
================= ====================================================
``get_pressed()`` :func:`pygame2.sdl.mouse.get_mouse_state()`
``get_pos()``     :func:`pygame2.sdl.mouse.get_mouse_state()`
``get_rel()``     :func:`pygame2.sdl.mouse.get_relative_mouse_state()`
``set_pos()``     :func:`pygame2.sdl.mouse.warp_mouse_in_window()`
``set_visible()`` :func:`pygame2.sdl.mouse.show_cursor()`
``get_focused()`` :func:`pygame2.sdl.mouse.get_mouse_focus()`
``set_cursor()``  :func:`pygame2.sdl.mouse.set_cursor()`
``get_cursor()``  :func:`pygame2.sdl.mouse.get_cursor()`
================= ====================================================

pygame.movie
^^^^^^^^^^^^
No such module is planned for Pygame2.

pygame.Overlay
^^^^^^^^^^^^^^
You can work with YUV overlays by using the :mod:`pygame2.sdl.render`
with :class:`pygame2.sdl.render.SDL_Texture` objects.

pygame.PixelArray
^^^^^^^^^^^^^^^^^
You can access pixel data of sprites and surfaces directly via the
:class:`pygame2.video.PixelView` class. It does not feature
comparision or extractions methods.

pygame.Rect
^^^^^^^^^^^
No such functionality is available for Pygame2.

pygame.scrap
^^^^^^^^^^^^
Pygame2 offers basic text-based clipboard access via the
:mod:`pygame2.sdl.clipboard` module. A feature-rich clipboard API as for
Pygame does not exist yet.

pygame.sndarray
^^^^^^^^^^^^^^^
No such module is available for Pygame2 yet.

pygame.sprite
^^^^^^^^^^^^^
Pygame2 uses a different approach of rendering and managing sprite
objects via a component-based system and the
:class:`pygame2.video.Sprite` class. A sprite module as for Pygame is not
available.

pygame.Surface
^^^^^^^^^^^^^^
======================= ===================================================
pygame.Surface          Pygame2
======================= ===================================================
``blit()``              :meth:`pygame2.video.SpriteRenderer.render()`,
                        :func:`pygame2.sdl.surface.blit_surface()`
``convert()``           :func:`pygame2.sdl.surface.convert_surface()`
``convert_alpha()``     :func:`pygame2.sdl.surface.convert_surface()`
``copy()``              :func:`pygame2.sdl.surface.convert_surface()`
``fill()``              :func:`pygame2.video.fill()`,
                        :func:`pygame2.sdl.surface.fill_rect()`,
                        :func:`pygame2.sdl.surface.fill_rects()`
``scroll()``            No equivalent yet
``set_colorkey()``      :func:`pygame2.sdl.surface.set_color_key()`
``get_colorkey()``      :func:`pygame2.sdl.surface.get_color_key()`
``set_alpha()``         :func:`pygame2.sdl.surface.set_surface_alpha_mod()`
``get_alpha()``         :func:`pygame2.sdl.surface.get_surface_alpha_mod()`
``lock()``              :func:`pygame2.sdl.surface.lock_surface()`
``unlock()``            :func:`pygame2.sdl.surface.unlock_surface()`
``mustlock()``          :func:`pygame2.sdl.surface.SDL_MUSTLOCK()`
``get_locked()``        No equivalent planned
``get_locks()``         No equivalent planned
``get_at()``            Direct access to the pixels for surfaces can be
                        achieved via the
                        :class:`pygame2.video.PixelView` class
``set_at()``            Direct access to the pixels for surfaces can be
                        achieved via the
                        :class:`pygame2.video.PixelView` class
``get_at_mapped()``     No equivalent planned
``get_palette()``       via :attr:`pygame2.sdl.surface.SDL_Surface.format`
                        and the
                        :attr:`pygame2.sdl.pixels.SDL_PixelFormat.palette`
                        attribute.
``get_palette_at()``    ``pygame2.sdl.pixels.SDL_Palette.colors[offset]``
``set_palette()``       :func:`pygame2.sdl.surface.set_surface_palette()`
``set_palette_at()``    ``pygame2.sdl.pixels.SDL_Palette.colors[offset]``
``map_rgb()``           :func:`pygame2.sdl.pixels.map_rgb()`
``unmap_rgb()``         :func:`pygame2.sdl.pixels.get_rgb()`
``set_clip()``          :func:`pygame2.sdl.surface.set_clip_rect()`
``get_clip()``          :func:`pygame2.sdl.surface.get_clip_rect()`
``subsurface``          No equivalent yet
``get_parent()``        As for ``subsurface``
``get_abs_parent()``    As for ``subsurface``
``get_offset()``        As for ``subsurface``
``get_abs_offset()``    As for ``subsurface``
``get_size()``          :attr:`pygame2.video.Sprite.size`,
                        :attr:`pygame2.sdl.surface.SDL_Surface.size`
``get_width()``         ``pygame2.video.Sprite.size[0]``,
                        ``pygame2.sdl.surface.SDL_Surface.size[0]``
``get_height()``        ``pygame2.video.Sprite.size[1]``,
                        ``pygame2.sdl.surface.SDL_Surface.size[1]``
``get_rect()``          :attr:`pygame2.video.Sprite.area`
``get_bitsize()``       :attr:`pygame2.sdl.pixels.SDL_PixelFormat.BitsPerPixel`
``get_bytesize()``      :attr:`pygame2.sdl.pixels.SDL_PixelFormat.BytesPerPixel`
``get_flags()``         No equivalent yet
``get_pitch()``         :attr:`pygame2.sdl.surface.SDL_Surface.pitch`
``get_masks()``         :attr:`pygame2.sdl.pixels.SDL_PixelFormat.Rmask`, ...
``get_shifts()``        :attr:`pygame2.sdl.pixels.SDL_PixelFormat.Rshift`, ...
``get_losses()``        :attr:`pygame2.sdl.pixels.SDL_PixelFormat.Rloss`, ...
``get_bounding_rect()`` No equivalent yet
``get_view()``          :class:`pygame2.video.PixelView`
``get_buffer()``        :class:`pygame2.video.PixelView` or
                        :attr:`pygame2.sdl.surface.SDL_Surface.pixels`
======================= ===================================================

pygame.surfarray
^^^^^^^^^^^^^^^^
2D and 3D pixel access can be achieved via the
:class:`pygame2.video.PixelView` class in environments without
numpy. Simplified numpy-array creation with direct pixel access (similar
to ``pygame.surfarray.pixels2d()`` and ``pygame.surfarray.pixels3d()``
will be made available via the :mod:`pygame2.video.pixelaccess` module in the
future.

pygame.time
^^^^^^^^^^^
=============== =================================================
pygame.time     Pygame2
=============== =================================================
``get_ticks()`` :func:`pygame2.sdl.timer.get_ticks()`
``wait()``      :func:`pygame2.sdl.timer.delay()`
``delay()``     :func:`pygame2.sdl.timer.delay()`
``Clock``       No equivalent yet
=============== =================================================

pygame.transform
^^^^^^^^^^^^^^^^
The are no transformation helpers in Pygame2 at moment. Those might be
implemented later on via numpy helpers, the Python Imaging Library or
other 3rd party packages.

pygame.version
^^^^^^^^^^^^^^
=============== =================================================
pygame.version  Pygame2
=============== =================================================
``ver``         :attr:`pygame2.__version__`
``vernum``      :attr:`pygame2.version_info`
=============== =================================================
