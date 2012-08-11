.. module:: pygame2.events
   :synopsis: General purpose event handling routines.

:mod:`pygame2.events` - General purpose event handling routines
===============================================================

.. class:: EventHandler(sender)

   A simple event handling class, which manages callbacks to be
   executed.

   The EventHandler does not need to be kept as separate instance, but
   is mainly intended to be used as attribute in event-aware class
   objects. ::

       >>> def myfunc(sender):
       ...     print("event triggered by %s" % sender)
       ...
       >>> class MyClass(object):
       ...     def __init__(self):
       ...         self.anevent = EventHandler(self)
       ...
       >>> myobj = MyClass()
       >>> myobj.anevent += myfunc
       >>> myobj.anevent()
       event triggered by <__main__.MyClass object at 0x801864e50>


   .. attribute:: callbacks

      A list of callbacks currently bound to the :class:`EventHandler`.

   .. attribute:: sender

      The responsible object that executes the :class:`EventHandler`.

   .. method:: add(callback : Callable)

      Adds a callback to the :class:`EventHandler`.

   .. method:: remove(callback : Callable)

      Removes a callback from the :class:`EventHandler`.

   .. method:: __call__(*args)

      Executes all connected callbacks in the order of addition,
      passing the :attr:`sender` of the :class:`EventHandler` as first
      argument and the optional args as second, third, ... argument to
      them.

   .. method:: process()

      Processes all :class:`Component` items within their corresponding
      :class:`System` instances.

   .. method:: remove_system(system : System)

      Removes a processing :class:`System` from the world.

.. class:: MPEventHandler(sender)

   An asynchronous event handling class based on :class:`EventHandler`,
   in which callbacks are executed in parallel. It is the responsibility
   of the caller code to ensure that every object used maintains a
   consistent state. The :class:`MPEventHandler` class will not apply
   any locks, synchronous state changes or anything else to the
   arguments being used. Cosider it a "fire-and-forget" event handling
   strategy.

   .. note::

      The :class:`MPEventHandler` relies on the :mod:`multiprocessing`
      module. If the module is not available in the target environment,
      a :exc:`pygame2.compat.UnsupportedError` is raised.
