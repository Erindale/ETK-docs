.. index:: Curves; Curve Lerp
.. _etk-curves-curve_lerp:

***********
 Curve Lerp
***********

.. figure:: /images/nodes-curve_lerp.png
   :align: right

   The ETK_Curve Lerp node.

The **Curve Lerp** group uses the process of linear interpolation to
construct a new curve from two input curves.


Inputs
=======

|GEOMETRY| Curve1
   The first input curve.

|GEOMETRY| Curve2
   The second input curve.

|INTEGER_FIELD_SINGLE| Resolution
   The resolution to use for the generated curve.

|FLOAT_FIELD_SINGLE| Fac
   Can be used to favor the first input curve (0) or the second (1).

|BOOLEAN| Poly / Bezier


Outputs
========

|GEOMETRY| Curve
   The interpolated curve.

Example Usage
==============

.. figure:: /images/nodes-curve_lerp_basic.png
   :align: center
   :width: 800

   Using **Curve Lerp**, interpolate between two circles, one rotated
   90° on one axis. The input curves use thinner
   :ref:`etk-curves-pipes` to differentiate them from the interpolated
   geometry.
