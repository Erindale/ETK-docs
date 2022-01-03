.. index:: Generators; Cylinder
.. _etk.generators.cylinder:

*********
 Cylinder
*********

.. figure:: /images/nodes-cylinder.png
   :align: right

   The **ETK_Cylinder** node group.

The **Cylinder** node group creates a cylinder that can be
configured in several ways.


Inputs
=======

|INTEGER_SINGLE| Vertices
   The integer count of vertices, or resolution, of the cylinder's
   circular ends.

|INTEGER_SINGLE| Parallels
   The number of *cuts*, including the two that form the top and
   bottom.

|FLOAT_SINGLE| Top Radius
   The radius of the top circle.

|FLOAT_SINGLE| Bottom Radius
   The radius of the bottom circle.

|FLOAT_SINGLE| Depth
   The height of the cylinder.

|FLOAT_SINGLE| U Min
   The starting angle of the cylinder's top and bottom caps, in degrees.

|FLOAT_SINGLE| U Max
   The ending angle of the cylinder's caps, in degrees.

|FLOAT_FIELD_SINGLE| Twist
   The amount of rotation in degrees to turn the top of the cylinder.
   The default is 0° or no twist.

|BOOLEAN_SINGLE| Use Spacing
   A toggle to use spacing to specify points around the circles
   instead of vertices.

|FLOAT_SINGLE| Spacing
   The distance between neighboring vertices on the circles that form
   the top and bottom caps. This is ignored unless *Use Spacing* is
   selected.


Outputs
========

|GEOMETRY| Geometry
   The generated cylinder geometry.

|INTEGER_SINGLE| Size
   The number of points generated.

|FLOAT_FIELD| θ Fac
   A 0..1 gradient of the vertices around *each* parallel.

|FLOAT_FIELD| Z Fac
   A 0..1 gradient along the Z axis of the points, which can be used
   to find the parallel vertices along the cylinder.

|VECTOR_FIELD| Rotation
   Provides access to the rotation vector of each vertex.


Example Usage
==============

.. figure:: /images/nodes-cylinder_basic.png
   :align: center
   :width: 800

   Using the **ETK_Cylinder** group to create a simple tapered cone.
