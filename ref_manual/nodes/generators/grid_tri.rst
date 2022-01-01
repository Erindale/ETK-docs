.. index:: Generators; Grid Tri
.. _etk.generators.grid_tri:

*********
 Grid Tri
*********

.. figure:: /images/nodes-grid_tri.png
   :align: right

   The ETK_Grid Tri node.


The **Grid Tri** node can be used for 2-dimensional equilateral triangle
tessellations.


Inputs
=======

|INTEGER_SINGLE| X Count
    Integer value for number of vertices in the X axis.

|INTEGER_SINGLE| Y Count
    Integer value for number of vertices in the Y axis.

|FLOAT_SINGLE| Side Length
    The side length of the triangle.

|BOOLEAN_FIELD_SINGLE| Randomise Rotation?
    Check to randomize the rotation.

|INTEGER_FIELD_SINGLE| Seed
    The seed for the randomisation.

|BOOLEAN_SINGLE| Centred
    A toggle to choose if the grid is centred on the origin or aligned
    on the bottom left corner.


Outputs
========

|GEOMETRY| Triangles
   The generated geometry.

|GEOMETRY| Centres
   Ouput a point at the centre of each triangle.

|INTEGER_SINGLE| Size
   The total number of points generated.

|FLOAT_FIELD| X Fac
   A 0-1 gradient across the points in the X axis.

|FLOAT_FIELD| Y Fac
   A 0-1 gradient across the points in the Y axis.

|BOOLEAN_FIELD| Row Alt
   True on alternate rows.

|VECTOR_FIELD| Rotation
   The rotation vector of each tile.


Example Usage
==============

.. figure:: /images/nodes-grid_tri_basic.png
   :align: center
   :width: 800

   Using **Grid Tri** to generate a simple grid of triangles, which
   are scaled slightly to show the outlines of the instances.
