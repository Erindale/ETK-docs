.. _etk_nodes-falloff:

********
 Falloff
********

All of the Falloff group nodes work in a similar manner --- they take
a 0..1 input and apply a mathematical function to it. The result may
be greater than or less than 0. There are a number of interesting
application for these falloff nodes, particularly in animation.

.. _falloff_graph:

.. rubric:: Node group for Falloff examples

Instead of an example on each node, a graph of the function is
presented. The node group used to build the graph is presented here
for reference.

.. figure:: /images/nodes-falloff_graph.png
   :align: center
   :width: 800

   Using a mesh line in X, constrained between our desired 0..1 range,
   is used to demonstrate the **Falloff** group nodes.

.. toctree::
   :maxdepth: 1

   easing_back.rst
   easing_bounce.rst
   easing_circular.rst
   easing_elastic.rst
   easing_exponential.rst
   easing_mixer.rst
   easing_sine.rst
   easing+.rst
