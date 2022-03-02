.. index:: Mapping; Cartesian to Spherical
.. _etk-mapping-cartesian_to_spherical:

***********************
 Cartesian to Spherical
***********************

.. figure:: /images/nodes-cartesian_to_spherical.png
   :align: right

   The ETK_Cartesian to Spherical node.

The **Cartesian to Spherical** group converts cartesian vector
coordinates to spherical coordinates. Spherical coordinates are often
thought of as the 3D version of the polar coordinate system.

See also :ref:`etk-mapping-spherical_to_cartesian`.


Inputs
=======

|FLOAT_FIELD_SINGLE| (x, y, z)
   The cartesian coordinates to convert.

Outputs
========

|FLOAT_FIELD_SINGLE| (r, |THETA| , |PHI| )
   The resulting spherical coordinates [#]_ as a vector with,

      * Radial distance *r* (distance to origin.)
      * Polar angle |THETA| (angle with respect to the polar axis.)
      * Azimuthal angle |PHI| (angle of rotation from the initial meridian
        plane.)


Examples
========

See :ref:`etk-mapping-space_converter`
for one example of using the spherical coordinate system.

-----------

.. rubric:: Footnotes

.. [#] This is the `ISO 80000 2:2019
       <https://en.wikipedia.org/wiki/Spherical_coordinate_system>`_
       convention.
