.. index:: Curves; Bevel a Curve
.. _etk-curves-bevel_a_curve:

**************
 Bevel a Curve
**************

.. figure:: /images/nodes-bevel_a_curve.png
   :align: right

   The ETK_Bevel a Curve node.

The **Bevel a Curve** group bevels a curve using a profile shape along
a path. A curve for tapering influences the size of the profile as it
is instanced along the path.

Inputs
=======

|GEOMETRY| Path Curve
   Bevel the curve along this path.

|GEOMETRY| Profile Curve
   Along the path, use this curve as a profile.

|GEOMETRY| Taper Curve
   Use this curve to influence the taper of the profile along the
   curve.

|INTEGER_FIELD_SINGLE| Resolution
   The output spline resolution.

|FLOAT_FIELD_SINGLE| Tilt
   The output curve tilt.

|FLOAT_FIELD_SINGLE| Radius
   A multiplier of the taper along the path.

|BOOLEAN| Fill Caps
   A boolean input, ticked to fill the end caps.


Outputs
========

|GEOMETRY| Mesh
   The generated mesh.

Examples
========

.. figure:: /images/nodes-bevel_a_curve_basic.png
   :align: center
   :width: 800

   The **Bevel a Curve** group is used here to shape a horn using a
   bezier segment to form the path, a bezier circle as a profile, and
   another segment to taper the horn.
