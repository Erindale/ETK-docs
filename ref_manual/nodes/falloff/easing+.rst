.. index:: Falloff; Easing+
.. _etk-falloff-easing+:

********
 Easing+
********

.. figure:: /images/nodes-easing+.png
   :align: right

   The ETK_Easing+ node.

The **Easing+** group allows the user to control the exponent.



Inputs
=======

|FLOAT_FIELD| 0..1
   The input value in the range of 0..1.

|BOOLEAN_FIELD_SINGLE| Ease In
   Apply the function to the start of the range.

|BOOLEAN_FIELD_SINGLE| Ease Out
   Apply the function to the last half of the range.

|FLOAT_FIELD_SINGLE| Exponent
   The desired exponent to apply across the range.

Outputs
========

|FLOAT_FIELD_SINGLE| Value
   The output with the falloff function applied.


Function Graphs
===============

Since Falloff group nodes apply a function across a range, it is
useful to visualize the working of the node with a graph. The graphs
were built using this :ref:`falloff_graph`.

.. list-table:: Easing+ function graphs
   :align: center

   * - .. image:: /images/nodes-easing+_both.png
     - .. image:: /images/nodes-easing+_in.png
     - .. image:: /images/nodes-easing+_out.png
   * - **Ease In** and **Ease Out** checked.
     - **Ease In** only.
     - **Ease Out** only.
