.. index:: Curves; Curve Attributes
.. _etk-curves-curve_attributes:

*****************
 Curve Attributes
*****************

.. figure:: /images/nodes-curve_attributes.png
   :align: right

   The ETK_Curve Attributes node.

The **Curve** group is a convenience node that can be used in a
node pipeline to set various attributes on a curve and also access the
length of the curve.

Inputs
=======

|GEOMETRY| Curve
   The input curve.

|INTEGER_FIELD_SINGLE| Resolution
   Set the resolution on the output curve.

|FLOAT_FIELD_SINGLE| Radius
   Set the radius on the output curve.

|FLOAT_FIELD_SINGLE| Tilt
   Set the tilt on the output curve.

|BOOLEAN_FIELD_SINGLE| Cyclic
   Set the output curve to cyclic if checked.


Outputs
========

|GEOMETRY| Curve
   The output geometry.

|FLOAT| Length
   The length of the curve.


Examples
========

.. todo:: Add example for ETK_Curve Attributes
