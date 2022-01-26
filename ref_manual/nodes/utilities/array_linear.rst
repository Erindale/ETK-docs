.. index:: Utilities; Array Linear
.. _etk-utilities-array_linear:

*************
 Array Linear
*************

.. figure:: /images/nodes-array_linear.png
   :align: right

   The ETK_Array Linear node.

The **Array Linear** group duplicates the input geometry along a line
defined by the user. This line is specified by a starting point and
either a count of objects with an offset or by setting a spacing
amount to an end point. See also
:ref:`etk-utilities-array_radial` and :ref:`etk-utilities-array_spline`.

Inputs
=======

|GEOMETRY| Geometry
   The input geometry to duplicate.

|INTEGER| Count
   When set to *Offset* this specifies the number of instances to
   place at that offset. This value is ignored if *Use End* is selected.

|VECTOR| Start
   The starting position.

|VECTOR| Offset / End
   This vector value is interpreted as the *End* target if *Use End*
   is selected, otherwise it is the offset.

|BOOLEAN| Use End
   Interpret *Offset / End* as an end position of the array.

|FLOAT| Spacing
   Space object this amount. This is ignored unless *Use Spacing* is
   selected.

|FLOAT| Use Spacing
   Use the spacing value to determine how many objects to place
   between *Start* and *Offset / End*. For spacing to work, *Use End*
   must be selected.

|FLOAT_FIELD_SINGLE| Align Rotation
   Align instances along the direction of the array.


Outputs
========

|GEOMETRY| Instances
   The generated instances.


Examples
========

.. figure:: /images/nodes-array_linear_basic.png
   :align: center
   :width: 800

   Use two **Array Linear** groups to create a geometric pattern of
   cubes. Both arrays use *Spacing* to achieve this effect.
