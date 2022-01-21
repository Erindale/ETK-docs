.. index:: Generators; Ellipse
.. _etk-generators-ellipse:

********
 Ellipse
********

.. figure:: /images/nodes-ellipse.png
   :align: right

   The ETK_Ellipse node.

From the `wiki article <https://en.wikipedia.org/wiki/Ellipse>`_ on
the ellipse,

   *An ellipse is a plane curve surrounding two focal points, such that
   all points on the curve, the sum of the two distances to the focal
   points is a constant.*

The **Ellipse** group node generates points on the elliptical arc
defined by its inputs. Of the two *radius* inputs, the longer radius is
typically called the major axis and the shorter one, the minor axis.
If they are equal this node will form a circle.


Inputs
=======

|INTEGER| Vertices
    The resolution or number of points to generate.

|FLOAT| Radius X
    This determines the width along the X axis.

|FLOAT| Radius Y
    This determines the height along the Y axis.

|FLOAT| U Min
    The starting angle of the elliptical arc.

|FLOAT| U Max
    The ending angle of the elliptical arc.

|BOOLEAN| Use Spacing
    A toggle to use the *Spacing* value instead of *Vertices*.

|FLOAT| Spacing
    If *Use Spacing* is selected, the distance between points of the
    ellipse.

|BOOLEAN| Centre Vertex
    If selected, place a point at the center of the ellipse.


Outputs
========

|GEOMETRY| The generated points.

|INTEGER| Size
    The number of points generated.

|FLOAT_FIELD| Fac
    A 0..1 gradiant along the generated points.

|VECTOR_FIELD| Rotation
    A rotation vector of the point to the centre of the ellipse.


Examples
========

.. figure:: /images/nodes-ellipse_basic.png
   :align: center
   :width: 800

   Using the **Ellipse** node to create an ellipse of cubes which
   have been adjusted by the rotation vector to face the centre axis.
