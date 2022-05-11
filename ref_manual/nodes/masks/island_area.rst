.. index:: Masks; Island Area
.. _etk-masks-island_area:

************
 Island Area
************

.. figure:: /images/nodes-island_area.png
   :align: right

   The ETK_Island Area node.

The **Island Area** group populates a mask of island indices whose
area is less than or equal to a given threshold.


Inputs
=======

|FLOAT_FIELD_SINGLE| Threshold

   The area value for comparison.


Outputs
========

|BOOLEAN_FIELD| Mask

   All islands in the geometry with :math:`area \leq Threshold`.


|BOOLEAN_FIELD| Inverted

   For convenience, the inverse of *Mask*.


Examples
=========

.. rubric:: Identifying islands by area

.. figure:: /images/nodes-island_area_basic_panels.png
   :align: right

   Islands with areas of 0.25, 1.0, and 2.25 square meters.


This is a trivial example but shows precisely how this node works.
Three islands are created with areas of .25, 1, and 2.25 square
meters. An **Island Area** node is then used to color those below the
threshold of 2.2 square meters in blue.

.. figure:: /images/nodes-island_area_basic.png
   :align: center
   :width: 800

   Using the **Island Area** node to identify islands by area.
