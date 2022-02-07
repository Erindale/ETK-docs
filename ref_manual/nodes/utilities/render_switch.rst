.. index:: Utilities; Render Switch
.. _etk-utilities-render_switch:

**************
 Render Switch
**************

.. figure:: /images/nodes-render_switch.png
   :align: right

   The ETK_Render Switch node.

The **Render Switch** group provides a mechanism to use one float
value for viewport viewing and another for rendering. This can be used
when the rendered geometry contains a dense distribution and you would
prefer to view a smaller distribution.

Inputs
=======

|FLOAT_FIELD_SINGLE| Viewport Value

   The float value to be used in the viewport.

|FLOAT_FIELD_SINGLE| Render Value

   The float value to use in the render.

|BOOLEAN_FIELD_SINGLE| Show Render

    A switch to use the render value in the viewport. Checked or not,
    *Render Value* will be used for renders.


Outputs
========

|FLOAT_FIELD_SINGLE| Output

   The output value.


Examples
========

.. rubric:: Basic density control

This example uses the **Render Switch** to control the density of the
Poisson Disk distribution to allow a tighter (0.1) distance on render
while viewing a sparse distribution in the viewport.

.. figure:: /images/nodes-render_switch_basic_01.png
   :align: center
   :width: 800

   The node group distributes cubes on a subdiv'd and smoothed cube.

.. figure:: /images/nodes-render_switch_basic_comp.png
   :align: center

   On the left is the viewport with the render switch off, the center
   with the switch on, and the final render.
