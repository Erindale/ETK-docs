.. index:: Masks; Selection Prism
.. _etk-masks-selection_prism:

****************
 Selection Prism
****************

.. figure:: /images/nodes-selection_prism.png
   :align: right

   The ETK_Selection Prism node.

The **Selection Prism** group provides an n-sided polygon which can be
used as a mask against a geometry. Like other selection groups, a
preview is provided to help view the location of the prism.


Inputs
=======

|INTEGER| Sides
   The number of sides of the polygon.

|FLOAT| Radius
   Radial distance from center to edge.

|VECTOR_FIELD_SINGLE| Centre
   A vector to position the prism.

|VECTOR_FIELD_SINGLE| Rotation
   A rotational vector for angular masking.


Outputs
========

|BOOLEAN_FIELD| Inside
   Yields *true* for vertices inside the prism.

|BOOLEAN_FIELD| Outside
   Yields *true* for vertices outside the prism.

|FLOAT_FIELD| SDF

|GEOMETRY| Preview
   Real geometry that can be joined to the view to aid in placing the
   prism.


Examples
========

.. todo:: Add example for ETK_Selection Prism
