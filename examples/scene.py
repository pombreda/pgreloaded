"""Scene management examples."""
import sys

from pygame2.scene import Scene, SceneManager

# Try to import the video system and event system. Since pygame2.video makes
# use of pygame2.sdl, the import might fail, if the SDL DLL could not be
# loaded. In that case, just print the error and exit with a proper
# error code.
try:
    import pygame2.video as video
    import pygame2.sdl.events as sdlevents
except ImportError:
    import traceback
    traceback.print_exc()
    sys.exit(1)


# A simple, extended Scene that contains visual components
class ExampleScene(Scene):
    def __init__(self, name):
        super(ExampleScene, self).__init__(name)
        self.components = []


# Creates the first example scene
def create_scene1(manager):
    print("Creating scene 1")
    scene = ExampleScene("Scene 1")
    button_back = video.Button(size=(100, 50))
    button_back.position = 200, 200
    video.fill(button_back, 0xFFFFFFFF)
    button_back.click += lambda btn, ev: manager.pop()
    scene.components.append(button_back)
    return scene


def create_scene2(manager):
    print("Creating scene 2")
    scene = ExampleScene("Scene 2")
    button_back = video.Button(size=(100, 50))
    button_back.position = 200, 200
    video.fill(button_back, 0xFFFFFFFF)
    button_back.click += lambda btn, ev: manager.pop()
    scene.components.append(button_back)
    return scene


def create_scene3(manager):
    print("Creating scene 3")
    scene = ExampleScene("Scene 3")
    button_back = video.Button(size=(100, 50))
    button_back.position = 200, 200
    video.fill(button_back, 0xFFFFFFFF)
    button_back.click += lambda btn, ev: manager.pop()
    scene.components.append(button_back)
    return scene


def create_scene4(manager):
    print("Creating scene 4")
    scene = ExampleScene("Scene 4")
    button_back = video.Button(size=(100, 50))
    button_back.position = 200, 200
    video.fill(button_back, 0xFFFFFFFF)
    button_back.click += lambda btn, ev: manager.pop()
    scene.components.append(button_back)
    return scene


def switch_to(manager, scene):
    print("Switching to %s" % scene.name)
    manager.push(scene)


def start_mainmenu(scene):
    scene.components = []
    button_scene1 = video.Button(size=(100, 50))
    button_scene1.position = 100, 100
    video.fill(button_scene1, 0xFFFFFFFF)
    button_scene1.click += lambda btn, ev: \
        switch_to(scene.manager, create_scene1(scene.manager))
    scene.components.append(button_scene1)

    button_scene2 = video.Button(size=(100, 50))
    button_scene2.position = 100, 160
    video.fill(button_scene2, 0xFFFFFFFF)
    button_scene2.click += lambda btn, ev: \
        switch_to(scene.manager, create_scene2(scene.manager))
    scene.components.append(button_scene2)

    button_scene3 = video.Button(size=(100, 50))
    button_scene3.position = 100, 220
    video.fill(button_scene3, 0xFFFFFFFF)
    button_scene3.click += lambda btn, ev: \
        switch_to(scene.manager, create_scene3(scene.manager))
    scene.components.append(button_scene3)

    button_scene4 = video.Button(size=(100, 50))
    button_scene4.position = 100, 280
    video.fill(button_scene4, 0xFFFFFFFF)
    button_scene4.click += lambda btn, ev: \
        switch_to(scene.manager, create_scene4(scene.manager))
    scene.components.append(button_scene4)


def end_scene(scene):
    print("Scene %s ended" % scene.name)


def run():
    # You know those from the helloworld.py example.
    # Initialize the video subsystem, create a window and make it visible.
    video.init()
    window = video.Window("Pixel Access", size=(800, 600))
    window.show()

    # Since all gui elements are sprites, we can use the SpriteRenderer
    # class, we learned about in helloworld.py, to draw them on the
    # Window.
    renderer = video.SpriteRenderer(window)

    # Create a new UIProcessor, which will handle the user input events
    # and pass them on to the relevant user interface elements.
    uiprocessor = video.UIProcessor()

    # Create a scene manager - this one will take care of managing the
    # different scenes.
    scenemanager = SceneManager()
    # Every time we switch to a different scene, reset the video window, so
    # we do not have any artifacts left on the screen.
    scenemanager.switched += lambda mgr: video.fill(renderer.surface, 0x0)

    # Create the initial scene.
    mainmenu = Scene("Main Menu")
    # Bind the start and end events of the scene. started() will be invoked
    # every time the SceneManager starts the scene. ended() will be invoked,
    # if the scene ends, e.g. if a new scene is pushed to the manager.
    mainmenu.started += start_mainmenu
    mainmenu.ended += end_scene

    # Push the initial scene to the SceneManager.
    scenemanager.push(mainmenu)

    running = True
    while running:
        # Process the SceneManager. This takes care of updating the scene
        # states by checking, if a new scene has to be displayed or not.
        scenemanager.update()

        # The main event loop; we already learned about that in other examples.
        # Check for the events and pass them around.
        event = sdlevents.poll_event(True)
        while event is not None:
            if event.type == sdlevents.SDL_QUIT:
                running = False
            # Pass the SDL2 events to the UIProcessor, which takes care of
            # the user interface logic.
            uiprocessor.dispatch(scenemanager.current.components, event)
            event = sdlevents.poll_event(True)
        # Render all components on all scenes.
        renderer.render(scenemanager.current.components)
        window.refresh()
    video.quit()
    return 0

if __name__ == "__main__":
    sys.exit(run())
