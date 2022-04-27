.. index:: Masks; Select Similar Verts
.. _etk-masks-select_similar_verts:

*********************
 Select Similar Verts
*********************

.. figure:: /images/nodes-select_similar_verts.png
   :align: right

   The ETK_Select Similar Verts node.

The **Select Similar Verts** group provides a boolean mask to discern
similar normals, adjacent edges or faces.


Inputs
======

|INTEGER_FIELD_SINGLE| Index

   The *Index* field value of the target vertex.

|FLOAT_FIELD_SINGLE| Deviation

   A value to allow some fuzziness to the comparison. If set to
   :math:`0`, only exact matches will make it into the mask.


Outputs
=======

|BOOLEAN_FIELD| Normal

   Calculates the
   `dot product <https://en.wikipedia.org/wiki/Dot_product>`_,
   of the target's normal and the normal of all vertices and returns
   true if that value is within the *deviation* of equivalence.

.. NOTE:: If the two vectors are equivalent, the *dot product*
   calculation would return a value of 1, if exactly opposite, -1.
   This means that a *Deviation* larger than 2 will include all
   vertices.

|BOOLEAN_FIELD| Adjacent Edges

   A boolean mask of the vertices that have the same number of
   adjacent edges.

|BOOLEAN_FIELD| Adjacent Faces

   A boolean mask of the vertices that have the same number of
   adjacent faces.


Examples
=========

.. rubric:: The basic example

.. figure:: /images/nodes-select_similar_verts_basic_comp.png
   :align: right

This example instantiates icospheres on a divided and wired cube. On
the left, *Adjacent edges* were considered and the icospheres are
instantiated only on the corners because the vertex at
:math:`index == 0` is a corner and only the corners have 3 adjacent
edges.

On the right, *Normals* were considered on :math:`index == 0` with a
*Deviation* of :math:`1/3`. With a *Deviation* of :math:`0`, there would
only be a single icosphere instantiated.

.. figure:: /images/nodes-select_similar_verts_basic.png
   :align: center
   :width: 800

   Using **Select Similar Verts** to highlight vertices on a divided
   cube.
