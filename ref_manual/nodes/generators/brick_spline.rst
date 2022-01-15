.. index:: Generators; Brick Spline
.. _etk-generators-brick_spline:

*************
 Brick Spline
*************

.. figure:: /images/nodes-brick_spline.png
   :align: right

   The ETK_Brick Spline node.

The **Brick Spline** group builds a brick wall along a
Curve object.

See also :ref:`etk-generators-brick_straight`,
:ref:`etk-generators-brick_arc`.


Inputs
=======

|OBJECT| Spline
   The bezier curve object on which to form the brick wall.

|INTEGER_FIELD_SINGLE| Spline Resolution
    This sets the number of points along the spline.

|COLLECTION| Bricks
    Source bricks from the given collection.

|FLOAT| Brick Width
    The width of the bricks.

|FLOAT| Brick Height
    The height of the bricks.

|FLOAT| Wall Height
    The target wall height.

|BOOLEAN| Use Z Count
    A toggle to use *Z Count* instead of *Wall Height*.

|INTEGER| Z Count
    Integer input for number of bricks in Z.

|BOOLEAN_FIELD_SINGLE| Offset Switch
    A toggle to change the direction of the offset rows.


Outputs
========

|GEOMETRY| Geometry
    The generated geometry using bricks.

|GEOMETRY| Points
    The positions of the bricks.

|FLOAT_FIELD| Curve Fac
    A 0-1 gradient across the points along the curve.

|FLOAT_FIELD| Z Fac
    A 0-1 gradient across the points in the Z axis.

|VECTOR_FIELD| Rotation
    The rotation vector of each brick.


Example Usage
==============

.. figure:: /images/nodes-brick_spline_basic.png
   :align: center
   :width: 800

   Using a Bezier Curve object twisted into an S-curve in the XY axis,
   use **Brick Spline** to build a wall along the spline.
