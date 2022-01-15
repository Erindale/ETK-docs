.. index:: Curves; Points to Bezier
.. _etk.curves.points_to_bezier:

*****************
 Points to Bezier
*****************

.. figure:: /images/nodes-points_to_bezier.png
   :align: right

   The ETK_Points to Bezier node.

The **Points to bezier** group generates a curve based on a given set
of points.


Inputs
=======

|GEOMETRY| Points
   The points used to form the generated curve.

|INTEGER_FIELD_SINGLE| Resolution
   Number of points in the generated curve.

|BOOLEAN_FIELD_SINGLE| Cyclic
   Join ends together if checked.


Outputs
========

|GEOMETRY| Curve
   The generated curve.


Example Usage
==============

.. figure:: /images/nodes-points_to_bezier_basic.png
   :align: center
   :width: 800

   Using a 3 X 3 Grid as input, generate a curve with the **Points to
   Bezier** group. The generated curve is given some thickness with the
   :ref:`etk-curves-pipes` group and joined with small cubes that have been
   instanced on the grid.
