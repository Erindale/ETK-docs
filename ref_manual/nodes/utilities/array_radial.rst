.. index:: Utilities; Array Radial
.. _etk-utilities-array_radial:

*************
 Array Radial
*************

.. figure:: /images/nodes-array_radial.png
   :align: right

   The ETK_Array Radial node.

The **Array Radial** group builds instances of the input geometry
around a given radius. The user may specify the number of elements
created using either a count or spacing value.

See also
:ref:`etk-utilities-array_linear` and :ref:`etk-utilities-array_spline`.


Inputs
=======

|GEOMETRY| Geometry
   The input geometry.

|INTEGER| Count
   The number of instances to arrange radially. This value is ignored
   if *Use Spacing* is selected.

|INTEGER| Radius
   Build the circle using this value.

|VECTOR_FIELD_SINGLE| Centre
   The position about which to rotate.

|FLOAT| Spacing

|BOOLEAN| Use Spacing
   Use *Spacing* value to set the number of instances created at the
   given *Radius*. When selected, *Count* is ignored.

|FLOAT_FIELD_SINGLE| Align Rotation
   Align instances to *Centre*.


Outputs
========

|GEOMETRY| Intances
   The new array of geometry arrayed in a circle.


Examples
========

.. figure:: /images/nodes-array_radial_basic.png
   :align: center
   :width: 800

   Two **Array Radial** groups are used to create concentric circles
   of objects. The outer array of cubes uses a *Count* of 7, the array
   of icospheres uses *Spacing* to achieve the a similar number of
   elements in the array.
