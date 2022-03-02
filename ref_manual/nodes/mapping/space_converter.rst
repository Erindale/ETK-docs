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

.. rubric:: Navigating coordinate systems

This example presents a coordinate system sandbox for playing with
coordinate systems. The left-side variables are the resolution, Index
field, and the multiples of :math:`\pi` over the line resolution.

.. figure:: /images/nodes-space_converter_basic.png
   :align: center
   :width: 800

   Using the **Space Converter** to experiment with coordinate systems.

We setup a vector (the *Combine XYZ* node) as input into our **Space
Converter**. And feed it with the radius (*x*), polar angle |THETA|
(*y*), and azimuth angle |PHI| (*z*).

+-------------------------------------------------------+-------------------------------------------------------+-------------------------------------------------------+
| *Fixed radius*                                        | *Increasing radius*                                   | *Output to Cylindrical*                               |
+-------------------------------------------------------+-------------------------------------------------------+-------------------------------------------------------+
| .. figure:: /images/nodes-space_converter_basic_0.png | .. figure:: /images/nodes-space_converter_basic_1.png | .. figure:: /images/nodes-space_converter_basic_2.png |
+-------------------------------------------------------+-------------------------------------------------------+-------------------------------------------------------+

From left to right:

   * Fixed radius: the *x* input is masked to force it to a default of
     1M, creating a single iteration of the shape.

   * Increasing radius: the *x* input is un-masked so the radius is
     determined by :math:`index\over{resolution}`.

   * Output to cylindrical: input to the **Space Converter** is
     interpreted as spherical on input but output as cylindrical.
