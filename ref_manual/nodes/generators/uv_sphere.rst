.. index:: Generators; UV Sphere
.. _etk-generators-uv_sphere:

**********
 UV Sphere
**********

.. figure:: /images/nodes-uv_sphere.png
   :align: right

   The ETK_UV Sphere node.

A group to generate a UV Sphere.

Using U (horizontal) and V (vertical) limits define the region if a
full sphere isn’t needed.

Inputs
=======

|FLOAT_FIELD_SINGLE| Radius
   The radius of the sphere in meters..

|INTEGER| U Count
   The number of vertices in the U direction per loop.

|INTEGER| V Count
   The number of loops.

|FLOAT_FIELD_SINGLE| U Min
   The lower U limit in degrees.

|FLOAT_FIELD_SINGLE| U Max
   The upper U limit in degrees.

|FLOAT_FIELD_SINGLE| V Min
   The lower V limit in degrees.

|FLOAT_FIELD_SINGLE| V Max
   The upper V limit in degrees.


Outputs
========

|GEOMETRY| Geometry
   The generated geometry.

|INTEGER| Size
   The total number of points generated.

|FLOAT_FIELD| U Fac
   A 0-1 gradient around the points in the U direction.

|FLOAT_FIELD| V Fac
   A 0-1 gradient around the points in the V direction.

|VECTOR| Rotation
   The rotation vector for each point.


Examples
========

.. figure:: /images/nodes-uv_sphere_basic.png
   :align: center
   :width: 800

   The **UV Sphere** group used to create a sphere with a hole.
