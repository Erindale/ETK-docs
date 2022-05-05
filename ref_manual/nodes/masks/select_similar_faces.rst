.. index:: Masks; Select Similar Faces
.. _etk-masks-select_similar_faces:

*********************
 Select Similar Faces
*********************

.. figure:: /images/nodes-select_similar_faces.png
   :align: right

   The ETK_Select Similar Faces node.

The **Select Similar Faces** group generates a field-based mask of
matching faces.


Inputs
======

|INTEGER_FIELD_SINGLE| Index
   The *index* of the face to use as a target.

|FLOAT_FIELD_SINGLE| Deviation
   A fuzziness factor to allow a :math:`\pm` range on the results.

|GEOMETRY| Geo (for perimeter)
   The input geometry, only used to determine the perimeter mask.


Outputs
=======

|BOOLEAN_FIELD| Coplanar
   Create a mask of faces that are coplanar with the face at the target
   *Index*.

|BOOLEAN_FIELD| Normal
   Generate a mask of faces whose normal matches the normal of the
   face at *Index*.

|BOOLEAN_FIELD| Sides
   Create a mask of faces whose count of face neighbors are the same
   as the face at *Index*.

|BOOLEAN_FIELD| Area
   Create a mask of faces whose area is the same as the face at *Index*.

|BOOLEAN_FIELD| Perimeter
   Generates a mask of faces whose perimeter value is equal to that of
   the target face at *Index*. This requires the source geometry
   to be attached.


Examples
========

.. rubric:: Four (almost) out of five outputs

.. figure:: /images/nodes-select_similar_faces_basic_comp.png
   :align: center

   The output from a single node setup using different outputs.

Starting with a bisected cube with all faces extruded, a target face
is selected (:math:`Index = 8`) and then various masks are
created. The target face is colored red, and the mask selection faces
are blue.

* On the left is the node tree with the *Coplanar* mask output
  attached.
* The middle is the *Normal* mask.
* On the right is the *Area* mask.

Not shown is the output from the *Perimeter* mask because it matches
the *Area* mask.

.. figure:: /images/nodes-select_similar_faces_basic_gn.png
   :align: center
   :width: 800

   Using the **Select Similar Faces** node to find matching faces.
