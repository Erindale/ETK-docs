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

.. rubric:: Tilting curves

.. figure:: /images/curve-attribute-basic-comp.gif
   :align: right

To create the animation on the right, a default quadratic bezier curve
instance is used to instance cubes along its path. The cubes are
adjusted by the height and translated so that the origin will lie
along the curve. The *Tilt* parameter is then animated in 15 |DEGREES|
increments from 0 to 90 |DEGREES|, then back to 0.

Note how the *Normal* output is used to set the *Rotation* to take
advantage of the tilt value.

.. figure:: /images/nodes-curve_attribute_basic.png
   :align: center
   :width: 800

   Using **Curve Attribute** to tweak instances along a curve. The
   animated input to the *Tilt* input has been omitted for brevity.
