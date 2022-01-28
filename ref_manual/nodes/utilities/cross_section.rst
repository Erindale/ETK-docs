.. index:: Utilities; Cross Section
.. _etk-utilities-cross_section:

**************
 Cross Section
**************

.. figure:: /images/nodes-cross_section.png
   :align: right

   The ETK_Cross Section node.

The **Cross Section** group allows cuts in an input mesh according to
cut locations specified by vertices in another mesh.


Inputs
=======

|GEOMETRY| Mesh
   The input mesh to cut.

|GEOMETRY| Cut Locations
   A mesh specifying cut locations in the XY plane. This can be as
   simple as a sub-divided line.

|VECTOR_FIELD_SINGLE| Cut Rotations
   The direction of the cut in degrees. The default (0,0,0) cuts
   the mesh parallel to the XY plane.

|BOOLEAN_FIELD_SINGLE| Fill

|GEOMETRY| Alternate Cutter


Outputs
========

|GEOMETRY| Geometry


.. Caution:: Boolean-based so this node may fail.

Examples
========

Basic cross-section
-------------------

This first example make horizontal cross-sections specified by a
hexahedron that has been subdivided in Z. The target mesh is a simple
cone and the slices have been wired and joined to the output.

.. figure:: /images/nodes-cross_section_basic.png
   :align: center
   :width: 800

   Using the **Cross Section** group to make cross-sections in a cone.


Vertical cuts
-------------

For this example a subdivided line is used and positioned in the
Y-axis to cut a cone. The vertices are rendered as red icospheres and
the slices in blue. Vertical cuts are specified with (90°,0,0) so we
get vertical slices in X.

.. figure:: /images/nodes-cross_section_v.png
   :align: center
   :width: 800

   Using the **Cross Section** group to make vertical cross-sections.
