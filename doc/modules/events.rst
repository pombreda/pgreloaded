.. module:: pygame2.events
   :synopsis: General purpose event handling routines.

:mod:`pygame2.events` - General purpose event handling routines
===============================================================

.. todo::

   Add a describtion.

.. class:: EventHandler(sender)

   A simple event handling class, which manages callbacks to be
   executed.

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
