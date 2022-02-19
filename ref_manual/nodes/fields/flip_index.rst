.. index:: Fields; Flip Index
.. _etk-fields-flip_index:

***********
 Flip Index
***********

.. figure:: /images/nodes-flip_index.png
   :align: right

   The ETK_Flip Index node.

The *Flip Index* group provides a mechanism to alter the order of indices
in a 2D area.


Inputs
=======

|INTEGER_FIELD_SINGLE| U Size
   Size in the U dimension.

|INTEGER_FIELD_SINGLE| V Size
   Size in the V dimension.


Outputs
========

|FLOAT_FIELD| Value
   The resulting index value.


Examples
========

.. rubric:: Flipping grid indices

This example partially tracks the
`Flip Index video tutorial <https://www.youtube.com/watch?v=9MmLXVx5yf8>`_
that was created specifically for this node group. In this example a
simple Grid mesh primitive is used.

If a mesh line is provided with a resolution matching the number of
vertices in this grid, and the position of the vertices in the grid
are transfered to the grid in index order, the index sequence
of the vertices will be apparent.

.. figure:: /images/nodes-flip_index_basic_comp.png
   :align: center

   The :math:`4 \times 8` grid, with a mesh line showing before and
   after flipping.

In the node network for this, U and V are separated into input values
that can be used to determine the count of our target mesh line, the
size of the **Grid**, and the inputs to the **Flip Index**
group. A **Transfer Attribute** node is used to transfer the flipped
positions to the mesh line.

.. figure:: /images/nodes-flip_index_basic.png
   :align: center
   :width: 800

   The **Flip Index** group is used to flip indices on a grid.
