.. index:: Masks; Select Similar Edges
.. _etk-masks-select_similar_edges:

*********************
 Select Similar Edges
*********************

.. figure:: /images/nodes-select_similar_edges.png
   :align: right

   The ETK_Select Similar Edges node.

The **ETK_Select Similar Edges** group creates a mask based on
similarities to a target edge.


Inputs
=======

|INTEGER_FIELD_SINGLE| Index
   The edge at the target *Index*.

|FLOAT_FIELD_SINGLE| Deviation
   A fuzziness value for the comparison.


Outputs
========

|BOOLEAN_FIELD| Direction
   Create a mask of all edges that have the same direction as the
   edge at *Index*.

|BOOLEAN_FIELD| Length
   Create a mask containing all edges that are the same length as the
   edge at *Index*.

|BOOLEAN_FIELD| Edge Angle
   Create a mask of all edges having the same edge angle as the edge
   at *Index*.

|BOOLEAN_FIELD| Adjacent Faces
   Create a mask of all edges having the same number of adjacent faces
   as the target edge. One application for this output is for finding
   the non-manifold edges of a geometry.


Examples
========

.. rubric:: A UV Sphere example

.. figure:: /images/nodes-select_similar_edges_basic_comp.png
   :align: center

   Example images using **Select Similar Edges**.

In this example, the same target is used for both images. The image on
the left builds a mask using edge *Angle* from which you can tell that
the mask comparison uses unsigned angles since the mask includes edges
below the equator. On the right, the *Length* is selected for the same
edge. Note how all longitudinal edges of a UVSphere have an equal
length.

.. figure:: /images/nodes-select_similar_edges_gn.png
   :align: center
   :width: 800

   Using **Select Similar Edges** to create masks for instances on a
   UVSphere.

The nodes along the top create the UVSphere geometry colored yellow,
along the bottom the nodes instantiate the red ICO Sphere at the
requested edge at *Index*.
