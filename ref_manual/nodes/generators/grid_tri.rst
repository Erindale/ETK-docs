.. index:: Generators; Grid Tri
.. _etk.generators.grid_tri:

*********
 Grid Tri
*********

.. figure:: /images/nodes-grid_tri.png
   :align: right

   The ETK_Grid Tri node.


The GRID TRI node can be used for 2-dimensional equilateral triangle
tessellations.


Inputs
=======

X Count
    Integer value for number of vertices in the X axis.

Y Count
    Integer value for number of vertices in the y axis.

Side Length
    The side length of the triangle.

Randomise Rotation?
    Check to randomize the rotation.

Seed
    The seed for the randomisation.

Centred?
    A toggle to choose if the grid is centred on the origin on aligned
    or the bottom left corner.

Properties
===========

This node has no properties.

Outputs
========

Triangles
   The generated geometry.

Centres
   Ouput a point at the centre of each triangle.

Size
   The total number of points generated.

X Fac
   A 0-1 gradient across the points in the X axis.

Y Fac
   A 0-1 gradient across the points in the Y axis.

Row Alt
   Description of Row Alt

Rotation
   Description of Rotation


Example Usage
==============

.. todo:: Add example for ETK_Grid Tri
