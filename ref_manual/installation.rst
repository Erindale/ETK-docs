.. _getting-started-installation:

Installation
============

.. figure:: /images/install-pref_main.png
   :align: right

   Step 1: Open the ``Preferences`` dialog.

The add-on can be installed like any other Blender add-on. To install
simply navigate to the Add-on Preferences window and click “Install”.
Then navigate to the |ETK_ZIPFILE| file and select “Install
Add-on”. Once installed, be sure to enable the addon.

The way we’ve made the addon means that it will import all the nodes
when you open Blender, start a new file or load a file. This prevents
any duplicate data-blocks being created so whenever you add a group
from the menu, it will be linked to all the others of the same type.

In the future we may be able to only import nodes as they’re required
but with this |ETK_VERSION| release, this is how we’re doing it (There are
complications with multi-layer groups which will be resolved in future
updates thanks to additional nodes in Blender 3.X).

.. figure:: /images/install-pref_addons.png
   :align: center

   Step 2: Select ``Add-ons`` from the left panel then ``Install``.

.. figure:: /images/install-pref_addon_install.png
   :align: center

   Step 3: Navigate to the downloaded zip file, select and press
   ``Install Add-on``.

.. figure:: /images/install-pref_addon_enable.png
   :align: center

   Step 4: Be sure to enable the addon after the installation.
