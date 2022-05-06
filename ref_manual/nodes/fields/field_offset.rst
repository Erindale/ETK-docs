.. index:: Fields; Field Offset
.. _etk-fields-field_offset:

*************
 Field Offset
*************

.. figure:: /images/nodes-field_offset.png
   :align: right

   The ETK_Field Offset node.

The **Field Offset** group takes a geometry as input and bumps the
*Index* of an input *Field* by a given amount. Consider the simplest
Grid mesh with 4 vertices. The positions :math:`P_{0-3}`
would look like this as the offset is incremented.

+-------------+-------------+-------------+-------------+
| Offset 0    |      1      |      2      |      3      |
+=============+=============+=============+=============+
| :math:`P_0` | :math:`P_3` | :math:`P_2` | :math:`P_1` |
+-------------+-------------+-------------+-------------+
| :math:`P_1` | :math:`P_0` | :math:`P_3` | :math:`P_2` |
+-------------+-------------+-------------+-------------+
| :math:`P_2` | :math:`P_1` | :math:`P_0` | :math:`P_3` |
+-------------+-------------+-------------+-------------+
| :math:`P_3` | :math:`P_2` | :math:`P_1` | :math:`P_0` |
+-------------+-------------+-------------+-------------+

Inputs
=======

|GEOMETRY| Geometry
   The geometry which will have its field manipulated.

|VECTOR_FIELD_SINGLE| Field
   The field to bump by *Index Offset*.

|INTEGER_FIELD_SINGLE| Index Offset
   Offset the index of *Field* by this amount. A default value of
   :math:`0` has no effect.


Outputs
========

|VECTOR_FIELD| Field
   The modified field.


Examples
========

.. rubric:: Offsetting the Position

.. figure:: /images/nodes-field-offset-basic-comp.gif
   :align: right

This example animates a cube around a grid by offsetting the
*Position* field of the grid and only instantiating the cube at
*Index* 0. The node group uses the *Frame* output of the new
*Scene Time* node to render 16 frames (:math:`[0\ldots 15]`).

Compare this to the :ref:`etk-fields-field_shuffle` group.

.. figure:: /images/nodes-field_offset_basic.png
   :align: center
   :width: 800

   The **Field Offset** group is used to move the *Position* at
   *Index* zero around a grid geometry.
