.. index:: Masks; Points Inside Mesh
.. _etk-masks-points_inside_mesh:

*******************
 Points Inside Mesh
*******************

.. figure:: /images/nodes-points_inside_mesh.png
   :align: right

   The ETK_Points Inside Mesh node.

The **Points Inside Mesh** group provides a mask, based on a mesh,
that can be used for selections of points that lie within the given
mesh.


Inputs
=======

|GEOMETRY| Mesh
   The input mesh on which to base the mask.

|INTEGER| Accuracy
   Subdivides the input *Mesh* by this amount to increase the shapes
   accuracy.

|BOOLEAN_FIELD_SINGLE| Backface Check
   Performs additional checks on back-facing areas of the mesh.


Outputs
========

|BOOLEAN_FIELD_SINGLE| Fast
   Uses raycasting to determine mask.

|BOOLEAN_FIELD_SINGLE| Full
   A more compute-intensive check in all directions. This is most
   useful if the input mesh and target have complicated geometry with
   lots of nooks and crannies.


Examples
========

.. rubric:: Masking a point cloud

This example starts with a point cloud and selects only the points
within a mesh.

.. figure:: /images/nodes-points_inside_mesh_basic_comp.png
   :align: center

   The point cloud, mask, and result.

The mask object, a simple cross of cylinders shown in wireframe,
separately and brought into our node tree with an **Object Info**
node. The cross is imported and attached to the **Points Inside Mesh**
group. A :ref:`etk-generators-grid` node is used to create the point
cloud and is randomised slightly to add interest.

.. figure:: /images/nodes-points_inside_mesh_basic.png
   :align: center
   :width: 800

   The **Points Inside Mesh** at work, masking out points not found
   within the object.
