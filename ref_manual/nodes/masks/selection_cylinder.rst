.. index:: Masks; Selection Cylinder
.. _etk-masks-selection_cylinder:

*******************
 Selection Cylinder
*******************

.. figure:: /images/nodes-selection_cylinder.png
   :align: right

   The ETK_Selection Cylinder node.

The **Selection Cylinder** group provides a cylinder to define a
geometry to use as a selection mask.

See also :ref:`etk-masks-selection_box`.


Inputs
=======

|FLOAT| Radius
   The radius of the cylinder.

|VECTOR_FIELD_SINGLE| Centre
   Adjust this value to position the cylinder.

|VECTOR_FIELD_SINGLE| Rotation
   Access to the selection cylinder's rotation vector.


Outputs
========

|BOOLEAN_FIELD| Inside
   Boolean mask of points inside the cylinder.

|BOOLEAN_FIELD| Outside
   Boolean mask of points outside the cylinder.

.. index:: Signed Distance Function; Selection Cylinder

|FLOAT_FIELD| SDF
   A signed distance function that yields increasing values
   further from the cylinder boundary.

|GEOMETRY| Preview
   The geometry of the cylinder that can be joined to the **Group
   Output** to help position the selection.


Examples
========

This example displays the **Selection Cylinder** preview as well as
using the SDF output to tweak the size of instances.

.. figure:: /images/nodes-selection_cylinder_basic.png
   :align: center
   :width: 800

   Using a **Selection Cylinder** to select points in a point cloud.
   Very similar to :ref:`etk-masks-selection_box`.
