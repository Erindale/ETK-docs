.. index:: Fields; Field Length
.. _etk-fields-field_length:

*************
 Field Length
*************

.. figure:: /images/nodes-field_length.png
   :align: right

   The ETK_Field Length node.

The **Field Length** group obtains the length of the list of vertices
from a geometry.


Inputs
=======

|GEOMETRY| Geometry
   The geometry on which to find its vertex list length.

Outputs
========

|INTEGER| Length
   The number of vertices in the geometry.


Examples
========

.. figure:: /images/nodes-field_length_basic.png
   :align: center
   :width: 800

   A long-winded example that find the length of a grid, retrieved from
   a **Field Length** group, and displays it below the geometry as a
   string.
