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
See also :ref:`etk-mapping-cylindrical_to_cartesian`.

Inputs
=======

|VECTOR_FIELD_SINGLE| (x,y,z)
   The cartesian vector coordinates to convert.

Outputs
========

|FLOAT_FIELD_SINGLE| (r,θ,z)
   The converted cylindrical coordinates, where
      * *r* is the axial radius, sometime annotated as ρ (rho), or the
        projection of the radius onto the XY plane.
      * θ is the rotational angle
      * and *z* is the elevation


Examples
========

.. figure:: /images/nodes-cartesian_cylindrical_basic.png
   :align: center
   :width: 800

   Using a sphere as input, the **Cartesian to Cylindrical** group is
   used to fake a bevel by clamping Z and constraining the radius
   before converting back to cartesian coordinates.
