.. index:: Masks; Edge Length
.. _etk-masks-edge_length:

************
 Edge Length
************

.. figure:: /images/nodes-edge_length.png
   :align: right

   The ETK_Edge Length node.

The **Edge Length** group returns a mask containing edge indices whose
length is within a given threshold.


Inputs
=======

|FLOAT_FIELD_SINGLE| Threshold

   An input length, any edge with a length less than this is
   represented in the mask.


Outputs
========

|BOOLEAN_FIELD| Mask

   Output mask containing all edge indices less than *Threshold*.


|BOOLEAN_FIELD| Inverted

   For convenience, the inverse of *Mask*.


|FLOAT_FIELD| Length

   The length value of all edge fields.


Examples
=========

.. rubric:: Building a shape with masks

Masks have many intertaining uses. This example builds on a small
number of mask group nodes to build a simple object. The rings of a
UVSphere form edges that decrease in length as they approach the poles
in either Z direction.

.. figure:: /images/nodes-edge_length_basic_a.png
   :align: center

   Step 1: Remove all edges less than 0.12m from a sphere.

Removing the vertex at the top and bottom will leave us with a
truncated sphere. There are several ways to do this but using the
built-in **Edge Neighbors** node to determine absent faces seems like
the easiest.

.. figure:: /images/nodes-edge_length_basic_b.png
   :align: center

   Step 2: Removing the poles using a mask of all edges with no face
   neighbors.

We want to extrude the edges at the top and bottom and we can do that
with a **Boundary Loop** node. It is not quite the shape we want but
it is a start.

.. figure:: /images/nodes-edge_length_basic_c.png
   :align: center

   Step 3: Extruding the raw edges of the sphere.

Finally, the final shape is completed by controlling the direction of
the exclusion. The *Offset* of the extrusion is set by a vector with a
value of :math:`[0.0, 0.0, 1.0]`. The *Scale* of that offset is
determined by whether the edge is above or below the origin then
multiplied by the desired value.

.. figure:: /images/nodes-edge_length_basic_d.png
   :align: center
   :width: 800

   Step 4: Controlling the extrusion with standard geometry nodes.
