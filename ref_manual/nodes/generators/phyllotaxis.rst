.. index:: Generators; Phyllotaxis
.. _etk.generators.phyllotaxis:

************
 Phyllotaxis
************

.. figure:: /images/nodes-phyllotaxis.png
   :align: right

   The ETK_Phyllotaxis node.

The PHYLLOTAXIS group is great. Thanks to Benny Govaerts for
recommending I make this. Phyllotaxic spirals are the way that plants
arrange leaves up a stem, or sunflower seeds on the flower head, or
pine cone scales and many others. You can get some really beautiful
arrangements with this group.


Inputs
=======

|INTEGER_SINGLE| Vertices
   Integer value for the total number of vertices.

|FLOAT_FIELD_SINGLE| Angle
   The angle in degrees that each point is offset by 137.5° by
   default.

|FLOAT_FIELD_SINGLE| Radius
   The radius of the phyllotaxis.

|FLOAT_FIELD_SINGLE| Expand
   The ratio of the radius by which to push out the centre points.

|FLOAT_FIELD_SINGLE| Depth
   The height of the phyllotaxis.

|FLOAT_FIELD_SINGLE| Exponent
   To control the curve of the depth value.


Outputs
========

|GEOMETRY| Geometry
   The generated geometry.

|INTEGER_SINGLE| Size
   The total number of points generated.

|FLOAT_FIELD| Falloff
   A gradient from 0-1 starting at the centre and reaching 1 at the
   outer- most point. Useful for controlling scale / rotation of
   points.

|VECTOR_FIELD| Rotation
   Exposes the rotation vector for each vertex.


Example Usage
==============

.. figure:: /images/nodes-phyllotaxis_basic.png
   :align: center
   :width: 800

   A **Phyllotaxis** group node used to instantiate 200 cubes.
