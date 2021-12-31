.. index:: Generators; Grid
.. _etk.generators.grid:

*****
 Grid
*****

.. figure:: /images/nodes-grid.png
   :align: right

   The ETK_Grid node.

The **Grid** node outputs a 3D grid. It can be used to create a plane or a
2D grid as well but if a 3D grid is required it can do that. Rather
than a subdivided cube which just has points on the surface, the **Grid**
node will generate points throughout the volume as well.


Inputs
=======

|INTEGER_SINGLE| X Count
    Integer value for number of vertices in the X axis.

|INTEGER_SINGLE| Y Count
    Integer value for number of vertices in the Y axis.

|INTEGER_SINGLE| Z Count
    Integer value for number of vertices in the Z axis.

|VECTOR_FIELD_SINGLE| Size
    The overall size of the grid in metres.

|BOOLEAN_FIELD_SINGLE| Use Spacing
    Toggle to change the **Size** from overall size to the spacing between
    points.

|FLOAT_FIELD_SINGLE| Randomise
    Maximum distance to randomise position by.

|INTEGER_FIELD_SINGLE| Seed
     The seed for the randomisation.

|BOOLEAN_FIELD_SINGLE| Centred
    A toggle to choose if the grid is centred on the origin or aligned
    on the bottom left corner.


Outputs
========

|GEOMETRY| Geometry
    The generated geometry.

|INTEGER_SINGLE| Size
    The total number of points generated.

|FLOAT_FIELD| X Fac
    A 0-1 gradient across the points in the X axis.

|FLOAT_FIELD| Y Fac
    A 0-1 gradient across the points in the Y axis.

|FLOAT_FIELD| Z Fac
    A 0-1 gradient across the points in the Z axis.


Example Usage
==============

This example builds a 3D grid out of which the inside points in X and
Z are removed to form a hollow box of icospheres.

.. figure:: /images/nodes-grid_example.png
   :width: 800
   :align: center

   Node group for **Grid** example (click to enlarge).
