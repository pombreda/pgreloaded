.. module:: pygame2.particles
   :synopsis: A simple particle system.

:mod:`pygame2.particles` - A simple particle system
===================================================

.. inheritance-diagram:: pygame2.particles
   :parts: 1

.. class:: ParticleEngine()

   A simple particle processing system. The :class:`ParticleEngine`
   takes care of creating, updating and deleting particles via callback
   functions. It only decreases the life of the particles by itself and
   marks them as dead, once the particle's life attribute has reached 0
   or below.

   .. attribute:: createfunc

      Function for creating new particles. The function needs to take
      two arguments, the ``world`` argument passed to :meth:`process()`
      and a list of the particles considered dead (:attr:`Particle.life`
      <= 0). ::

        def creation_func(world, deadparticles):
            ...

   .. attribute:: updatefunc

      Function for updating existing, living particles. The function
      needs to take two arguments, the ``world`` argument passed to
      :meth:`process()` and a :class:`set` of the still living
      particles. ::

        def update_func(world, livingparticles):
            ...

   .. attribute:: deletefunc

      Function for deleting dead particles. The function needs to take
      two arguments, the ``world`` argument passed to :meth:`process()`
      and a list of the particles considered dead (:attr:`Particle.life`
      <= 0). ::

        def deletion_func(world, deadparticles):
            ...

.. class:: Particle(x, y, life : int)

   A simple particle component type. It only contains information about
   a x- and y-coordinate and its current life time. The life time will
   be decreased by 1, everytime the particle is processed by the
   :class:`ParticleEngine`.

   .. attribute:: x

      The x coordinate of the particle.

   .. attribute:: y

      The y coordinate of the particle.

   .. attribute:: life

      The remaining life time of the particle.

   .. attribute:: position

      The x- and y-coordinate of the particle as tuple.
