.. index:: Masks; Select Similar Islands
.. _etk-masks-select_similar_islands:

***********************
 Select Similar Islands
***********************

.. figure:: /images/nodes-select_similar_islands.png
   :align: right

   The ETK_Select Similar Islands node.

The **ETK_Select Similar Islands** group will create a mask of
matching islands in a geometry. When two vertices are connected by an
edge or shared vertex, they are considered the same island.


Inputs
=======

|INTEGER_FIELD_SINGLE| Index
   The target island's *Index* on which to build the mask.

|FLOAT_FIELD_SINGLE| Deviation
   A fuzziness factor.


Outputs
========

|BOOLEAN_FIELD| Vertex Count
   Given an island identified by *Index*, provide a mask of all
   islands that match the count of vertices.

|BOOLEAN_FIELD| Area
   Creates a mask of all islands that match the area of the target
   island, identified by *Index*.


Examples
=========

.. rubric:: Simple grid islands

.. figure:: /images/nodes-select_similar_islands_basic_image.png
   :align: right

   A set of five islands created from a grid.

For this example, islands are created by taking a grid and removing
bits of geometry. The target chosen, in red, has the *Index* of 5 and
all islands that match the *Vertex Count* output mask are coloured
blue. Because this is a simple grid, the image would be the same if we
were to use the *Area* output as the mask.

.. figure:: /images/nodes-select_similar_islands_basic.png
   :align: center
   :width: 800

   Using **Select Similar Islands** to create a mask of islands
   similar to the target.
