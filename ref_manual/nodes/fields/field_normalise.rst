.. index:: Fields; Field Normalise
.. _etk-fields-field_normalise:

****************
 Field Normalise
****************

.. figure:: /images/nodes-field_normalise.png
   :align: right

   The ETK_Field Normalise node.

The **Field Normalise** group takes a vector field and maps all
vectors to values between 0 and 1.


Inputs
=======

|GEOMETRY| Geometry
   The geometry on which to read the *Field*.

|VECTOR_FIELD_SINGLE| Field
   The vector rield value to normalise.


Outputs
========

|VECTOR_FIELD_SINGLE| Field
   The normalised output.


Examples
========

.. figure:: /images/nodes-field_normalise_basic.png
   :align: center
   :width: 800

   The outer 2m radius circle is our input, the *Position* field is
   normalised and then used to set the position.
