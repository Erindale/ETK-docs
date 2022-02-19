.. index:: Masks; Selection Sphere
.. _etk-masks-selection_sphere:

*****************
 Selection Sphere
*****************

.. figure:: /images/nodes-selection_sphere.png
   :align: right

   The ETK_Selection Sphere node.

The **Selection Sphere** group provides a field-based spherical mask.


Inputs
=======

|FLOAT| Radius
   The radius of the selection sphere.

|VECTOR| Centre
   The sphere's centre, used to position the sphere.


Outputs
========

|BOOLEAN_FIELD| Inside
   Boolean field that yields *True* inside the selection sphere.

|BOOLEAN_FIELD| Outside
   Boolean field that yields *True* outside the selection sphere.

.. index:: Signed Distance Function; Selection Sphere

|FLOAT_FIELD| SDF
   A signed-distance-function which yields negative values within the
   sphere, increasing positive values outside.

|GEOMETRY| Preview
   Real geometry that can be join'd to the output temporarily to place
   the selection.


Examples
========

.. rubric:: Cutting a cube with a sphere

In this example a bite is taken out of the corner of a subdivided
cube. The cube is specified as :math:`{4}\times{4}\times{4}` and the
cube instances are scaled down to fill the perimeter tightly. The
default 2-meter radius is used for the selection sphere.

.. figure:: /images/nodes-selection_sphere_basic.png
   :align: center
   :width: 800

   The **Selection Sphere** used to take a corner out of a subdivided
   cube, viewed here with the selection preview joined to the output
   geometry.

For this example, the :math:`{3}\times{3}` cube is at the origin and the
**Spherical Selection** group specifies a *Centre* offset :math:`(1,1,1)`.

.. figure:: /images/nodes-selection_sphere_basic_comp.png
   :align: center

   The subdivided cube, a spherical selection removed, and the same
   setup with the SDF output attached to the scale of the instances.
