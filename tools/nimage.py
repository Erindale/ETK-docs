#! /usr/bin/env python3
# -*- utf-8 -*-

# nimage --- node image processing.
#
# Simplify, as best possible, the process of creating node images for
# the documentation. I've found no trivial way. This script is a
# front-end to imagemagick's convert utility that will copy a snapped
# node image to a fixed size in the sphinx-doc's image location.
#
# In Blender,
#   Open Blender and start a geometry node session
#   Shift-a to insert a one or more nodes
#   Enlarge as big as you can
#   Using Window/Save Screenshot(Editor), snap an image of the geometry
#      editor view containing the node
#   Save it to the default ~/Documents/screen.png
#
# In GIMP,
#    Open screen.png
#    Set view to 100%
#    Rectangle-select portion containing the node
#    Ctrl-C to select
#    Shift-Ctrl-V to create a new image with the selection
#    Shift-Ctrl-E to Export As ...
#    Name output in lower case, spaces as underscores (_)
#
# In a separate terminal window,
#   Use this utility from the top of the documentation tree,
#   $ ./tools/nimage.py curve_attribute
#   ... presuming this is the "ETK_Curve Attribute" node.
#
# The image will be reduced to 300 pixels wide (and whatever height).
#

import argparse
import os
import os.path
import pathlib
import subprocess
import sys

def subArgs():
    parser = argparse.ArgumentParser(description='nimage args parsing')
    parser.add_argument('--in-folder',
                        default='~/Documents/etk',
                        help='source folder of image files')
    parser.add_argument('--width',
                        default=300,
                        type=int,
                        help='width in pixels of output image')
    parser.add_argument('--out-folder',
                        default='./ref_manual/images',
                        help='output image location')
    args = parser.parse_args()
    return args


def main(args):
    imagepath = pathlib.Path(os.path.expanduser(args.in_folder))
    for image in list(imagepath.glob('./*.png')):
        base = 'nodes-{0}'.format(os.path.basename(image).replace('-','_'))
        outimage = os.path.join(args.out_folder, base)
        print('Converting {0} -> {1} '.format(image, base))
        subprocess.check_output(['convert',
                                 '-resize',
                                 '{0}x'.format(args.width),
                                 image,
                                 outimage
                                 ])

# MAIN
if __name__ == "__main__":
    args = subArgs()
    main(args)
    sys.exit(0)
