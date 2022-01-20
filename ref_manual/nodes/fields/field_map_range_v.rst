.. index:: Fields; Field Map Range V
.. _etk-fields-field_map_range_v:

******************
 Field Map Range V
******************

.. figure:: /images/nodes-field_map_range_v.png
   :align: right

   The ETK_Field Map Range V node.

The **Field Map Range V** group takes a vector field of a geometry and
maps it to new vector. See also :ref:`etk-fields-field_map_range_f`.


Inputs
=======

|GEOMETRY| Geometry
   The geometry to use for values to map.

|VECTOR_FIELD_SINGLE| Value
   The vector value to map.

|VECTOR_FIELD_SINGLE| To Min
   Use this value as a minimum for input *Value*.

|VECTOR_FIELD_SINGLE| To Max
   Use this value as a maximum for input *Value*.


Outputs
========

|VECTOR_FIELD_SINGLE| Result
   Remapped vector output.


Example Usage
==============

.. figure:: /images/nodes-map_range_v_basic.png
   :align: center
   :width: 800

   The **Field Map Range V** group is used here to remap the position
   vectors of one curve into a smaller curve then joined into a
   shape with a :ref:`etk-curves-loft_curves` group.
