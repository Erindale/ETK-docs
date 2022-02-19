.. index:: Masks; Selection Plane
.. _etk-masks-selection_plane:

****************
 Selection Plane
****************

.. figure:: /images/nodes-selection_plane.png
   :align: right

   The ETK_Selection Plane node.

The **Selection Plane** group provides a mask for vertices above or
below a plane.


Inputs
=======

|VECTOR_FIELD_SINGLE| Centre
   Position vector of the centre of the plane.

|VECTOR_FIELD_SINGLE| Up
   Direction of what is considered *up* in the selection plane. The
   default is the Z-axis.

Outputs
========

|BOOLEAN_FIELD| Inside
   Yields *true* if the geometry, relative to the field *Up*,
   is above the plane.

|BOOLEAN_FIELD| Outside
   Yields *true* if the geometry is below the plane.

.. index:: Signed Distance Function; Selection Plane

|FLOAT_FIELD| SDF
   A signed distance function yielding larger values further from the
   plane.

|GEOMETRY| Preview
   Real geometry of the selection plane that can be viewed to help in
   placement.

Examples
========

.. figure:: /images/nodes-selection_plane_basic.png
   :align: center
   :width: 800

   Using a **Selection Plane** to drive a switch that sets the *drop
   distance* on a :ref:`etk-curves-to_wires` group node on a cube.
