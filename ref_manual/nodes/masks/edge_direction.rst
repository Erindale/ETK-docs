.. index:: Masks; Edge Direction
.. _etk-masks-edge_direction:

***************
 Edge Direction
***************

.. figure:: /images/nodes-edge_direction.png
   :align: right

   The ETK_Edge Direction node.

The **Edge Direction** group provides a mask containing edge indices
that match a given direction vector.


Inputs
=======

|VECTOR_FIELD_SINGLE| Vector

   The input vector on which to base the mask.

|FLOAT_FIELD_SINGLE| Deviation

   Matching edges are allowed to vary by this amount.


Outputs
========

|BOOLEAN_FIELD| Mask

   The mask of edge indices that match the direction of the input vector.

|BOOLEAN_FIELD| Inverted

   For convenience, all non-matches.

|FLOAT_FIELD| Fac

   A :math:`[0\ldots 1]` value giving the quality of the match
   regardless of deviation.


Examples
=========

.. rubric:: Bare-bones example

Starting with a simple box, edges that match an input direction are
extruded. This is probably the most basic of examples but gives an
idea of what the **Edge Direction** group can do.

.. figure:: /images/nodes-edge_direction_basic_comp.png
   :align: center

   Edges extruded along X (left), Y, and Z.

.. figure:: /images/nodes-edge_direction_basic.png
   :align: center
   :width: 800

   Using **Edge Direction** to build a mask of all edges matching an
   input direction vector.
