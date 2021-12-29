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

X Count
    Integer value for number of vertices in the X axis.

Y Count
    Integer value for number of vertices in the Y axis.

Z Count
    Integer value for number of vertices in the Z axis.

Size
    The overall size of the grid in metres.

Use Spacing?
    Toggle to change the **Size** from overall size to the spacing between
    points.

Randomise
    Maximum distance to randomise position by.

Seed
     The seed for the randomisation.

Centred?
    A toggle to choose if the grid is centred on the origin or aligned
    on the bottom left corner.


Properties
===========

This node has no properties.

Outputs
========

Geometry
    The generated geometry.

Size
    The total number of points generated.

Index
    An attribute containing the index for each point (eg. 0, 1, 2,
    3...).

.. figure:: /images/nodes-grid_example_render.png
   :width: 400
   :align: right

X Fac
    A 0-1 gradient across the points in the X axis.

Y Fac
    A 0-1 gradient across the points in the Y axis.

Z Fac
    A 0-1 gradient across the points in the Z axis.


Example Usage
==============

This example builds a 3D grid out of which the inside points in X and
Z are removed to form a hollow box of icospheres.

.. figure:: /images/nodes-grid_example.png
   :width: 800
   :align: center

   Node group for **Grid** example (click to enlarge).
