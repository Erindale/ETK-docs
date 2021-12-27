#! /bin/env python3
#
# Walk through the ETK add-on json file (thank you) and build a
# starting document tree for sphinx.
#
# WARNING: Don't run this in the production doc tree that has existing
# RST files as it will over-write them.
#
# - Glen Larsen

import json
import os
import os.path
import sys

CURDIR = os.path.abspath(os.getcwd())

def chapter_heading(title):
    chapter = '*********************************'
    t = chapter[0:len(title) + 1]
    return '\n{0}\n {1}\n{2}\n\n'.format(t, title, t)

def section_heading(header):
    section = '================================'
    return '\n{0}\n{1}\n\n'.format(header, section[0:len(header) + 1])

def make_rst(top, node):
    title = node.removeprefix('ETK_')
    base = title.replace(' ', '_').lower()
    rst_fname = base + '.rst'
    with open(rst_fname, 'w') as rst:
        rst.write('.. index:: {0}; {1}\n'.format(top, title))
        rst.write('.. _etk.{0}.{1}:\n'.format(top.lower(), base))
        rst.write(chapter_heading(title))
        rst.write('.. figure:: /images/nodes-{0}.png\n'.format(base))
        rst.write('   :align: right\n\n')
        rst.write('   The {0} node.\n\n'.format(node))
        rst.write('.. todo:: {0} node description.\n\n'.format(node))
        rst.write(section_heading('Inputs'))
        rst.write('Input1\n   Description of Input1\n')
        rst.write(section_heading('Properties'))
        rst.write('This node has no properties\n')
        rst.write(section_heading('Outputs'))
        rst.write('Output1\n   Description of Output1\n')
        rst.write(section_heading('Example Usage'))
        rst.write('.. todo:: Add example for {0}\n'.format(node))
    return rst_fname

def main(argv):
    chapters = []
    for fname in argv:
        with open(fname) as etk:
            nodes = json.load(etk)
            for top in nodes:
                topdir = os.path.join(CURDIR, top.lower())
                chapters.append(os.path.basename(topdir))
                if not os.path.exists(topdir):
                    os.mkdir(topdir)
                os.chdir(topdir)
                sections = []
                for node in nodes[top]:
                    sections.append(make_rst(top, node))
                # Create a section-level index
                with open('index.rst', 'w') as idx:
                    idx.write('.. _etk_nodes-{0}:\n'.format(top.lower()))
                    idx.write(chapter_heading(top))
                    idx.write('.. todo:: {0} description\n\n'.format(top))
                    idx.write('.. toctree::\n')
                    idx.write('   :maxdepth: 1\n\n')
                    for section in sections:
                        idx.write('   {0}\n'.format(section))

    # Create a top-level index with all chapters
    with open(os.path.join(CURDIR, 'index.rst'), 'w') as idx:
        idx.write('.. _etk_nodes:\n')
        idx.write(chapter_heading('ETK Nodes'))
        idx.write('.. toctree::\n   :maxdepth: 2\n\n')
        for c in chapters:
            idx.write('   {0}/index.rst\n'.format(c))

if __name__ == "__main__":
    main(sys.argv[1:])
