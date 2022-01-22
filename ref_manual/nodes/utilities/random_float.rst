.. index:: Utilities; Random Float
.. _etk-utilities-random_float:

*************
 Random Float
*************

.. figure:: /images/nodes-random_float.png
   :align: right

   The ETK_Random Float node.

The **Random Float** group generates a random float value based on an
input value and deviation.


Inputs
=======

|FLOAT_FIELD_SINGLE| Value
   The input value.

|FLOAT_FIELD_SINGLE| Deviation
   Generate a float that is plus or minus this amount from the input
   *Value*.

|INTEGER_FIELD_SINGLE| Seed
   Randomization seed.


Outputs
========

|FLOAT_FIELD_SINGLE| Value
   The generated random float value.


Examples
========

.. figure:: /images/nodes-random_float_basic.png
   :align: center
   :width: 800

   Creating a wobbly sphere with the **Random Float** and **UV
   Sphere** node, which allows a field input on *Radius*.
