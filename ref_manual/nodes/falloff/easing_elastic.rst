.. index:: Falloff; Easing Elastic
.. _etk-falloff-easing_elastic:

***************
 Easing Elastic
***************

.. figure:: /images/nodes-easing_elastic.png
   :align: right

   The ETK_Easing Elastic node.

The **Easing Elastic** group applies a function that slowly enters
and/or exits a fast transition with a slight bounce.


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

.. Hint:: Take care with clamping the output of this node.


Function Graphs
===============

Since Falloff group nodes apply a function across a range, it is
useful to visualize the working of the node with a graph. The graphs
were built using this :ref:`falloff_graph`.

.. list-table:: Easing Elastic function graphs
   :align: center

   * - .. image:: /images/nodes-easing_elastic_both.png
     - .. image:: /images/nodes-easing_elastic_in.png
     - .. image:: /images/nodes-easing_elastic_out.png
   * - **Ease In** and **Ease Out** checked.
     - **Ease In** only.
     - **Ease Out** only.
