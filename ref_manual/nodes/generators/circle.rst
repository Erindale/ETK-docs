.. index:: Generators; Circle
.. _etk.generators.circle:

*******
 Circle
*******

The **Circle** node group is for creating circles and arcs.

.. figure:: /images/nodes-circle.png
   :align: right

   The ETK_Circle node.


Inputs
=======

|INTEGER_SINGLE| Vertices
    The count of vertices in the circle.

|FLOAT_SINGLE| Radius
    The circle's radius.

|FLOAT_SINGLE| U Min
    The starting angle of the arc in degrees.

|FLOAT_SINGLE| U Max
    The ending angle of the arc in degrees.

|BOOLEAN_SINGLE| Use Spacing
    A toggle to use the *Spacing* value instead of vertex count.

|FLOAT_SINGLE| Spacing
    The distance along the arc of the circle on which to place points.

|BOOLEAN_SINGLE| Centre Vertex
    tbd

Outputs
========

|GEOMETRY| Geometry
    The generated points.

|INTEGER_SINGLE| Size
    The total number of points generated.

|FLOAT_FIELD| Fac
    A 0-1 gradient across the points.

|VECTOR_FIELD| Rotation


Example Usage
==============

.. figure:: /images/nodes-circle_basic.png
   :align: center
   :width: 800

   The **ETK_Circle** group can be used to create a circle of icospheres.
