.. index:: Fields; Field Map Range F
.. _etk-fields-field_map_range_f:

******************
 Field Map Range F
******************

.. figure:: /images/nodes-field_map_range_f.png
   :align: right

   The ETK_Field Map Range F node.

The **Field Map Range F** group takes a float input field and maps
that value to a new result. See also :ref:`etk-fields-field_map_range_v`.


Inputs
=======

|GEOMETRY| Geometry
   The geometry to use for values to map.

|FLOAT_FIELD_SINGLE| Value
   The float field value to map.

|FLOAT_FIELD_SINGLE| To Min
   Use this value as a minimum for input *Value*.

|FLOAT_FIELD_SINGLE| To Max
   Use this value as a maximum for input *Value*.

Outputs
========

|FLOAT_FIELD_SINGLE| Result
   Field for mapped values.


Examples
========

.. rubric:: Profile curve radius mapping

Manipulating the radius of a curve makes an interesting example for
the **Field Map Range F** group. Consider a bezier segment with a
taper set along its length determined by the *Factor* output from a *Spline
Parameter*. The radius of *Curve Circle* used for the *Curve to Mesh*
node is influenced by the curve radius that we have set (0.1) so that without
mapping, that radius will range from :math:`[0.0\ldots 0.1]`.
This is shown in the left
image below (when the **Field Map Range F** group is masked.)

.. figure:: /images/nodes-field_map_range_f_basic_comp.png
   :align: center

   Before and after applying the **Field Map Range F** group node.

The right image, with the **Field Map Range F** unmasked, maps the
:math:`[0\ldots 1]` range provided by the factor to
:math:`[0.25\ldots 3.0]`. This range of values influences the radius of
the *Profile Curve* along the curve.

.. figure:: /images/nodes-field_map_range_f_basic.png
   :align: center
   :width: 800

   The **Field Map Range F** group used to alter the radius of a
   profile curve.
