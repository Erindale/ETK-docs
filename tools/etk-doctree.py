#! /bin/env python3
#
# Walk through the ETK add-on json file (thank you) and build a
# document tree for sphinx.
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
    if os.path.exists(rst_fname):
        return ''
    with open(rst_fname, 'w') as rst:
        rst.write('.. index:: {0}; {1}\n'.format(top, title))
        rst.write('.. _etk-{0}-{1}:\n'.format(top.lower(), base))
        rst.write(chapter_heading(title))
        rst.write('.. figure:: /images/nodes-{0}.png\n'.format(base))
        rst.write('   :align: right\n\n')
        rst.write('   The {0} node.\n\n'.format(node))
        rst.write('The {0} group ...\n\n'.format(node))
        rst.write(section_heading('Inputs'))
        rst.write('Input1\n   Description of Input1\n')
        rst.write(section_heading('Outputs'))
        rst.write('Output1\n   Description of Output1\n')
        rst.write(section_heading('Examples'))
        rst.write('.. todo:: Add example for {0}\n'.format(node))
    return rst_fname

def main(argv):
    for fname in argv:
        with open(fname) as etk:
            nodes = json.load(etk)
            for top in nodes:
                topdir = os.path.join(CURDIR, 'nodes', top.lower())
                if not os.path.exists(topdir):
                    os.mkdir(topdir)
                os.chdir(topdir)
                sections = []
                for node in nodes[top]:
                    rst = make_rst(top, node)
                    if len(rst) > 0:
                        print(f"Created {rst}")
                        sections.append(rst)
                # append to TOC on new sections
                if len(sections) > 0:
                    with open('index.rst', 'a') as idx:
                        for section in sections:
                            idx.write('   {0}\n'.format(section))

if __name__ == "__main__":
    main(sys.argv[1:])
