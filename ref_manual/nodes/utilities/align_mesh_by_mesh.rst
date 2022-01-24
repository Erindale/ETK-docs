.. index:: Utilities; Align Mesh by Mesh
.. _etk-utilities-align_mesh_by_mesh:

*******************
 Align Mesh by Mesh
*******************

.. figure:: /images/nodes-align_mesh_by_mesh.png
   :align: right

   The ETK_Align Mesh by Mesh node.

The **Align Mesh by Mesh** group allows you to align a mesh with the
origin or a target mesh.


Inputs
=======

|GEOMETRY| Geometry
   The mesh to align.

|GEOMETRY| Target
   The target mesh to which the input geometry is aligned. If
   unconnected, the input geometry will align to the origin.

|BOOLEAN| Align X
   Align the input geometry along the X-axis of the target geometry.

|BOOLEAN| Align Y
   Align along the Y-Axis.

|BOOLEAN| Align Z
   Align along the Z-axis.

|FLOAT| ← G ➞
   A 0 .. 1 slider to select the alignment position of the geometry on
   the selected axis or axes.

|FLOAT| ← T ➞
   A 0 .. 1 slider to select the alignment position of the target to
   use in the alignment.

.. note:: The default slider settings are G = 0 and T = 1.0 with
          alignment along the Z-axis, meaning align the bottom of the
          geometry to the top of the target.


Outputs
========

|GEOMETRY| Geometry
   The output geometry.

Examples
========

.. figure:: /images/nodes-align_mesh_by_mesh_basic.png
   :align: center
   :width: 800

   In this example, the cylinder is the target mesh to which a cube is
   stacked on top as well as on the side.
