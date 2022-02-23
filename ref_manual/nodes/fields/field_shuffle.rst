.. index:: Fields; Field Shuffle
.. _etk-fields-field_shuffle:

**************
 Field Shuffle
**************

.. figure:: /images/nodes-field_shuffle.png
   :align: right

   The ETK_Field Shuffle node.

The **Field Shuffle** group randomly shuffles a field within a geometry.


Inputs
=======

|GEOMETRY| Geometry
   The input geometry.

|VECTOR_FIELD_SINGLE| Field
   The field to randomly shuffle.

|INTEGER_FIELD_SINGLE| Seed
   The randomisation seed.

Outputs
========

|VECTOR_FIELD_SINGLE| Field
   The output, the shuffled *Field* value.

.. caution:: Expect data loss.


Examples
========

.. rubric:: Shuffling positions in a grid

This example uses the **Field Shuffle** group to shuffle positions in
a grid. A simple :math:`4\times 4` grid is constructed and displayed
and, after shuffling the positions, a single cube is instanced at
frame :math:`N, where N \in \{0, 1, \ldots, 15\}`. The two animations
share the same node network, one masking the **Field Shuffle** node.

.. figure:: /images/nodes-field-shuffle-basic-masked.gif
   :align: left

   With **Field Shuffle** masked.

.. figure:: /images/nodes-field-shuffle-basic-comp.gif
   :align: right

   With **Field Shuffle** unmasked.

.. figure:: /images/nodes-field_shuffle_basic.png
   :align: center
   :width: 800

   Using **Field Shuffle** to randomise positions.
