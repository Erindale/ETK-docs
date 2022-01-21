.. index:: Fields; Field Get Item
.. _etk-fields-field_get_item:

***************
 Field Get Item
***************

.. figure:: /images/nodes-field_get_item.png
   :align: right

   The ETK_Field Get Item node.

The **Field Get Item** group retrieves a field value, an *Item*, at a
specific *Index*.


Inputs
======

|GEOMETRY| Geometry
   The geometry on which to retrieve the *Item*.

|VECTOR_FIELD_SINGLE| Field
   The field to retrieve.

|INTEGER_FIELD_SINGLE| Index
   Retrieve the field at this index.

Outputs
=======

|VECTOR_FIELD_SINGLE| Item
   The value of the selected field at the given index.

|INTEGER_FIELD_SINGLE| Index
   Access to the *Index* of the retrieved item.


Example Usage
=============

.. figure:: /images/nodes-field_get_item_basic.png
   :align: center
   :width: 800

   Using the **Field Get Item** group to retrieve the position of a
   Grid position (Index 10) and instance a small cube at that
   location. Note the use of the :ref:`etk-generators-vertex` group.
