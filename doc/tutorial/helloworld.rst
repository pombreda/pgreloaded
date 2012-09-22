.. _hello_world:

Hello World
===========
Ahhh, the great tradition of saying "Hello World" in a programming
language. To whet your appetite, we will do the same with a most simple
application, which will display the typical Pygame logo. It is not
important to understand anything at once, which will be used by the
example. Nearly all parts used now are explained in later chapters, so
do not hesitate, if the one or other explanation is missing.

Importing
---------
Let's start with importing some basic modules, which are necessary to
display a small nice window and to do some basic drawing within that
window. ::

    import sys

    from pygame2.resources import Resources
    RESOURCES = Resources(__file__, "resources")

    try:
        import pygame2.video as video
    except ImportError:
        import traceback
        traceback.print_exc()
        sys.exit(1)

We start with importing some resources from the ``resources`` folder, so
that we have a test image around to display on the window later on. In
your own applications, it is unlikely that you will ever need to import
them.

Afterwards, we try to import :mod:`pygame2.video` module, which is
necessary for displaying the window and image. :mod:`pygame2.video` requires
:mod:`pygame2.sdl`, so in case it could not load the SDL bindings, we will
print the exact error stack information and exit with a failure.

Window creation and image loading
---------------------------------
Any graphical application requires access to the screen, mostly in form
of a window, which basically represents a portion of the screen, the
application has access to and the application can manipulate. In most cases
that portion has a border and title bar around it, so the user can move
it around on the screen and reorganize anything, so it fits his needs.

Once we have imported all necessary parts, let's create a window to have
access to the screen, so we can display the logo and thus represent it
to the user. ::

    video.init ()

    sprite = video.SoftSprite(RESOURCES.get("hello.bmp"))

    window = video.Window("Hello World!", size=(640, 480))
    window.show()

    renderer = video.SpriteRenderer(window)
    renderer.render(sprite)

First, we initialize the :mod:`pygame2.video` internals, so we can have
access to the screen and create windows on top of it. Afterwards, we get
an image from the :mod:`pygame2.examples` package and create a
:class:`pygame2.video.sprite.SoftSprite` from it, which can be easily
shown later on.

Once done with that, :class:`pygame2.video.window.Window` will create the
window for us and we supply a title to be shown on the window's border along
with its initial size. Since :class:`pygame2.video.window.Window` instances are
not shown by default, we have to tell the operating system and window manager
that there is a new window to display by calling
:meth:`pygame2.video.window.Window.show()`.

To display the image, we will use a
:class:`pygame2.video.sprite.SoftSpriteRenderer`, which can copy the
image to the window for display. The
:class:`pygame2.video.sprite.SoftSpriteRenderer` needs to know, where to
copy to, so we supply the window as target for copy and display
operations. All left to do is to actually initiate the copy process by
calling :class:`pygame2.video.sprite.SoftSpriteRenderer.render()` with
the image we created earlier.

.. tip::

   You will notice that the sprite used above will always be drawn at the
   top-left corner of the :class:`pygame2.video.window.Window`. You can change
   the position of where to draw it by changing its
   :attr:`pygame2.video.sprite.SoftSprite.position` value. ::

        # will cause the renderer to draw the sprite 10px to the right and
        # 20 px to the bottom
        sprite.position = 10, 20

        # will cause the renderer to draw the sprite 55px to the right and
        # 10 px to the bottom
        sprite.position = 55, 10

   Experiment with different values to see their effect. Do not forget to do
   this *before* ``renderer.render(sprite)`` is called.

Making the application responsive
---------------------------------
We are nearly done now. We have an image to display, we have a window, where
the image should be displayed on, so we can execute the written code, not?

Well, yes, but the only thing that will happen is that we will notice a
short flickering before the application exits. Maybe we can even see
the window with the image for a short moment, but that's not what we
want, do we?

To keep the window on the screen and to make it responsive to user
input, such as closing the window, react upon the mouse cursor or key
presses, we have to add a so-called event loop. The event loop will deal
with certain types of actions happening on the window or while the
window is focused by the user and - as long as the event loop is
running - will keep the window shown on the screen. ::

    processor = video.TestEventProcessor()
    processor.run(window)

Since this is a very first tutorial, we keep things simple here and hide the
dummy class for testing an application startup without actually dealing with
event loop magic in the :class:`pygame2.video.TestEventProcessor`. It is a
events. By calling :meth:`pygame2.video.TestEventProcessor.run()`, we
implicitly start the event loop, so that it can take care of everything for us.

And here it ends...
-------------------

The window is shown, the image is shown, great! All left to do is to actually
clean up everything, once the application finishes. Luckily the
:class:`pygame2.video.TestEventProcessor` knows, when the window is closed, so
it will exit from the event loop. Once it exits, we definitely should clean up
the video internals, we initialized at the beginning. Thus, a final call to ::

    video.quit()

should definitely be made.
