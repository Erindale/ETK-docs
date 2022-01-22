.. index:: Utilities; Random Vector
.. _etk-utilities-random_vector:

**************
 Random Vector
**************

.. figure:: /images/nodes-random_vector.png
   :align: right

   The ETK_Random Vector node.

The **Random Vector** group takes an input vector and generates a
random new vector.


Inputs
=======

|VECTOR_FIELD_SINGLE| Vector
   The input vector to use as a basis for the new vector.

|VECTOR_FIELD_SINGLE| Deviation
   Controls in what direction the new vector will be generated

|INTEGER_FIELD_SINGLE| Seed
   Randomization seed.


Outputs
========

|VECTOR_FIELD_SINGLE| Vector
   The generated vector


Examples
========

.. figure:: /images/nodes-random_vector_basic.png
   :align: center
   :width: 800

   Using the **Random Vector** group to randomly displace points on a
   grid in the Z direction.
