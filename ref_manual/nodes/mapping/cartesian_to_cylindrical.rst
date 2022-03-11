.. index:: Mapping; Cartesian to Cylindrical
.. _etk-mapping-cartesian_to_cylindrical:

*************************
 Cartesian to Cylindrical
*************************

.. figure:: /images/nodes-cartesian_to_cylindrical.png
   :align: right

   The ETK_Cartesian to Cylindrical node.

The **Cartesian to Cylindrical**  group converts between cartesian
and cylindrical coordinates.

See also :ref:`etk-mapping-cylindrical_to_cartesian`,
`cylindrical coordinate system
<https://en.wikipedia.org/wiki/Cylindrical_coordinate_system>`_
article in wikipedia.

Inputs
=======

|VECTOR_FIELD_SINGLE| (x, y, z)
   The cartesian vector coordinates to convert.

Outputs
========

|FLOAT_FIELD_SINGLE| (r, |THETA|, z)
   The converted cylindrical coordinates, where

      * *r* is the axial radius, sometime annotated as |RHO| (rho), or the
        projection of the radius onto the XY plane.
      * |THETA| is the rotational angle
      * and *z* is the elevation

Examples
========

.. rubric:: Faking a bevel

.. index::
   pair: Examples using; Clamp

This odd node group takes a UV Sphere and creates a cylinder by
constraining the radius using the Minimum option of a math node. The
height is then constrained using a *Clamp* utility node, leaving a
small (0.1) bevel at both ends.

.. figure:: /images/nodes-cartesian_cylindrical_basic.png
   :align: center
   :width: 800

   Using a sphere as input, the **Cartesian to Cylindrical** group is
   used to fake a bevel by clamping Z and constraining the radius
   before converting back to cartesian coordinates.


.. rubric:: Exploiting cylindrical coordinates

.. figure:: /images/nodes-cartesian_cylindrical_radius_example_1.png
   :align: right

   Three samples of a radial saw pattern.

.. index::
   pair: Examples using; Wrap

Cylindrical coordinates are especially useful when all you need for
your model is a tweak in the radius around a circle. The radial
saw-looking images at the right are created by taking a mesh circle
and tweaking the radius in increasing amounts for a portion circle.
This is duplicated using the wrap option of a math node so the
projections loop around the circle. The two integer inputs are the
number of *Points* and *Height* of the projection. These are also used
to create a filled circle with the appropriate resolution so the wrap
works evenly.

The set of images on the right were created using the following
configurations,

+--------+--------+
| Points | Height |
+========+========+
| 6      | 4      |
+--------+--------+
| 12     | 4      |
+--------+--------+
| 20     | 8      |
+--------+--------+

The *Multiply Add* math node is used to calculate a new value for the
radius (the *x* of the *Vector Separate* and *Combine* pair) based on
the input and then sets that position.

.. figure:: /images/nodes-cartesian_cylindrical_radius_example.png
   :align: center
   :width: 800

   The node group showing how cartesian to cylindrical mapping can be
   helpful with shapes like this.
