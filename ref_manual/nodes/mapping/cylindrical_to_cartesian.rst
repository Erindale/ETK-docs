.. index:: Mapping; Cylindrical to Cartesian
.. _etk-mapping-cylindrical_to_cartesian:

*************************
 Cylindrical to Cartesian
*************************

.. figure:: /images/nodes-cylindrical_to_cartesian.png
   :align: right

   The ETK_Cylindrical to Cartesian node.

The **Cylindrical to Cartesian** group converts cylindrical
coordinates to cartesian coordinates.
See also :ref:`etk-mapping-cartesian_to_cylindrical`.

Inputs
=======

|FLOAT_FIELD_SINGLE| (r, |THETA|, z)
   The cylindrical coordinates to convert, where

      * *r* is the axial radius, sometime annotated as |RHO| (rho), or the
        projection of the radius onto the XY plane.
      * |THETA| is the rotational angle
      * and *z* is the elevation

Outputs
========

|FLOAT_FIELD_SINGLE| (x, y, z)
   The resulting cartesian coordinates.


Examples
========

.. rubric:: When you just want the radius

This first example makes a cupcake mold using cylindrical coordinates
to adjust every other vertex along the top radius of a cylinder.

.. figure:: /images/nodes-cylindrical_to_cartesian_basic.png
   :align: center
   :width: 800

   Using the cylindrical coordinates to construct a cupcake wrapper.
