.. index:: Experimental; Marching Cubes
.. _etk-experimental-marching_cubes:

***************
 Marching Cubes
***************

.. figure:: /images/nodes-marching_cubes.png
   :align: right

   The ETK_Marching Cubes node.

The **ETK_Marching Cubes** group is a wrapper around Blender's
`Volume Cube <https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/volume/volume_cube.html>`_
and
`Volume to Mesh <https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/volume/volume_to_mesh.html>`_
node groups that provides an interface more convenient for creating an
`Isosurface <https://en.wikipedia.org/wiki/Isosurface>`_, defined by
a field input, within the given bounds.


From the wikimedia article on `Isosurface <https://en.wikipedia.org/wiki/Isosurface>`_,

   "The marching cubes algorithm [...] creates a surface by
   intersecting the edges of a data volume grid with the volume
   contour. Where the surface intersects the edge the algorithm
   creates a vertex. By using a table of different triangles depending
   on different patterns of edge intersections the algorithm can
   create a surface."

More information on marching cubes can be found in
the Wikipedia article on `marching cubes <https://en.wikipedia.org/wiki/Marching_cubes>`_.


Inputs
=======

|FLOAT_FIELD_SINGLE| Field
   Typically the value of a signed distance function (SDF) that
   defines hits at the vertices of each cube within the bounds.

|FLOAT| Threshold
   Voxels with a larger size are considered to be inside the mesh. The
   mesh will be generated on the boundary of inside and outside
   voxels. This is also called `iso value`.  [#vtm]_

|VECTOR| Bounds Min
   One corner of the rectangular prism in which to evaluate the field.

|VECTOR| Bounds Max
   The other corner of the rectangular prism in which to evaluate the
   field.

|FLOAT| Sample Size
   The size of the cube to sample.

|FLOAT| Voxel Size
   The voxel resolution.

|FLOAT| Adaptivity
   Reduces the final face count by simplifying geometry where detail
   is not needed. This is similar to decimating the final to reduce
   resolution where it is not needed. [#vtm]_

.. TIP::
   The *Bounds Min* and *-Max* along with the *Sample Size* form the
   resolution used by the algorithm to calculate hits. The *Voxel
   Size* and *Adaptivity* define the output characteristics.

.. CAUTION::
   Take care when setting the bounds values and the *Sample Size*.
   These two values together determine the number of cubes within the
   bounding cube and can easily stress memory.

Outputs
========

|GEOMETRY| Mesh
   Output mesh.


Examples
=========

.. todo:: Add example for ETK_Marching Cubes


------------

.. rubric:: Footnotes

.. [#vtm] Reprinted from `Volume to Mesh
       <https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/volume/volume_to_mesh.html>`_
       node.
