.. index:: Generators; Brick Arc
.. _etk.generators.brick_arc:

**********
 Brick Arc
**********

.. figure:: /images/nodes-brick_arc.png
   :align: right

   The ETK_Brick Arc node.


The BRICK ARC group is for creating curved corner walls with a
standard half-brick offset between rows. We don’t have any analytical
tools at the moment so you do have to write in your own brick size
(for now).

See also :ref:`etk.generators.brick_straight`,
:ref:`etk.generators.brick_spline`.


Inputs
=======

|COLLECTION| Bricks
   The collection containing brick objects.

|FLOAT_SINGLE| Brick Width
    The width of the bricks.

|FLOAT_SINGLE| Brick Height
    The height of the bricks.

|FLOAT_SINGLE| Radius
    The arc radius.

|FLOAT_SINGLE| Angle

|FLOAT_SINGLE| Wall Height
    The target wall height.

|FLOAT_SINGLE| Rotation
    Rotation of the wall in degrees.

|BOOLEAN_SINGLE| Use X Count
    Toggle to use *X Count* instead of *Radius*

|INTEGER_SINGLE| X Count
    Integer input for number of bricks in X.

|BOOLEAN_SINGLE| Use Z Count
    A toggle to use *Z Count* instead of *Wall Height*.

|INTEGER_SINGLE| Z Count
    Integer input for number of bricks in Z.

|BOOLEAN_FIELD_SINGLE| Offset Switch
    A toggle to change the direction of the offset rows.


Outputs
========

|GEOMETRY| Geometry
    The generated geometry using bricks.

|GEOMETRY| Points
    The positions of bricks

|INTEGER_SINGLE| Size
    The total number of bricks generated.

|FLOAT_SINGLE| Radius
    The arc radius in meters.

|FLOAT_FIELD| X Fac
    A 0-1 gradient across the points in the X axis.

|FLOAT_FIELD| Y Fac
    A 0-1 gradient across the points in the Y axis.

|VECTOR_FIELD| Rotation
    A rotation vector for each brick in the wall.


Example Usage
==============

.. figure:: /images/nodes-brick_arc_basic.png
   :align: center
   :width: 800

   An brick arc wall built with default settings.
