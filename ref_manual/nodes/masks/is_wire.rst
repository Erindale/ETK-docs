.. index:: Masks; Is Wire
.. _etk-masks-is_wire:

********
 Is Wire
********

.. figure:: /images/nodes-is_wire.png
   :align: right

   The ETK_Is Wire node.

A *wire* is an edge with no adjacent faces, which can sometimes occur
when manipulating geometry. The **Is Wire** node provides a mask
identifying wires in a geometry.

Inputs
=======

No inputs, uses attached fields as context.

Outputs
========

|BOOLEAN_FIELD| Mask

   A boolean field identifying all edges with no faces in a geometry.

|BOOLEAN_FIELD| Inverted

   For convenience, the inverted *Mask*.


Examples
=========

.. figure:: /images/nodes-is_wire_basic_comp.png
   :align: right

   Edge artifacts, before and after.

Floating point operations can sometimes cause unwanted artifacts to be
left on objects manipulated by geometery nodes. The **Is Wire** node
group is a useful node for taking care of this by removing edges with
no faces (wires). On the right is an example created with a
:ref:`etk-masks-mesh_side` node group on a UVSphere. The image on the left
is with the final geometry masked, and unmasked on the right.

See also :ref:`masks-edge_length-example`.

.. figure:: /images/nodes-is_wire_basic.png
   :align: center
   :width: 800

   Using **Is Wire** to remove edges without faces.
