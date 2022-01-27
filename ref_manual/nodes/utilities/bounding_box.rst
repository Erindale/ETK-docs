.. index:: Utilities; Bounding Box
.. _etk-utilities-bounding_box:

*************
 Bounding Box
*************

.. figure:: /images/nodes-bounding_box.png
   :align: right

   The ETK_Bounding Box node.

The **Bounding Box** group provides a box defined by the bounds of the
input geometry. The *Centre* and extents of all axes are provided as
outputs.


Inputs
=======

|GEOMETRY| Geometry
   The geometry on which to determine the bounding box.

Outputs
========

|GEOMETRY| Bounding Box
   A cube geometry that encompasses the extent of the input object.

|VECTOR| Centre
   A position vector of the centre of the geometry.

|FLOAT| Min X
   The minimum extent on the X-axis.

|FLOAT| Max X
   The maximum extent on the X-axis.

|FLOAT| Min Y
   The minimum extent on the Y-axis.

|FLOAT| Max Y
   The maximum extent on the Y-axis.

|FLOAT| Max Z
   The maximum extent on the Z-axis.

|FLOAT| Min Z
   The minimum extent on the Z-axis.

|FLOAT| Size X
   Length of bounding box along the X-axis.

|FLOAT| Size Y
   Length of bounding box along the Y-axis.

|FLOAT| Size Z
   Length of bounding box along the Z-axis.


Examples
========

.. figure:: /images/nodes-bounding_box_basic.png
   :align: center
   :width: 800

   Using the **Bounding Box** in its simplest form to display the
   bounds of a icosphere.
