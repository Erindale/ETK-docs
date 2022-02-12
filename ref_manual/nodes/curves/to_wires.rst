.. index:: Curves; To Wires
.. _etk-curves-to_wires:

*********
 To Wires
*********

.. figure:: /images/nodes-to_wires.png
   :align: right

   The ETK_To Wires node.

The **To Wires** group converts a geometry to a wireframe.


Inputs
=======

|GEOMETRY| Geometry
   The input geometry from which to make the wireframe.

|BOOLEAN_FIELD_SINGLE| Selection
   Portions of the geometry can be masked using this field.

|INTEGER| Count

|FLOAT_FIELD_SINGLE| Drop Distance

|FLOAT_FIELD_SINGLE| Deviation

|INTEGER_FIELD_SINGLE| Seed

|INTEGER_FIELD_SINGLE| Wire Resolution
   The number of segments in the wire.

|INTEGER_FIELD_SINGLE| Profile Resolution
   The profile of the wire.

|FLOAT| Profile Radius
   The radius of the wire.


Outputs
========

|GEOMETRY| Mesh

|GEOMETRY| Curve


Examples
========

.. todo:: Add example for ETK_To Wires
