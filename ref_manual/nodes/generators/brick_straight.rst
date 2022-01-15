.. index:: Generators; Brick Straight
.. _etk-generators-brick_straight:

***************
 Brick Straight
***************

.. figure:: /images/nodes-brick_straight.png
   :align: right

   The ETK_Brick Straight node.

The **Brick Straight** group is for creating brick walls with a standard
half-brick offset between rows. We don’t have any analytical tools at
the moment so you do have to write in your own brick size (for now).

See also :ref:`etk-generators-brick_arc`, :ref:`etk-generators-brick_spline`.

Inputs
=======

|COLLECTION| Bricks
   The collection containing brick objects.

|FLOAT| Brick Width
    The width of the bricks.

|FLOAT| Brick Height
    The height of the bricks.

|FLOAT| Wall Length
    The target wall length.

|FLOAT| Wall Height
    The target wall height.

|BOOLEAN| Use X Count
    Toggle to use *X Count* instead of *Wall Length*

|INTEGER| X Count
    Integer input for number of bricks in X.

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

|INTEGER| Size
    The total number of bricks generated.

|FLOAT_FIELD| X Fac
    A 0-1 gradient across the points in the X axis.

|FLOAT_FIELD| Y Fac
    A 0-1 gradient across the points in the Y axis.


Example Usage
==============

.. figure:: /images/nodes-brick_straight_basic.png
   :align: center
   :width: 800

   Using the **Brick Straight** node, with a little scaling to
   accentuate the bricks, to generate a wall.
