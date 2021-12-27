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
#   Shift-a to insert a node
#   Enlarge as big as you can
#   Using Window/Save Screenshot(Editor), snap an image of the geometry
#      editor view containing the node
#   Save it to the default ~/Documents/screen.png
#
# In a separate terminal window,
#   Use this utility from the top of the documentation tree,
#   $ ./tools/nimage.py curve_attribute
#   ... presuming this is the "ETK_Curve Attribute" node.
#
# The image will be reduced to 300 pixels wide (and whatever height).
#

import argparse
import logging
import os
import os.path
import sys
import subprocess

def subArgs():
    parser = argparse.ArgumentParser(description='nimage args parsing')
    parser.add_argument('node',
                        help='Name of node in the screenshot'
                        )
    parser.add_argument('--screenshot',
                        default='~/Documents/screen.png',
                        help='source folder of rst files')
    parser.add_argument('--width',
                        default=300,
                        type=int,
                        help='width in pixels of output image')
    parser.add_argument('--image-folder',
                        default='./ref_manual/images',
                        help='image location')
    args = parser.parse_args()
    return args


def main(args):
    fnm = 'nodes-{0}.png'.format(args.node)
    screenshot = os.path.expanduser(args.screenshot)
    if os.path.exists(screenshot):
        outimage = os.path.join(args.image_folder, fnm)
        stat = subprocess.check_output(['convert',
                                        '-resize',
                                        '{0}x'.format(args.width),
                                        screenshot,
                                        outimage
                                        ])
        if stat == 0:
            logging.info('Image file created: %s' % outimage)
    else:
        logging.error('Missing file - %s' % screenshot)


if __name__ == "__main__":
    logger = logging.getLogger('nimage')
    logging.basicConfig(encoding='utf-8',
                        level=logging.DEBUG,
                        format='%(levelname)s %(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %I:%M:%S',
                        )
    args = subArgs()
    main(args)

    sys.exit(0)
