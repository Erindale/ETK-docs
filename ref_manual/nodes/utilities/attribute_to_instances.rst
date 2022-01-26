.. index:: Utilities; Attribute to Instances
.. _etk-utilities-attribute_to_instances:

***********************
 Attribute to Instances
***********************

.. figure:: /images/nodes-attribute_to_instances.png
   :align: right

   The ETK_Attribute to Instances node.

The **Attribute to Instances** group transfers an attribute from one
geometry to set of instances. The result is realized geometry with the
new attribute.


Inputs
=======

|GEOMETRY| Instances
   Input geometry.

|GEOMETRY| Target
   The geometry holding the attribute to transfer.

|VECTOR_FIELD_SINGLE| Attribute
   The attribute to transfer to the instances.

|BOOLEAN_FIELD_SINGLE| Nearest Face / Nearest
   Select the mapping source of the attribute.


Outputs
========

|GEOMETRY| Real Geometry
   The realized geometry.

|VECTOR| Attribute
   The attribute field passed to output.


Examples
========

Basic example
-------------

A grid is created and translated (0.5,0.5,0.0) so the bottom left
position of the grid is at the origin. Cubes are instanced to this 6x6
grid and, using the original grid as the *Target* of the **Attribute
to Instances** group, the *Position* is transfered to the instances.
This position field is added to the **Group Output** and named *pos*.
In the shading editor that attribute is supplied across the surface of
the realized geometry.

.. figure:: /images/nodes-attribute_to_instance_basic.png
   :align: center
   :width: 800

   Using **Transfer to instances** to transfer grid positions to
   instances on the grid.
