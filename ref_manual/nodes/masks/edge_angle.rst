.. index:: Masks; Edge Angle
.. _etk-masks-edge_angle:

***********
 Edge Angle
***********

.. figure:: /images/nodes-edge_angle.png
   :align: right

   The ETK_Edge Angle node.

The **Edge Angle** group is a wrapper around the built-in *Edge Angle*
node and returns a boolean mask field that yields True when the edge
angle is greater than a given threshold.


Inputs
=======

|FLOAT_FIELD_SINGLE| Threshold
   The angle in degrees to use as a determinant.

|BOOLEAN_FIELD_SINGLE| Signed
   Factor in edges with concave (positive) and convex (negative)
   angles.


Outputs
========

|BOOLEAN_FIELD| Mask
   True if the edge angle is greater than the given threshold.

|BOOLEAN_FIELD| Inverted
   The inverse of *Mask*.


Examples
=========

.. figure:: /images/nodes-edge_angle_basic_1.png
   :align: right

.. rubric:: Material assignment based on edge angle

This example presents small cubes instanced on the points of a UV
Sphere where the color of the cubes is determined by the edge angle.
In this example, Blue cubes are instantiated when the edge angle is
greater than the *Threshold* of 10.8°.

.. figure:: /images/nodes-edge_angle_basic_2.png
   :align: center
   :width: 800

   Using **Edge Angle** node group to control the color of instances
   via the edge angle on a UV Sphere.
