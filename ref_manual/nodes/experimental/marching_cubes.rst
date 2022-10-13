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

.. rubric:: A simple sphere

.. figure:: /images/nodes-marching_cubes_eg1.png
   :align: right

   An SDF sphere with its wireframes.

The sphere is the canonical example of simple SDF. The function is the
distance from a point which is then subtracted from the desired
diameter.

Because marching cubes can be resource intensive, the default is
rather small. Note the changes from the default,

* The bounds in our example has been increased to a
  :math:`4\times{4}\times{4}` cube.

* Threshold = 0.0

* Sample Size = 0.1M

* Voxel Size = 0.06M

Recreating this example and playing with these values is very
instructive.

.. figure:: /images/nodes-marching_cubes_eg1_gn.png
   :align: center
   :width: 800

   Constructing a sphere using **Marching Cubes**.

.. rubric:: A cube

.. figure:: /images/nodes-marching_cubes_eg2.png
   :align: right

Making a cube can be a little more involved. We use the ``Absolute``
value of the ``Position`` vector, subtract to get the side length, then
determine the final SDF value using the *Maximum* value on each axis.

.. figure:: /images/nodes-marching_cubes_eg2_gn.png
   :align: center
   :width: 800

   Constructing a cube with the **Marching Cubes** group node.


.. rubric:: The coolness of marching cubes

.. figure:: /images/nodes-marching_cubes_eg3.png
   :align: right

   Merging two objects.

Once you have an object defined you can build other structures by
combining their respective SDF outputs. Here the sphere's center has
been offset and AND'ed with the cube using a ``Smooth Minimum`` math
operation on the output of the cube and sphere. Tweaking the
*Distance* in this node can have interesting effects.

The cube SDF is omitted in the node tree since it is shown above.

.. figure:: /images/nodes-marching_cubes_eg3_gn.png
   :align: center
   :width: 800

   Using a ``Smooth Minimum`` operation to do a boolean union of two
   SDF functions.


------------

.. rubric:: Footnotes

.. [#vtm] Reprinted from `Volume to Mesh
       <https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/volume/volume_to_mesh.html>`_
       node.
