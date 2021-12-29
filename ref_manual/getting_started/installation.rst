.. _getting-started-installation:

Installation
============

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
