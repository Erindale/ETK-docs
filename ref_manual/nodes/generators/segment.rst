.. index:: Generators; Segment
.. _etk-generators-segment:

********
 Segment
********

.. figure:: /images/nodes-segment.png
   :align: right

   The ETK_Segment node.

The **Segment** group node functions similar to the default Line
primitive node in *End Point* mode but with a socket to toggle between
vertex count and spacing mode.

Inputs
=======

|INTEGER| Vertices
   The number of points in the generated segment.

|VECTOR| A
   Vector for the start point of the line.

|VECTOR| B
   Vector for the end point of the line.

|BOOLEAN| Use Spacing
   If selected, the *Vertices* value is ignored and the number of
   vertices between *A* and *B* is determined by *Spacing*

|FLOAT| Spacing
   This value determines the number of points in the segment when *Use
   Spacing* is set.


Outputs
========

|GEOMETRY| Geometry
   The generated geometry.

|INTEGER| Size
   The total number of points generated.

|FLOAT_FIELD| Fac
   A 0..1 gradiant across the points.

|VECTOR_FIELD| Rotation
   The rotation vector for each vertex.


Example Usage
==============

Line vs. Segment
----------------

This example examines the difference between the **ETK_Segment** (on
top) and the **ETK_Line**. A *Line* sets a start point and direction
and then uses length as the distance between each vertex. A *Segment*
specifies a start *A* and end *B* point and, in this example, our line is 5
metres long and parallels the X axis 1 metre away in the Y direction.
Since *Use Spacing* is set in *Segment*, the *Vertices* value is
ignored and the *Spacing* value is used to determine the number of points.

.. figure:: /images/nodes-segment_basic.png
   :align: center
   :width: 800

   A comparison of **ETK_Segment** and **ETK_Line**.
