.. index:: Falloff; Easing Sine
.. _etk-falloff-easing_sine:

************
 Easing Sine
************

.. figure:: /images/nodes-easing_sine.png
   :align: right

   The ETK_Easing Sine node.

The **Easing Sine** group employs the sine function along the input
range. This can provide a nice soft transition.


Inputs
=======

|FLOAT_FIELD| 0..1
   The input value in the range of 0..1.

|BOOLEAN_FIELD_SINGLE| Ease In
   Apply the function to the start of the range.

|BOOLEAN_FIELD_SINGLE| Ease Out
   Apply the function to the last half of the range.


Outputs
========

|FLOAT_FIELD_SINGLE| Value
   The output with the falloff function applied.


Function Graphs
===============

Since Falloff group nodes apply a function across a range, it is
useful to visualize the working of the node with a graph. The graphs
were built using this :ref:`falloff_graph`.

.. list-table:: Easing Sine function graphs
   :align: center

   * - .. image:: /images/nodes-easing_sine_both.png
     - .. image:: /images/nodes-easing_sine_in.png
     - .. image:: /images/nodes-easing_sine_out.png
   * - **Ease In** and **Ease Out** checked.
     - **Ease In** only.
     - **Ease Out** only.
