.. index:: Curves; Loft Curves
.. _etk-curves-loft_curves:

************
 Loft Curves
************

.. figure:: /images/nodes-loft_curves.png
   :align: right

   The ETK_Loft Curves node.

The **Loft Curves** group creates a mesh by lofting a set of curves.


Inputs
=======

|GEOMETRY| Curves
   The set of curves to loft.

|INTEGER| U Resolution
   Resolution in U.

|INTEGER| V Resolution
   Resolution in V.

|FLOAT_FIELD_SINGLE| U Min
   Generate the mesh starting at this point in U.

|FLOAT_FIELD_SINGLE| U Max
   Generate mesh on up to this point in U.

|FLOAT_FIELD_SINGLE| V Min
   Generate the mesh starting at this point in V.

|FLOAT_FIELD_SINGLE| V Max
   Generate mesh on up to this point in V.

|INTEGER| Cycle: None|U|V


|BOOLEAN| Cap
   Cap the ends of the input curves.

|BOOLEAN| Use Spacing

|FLOAT| Minimum Distance

|BOOLEAN| Linear / Cubic
   Select the type of lofting, Linear (unchecked) or Cubic


Outputs
========

|GEOMETRY| Mesh
   The output mesh of lofted curves (U and V.)

|GEOMETRY| U Curves
   Only the curves in U.

|GEOMETRY| V Curves
   Only the curves in V.

|INTEGER| Size
   The number of points in the output mesh.

|FLOAT_FIELD| U Fac
   A 0-1 gradient along U.

|FLOAT_FIELD| V Fac
   A 0-1 gradient along V.

|VECTOR_FIELD| Rotation
   A rotation vector for each point.


Example Usage
==============

A 3 Curve Loft
--------------

This first example uses three curves and are joined in this order,

   1. A foundational curve in the XY plane.
   2. Curve 1 rotated -90° around X and elevated in Z.
   3. Curve 1 rotated 180° around X and moved in Y.

It is important to join the curves in the proper order before
attaching to the **Loft Curves** group node.

.. figure:: /images/nodes-loft_curves_basic.png
   :align: center
   :width: 800

   Using the **Loft Curves** node to create a mesh by lofting a set of
   curves. The 3 input curves have been accentuated using
   :ref:`etk-curves-pipes`. Note the use of *U Min* and *U Max* to
   limit the mesh in one axis.
