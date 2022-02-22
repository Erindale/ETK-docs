.. index:: Curves; To Wires
.. _etk-curves-to_wires:

*********
 To Wires
*********

.. figure:: /images/nodes-to_wires.png
   :align: right

   The ETK_To Wires node.

The **To Wires** group takes an input geometry and creates a
wireframe. There are a number of options to add interest to the
resulting mesh.


Inputs
=======

|GEOMETRY| Geometry
   The input geometry from which to make the wireframe.

|BOOLEAN_FIELD_SINGLE| Selection
   Portions of the geometry can be masked using this field.

|INTEGER| Count
   The number of wires between vertices. This is most apparent when
   *Deviation* is greater than zero.

|FLOAT_FIELD_SINGLE| Drop Distance
   Allow the connection between vertices to sag this amount.

|FLOAT_FIELD_SINGLE| Deviation
   Allows the *Drop Distance* to vary randomly by this amount. When the
   *Count* is greater than zero, each strand will have a different
   value applied.

|INTEGER_FIELD_SINGLE| Seed
   The randomisation seed to apply to the *Deviation*.

|INTEGER_FIELD_SINGLE| Wire Resolution
   The number of segments in the wire. Increasing this value will
   improve the effect of *Drop Distance*.

|INTEGER_FIELD_SINGLE| Profile Resolution
   The profile of the wire. The default 3 is the smallest value to
   create a 3D shape.

|FLOAT| Profile Radius
   The radius of the wire.


Outputs
========

|GEOMETRY| Mesh
   The output mesh.

|GEOMETRY| Curve
   The output geometry as a curve.


Examples
========

.. rubric:: Simple wireframes

Using an Ico Sphere as the input mesh, the **To Wires** node group is
used to represent that mesh as wires.


.. figure:: /images/nodes-to_wire_basic_comp.png
   :align: center

   Various configurations using the **To Wires** group.

Above, from left to right,

   * The plain Ico Sphere
   * Count=1, Drop Distance=0, Wire Resolution=1
   * Count=3, Drop Distance=0.2, Deviation=0.4, Wire Resolution=12

.. figure:: /images/nodes-to_wire_basic.png
   :align: center
   :width: 800

   The Ico Sphere with the **To Wires** group and a small amount of
   *Drop Distance* and no *Deviation*.


The other output available is *Curves*.

.. figure:: /images/nodes-to_wire_basic_curves.png
   :align: center
   :width: 800

   Selecting only vertices above the XY plane and outputting a curve.
