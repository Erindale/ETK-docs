.. index:: Falloff; Easing Mixer
.. _etk-falloff-easing_mixer:

*************
 Easing Mixer
*************

.. figure:: /images/nodes-easing_mixer.png
   :align: right

   The ETK_Easing Mixer node.

The **Easing Mixer** group allows the user to mix transitions between
two falloff functions.


Inputs
=======

|FLOAT_FIELD| 0..1
   The input value in the range of 0..1.

|BOOLEAN_FIELD_SINGLE| Ease In
   Apply the function to the start of the range.

|BOOLEAN_FIELD_SINGLE| Ease Out
   Apply the function to the last half of the range.

|FLOAT_FIELD_SINGLE| Blend
   Blend between the two input functions.


Outputs
========

|FLOAT_FIELD_SINGLE| Value
   The output with the falloff function applied.


Example Usage
=============


Easing Sine in, Elastic out
---------------------------

By way of example, the two falloff functions,
:ref:`etk-falloff-easing_sine` and
:ref:`etk-falloff-easing_elastic` are mixed at 50%.

.. figure:: /images/nodes-easing_mixer_basic.png
   :align: center
   :width: 800

   Mix between Sine easing in and Elastic out.
