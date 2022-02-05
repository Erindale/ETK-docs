.. index:: Mapping; Space Converter
.. _etk-mapping-space_converter:

****************
 Space Converter
****************

.. figure:: /images/nodes-space_converter.png
   :align: right

   The ETK_Space Converter node.

The **Space Converter** group is the Swiss army knife of coordinate
converters that will convert between any of three coordinate systems.


Inputs
=======

|VECTOR_FIELD_SINGLE| Vector
   The input vector.

|INTEGER_FIELD_SINGLE| Cart|Cyl|Sp
   An enumerated value of 0, 1, or 2, that matches the input vector
   coordinate system,
   * 0, the default, cartesian coordinates
   * 1 cylindrical
   * 2 spherical

|INTEGER_FIELD_SINGLE| Cart|Cyl|Sp
   An enumerated value of 0, 1, or 2, to specify the output coordinate
   system.

Outputs
========

|VECTOR_FIELD_SINGLE| Vector
   The resulting output vector.


Examples
========

.. todo:: Add example for ETK_Space Converter
