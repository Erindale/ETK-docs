.. index:: Masks; Expand Selection
.. _etk-masks-expand_selection:

*****************
 Expand Selection
*****************

.. figure:: /images/nodes-expand_selection.png
   :align: right

   The ETK_Expand Selection node.

The **Expand Selection** group takes as input a selection on a given
geometry and expands the scope of the selection by a given amount.


Inputs
=======

|GEOMETRY| Geometry

   Input geometry.


|BOOLEAN_FIELD_SINGLE| Selection

   Input selection mask.

|INTEGER_FIELD_SINGLE| Grow

   Amount to grow the selection.

Outputs
========

|GEOMETRY| Geometry

   Output geometry.

|BOOLEAN_FIELD| Selection

   The output selection, larger than the input selection based on the
   *Grow* input value.

Examples
=========

.. rubric:: Extruding an expanded boundary loop

.. figure:: /images/nodes-expand_selection_basic.png
   :align: right

   A grid with its boundary grown and extruded.

The :ref:`etk-masks-boundary_loop` selects the outer boundary of the
grid and the **Expand Selection** group is used to grow that by 2. In
our example, increasing the *Grow* value will enlarge the selection
towards the center.

.. figure:: /images/nodes-expand_selection_basic_gn.png
   :align: center
   :width: 800

   Using the **Expand Selection** group to grow a selection.

.. rubric:: A side note on masks

.. figure:: /images/nodes-expand_selection_and.png
   :align: right

   AND'ing the inverted boundary loop to modify the extrusion.

Masks provide opportunities for creating interesting shapes. Here is
an example of using a single AND boolean operation on the inverted
**Boundary Mask** with the above example.

.. figure:: /images/nodes-expand_selection_and_gn.png
   :align: center
   :width: 800

   Using a single boolean operation to modify our example image.
