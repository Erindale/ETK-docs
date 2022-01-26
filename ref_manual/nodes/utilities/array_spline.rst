.. index:: Utilities; Array Spline
.. _etk-utilities-array_spline:

*************
 Array Spline
*************

.. figure:: /images/nodes-array_spline.png
   :align: right

   The ETK_Array Spline node.

The **Array Spline** group instances objects along a curve spline.

See also
:ref:`etk-utilities-array_linear` and :ref:`etk-utilities-array_radial`.


Inputs
=======

|GEOMETRY| Geometry
   The input geometry.

|GEOMETRY| Spline
   The curve on which to array instances.

|INTEGER_FIELD_SINGLE| Resolution
   Sets the spline resolution.

|INTEGER| Count
   Count of objects to place on the curve.

|FLOAT| Spacing
   The spacing value determines the number of instances created along
   the spline. If the spacing is greater than the length of the spline
   no new instances will be created. This value is ignored unless *Use
   Spacing* is set.

|BOOLEAN| Use Spacing
   Use *Spacing*, ignore *Count*.

|BOOLEAN_FIELD_SINGLE| Align Rotation
   Align the instances with the curve.


Outputs
========

|GEOMETRY| Instances
   The generated instances.


Examples
========

.. figure:: /images/nodes-array_spline_basic.png
   :align: center
   :width: 800

   Using the *Count* method, use **Array Spline** to create 12 cubes
   on a spline.
