.. index:: Fields; Flip Index
.. _etk-fields-flip_index:

***********
 Flip Index
***********

.. figure:: /images/nodes-flip_index.png
   :align: right

   The ETK_Flip Index node.

The *Flip Index* group is used to modify the dimensions of a 2D area.


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

This example tracks the
`Flip Index video tutorial <https://www.youtube.com/watch?v=9MmLXVx5yf8>`_
that was created specifically for this node group.

The first step is to create a simple grid that can be used to make our
explanation easier. This custom node group we'll call **UV
Grid** that will take a horizontal (U) dimension and vertical (V)
dimension and lay the indices out along X and Y. Each cell in our UV grid
will be :math:`1 \times 1` blender units.

.. figure:: /images/nodes-flip_grid.png
   :align: center
   :width: 800

   The **UV Grid** node group.

If a mesh line is provided with a resolution matching the number of
vertices in this UV grid, and the position of the vertices in the grid
are set, in order of the indices, to the line, the index sequence of the
vertices will be apparent.

.. figure:: /images/nodes-uv_flip_comp.png
   :align: center

   Before and after flipping.

In the node network for this, U and V are separated into input values
that can be used to determine the count of our target mesh line, the
size of the **UV Grid**, and provide the inputs to the **Flip Index**
group. A **Transfer Attribute** node is used to set the flipped
positions to the mesh line.

.. figure:: /images/nodes-flip_index_basic.png
   :align: center
   :width: 800

   The **Flip Index** group is used to flip a grid's UV dimension.
