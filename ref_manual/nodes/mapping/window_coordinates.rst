.. index:: Mapping; Window Coordinates
.. _etk-mapping-window_coordinates:

*******************
 Window Coordinates
*******************

.. figure:: /images/nodes-window_coordinates.png
   :align: right

   The ETK_Window Coordinates node.

The **Window Coordinates** group provides a coordinate system that are
fixed to a Camera object's field of view.


Inputs
=======

|OBJECT| Camera
   The camera object onto which the window coordinates will be fixed.

|FLOAT_FIELD_SINGLE| Camera FOV
   The field of view of the camera.

|INTEGER_FIELD_SINGLE| Resolution X
   Camera resolution on the X-axis.

|INTEGER_FIELD_SINGLE| Resolution Y
   Camera resolution on the Y-axis.


Outputs
========

|VECTOR_FIELD| Vector
   The output window coordinate vector.


Examples
========

The better explanation of this node is in the video
`Every ETK Node <https://www.youtube.com/watch?v=57FaqP_Q36w&t=3789s>`_
which has an example applicable to textures.

.. rubric:: Window coordinates

A Gradient Texture node is used with window coordinates to drive a
linear gradient. This gradient is output from the node group and then
set on a Diffuse shader with the default name of *Material*.

.. figure:: /images/nodes-window_coordinates_basic.png
   :align: center
   :width: 800

   The **Window Coordinates** group used to drive a gradient.

A simple mesh Plane is used with the material set to our gradient
texture. With this setup we can animate the plane from left to right
within our camera view and show the results with the **Window
Coordinates** node group masked (left) and unmasked.

+----------------------------------------------------------+-----------------------------------------------------------+
|  .. figure:: /images/window-coordinates-basic-masked.gif | .. figure:: /images/window-coordinates-basic-unmasked.gif |
|     :align: center                                       |    :align: center                                         |
+----------------------------------------------------------+-----------------------------------------------------------+

Window coordinates project a simple UV coordinate system with
:math:`[0\ldots 1]` from left to right (U) and
:math:`[0\ldots 1]` from bottom to top (V). With the window coordinates
in use, the object's coordinate system is fixed to the field of view of the
camera object. Driving the gradient texture with the default object
coordinates will cause the texture to remain fixed to the object.
