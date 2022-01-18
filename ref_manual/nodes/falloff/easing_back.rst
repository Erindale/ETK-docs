.. index:: Falloff; Easing Back
.. _etk-falloff-easing_back:

************
 Easing Back
************

.. figure:: /images/nodes-easing_back.png
   :align: right

   The ETK_Easing Back node.

The **Easing Back** group applies a soft rebound function to the start
and end of the input's range.


Inputs
=======

|FLOAT_FIELD| 0..1
   The input value in the range of 0..1.

|BOOLEAN_FIELD_SINGLE| Ease In
   Apply the function to the start of the range.

|BOOLEAN_FIELD_SINGLE| Ease Out
   Apply the function to the last half of the range.

|FLOAT_FIELD_SINGLE| Constant
   A float value applied throughout the range.

.. Hint:: With *Constant* > 0, some values in the output will be
          outside the range of 0..1 so take care with clamping.

Outputs
========

|FLOAT_FIELD_SINGLE| Value
   The output with the falloff function applied.


Function Graphs
===============

Since Falloff group nodes apply a function across a range, it is
useful to visualize the working of the node with a graph. The graphs
were built using this :ref:`falloff_graph`.

.. list-table:: Easing Back function graphs
   :align: center

   * - .. image:: /images/nodes-easing_back_both.png
     - .. image:: /images/nodes-easing_back_in.png
     - .. image:: /images/nodes-easing_back_out.png
   * - **Ease In** and **Ease Out** checked.
     - **Ease In** only.
     - **Ease Out** only.
