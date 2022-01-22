.. index:: Utilities; Twist
.. _etk-utilities-twist:

******
 Twist
******

.. figure:: /images/nodes-twist.png
   :align: right

   The ETK_Twist node.

The **Twist** group twists some or all of the geometry around an axis.


Inputs
=======

|GEOMETRY| Geometry
   The input geometry to modify with a twist.

|FLOAT_FIELD_SINGLE| Angle Min
   Starting angle.

|FLOAT_FIELD_SINGLE| Angle Max
   Ending angle.

|VECTOR| Twist Axis
   The axis along which to perform the twist.

|FLOAT_FIELD_SINGLE| Limit Min
   Start twisting at this fraction along the *Twist Axis*.

|FLOAT_FIELD_SINGLE| Limit Max
   Stop twisting at this fraction.

|VECTOR| Centre
   Move the center of the twist.

|BOOLEAN_FIELD_SINGLE| Linear / Smoother Step
   * Unchecked, use a linear rotation for twisting.
   * Checked, use smoother step algorithm to twist.

Outputs
========

|GEOMETRY| Geometry
   The output geometry.

Examples
========

.. figure:: /images/nodes-twist_basic.png
   :align: center
   :width: 800

   Use the **Twist** group to twist the middle part of a piece of
   geometry 90° around the Z-axis. Note how the *Limit* inputs are
   used to only twist the middle section.
