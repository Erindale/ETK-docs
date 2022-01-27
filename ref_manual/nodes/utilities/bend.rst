.. index:: Utilities; Bend
.. _etk-utilities-bend:

*****
 Bend
*****

.. figure:: /images/nodes-bend.png
   :align: right

   The ETK_Bend node.

The **Bend** group can bend geometry into satisfying shapes. Use it by
itself or with the :ref:`etk-utilities-twist` group.


Inputs
=======

|GEOMETRY| Geometry
   Input geometry.

|FLOAT| Angle
   Amount to bend around the *Bend Axis*.

|GEOMETRY| Bend Axis
   Bend around this axis. Some addition control is available
   specifying a *Custom Centre*.

|FLOAT_FIELD_SINGLE| Limit Min
   A 0..1 factor input, a percentage of where along the axis to start
   the bend.

|FLOAT_FIELD_SINGLE| Limit Max
   A 0..1 factor input, a percentage of where along the axis to stop
   bending.

|BOOLEAN_FIELD_SINGLE| Custom Centre
   If unchecked, use the object origin as a centre, otherwise use the
   input vector *Centre* as the centre.

|VECTOR_FIELD_SINGLE| Centre
   Use this centre position when *Custom Centre* is checked.

Outputs
========

|GEOMETRY| Geometry
   The output geometry.


Examples
========

.. figure:: /images/nodes-bend_basic.png
   :align: center
   :width: 800

   Use the **Bend** group to bend the middle (min=0.25, max=0.5) into
   a U-shaped magnet (1/2 of 360° bend to make the U-turn). Note how
   a *Custom Centre* is used to move the axis out and spread the U
   apart.
