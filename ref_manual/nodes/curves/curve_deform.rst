.. index:: Curves; Curve Deform
.. _etk-curves-curve_deform:

*************
 Curve Deform
*************

.. figure:: /images/nodes-curve_deform.png
   :align: right

   The ETK_Curve Deform node.

The **ETK_Curve Deform** group uses a curve to reshape a mesh.


Inputs
=======

|GEOMETRY| Geometry
   The input geometry.


|GEOMETRY| Curve
   The control curve for deforming the input geometry.


Outputs
========

|GEOMETRY| Geometry
   Deformed geometry.


Examples
=========

.. rubric:: Cylinder animation

.. figure:: /images/curve-deform-comp.gif
   :align: right
   :width: 360

This example takes a simple vertical cylinder, with increased side
segments, and deforms it along a ``Bezier Segment`` used as a control
curve to the ``Curve Deform`` node. Six frames are animated using
the ``Scene Time -> Frame`` as input to
the :ref:`etk-falloff-easing_sine` falloff node to modify the curves
handles along the X-axis. The final six frames of the animation
are the first six images in reverse.

.. figure:: /images/nodes-curve_deform_gn.png
   :align: center
   :width: 800

   The ``Curve Deform`` node used to reshape a cylinder controlled by
   a curve that is in turn tweaked by the
   :ref:`etk-falloff-easing_sine` node group.
