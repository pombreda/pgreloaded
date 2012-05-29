.. module:: pygame2.ebs
   :synopsis: A component-based entity system framework.

:mod:`pygame2.ebs` - A component-based entity system framework
==============================================================

This module loosely follows a component oriented pattern to separate
object instances, carried data and processing logic within applications
or games. It uses a entity based approach, in which object instances are
unique identifiers, while their data is managed within components, which
are separately stored. For each individual component type a processing
system will take care of all necessary updates for the World
environment.

.. class:: Component()

   Data object for entities.

   A Component should ideally only consist of the minimum set of data
   that specifies a certain behaviour of an entity in the application
   world. It does not carry any application logic, but only data that
   can be read or written.

.. class:: Entity(world : World)

    An entity is a specific object living in the application world. It
    does not carry any data or application logic, but merely acts as
    identifier label for data that is maintained in the application
    world itself.

    As such, it is an composition of components, which would not exist
    without the entity identifier. The entity itself is non-existent to
    the application world as long as it does not carry any data that can
    be processed by a system within the application world.

   .. attribute:: id

      The id of the Entity. Every Entity has a unique id, that is
      represented by a :class:`uuid.UUID` instance.

   .. attribute:: world

      The :class:`World` the entity reside in.

.. class:: Applicator()

   A processing system for combined data sets. The :class:`Applicator`
   is an enhanced :class:`System` that receives combined data sets based
   on its set :attr:`System.componenttypes`

   .. attribute:: componenttypes

      A tuple of :class:`Component` based class identifiers that shall
      be processed by the :class:`Applicator`.
      
   .. process(world : World, componentsets : iterable)
   
      Processes tuples of :class:`Component` items. ``componentsets`` will
      contain :class:`Component` tuples, that match the :attr:`componenttypes`
      of the :class:`Applicator`. If, for example, the :class:`Applicator`
      is defined as ::
      
        class MyApplicator(Applicator):
            def __init__(self):
                self.componenttypes = (Foo, Bar)

      its process method will receive ``(Foo, Bar)`` tuples ::
      
            def process(self, world, componentsets):
                for foo_item, bar_item in componentsets:
                    ...
   
      Additionally, the :class:`Applicator` will not process all possible
      combinations of valid components, but only those, which are associated
      with the same :class:`Entity`. That said, an :class:`Entity` *must*
      contain a ``Foo`` as well as a ``Bar`` :class:`Component` in order to
      have them both processed by the :class:`Applicator` (while a
      :class:`System` with the same ``componenttypes`` would pick either of 
      them, depending on their availability).
      
.. class:: System()

   A processing system within an application world consumes the
   components of all entities, for which it was set up. At time of
   processing, the system does not know about any other component type
   that might be bound to any entity.

   Also, the processing system does not know about any specific entity,
   but only is aware of the data carried by all entities.

   .. attribute:: componenttypes

      A tuple of :class:`Component` based class identifiers that shall
      be processed by the :class:`System`

   .. method:: process(world : World, components : iterable)

      Processes :class:`Component` items.

      This method has to be implemented by inheriting classes.


.. class:: World()

   An application world defines the combination of application data and
   processing logic and how the data will be processed. As such, it is a
   container object in which the application is defined.

   The application world maintains a set of entities and their related
   components as well as a set of systems that process the data of the
   entities. Each processing system within the application world only
   operates on a certain set of components, but not all components of an
   entity at once.

   The order in which data is processed depends on the order of the
   added systems.

   .. attribute:: systems

      The :class:`System` objects bound to the world.

   .. method:: add_system(system : System)

      Adds a processing :class:`System` to the world. The system will be
      added as last item in the processing order.

   .. method:: delete_entity(entity : Entity)

      Removes an :class:`Entity` from the World, including all
      :class:`Component` data that.

   .. method:: insert_system(index : int, system : System)

      Adds a processing :class:`System` to the world. The system will be
      added at the specified position in the processing order.

   .. method:: process()

      Processes all :class:`Component` items within their corresponding
      :class:`System` instances.

   .. method:: remove_system(system : System)

      Removes a processing :class:`System` from the world.
