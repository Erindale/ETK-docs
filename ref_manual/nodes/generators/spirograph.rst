.. index:: Generators; Spirograph
.. _etk-generators-spirograph:

***********
 Spirograph
***********

.. figure:: /images/nodes-spirograph.png
   :align: right

   The ETK_Spirograph node.

The **Spirograph** is a geometry drawing device that produces
mathematical
`roulette <https://en.wikipedia.org/wiki/Roulette_(curve)>`_
curves of the variety technically known as
`hypotrochoids <https://en.wikipedia.org/wiki/Hypotrochoid>`_
and
`epitrochoids <https://en.wikipedia.org/wiki/Epitrochoid>`_.
[#]_

The **Spirograph** group node revolves one circle around the perimeter of
another creating some really beautiful patterns.

Inputs
=======

|INTEGER| Vertices
   Integer value for the total number of vertices.

|FLOAT_FIELD_SINGLE| Draw
   Plots the path.

|FLOAT_FIELD_SINGLE| Turns
   The total number of revolutions that the minor circle will make per
   revolution of the major circle.

|FLOAT_FIELD_SINGLE| Major Radius
   The size of the outer circle.

|FLOAT_FIELD_SINGLE| Minor Radius
   The size of the inner circle.


Outputs
========

|GEOMETRY| Geometry
   The generated geometry.

|INTEGER| Size
   The total number of points generated.

|FLOAT| Fac
   A 0..1 gradient along the points.

|FLOAT| Falloff
   A gradient from 0 starting at the centre and increasing outwards.
   Useful for controlling scale / rotation of points.

|VECTOR| Rotation
   A rotation vector for each point.


Example Usage
==============

.. image:: /images/nodes-spirograph_basic.png
           :align: center
           :width: 800

-----------

.. rubric:: Footnotes

.. [#] Wikipedia article on the `Spirograph
       <https://en.wikipedia.org/wiki/Spirograph>`_ .
