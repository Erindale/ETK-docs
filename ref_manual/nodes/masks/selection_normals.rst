.. index:: Masks; Selection Normals
.. _etk-masks-selection_normals:

******************
 Selection Normals
******************

.. figure:: /images/nodes-selection_normals.png
   :align: right

   The ETK_Selection Normals node.

The **Selection Normals** group will make selections based on the
normals of a geometry. One application of this node is in placing
foliage only on those portions of a geometry that face up.


Inputs
=======

|VECTOR_FIELD_SINGLE| Vector
   A vector that defines the axis to select against.

|FLOAT_FIELD_SINGLE| Deviation
   The deviation from the input *Vector*.


Outputs
========

|BOOLEAN_FIELD| Inside
   True if inside the deviation.

|BOOLEAN_FIELD| Outside
   True if outside the deviation.

|FLOAT_FIELD| Fac
   A 0..1 factor that can be used instead of the boolean outputs.


Examples
========

.. rubric:: Basic normal masking

In this example a white and green material are defined on our
geometry. We set the entire sphere green to start, then white on all
faces that deviate by :math:`1\over{3}` *Inside* the Z-axis, then green on all
faces that deviate by :math:`2\over{3}` *Outside*.

.. figure:: /images/nodes-selection_normals_basic.png
   :align: center
   :width: 800

   Using a pair of **Selection Normals** groups as masks to set the
   material on a sphere.

.. figure:: /images/nodes-selection_normals_basic_fac.png
   :align: right
   :width: 400

Note that the second mask could have been achieved by adjusting the
vector to point the opposite direction on the group node. That is, a
vector of (0, 0, -1) with the deviation :math:`1\over{3}` and using
the *Inside* boolean output.

Also, the *Fac* output can sometimes be used to greater effectiveness
as shown on the right. In this node group the selection is managed
with a single **Selections Normals** but uses the *Fac* value to set
the material if it veers either side of :math:`1\over{6}` from the
Z-axis.
