.. index:: Mapping; Mapping
.. _etk-mapping-mapping:

********
 Mapping
********

.. figure:: /images/nodes-mapping.png
   :align: right

   The ETK_Mapping node.

The **Mapping** group is a field-based mapping node that takes an
input vector field and modifies its translation, rotation, and scale.
An invert input boolean field is provided to alter the interpretation
of the inputs. All inputs and outputs are fields.


Inputs
=======

|VECTOR_FIELD_SINGLE| Vector
   The input vector field to map.

|VECTOR_FIELD_SINGLE| Translation
   Translate the input vector.

|VECTOR_FIELD_SINGLE| Rotation
   Set the rotation of the input vector.

|VECTOR_FIELD_SINGLE| Scale
   Adjust scale of the input vector.

|BOOLEAN_FIELD_SINGLE| Invert
   Flip the direction of mapping. This allows a simple switch to
   inversely interpret all of mapping.


Outputs
========

|VECTOR_FIELD_SINGLE| Vector
   The resulting output vector field with all mapping applied.


Examples
========

.. rubric:: Rotation mapping

.. figure:: /images/mapping-basic-comp.gif
   :align: right

   Mapping rotations.

This example instances cubes on a small grid then using the **Mapping**
group to rotate every other instance on one axis. The upper part of
the node network establishes the grid and instances small cubes. Every
other cube will be have its rotation modified by the mapping node. The
maximum frame is set to 8 to rotate the instance 90 |DEGREES| and the
looping nature of the GIF animation makes it appear as a constant
circular motion.


.. figure:: /images/nodes-mapping_basic.png
   :align: center
   :width: 800

   Using the **Mapping** group node to rotate instances in Y.
