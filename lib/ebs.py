"""
A component-based entity system framework.

pygame2.ebs loosely follows a component oriented pattern to separate
object instances, carried data and processing logic within applications
or games. It uses a entity based approach, in which object instances are
unique identifiers, while their data is managed within components, which
are separately stored. For each individual component type a processing
system will take care of all necessary updates for the World
environment.
"""
from uuid import uuid4
from pygame2.compat import *

__all__ = ["Entity", "World", "System", "Component"]


class Component(object):
    """Data object for entities.

    A Component should ideally only consist of the minimum set of data
    that specifies a certain behaviour of an entity in the application
    world. It does not carry any application logic, but only data that
    can be read or written.
    """
    pass


class Entity(object):
    """A simple object entity.

    An entity is a specific object living in the application world. It
    does not carry any data or application logic, but merely acts as
    identifier label for data that is maintained in the application
    world itself.

    As such, it is an composition of components, which would not exist
    without the entity identifier. The entity itself is non-existent to
    the application world as long as it does not carry any data that can
    be processed by a system within the application world.
    """
    def __new__(cls, world, *args, **kwargs):
        if not isinstance(world, World):
            raise TypeError("world must be a World")
        entity = object.__new__(cls)
        entity._id = uuid4()
        entity._world = world
        world.entities.add(entity)
        return entity

    def __repr__(self):
        return "Entity(id=%s)" % self._id

    def __eq__(self, entity):
        return self._id == entity._id

    def __ne__(self, entity):
        return self._id != entity._id

    def __hash__(self):
        return hash(self._id)

    def __getattr__(self, name):
        """Gets the component data related to the Entity."""
        if name in ("_id", "_world"):
            return object.__getattr__(self, name)
        ctype = self._world._componenttypes[name]
        return self._world.components[ctype][self._id]

    def __setattr__(self, name, value):
        """Sets the component data related to the Entity."""
        if name in ("_id", "_world"):
            object.__setattr__(self, name, value)
        else:
            if not isinstance(value, Component):
                raise TypeError("only Component items can be bound")
            self._world.components[type(value)][self._id] = value

    def __delattr__(self, name):
        """Deletes the component data related to the Entity."""
        if name in ("_id", "_world"):
            raise AttributeError("'%s' cannot be deleted.", name)
        ctype = self._world._componenttypes[name]
        del self._world.components[ctype][self._id]

    @property
    def id(self):
        """The id of the Entity."""
        return self._id

    @property
    def world(self):
        """The world the Entity resides in."""
        return self._world


class World(object):
    """A simple application world.

    An application world defines the combination of application data and
    processing logic and how the data will be processed. As such, it is
    a container object in which the application is defined.

    The application world maintains a set of entities and their related
    components as well as a set of systems that process the data of the
    entities. Each processing system within the application world only
    operates on a certain set of components, but not all components of
    an entity at once.

    The order in which data is processed depends on the order of the
    added systems.
    """
    def __init__(self):
        """Creates a new World instance."""
        self.entities = set()
        self._systems = []
        self.components = {}
        self._componenttypes = {}

    def _add_system_information(self, system):
        if not isinstance(system, System):
            raise TypeError("system must be a  System")
        for classtype in system.componenttypes:
            if Component not in classtype.__mro__:
                raise TypeError("'%s' must be a  Component")
            if classtype not in self.components:
                self.components[classtype] = {}
                self._componenttypes[classtype.__name__.lower()] = classtype

    def delete_entity(self, entity):
        """Removes an Entity from the World, including all its data."""
        if not isinstance(entity, Entity):
            raise TypeError("entity must be a Entity")
        eid = entity.id
        for componentset in self.components.values():
            componentset.pop(eid, None)
        self.entities.discard(entity)

    def add_system(self, system):
        """Adds a processing system to the world.

        The system will be added as last item in the processing order.
        """
        self._add_system_information(system)
        self._systems.append(system)

    def insert_system(self, index, system):
        """Adds a processing system to the world.

        The system will be added at the specific position of the
        processing order.
        """
        self._add_system_information(system)
        self._systems.insert(index, system)

    def remove_system(self, system):
        """Removes a processing system from the world."""
        if not isinstance(system, System):
            raise TypeError("system must be a System")
        self._systems.remove(system)

    def process(self):
        """Processes all components within their corresponding systems."""
        components = self.components
        systems = self._systems
        for system in self._systems:
            s_process = system.process
            for ctype in system.componenttypes:
                s_process(self, components[ctype].values())

    @property
    def systems(self):
        """Gets the systems bound to the world."""
        return tuple(self._systems)


class System(object):
    """A processing system for component data.

    A processing system within an application world consumes the
    components of all entities, for which it was set up. At time of
    processing, the system does not know about any other component type
    that might be bound to any entity.

    Also, the processing system does not know about any specific entity,
    but only is aware of the data carried by all entities.
    """
    def __new__(cls, *args, **kwargs):
        system = object.__new__(cls)
        system.componenttypes = None
        return system

    def process(self, world, components):
        """Processes Component items.

        This must be implemented by inheriting classes.
        """
        raise NotImplementedError()
