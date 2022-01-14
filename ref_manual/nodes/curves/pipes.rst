.. index:: Curves; Pipes
.. _etk.curves.pipes:

******
 Pipes
******

.. figure:: /images/nodes-pipes.png
   :align: right

   The ETK_Pipes node.


The **Pipes** group takes a *mesh* or *curve* object and forms a pipe
onto that geometry.


Inputs
=======

|GEOMETRY| Mesh / Curve
   The input geometry on which to form a pipe.

|FLOAT| Radius
   Radius of the pipe.

|INTEGER| Resolution
   The resolution of the circumference of the pipe.

|BOOLEAN| Fill Caps
   Fill end caps of the pipe if checked.

Outputs
========

|GEOMETRY| Mesh
   The output mesh.

Example Usage
==============

.. figure:: /images/curves-pipes_basic.png
   :align: center
   :width: 800

   Using an **ETK_Pipes** group to create a simple spring.
