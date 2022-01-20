.. index:: Fields; Index to Fac
.. _etk-fields-index_to_fac:

*************
 Index to Fac
*************

.. figure:: /images/nodes-index_to_fac.png
   :align: right

   The ETK_Index to Fac node.

The **Index to Fac** group takes a geometry as input and maps the
index to a 0..1 range on the output.

Inputs
=======

|GEOMETRY| Geometry
   Geometry in which the index will be found.

Outputs
========

|FLOAT_FIELD_SINGLE| Fac
   A 0..1 gradient representing the indices.

Example Usage
==============

.. figure:: /images/nodes-index_to_fac_basic.png
   :align: center
   :width: 800

   Using the **Index to Fac** group to recreate the
   :ref:`etk-falloff-easing_back` example. One advantage here is that
   the mesh line can be configured with *End Points* so resolution is
   more intuitive to configure.
