.. index:: Masks; Selection Box
.. _etk-masks-selection_box:

**************
 Selection Box
**************

.. figure:: /images/nodes-selection_box.png
   :align: right

   The ETK_Selection Box node.

The **Selection Box** group provides a mechanism for selecting points
based on a box. Preview geometry is available to aid in sizing and
positioning.


Inputs
=======

|VECTOR_FIELD_SINGLE| Centre
   Move the box by adjusting the position of the box origin.

|VECTOR_FIELD_SINGLE| Size
   Sets the dimensions of the selection box.

|VECTOR_FIELD_SINGLE| Rotation
   Rotate the selection about the *Centre*.

|FLOAT_FIELD_SINGLE| Round Corner
   Round the corners of the mask. It is best to use the *Preview* as
   you manipulate the corners.


Outputs
========

|BOOLEAN_FIELD| Inside
   A mask that selects points inside the box.

|BOOLEAN_FIELD| Outside
   A mask that selects points outside the box.

.. index:: Signed Distance Function; Selection Box

|FLOAT_FIELD| SDF
   A signed distance function that yields larger values further from
   the box boundary.

|GEOMETRY| Preview
   A preview of the selection box. This is real geometry that can be
   joined to the **Group Output** to visualise the mask.


Examples
========

.. rubric:: Box selecting a point cloud

The goal is to create a box selection of a point cloud by first
created a mass of points and using a **Selection Box** to only
instance points within the box.

.. figure:: /images/nodes-selection_box_basic_comp.png
   :align: center

   Point cloud, selection box, and final result.

The **Selection Box** is tilted slightly for effect and visualised by
joining its geometry to make it easier to manipulate in the viewport.
This is real geometry so should be disconnected in the final.

.. figure:: /images/nodes-selection_box_basic.png
   :align: center
   :width: 800

   The **Selection Box** group used to select a box points inside a
   box defined by a :ref:`etk-generators-grid`.

.. figure:: /images/nodes-selection_box_basic_sdf.png
   :align: right

With the SDF connected to the scale of the **Instance on Points**
node, interesting results can be obtained.
