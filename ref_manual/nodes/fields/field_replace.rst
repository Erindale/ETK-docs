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

.. figure:: /images/nodes-field_replace_2.png
   :align: right

   Field-based point creation.

The **Field Replace** node can be useful when selection inputs aren't
provided. This example manipulates the position at which points are
created based on a simple deteriminant. There are several reasonable
ways of accomplishing this particular task but it never hurts to have
additional tools.

.. figure:: /images/nodes-field_replace_gn.png
   :align: center
   :width: 800

   Using **Field Replace** to set positions of points on creation.
