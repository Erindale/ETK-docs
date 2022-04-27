.. index:: Masks; Boundary Loop
.. _etk-masks-boundary_loop:

**************
 Boundary Loop
**************

.. figure:: /images/nodes-boundary_loop.png
   :align: right

   The ETK_Boundary Loop node.

The **ETK_Boundary Loop** group creates a mask of non-manifest edges
in a geometry.


Inputs
=======

No inputs. Uses field context to determine the geometry.

Outputs
========

|BOOLEAN_FIELD| Mask
   A boolean mask of unconnected edges.


|BOOLEAN_FIELD| Inverted
   For convenience, the logical inverse of *Mask*.


Examples
=========

.. rubric:: Extruding a hole in a sphere

In this example, the **Boundary Loop** group node is used to identify a
hole created by deleted geometry, then extruding the edges of the hole
in a negative direction.

.. figure:: /images/nodes-boundary_loop_basic_comp.png
   :align: center

   Extruding from 0.6 (left), -0.1 (center) and -0.9.

The lower portion of a UVSphere has its vertices deleted when the
vertex's normal falls below a certain angle, determined by the
dot-product of the vertex normal and a vertical *normal*. After
deleting the geometry the edges at the cut boundary are found by
the **Boundary Loop** group and those edges are extruded downward.

.. figure:: /images/nodes-boundary_loop_basic_gn.png
   :align: center
   :width: 800

   Using the **Boundary Loop** node to find open edges.
