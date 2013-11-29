#!/usr/bin/env python3

"""
A pure python 3 script to parse `orgmode <http://orgmode.org/>`_ files and
spit out `JSON <http://wwww.json.org>`_. To this point it is mostly intended
to parse (tagged) notes. This work is licensed under the `GNU Affero General Public License v3 <https://www.gnu.org/licenses/agpl-3.0.en.html>`_.

.. moduleauthor:: tpltnt
"""
from io import TextIOWrapper
import sys

if 1 == len(sys.argv):
    print("usage:",sys.argv[0],"inputfile.org (outputfile.json)")
    print()
    print("if no output filename is give, the input (base) filename will be used")
    sys.exit(2)


orgmodefile = open(sys.argv[1], 'r')
if 3 == len(sys.argv):
    jsonfile = open(sys.argv[2], 'w')
if 2 == len(sys.argv):
    jsonfile = open(sys.argv[1].replace('.org','.json'), 'w')

if not isinstance(orgmodefile, TextIOWrapper):
    raise TypeError("orgmode file of wrong type")
if not isinstance(jsonfile, TextIOWrapper):
    raise TypeError("JSON file of wrong type")

orgmodefile.close()
jsonfile.close()
