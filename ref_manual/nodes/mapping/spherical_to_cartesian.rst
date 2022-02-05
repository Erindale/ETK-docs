.. index:: Mapping; Spherical to Cartesian
.. _etk-mapping-spherical_to_cartesian:

***********************
 Spherical to Cartesian
***********************

.. figure:: /images/nodes-spherical_to_cartesian.png
   :align: right

   The ETK_Spherical to Cartesian node.

The **Spherical to Cartesian** group converts between spherical and
cartesian coordinate systems.
See also :ref:`etk-mapping-cartesian_to_spherical`.


Inputs
=======

|FLOAT_FIELD_SINGLE| (r,θ,φ)
   The spherical coordinates to convert.

Outputs
========

|FLOAT_FIELD_SINGLE| (x,y,z)
   The cartesian coordinate results of conversion.

Examples
========


.. rubric:: Spherical coordinate display

Here the **Spherical to Cartesian** group is used to trace a portion
of a unit sphere. In all cases we use 1 for the radius and a **Field
Map Range** group to provide values for θ and φ in the range
:math:`0 .. {\pi\over{2}}` .

.. figure:: /images/nodes-spherical_to_cartesian_basic.png
   :align: center
   :width: 800

   Use the **Spherical to Cartesian** group to outline a portion of
   the unit sphere.
