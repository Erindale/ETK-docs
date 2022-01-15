.. index:: Curves; Wire Flood
.. _etk-curves-wire_flood:

***********
 Wire Flood
***********

.. figure:: /images/nodes-wire_flood.png
   :align: right

   The ETK_Wire Flood node.

The **Wire Flood** group populates the input geometry with wires
loops.

Inputs
=======

|GEOMETRY| Geometry
   Input geometry.

|FLOAT_FIELD_SINGLE| Density
   Controls the amount of wires generated.

|INTEGER| Seed
   Randomization seed.

|VECTOR_FIELD_SINGLE| Distance
   Controls the distance between the departure and return point of the
   wires. If decreased the wires will degenerate to a single wire
   since, at zero, it starts and returns to the same position.

|INTEGER| Resolution
   The circumferential resolution of the wire.

|FLOAT_FIELD_SINGLE| Wire Height
   Controls the distance the wires will loop away from the origin of
   the input geometry.

|FLOAT_FIELD_SINGLE| Wire Wiggle
   Increases the distortion along the wires.

|FLOAT_FIELD_SINGLE| Gravity
   Adds some sag in the -Z direction.

|FLOAT_FIELD_SINGLE| Wire Radius
   Adjusts the wire gauge.

|MATERIAL| Material
   A material to set on the wires.

Outputs
========

|GEOMETRY| Geometry
   The generated mass of wire geometry.

Example Usage
==============

.. figure:: /images/nodes-wire_flood_basic.png
   :align: center
   :width: 800

   This example applies the **Wire Flood** group to a
   smoothed :ref:`etk-generators-uv_sphere` object.
