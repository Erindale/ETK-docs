.. index:: Generators; Line
.. _etk.generators.line:

*****
 Line
*****

.. figure:: /images/nodes-line.png
   :align: right

   The ETK_Line node.

The **ETK_Line** group node functions similarly to the default *Line* primitive
node but with a socket to toggle between length and spacing (offset)
mode.

Inputs
=======

|INTEGER| Vertices
   Integer value for total number of vertices.

|VECTOR_FIELD_SINGLE| Start

|VECTOR_FIELD_SINGLE| Direction

|FLOAT_FIELD_SINGLE| Length
    The length of the line in meters.

|BOOLEAN_FIELD_SINGLE| Use Spacing
    When check, use the *Length* value as an offset for each vertex created.


Outputs
========

|GEOMETRY| Geometry
   The generated geometry,

|INTEGER| Size
   The total number of points generated.

|FLOAT_FIELD| Fac
   A 0-1 gradient across the points.

|VECTOR_FIELD_SINGLE| Rotation


Example Usage
==============

.. figure:: /images/nodes-line_basic.png
   :align: center
   :width: 800

   Using **ETK_Line** to spread 4 icospheres 1 meter apart in X. Note
   how *Use Spacing* is used in this example.
