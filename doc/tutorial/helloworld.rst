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
Pygame2 uses a strict seperation of modules to allow you to build and
import only those parts needed for your specific needs. In contrast to
Pygame, this forces you to write more import statements, but the benefit
is that you can keep your dependencies small.

Let's start with importing some basic SDL modules, which are necessary
to display a small nice window and to do some basic drawing within that
window. ::

  import sys
  import pygame2
  import pygame2.event
  import pygame2.image
  import pygame2.examples
  try:
      import pygame2.video
  except ImportError:
      print ("No pygame2.sdl support, which is required for pygame2.video")
      sys.exit ()

First of all, we import the :mod:`pygame2` core module, which allows us
to use some basic things, such as :class:`pygame2.Color` and
:class:`pygame2.Rect` objects. In nearly all graphics applications
written with pygame2, you will need the core.

Afterwards, we import the shipped examples. This is mainly done to have
the logo around, which resides within the :mod:`pygame2.examples`
package. In your own applications, it is unlikely that you will ever
need to import them.

Finally, we try to get the :mod:`pygame2.video` module, which is
necessary for displaying the window and image. As Pygame2 can run
without SDL support, we add a typical safety net to get out without too
much noise, if SDL support is not given.

Window Creation and Image Loading
=================================
Any graphical application requires access to the screen, mostly in form
of a window, which basically represents a portion of the screen, the
application has access to and the application can manipulate. In most cases
that portion has a border and title bar around it, so the user can move
it around on the screen and reorganize anything, so it fits his needs.

Once we have imported all necessary parts, let's create a window to have
access to the screen, so we can display the logo and thus represent it
to the user. ::

  pygame2.video.init ()

  imgresource = pygame2.examples.RESOURCES.get ("logo.bmp")
  surface = pygame2.image.load (imgresource)

  white = pygame2.Color (255, 255, 255)
  
  window = pygame2.video.Window ("Hello World!", surface.width + 10, surface.height + 10)
  window.fill (white)
  window.blit (surface, (5, 5))
  window.show ()

First, we initialize the :mod:`pygame2.video` internals, so we can
have access to the screen and create windows on top of it. Afterwards,
we get the logo from the :mod:`pygame2.examples` package and create a
:class:`pygame2.Surface` from it, which can be easily shown later on and
which allows us to determine the minimum window size we need to display it.
 
Once done with that, :class:`pygame2.video.Window` will create the
window for us. We make the window slightly larger than the image size
to have some small border around the image.

If the window is first created, it will appear all black on the screen
by default. We change that by filling the window with a white color
now and afterwards copy (which is called *blitting*) our loaded image to
the window. As you can see, we are using ``(5, 5)`` as second argument
to :meth:`pygame2.video.Window.blit`. This is the top-left (x, y) offset to
start copying the image contents at.

.. tip::

   Try to experiment with different values instead of (5, 5), for
   example (-10, 8) or (17, -12) to learn more about the blit offset and
   its behaviour.

Finally, we have to tell the operating system or window manager that the window
should be shown on the screen, which we can do with
:meth:`pygame2.video.Window.show()`

Making the Application responsive
=================================
We are nearly done now. We have an image to display, we have a window, where
the image should be displayed on, so we can execute the written code, not?

Well, yes, but the only thing that will happen is that we will notice a
short flickering before the application exits. Maybe we can even see
the window with the logo for a short moment, but that's not what we
want, do we?

To keep the window on the screen and to make it responsive to user
input, such as closing the window, react upon the mouse cursor or key
presses, we have to add a so-called event loop. The event loop will deal
with certain types of actions happening on the window or while the
window is focused by the user and - as long as the event loop is
running - will keep the window shown on the screen [#f1]_. ::

  okay = True
  while okay:
      for ev in pygame2.event.get ():
          if ev.is_quit ():
              okay = False
          if ev.is_keydown () and ev.key == pygame2.event.K_ESCAPE:
              okay = False

  video.quit ()

TBD

.. rubric:: Footnotes

.. [#f1] *shown* is not entirely true, but let's go with that for now.
