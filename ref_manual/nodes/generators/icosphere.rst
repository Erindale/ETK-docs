.. index:: Generators; Icosphere
.. _etk.generators.icosphere:

**********
 Icosphere
**********

.. figure:: /images/nodes-icosphere.png
   :align: right

   The ETK_Icosphere node.

Upcycling the Icosphere primitive node to add some extra
functionality.

Using U (horizontal) and V (vertical) limits to cull points if a full
sphere isn’t needed.

Inputs
=======

|FLOAT_SINGLE| Radius
   The radius of the sphere in meters.

|INTEGER_SINGLE| Subdivisions
    The level of subdivisions on the Icosphere.

|FLOAT_FIELD| U Min
   The lower U limit in degrees.

|FLOAT_FIELD| U Max
   The upper U limit in degrees.

|FLOAT_FIELD| V Min
   The lower V limit in degrees.

|FLOAT_FIELD| V Max
   The upper V limit in degrees.


Outputs
========

|GEOMETRY| Geometry
   The generated geometry.

|INTEGER_SINGLE| Size
   The total number of points generated.

|FLOAT_FIELD| U Fac
   A 0-1 gradient around the points in the U direction.

|FLOAT_FIELD| V Fac
   A 0-1 gradient around the points in the V direction.

|VECTOR_FIELD| Rotation
   The rotation vector for each generated point.


Example Usage
==============

.. figure:: /images/nodes-icosphere_basic.png
   :align: center
   :width: 800

   In this example, cubes have been instanced on the **Icosphere**
   then scaled using *V Fac* and rotated to face the center.
