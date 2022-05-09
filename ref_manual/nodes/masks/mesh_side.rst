.. index:: Masks; Mesh Side
.. _etk-masks-mesh_side:

**********
 Mesh Side
**********

.. figure:: /images/nodes-mesh_side.png
   :align: right

   The ETK_Mesh Side node.

The **Mesh Side** group creates a boolean mask of geometry elements
that face a given direction.


Inputs
=======

|GEOMETRY| Geometry

   Input geometry.

|VECTOR_FIELD_SINGLE| Vector

   A normal vector, faces (edges, points) are included in the mask if
   their normals match this input vector.

|FLOAT_FIELD_SINGLE| Deviation

   Allow some fuzziness in the selection, small values limit the mask
   to geometry elements that more closely match the input vector.


Outputs
========

|BOOLEAN_FIELD| Mask

   A boolean field mask of elements that match the input normal,
   :math:`\pm Deviation`.

|BOOLEAN_FIELD| Inverted

   For convenience, the inverse of *Mask*.

Examples
=========

.. rubric:: Slicing meshes

The **Mesh Side** node provides a versatile tool for slicing a mesh.
The top can be taken off a cube or, as shown in this example, a UV
Sphere. The normal vector input points in the positive Z direction and
the *Deviation* is used to determine how much of the sphere is cut.
The sphere is then separated by this selection and the top moved up by
a small amount.

.. figure:: /images/nodes-mesh_side_basic.png
   :align: center
   :width: 800

   Cutting a UV Sphere wit the **Mesh Side** node group.

.. NOTE:: Pay attention to context. This example uses *Face* context
          on the *Separate Geometry* node, *Point* or *Edge* context
          will give different results.

See also :ref:`etk-masks-is_wire` and :ref:`masks-edge_length-example`
for other examples.
