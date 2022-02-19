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

.. index:: Signed Distance Function; Selection Prism

|FLOAT_FIELD| SDF
   A signed distance function yielding increasing values further from
   the prism boundary.

|GEOMETRY| Preview
   Real geometry that can be joined to the view to aid in placing the
   prism.


Examples
========

.. rubric:: Prism selection

The setup for this example is a simple cube populated with smaller
cubes by a :ref:`etk-utilities-distribute_points_in_volume` group,
set fairly densely but with no randomisation.

.. figure:: /images/nodes-selection_prism_basic.png
   :align: center
   :width: 800

   Using a 3-sided **Selection Prism** to mask instances from a cube
   shape.

.. figure:: /images/nodes-selection_prism_basic_comp.png
   :align: center

   The unmasked instances, with mask and preview in the center, then without the
   preview.
