.. index:: Masks; Distance from Point
.. _etk-masks-distance_from_point:

********************
 Distance from Point
********************

.. figure:: /images/nodes-distance_from_point.png
   :align: right

   The ETK_Distance from Point node.

The **Distance from Point** group creates a mask of points within
a given distance from the point.


Inputs
=======

|INTEGER_FIELD_SINGLE| Index
   The *Index* of the target point.


|FLOAT_FIELD_SINGLE| Distance
   All points within this distance will be members of the output *Mask*.


Outputs
========

|BOOLEAN_FIELD| Mask
   Any point in the geometry that is within the distance from the
   target point will be *True* in this field outpout.


|BOOLEAN_FIELD| Inverted
   The inverse of *Mask*.


Examples
=========

.. rubric:: A movable hole

.. figure:: /images/nodes-distance_from_point_comp.png
   :align: center

   *Index = 24* (left), *Index = 60* (middle), and increasing the
   *Distance* from 0.1m to 0.6m on the right.

A hole is created within a grid using the **Distance from Point**
group at a point index in the center of the grid. The remaining
geometry is extruded at its boundaries, then joined with a hole'd
geometry to form a box. Move the hole by changing the index, enlarge
the hole by increasing the distance.

.. figure:: /images/nodes-distance_from_point_basic.png
   :align: center
   :width: 800

   Using **Distance from Point** to create a configurable hole in the
   center of a solid.

Note how the :ref:`etk-masks-boundary_loop` group is used on the grid
to extrude only the outer edges.
