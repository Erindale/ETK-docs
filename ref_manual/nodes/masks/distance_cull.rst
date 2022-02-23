.. index:: Masks; Distance Cull
.. _etk-masks-distance_cull:

**************
 Distance Cull
**************

.. figure:: /images/nodes-distance_cull.png
   :align: right

   The ETK_Distance Cull node.

The **Distance Cull** group provides a mask based on the distance from
a target object.


Inputs
=======

|OBJECT| Object
   The control object on which the culling reacts. This is typically a
   camera or empty.

|FLOAT_FIELD_SINGLE| Distance
   The distance from *Object* that defines the boundary for culling.

|FLOAT_FIELD_SINGLE| Falloff
   This value determines the hardness of culling at the boundary edge.


Outputs
========

|BOOLEAN_FIELD| Inside
   True for objects inside the mask.

|BOOLEAN_FIELD| Outside
   True for objects outside the mask.

.. index:: Signed Distance Function; Distance Cull

|FLOAT_FIELD| SDF
   A signed distance function output that can be used for compares to
   achieve similar outputs, essentially, :math:`inside <= 0 < outside`.


Examples
========

.. rubric:: Inside / Outside

.. figure:: /images/distance-cull-basic-comp.gif
   :align: right

The animation on the right was created by using an Empty as the
distance culling *Object* and moving it over cubes distributed
randomly on a grid. The *Falloff* is set to a small value so the
mask retains most of its circular shape without a hard edge.

Two node groups are presented below, either will create the animation.
The first using the *Inside* output to set the blue material, the
second uses the *SDF* output and a compare function to achieve the
same result.

.. figure:: /images/nodes-distance_cull_basic.png
   :align: center
   :width: 800

   The **Distance Cull** node group used set material colors based on
   its *Inside* output.

.. figure:: /images/nodes-distance_cull_basic_sdf.png
   :align: center
   :width: 800

   Same as above but using the *SDF* output with a compare.
