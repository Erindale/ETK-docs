.. index:: Generators; Grid Hex
.. _etk.generators.grid_hex:

*********
 Grid Hex
*********

.. figure:: /images/nodes-grid_hex.png
   :align: right

   The ETK_Grid Hex node.


Inputs
=======

|INTEGER_SINGLE| X Count
    Integer value for number of vertices in the X axis.

|INTEGER_SINGLE| Y Count
    Integer value for number of vertices in the Y axis.

|FLOAT_SINGLE| Side Length
    Length of each of the six sides.

|BOOLEAN_FIELD_SINGLE| Randomise Rotation
    Check to randomise the rotation of the hex tiles.

|INTEGER_FIELD_SINGLE| Seed
    The seed for the randomisation.

|BOOLEAN_FIELD_SINGLE| Centred
    If checked will center the grid.

Outputs
========
|GEOMETRY| Hexagons
   The generated geometry.

|GEOMETRY| Centres
   Ouput a point at the centre of each hexagon.

|INTEGER_SINGLE| Size
   The total number of points generated.

|FLOAT_FIELD| X Fac
   A 0-1 gradient across the points in the X axis.

|FLOAT_FIELD| Y Fac
   A 0-1 gradient across the points in the Y axis.

|VECTOR_FIELD| Rotation
   The rotation vector of each hexagonal tile.


Example Usage
==============

.. figure:: /images/nodes-grid_hex_basic.png
   :align: center
   :width: 800

   Using **Grid Hex** in its basic form to generate a 5 X 7 grid. The
   hexagons have been scaled slightly to accentuate their shape.
