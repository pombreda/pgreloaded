.. module:: pygame2.components
   :synopsis: Pre-defined components for pygame2.ebs.

:mod:`pygame2.components` - Pre-defined components
==================================================

This module contains often used data classes for applications. All data classes
inherit from the :class:`pygame2.ebs.Component` class to be usable with the
:mod:`pygame2.ebs` module.

.. class:: Position(x=0, y=0, z=0)

   A simple positional coordinate on a 2D plane or in a 3D room.

   Position objects can be accessed via their exposed attributes or by an
   index in the range [0:2]. ::

     pos = Position()
     pos.x = 5
     pos[2] = 7 # Change Position.z

   .. attribute:: x

      The value of the x-axis part of the positional coordinate.

   .. attribute:: y

      The value of the y-axis part of the positional coordinate.

   .. attribute:: z

      The value of the z-axis part of the positional coordinate.
