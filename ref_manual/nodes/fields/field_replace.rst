.. index:: Fields; Field Replace
.. _etk-fields-field_replace:

**************
 Field Replace
**************

.. figure:: /images/nodes-field_replace.png
   :align: right

   The ETK_Field Replace node.

The **Field Replace** group replaces a field value with another field
value. This can be used to alter positions within a geometry,
optionally controlled with a mask.


Inputs
======

|FLOAT_FIELD_SINGLE| Field Original
   This field value will be passed to output if the *Mask* is ``True``.

|FLOAT_FIELD_SINGLE| Field New
   This field value will be passed to output if the *Mask* is ``False``.

|BOOLEAN_FIELD_SINGLE| Mask
   The mask to determine if a replacement is made for this field.


Outputs
========

|FLOAT_FIELD_SINGLE| Field
   The output field value.

Examples
========

.. rubric:: Simple Field replacement

.. figure:: /images/nodes-field-replace-basic-comp.gif
   :align: right

Starting with a :math:`4\times 4` grid, all positions are shuffled by
the :ref:`etk-fields-field_shuffle` group. The **Field Replace** group is
then used to replace the positions for :math:`index < 8`, the left
half of the grid. The animation has 16 frames from :math:`0\ldots 15`
and a single cube is instanced on the position given by the frame
number.

The expectation is that the cube will traverse the grid in order first
half of the animation and then move to the original shuffled locations
on the last 8 frames.

.. figure:: /images/nodes-field_replace_basic.png
   :align: center
   :width: 800

   The **Field Replace** group used to replace a grid with shuffled
   position so that the left half is replaced with the original
   position.
