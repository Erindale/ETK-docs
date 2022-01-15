.. index:: Generators; Spherical Spiral
.. _etk-generators-spherical_spiral:

*****************
 Spherical Spiral
*****************

.. figure:: /images/nodes-spherical_spiral.png
   :align: right

   The ETK_Spherical Spiral node.


The **Spherical Spiral** node group wraps a spiral around a sphere in
the Z direction.


Inputs
=======

|INTEGER_FIELD_SINGLE| Points
   An integer number of points that will form the generated geometry.

|FLOAT| Radius
   The radius of the sphere.

|FLOAT| Rotations
   Number of rotations around the sphere.

|BOOLEAN| Reverse
   Form the spiral in the opposite direction


Outputs
========

|GEOMETRY| Geometry
   The generated geometry.

|INTEGER_FIELD_SINGLE| Size
   The number of points generated.

|FLOAT_FIELD| Curve Fac
   A 0..1 gradient along the curve of the geometry.

|FLOAT_FIELD| Z Fac
   A 0..1 gradient along the Z axis of all the generated points.

|FLOAT_FIELD| θ Fac
   A 0..1 gradient around

|VECTOR_FIELD| Rotation
   A rotation vector at each point.


Example Usage
==============

.. figure:: /images/nodes-spherical_sphere_basic.png
   :align: center
   :width: 800

   The default **ETK_Spherical Spiral** node group output.
