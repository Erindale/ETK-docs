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

Referring to the example in :ref:`masks-edge_length-example`, it is
possible to also clean up dangling edges in that example with the
**Is Wire** node group.

.. figure:: /images/nodes-is_wire_basic.png
   :align: center
   :width: 800

   Using **Is Wire** to remove edges without faces.
