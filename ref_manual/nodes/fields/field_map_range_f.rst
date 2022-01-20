.. index:: Fields; Field Map Range F
.. _etk-fields-field_map_range_f:

******************
 Field Map Range F
******************

.. figure:: /images/nodes-field_map_range_f.png
   :align: right

   The ETK_Field Map Range F node.

The **Field Map Range F** group takes a float input field and maps
that value to a new result. See also :ref:`etk-fields-field_map_range_v`.


Inputs
=======

|GEOMETRY| Geometry
   The geometry to use for values to map.

|FLOAT_FIELD_SINGLE| Value
   The float field value to map.

|FLOAT_FIELD_SINGLE| To Min
   Use this value as a minimum for input *Value*.

|FLOAT_FIELD_SINGLE| To Max
   Use this value as a maximum for input *Value*.

Outputs
========

|FLOAT_FIELD_SINGLE| Result
   Field for mapped values.


Example Usage
==============

.. todo:: Needs an example that doesn't look like Index_to_Fac.
