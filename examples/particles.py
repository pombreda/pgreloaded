"""Particle simulation"""
import sys
import random

# Import the particles module, so we have access to all relevant parts
# for dealing with particles.
import pygame2.particles as particles
# We will create some systems and an entity for creating the particle
# simulation. Hence we will need some things from the ebs module.
from pygame2.ebs import Entity, System, World

# Try to import the video system and event system. Since pygame2.video
# makes use of pygame2.sdl, the import might fail, if the SDL DLL could
# not be loaded. In that case, just print the error and exit with a
# proper error code.
try:
    import pygame2.video as video
    import pygame2.sdl.events as sdlevents
    import pygame2.sdl.mouse as sdlmouse
    import pygame2.sdl.timer as sdltimer
    import pygame2.sdl.surface as sdlsurface
    import pygame2.sdl.rect as sdlrect
except ImportError:
    import traceback
    traceback.print_exc()
    sys.exit(1)

# Import the resources, so we have easy access to the example images.
from pygame2.resources import Resources
RESOURCES = Resources(__file__, "resources")


# The Particle class offered by pygame2.particles only contains the life
# time information of the particle, which will be decreased by one each
# time the particle engine processes it as well as a x- and
# y-coordinate. This is not enough for us, since we want them to have a
# velocity as well to make moving them around easier. Also, each
# particle can look different for us, so we also store some information
# about the image to display on rendering in ptype.
#
# If particles run out of life, we want to remove them, since we do not
# want to flood our world with unused entities. Thus, we store a
# reference to the entity, the particle belongs to, too. This allows use
# to remove them easily later on.
class CParticle(particles.Particle):
    def __init__(self, entity, x, y, vx, vy, ptype, life):
        super(CParticle, self).__init__(x, y, life)
        self.entity = entity
        self.type = ptype
        self.vx = vx
        self.vy = vy


# A simple Entity class, that contains the particle information. This
# represents our living particle object.
class EParticle(Entity):
    def __init__(self, world, x, y, vx, vy, ptype, life):
        self.cparticle = CParticle(self, x, y, vx, vy, ptype, life)


# A callback function for creating new particles. It is needed by the
# ParticleEngine and the requirements are explained below.
def createparticles(world, deadones, count=None):
    if deadones is not None:
        count = len(deadones)
    # Create a replacement for each particle that died. The particle
    # will be created at the current mouse cursor position (explained
    # below) with a random velocity, life time, and image to be
    # displayed.
    for c in range(count):
        x = world.mousex
        y = world.mousey
        vx = random.random() * 3 - 1
        vy = random.random() * 3 - 1
        life = random.randint(20, 100)
        ptype = random.randint(0, 2)  # 0-2 denote the image to be used
        # We do not need to assign the particle to a variable, since it
        # will be added to the World and we do not need to do perform
        # any post-creation operations.
        EParticle(world, x, y, vx, vy, ptype, life)


# A callback function for updating particles. It is needed by the
# ParticleEngine and the requirements are explained below.
def updateparticles(world, particles):
    # For each existing, living particle, move it to a new location,
    # based on its velocity.
    for p in particles:
        p.x += p.vx
        p.y += p.vy


# A callback function for deleting particles. It is neede by the
# ParticleEngine and the requirements are explained below.
def deleteparticles(world, deadones):
    # As written in the comment for the CParticle class, we will use the
    # stored entity reference of the dead particle components to delete
    # the dead particles from the world.
    world.delete_entities(p.entity for p in deadones)


# Create a simple rendering system for particles. This is somewhat
# similar to the SprinteRenderer from pygame2.video. Since we operate on
# particles rather than sprites, we need to provide our own rendering
# logic.
class ParticleRenderer(System):
    def __init__(self, surface, images):
        # Create a new particle renderer. The surface argument will be
        # the targets surface to do the rendering on. images is a set of
        # images to be used for rendering the particles.
        super(ParticleRenderer, self).__init__()
        # Define, what Component instances are processed by the
        # ParticleRenderer.
        self.componenttypes = (CParticle, )
        self.surface = surface
        self.images = images

    def process(self, world, components):
        # Processing code that will render all existing CParticle
        # components that currently exist in the world. We have a 1:1
        # mapping between the created particle entities and associated
        # particle components; that said, we render all created
        # particles here.

        # We deal with quite a set of items, so we create some shortcuts
        # to save Python the time to look things up.
        #
        # The SDL_Rect is used for the blit operation below and is used
        # as destination position for rendering the particle.
        r = sdlrect.SDL_Rect()
        # TheSDL2 blit function to use. This will take an image
        # (SDL_Surface) as source and another one as target to copy the
        # source on. The whole process is called "blitting".
        doblit = sdlsurface.blit_surface
        # And some more shortcuts.
        target = self.surface
        images = self.images
        # Before rendering all particles, make sure the old ones are
        # removed from the surface by filling it will a black color.
        video.fill(target, 0x0)
        # Render all particles.
        for particle in components:
            # Set the correct destination position for the particle
            r.x = int(particle.x)
            r.y = int(particle.y)
            # Select the correct image for the particle.
            img = images[particle.type]
            # Render (or blit) the particle by using the designated
            # image.
            doblit(img.surface, None, target, r)


def run():
    # Create the environment, in which our particles will exist.
    world = World()

    # Set up the globally available information about the current mouse
    # position. We use that information to determine the emitter
    # location for new particles.
    world.mousex = 400
    world.mousey = 300

    # Create the particle engine. It is just a simple System that uses
    # callback functions to update a set of components.
    engine = particles.ParticleEngine()

    # Bind the callback functions to the particle engine. The engine
    # does the following on processing:
    # 1) reduce the life time of each particle by one
    # 2) create a list of particles, which's life time is 0 or below.
    # 3) call createfunc() with the world passed to process() and
    #    the list of dead particles
    # 4) call updatefunc() with the world passed to process() and the
    #    set of particles, which still are alive.
    # 5) call deletefunc() with the world passed to process() and the
    #    list of dead particles. deletefunc() is respsonible for
    #    removing the dead particles from the world.
    engine.createfunc = createparticles
    engine.updatefunc = updateparticles
    engine.deletefunc = deleteparticles
    world.add_system(engine)

    # We create all particles at once before starting the processing.
    # We also could create them in chunks to have a visually more
    # appealing effect, but let's keep it simple.
    createparticles(world, None, 300)

    # Initialize the video subsystem, create a window and make it visible.
    video.init()
    window = video.Window("Particles", size=(800, 600))
    window.show()

    # Create a set of images to be used as particles on rendering. The
    # images are used by the ParticleRenderer created below.
    images = (video.load_image(RESOURCES.get_path("circle.png")),
              video.load_image(RESOURCES.get_path("square.png")),
              video.load_image(RESOURCES.get_path("star.png"))
              )

    # Center the mouse on the window. We use the SDL2 functions directly
    # here. Since the SDL2 functions do not know anything about the
    # video.Window class, we have to pass the window's SDL_Window to it.
    sdlmouse.warp_mouse_in_window(window.window, 400, 300)

    # Hide the mouse cursor, os it does not show up - just show the
    # particles.
    sdlmouse.show_cursor(False)

    # As in colorpalettes.py, explicitly acquire the window's surface to
    # draw on.
    windowsurface = window.get_surface()

    # Create the rendering system for the particles. This is somewhat
    # similar to the SpriteRenderer, but since we only operate with
    # hundreds of particles (and not sprites with all their overhead),
    # we need an own rendering system.
    renderer = ParticleRenderer(windowsurface, images)
    world.add_system(renderer)

    # The almighty event loop. You already know several parts of it.
    running = True
    while running:
        event = sdlevents.poll_event(True)
        while event is not None:
            if event.type == sdlevents.SDL_QUIT:
                running = False
            if event.type == sdlevents.SDL_MOUSEMOTION:
                # Take care of the mouse motions here. Every time the
                # mouse is moved, we will make that information globally
                # available to our application environment by updating
                # the world attributes created earlier.
                world.mousex = event.motion.x
                world.mousey = event.motion.y
                # We updated the mouse coordinates once, ditch all the
                # other ones. Since world.process() might take several
                # milliseconds, new motion events can occur on the event
                # queue (10ths to 100ths!), and we do not want to handle
                # each of them. For this example, it is enough to handle
                # one per update cycle.
                sdlevents.flush_event(sdlevents.SDL_MOUSEMOTION)
                break
            event = sdlevents.poll_event(True)
        world.process()
        window.refresh()

    video.quit()
    return 0

if __name__ == "__main__":
    sys.exit(run())
