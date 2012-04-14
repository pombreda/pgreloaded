import sys
import unittest
from pygame2.ebs import *


class Position(Component):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


class PositionEntity(Entity):
    def __init__(self, world, x=0, y=0):
        self.position = Position(x, y)


class PositionSystem(System):
    def __init__(self):
        self.componenttypes = (Position,)

    def process(self, world, components):
        for c in components:
            c.x += 1
            c.y += 1


class EBSTest(unittest.TestCase):
    __tags__ = ["ebs"]

    def setUp(self):
        if sys.version.startswith("3.1"):
            self.assertIsInstance = \
                lambda x, t: self.assertTrue(isinstance(x, t))

    def tearDown(self):
        pass

    def test_Component(self):
        comp = Component()
        self.assertIsInstance(comp, Component)

        p = Position()
        self.assertIsInstance(p, Position)
        self.assertIsInstance(p, Component)

    def test_Entity(self):
        world = World()
        world.add_system(PositionSystem())

        e = Entity(world)
        e2 = Entity(world)
        self.assertIsInstance(e, Entity)
        self.assertIsInstance(e2, Entity)
        self.assertNotEqual(e, e2)

        p = PositionEntity(world)
        self.assertIsInstance(p, PositionEntity)
        self.assertIsInstance(p, Entity)

    def test_Entity_id(self):
        world = World()
        ent1 = Entity(world)
        ent2 = Entity(world)
        self.assertNotEqual(ent1.id, ent2.id)

    def test_Entity_world(self):
        world = World()
        world2 = World()
        ent1 = Entity(world)
        ent2 = Entity(world2)
        self.assertEqual(ent1.world, world)
        self.assertNotEqual(ent1.world, world2)
        self.assertEqual(ent2.world, world2)
        self.assertNotEqual(ent2.world, world)
        self.assertNotEqual(ent1.world, ent2.world)

    def test_Entity__inheritance(self):
        world = World()

        # No bound system, so this should raise an error.
        self.assertRaises(KeyError, PositionEntity, world)

        world.add_system(PositionSystem())
        pos1 = PositionEntity(world)
        pos2 = PositionEntity(world, 10, 10)
        for p in (pos1, pos2):
            self.assertIsInstance(p, PositionEntity)
            self.assertIsInstance(p, Entity)
            self.assertIsInstance(p.position, Position)
            self.assertIsInstance(p.position, Component)

    def test_World(self):
        w = World()
        self.assertIsInstance(w, World)

    def test_World_add_remove_system(self):
        world = World()
        self.assertIsInstance(world, World)

        for method in (world.add_system, world.remove_system):
            for val in (None, "Test", Position, Entity(world)):
                self.assertRaises(TypeError, method, val)

        psystem = PositionSystem()
        world.add_system(psystem)
        self.assertTrue(len(world.systems) != 0)
        self.assertTrue(psystem in world.systems)

        entity = PositionEntity(world)
        self.assertIsInstance(entity.position, Position)

        world.remove_system(psystem)
        self.assertTrue(len(world.systems) == 0)
        self.assertTrue(psystem not in world.systems)

        # The data must stay intact in the world, even if the processing
        # system has been removed.
        self.assertIsInstance(entity.position, Position)

    def test_World_entities(self):
        w = World()
        self.assertEqual(len(w.entities), 0)

        for x in range(100):
            Entity(w)
        self.assertEqual(len(w.entities), 100)

    def test_World_delete_entity(self):
        w = World()
        e1 = Entity(w)
        e2 = Entity(w)

        self.assertRaises(TypeError, w.delete_entity, None)
        self.assertRaises(TypeError, w.delete_entity, "Test")
        self.assertRaises(TypeError, w.delete_entity, 1234)

        self.assertEqual(len(w.entities), 2)
        w.delete_entity(e1)
        self.assertEqual(len(w.entities), 1)
        w.delete_entity(e2)
        self.assertEqual(len(w.entities), 0)

        # The next two should have no effect
        w.delete_entity(e1)
        w.delete_entity(e2)

    def test_System(self):
        world = World()
        self.assertRaises(TypeError, world.add_system, None)
        self.assertRaises(TypeError, world.add_system, 1234)
        self.assertRaises(TypeError, world.add_system, "Test")

        class ErrornousSystem(System):
            def __init__(self):
                pass

        esystem = ErrornousSystem()
        # No component types defined.
        self.assertRaises(TypeError, world.add_system, esystem)
        self.assertEqual(len(world.systems), 0)

        psystem = PositionSystem()
        world.add_system(psystem)
        self.assertTrue(psystem in world.systems)

    def test_System_process(self):
        world = World()

        class ErrornousSystem(System):
            def __init__(self):
                self.componenttypes = (Position,)

        esystem = ErrornousSystem()
        world.add_system(esystem)
        for x in range(10):
            PositionEntity(world)
        self.assertTrue(esystem in world.systems)
        self.assertRaises(NotImplementedError, world.process)

        world2 = World()
        psystem = PositionSystem()
        world2.add_system(psystem)
        for x in range(10):
            PositionEntity(world2)
        self.assertTrue(psystem in world2.systems)
        world2.process()
        for c in world2.components[Position].values():
            self.assertEqual(c.x, 1)
            self.assertEqual(c.y, 1)
        world2.process()
        for c in world2.components[Position].values():
            self.assertEqual(c.x, 2)
            self.assertEqual(c.y, 2)

if __name__ == '__main__':
    unittest.main()
