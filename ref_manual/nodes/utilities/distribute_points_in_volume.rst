.. index:: Utilities; Distribute Points in Volume
.. _etk-utilities-distribute_points_in_volume:

****************************
 Distribute Points in Volume
****************************

.. figure:: /images/nodes-distribute_points_in_volume.png
   :align: right

   The ETK_Distribute Points in Volume node.

The **ETK_Distribute Points in Volume** group generates and
distributes points within a geometry.


Inputs
=======

|GEOMETRY| Mesh
   The input mesh.

|BOOLEAN_FIELD_SINGLE| Selection

|FLOAT| Density

|FLOAT_FIELD_SINGLE| Density Factor

|FLOAT_FIELD_SINGLE| Randomise

|INTEGER_FIELD_SINGLE| Seed
   The seed for randomisation.

|BOOLEAN_FIELD_SINGLE| Fast / Accurate

|INTEGER| Accuracy

|BOOLEAN_FIELD_SINGLE| Backface Check
   Check to perform additional backface checking. This may be
   necessary on more complex geometry.


Outputs
========

|GEOMETRY| Points
   The distributed points.

Examples
========

.. todo:: Add example for ETK_Distribute Points in Volume
