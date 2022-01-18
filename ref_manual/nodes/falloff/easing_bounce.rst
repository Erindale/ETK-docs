.. index:: Falloff; Easing Bounce
.. _etk-falloff-easing_bounce:

**************
 Easing Bounce
**************

.. figure:: /images/nodes-easing_bounce.png
   :align: right

   The ETK_Easing Bounce node.

The **Easing Bounce** group applies a bounce to the start and / or
finish of the range.


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

.. list-table:: Easing Bounce function graphs
   :align: center

   * - .. image:: /images/nodes-easing_bounce_both.png
     - .. image:: /images/nodes-easing_bounce_in.png
     - .. image:: /images/nodes-easing_bounce_out.png
   * - **Ease In** and **Ease Out** checked.
     - **Ease In** only.
     - **Ease Out** only.
