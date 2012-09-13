import sys
import unittest
from pygame2.events import EventHandler
from pygame2.scene import *


class SceneTest(unittest.TestCase):
    __tags__ = ["scene"]

    def setUp(self):
        if sys.version.startswith("3.1"):
            self.assertIsInstance = \
                lambda x, t: self.assertTrue(isinstance(x, t))

    def tearDown(self):
        pass

    def test_SceneManager(self):
        mgr = SceneManager()
        self.assertIsInstance(mgr, SceneManager)
        self.assertEqual(mgr.scenes, [])
        self.assertIsNone(mgr.next)
        self.assertIsNone(mgr.current)

    def ttest_SceneManager_push_pop(self):
        scene1 = Scene()
        scene2 = Scene()
        mgr = SceneManager()
        mgr.push(scene1)
        self.assertEqual(mgr.next, scene1)
        self.assertIsNone(mgr.current)
        self.assertEqual(mgr.scenes, [])
        mgr.pop()
        self.assertEqual(mgr.next, scene1)
        self.assertIsNone(mgr.current)
        self.assertEqual(mgr.scenes, [])
        mgr.push(scene2)
        mgr.push(scene2)
        mgr.push(scene2)
        mgr.pop()
        mgr.pop()
        mgr.pop()
        self.assertEqual(mgr.next, scene2)
        self.assertIsNone(mgr.current)
        self.assertEqual(mgr.scenes, [])

        mgr.update()
        self.assertEqual(mgr.current, scene2)
        self.assertIsNone(mgr.next)
        self.assertEqual(mgr.scenes, [])
        mgr.push(scene1)
        self.assertEqual(mgr.current, scene2)
        self.assertEqual(mgr.next, scene1)
        self.assertEqual(mgr.scenes, [scene2])
        mgr.push(scene1)
        self.assertEqual(mgr.current, scene2)
        self.assertEqual(mgr.next, scene1)
        self.assertEqual(mgr.scenes, [scene2, scene2])
        mgr.push(scene1)
        self.assertEqual(mgr.current, scene2)
        self.assertEqual(mgr.next, scene1)
        self.assertEqual(mgr.scenes, [scene2, scene2, scene2])
        mgr.pop()
        self.assertEqual(mgr.current, scene2)
        self.assertEqual(mgr.next, scene2)
        self.assertEqual(mgr.scenes, [scene2, scene2])

    def test_SceneManager_pause_unpause_update(self):
        scene1 = Scene("Scene 1")
        scene2 = Scene("Scene 2")
        mgr = SceneManager()

        paused = []
        unpaused = []
        started = []
        ended = []

        def pause_cb(scene):
            paused.append(scene)

        def unpause_cb(scene):
            unpaused.append(scene)

        def started_cb(scene):
            started.append(scene)

        def ended_cb(scene):
            ended.append(scene)

        for s in (scene1, scene2):
            s.started += started_cb
            s.paused += pause_cb
            s.unpaused += unpause_cb
            s.ended += ended_cb

        mgr.push(scene1)
        self.assertEqual(scene1.state, SCENE_ENDED)
        self.assertTrue(scene1.has_ended)
        mgr.update()
        self.assertEqual(scene1.state, SCENE_RUNNING)
        self.assertTrue(scene1.is_running)
        self.assertEqual(started[0], scene1)

        mgr.pause()
        self.assertEqual(scene1.state, SCENE_PAUSED)
        self.assertTrue(scene1.is_paused)
        self.assertEqual(paused[0], scene1)
        self.assertEqual(started[0], scene1)

        mgr.unpause()
        self.assertEqual(scene1.state, SCENE_RUNNING)
        self.assertTrue(scene1.is_running)
        self.assertEqual(paused[0], scene1)
        self.assertEqual(started[0], scene1)
        self.assertEqual(unpaused[0], scene1)

        mgr.push(scene2)
        self.assertEqual(scene1.state, SCENE_RUNNING)
        self.assertTrue(scene1.is_running)
        self.assertEqual(mgr.current, scene1)
        self.assertEqual(mgr.next, scene2)

        paused = []
        started = []
        unpaused = []

        mgr.update()
        self.assertEqual(scene1.state, SCENE_ENDED)
        self.assertTrue(scene1.has_ended)
        self.assertEqual(started[0], scene2)
        self.assertEqual(scene2.state, SCENE_RUNNING)
        self.assertTrue(scene2.is_running)
        self.assertEqual(ended[0], scene1)
        self.assertEqual(mgr.current, scene2)
        self.assertEqual(mgr.next, None)

        paused = []
        started = []
        unpaused = []
        ended = []

        mgr.pop()
        self.assertEqual(mgr.current, scene2)
        self.assertEqual(mgr.next, scene1)
        mgr.update()
        self.assertEqual(scene2.state, SCENE_ENDED)
        self.assertTrue(scene2.has_ended)
        self.assertEqual(ended[0], scene2)
        self.assertEqual(scene1.state, SCENE_RUNNING)
        self.assertTrue(scene1.is_running)
        self.assertEqual(started[0], scene1)

    def test_Scene(self):
        scene = Scene()
        self.assertIsInstance(scene, Scene)
        self.assertIsNone(scene.name)
        self.assertEqual(scene.state, SCENE_ENDED)
        self.assertIsInstance(scene.started, EventHandler)
        self.assertIsInstance(scene.paused, EventHandler)
        self.assertIsInstance(scene.unpaused, EventHandler)
        self.assertIsInstance(scene.ended, EventHandler)

        scene = Scene("test")
        self.assertIsInstance(scene, Scene)
        self.assertEqual(scene.name, "test")

    def test_Scene_start_pause_unpause_end(self):
        scene = Scene()
        self.assertEqual(scene.state, SCENE_ENDED)

        # Starting
        scene.start()
        self.assertEqual(scene.state, SCENE_RUNNING)
        scene.start()
        self.assertEqual(scene.state, SCENE_RUNNING)

        # Restart
        scene.end()
        self.assertEqual(scene.state, SCENE_ENDED)
        scene.start()
        self.assertEqual(scene.state, SCENE_RUNNING)
        scene.start()
        self.assertEqual(scene.state, SCENE_RUNNING)
        scene.end()
        self.assertEqual(scene.state, SCENE_ENDED)

        # Pause/start
        scene.pause()
        self.assertEqual(scene.state, SCENE_ENDED)
        scene.start()
        self.assertEqual(scene.state, SCENE_RUNNING)
        scene.pause()
        self.assertEqual(scene.state, SCENE_PAUSED)
        scene.start()
        self.assertEqual(scene.state, SCENE_PAUSED)
        scene.unpause()
        self.assertEqual(scene.state, SCENE_RUNNING)
        scene.end()
        self.assertEqual(scene.state, SCENE_ENDED)

    def test_Scene_is_running_is_paused_has_ended(self):
        scene = Scene()
        self.assertEqual(scene.state, SCENE_ENDED)
        self.assertFalse(scene.is_running)
        self.assertFalse(scene.is_paused)
        self.assertTrue(scene.has_ended)
        scene.start()
        self.assertTrue(scene.is_running)
        self.assertFalse(scene.is_paused)
        self.assertFalse(scene.has_ended)
        scene.pause()
        self.assertFalse(scene.is_running)
        self.assertTrue(scene.is_paused)
        self.assertFalse(scene.has_ended)
        scene.unpause()
        self.assertTrue(scene.is_running)
        self.assertFalse(scene.is_paused)
        self.assertFalse(scene.has_ended)
        scene.end()
        self.assertFalse(scene.is_running)
        self.assertFalse(scene.is_paused)
        self.assertTrue(scene.has_ended)

if __name__ == '__main__':
    sys.exit(unittest.main())
