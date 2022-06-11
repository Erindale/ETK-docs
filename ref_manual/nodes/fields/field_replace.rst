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

.. todo:: Add example for ETK_Sort Vertices
