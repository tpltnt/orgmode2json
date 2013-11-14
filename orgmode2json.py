#!/usr/bin/env python3

"""
A pure python 3 class to parse `orgmode <http://orgmode.org/>`_ files and
spit out `JSON <http://wwww.json.org>`_. To this point it is mostly intended
to parse (tagged) notes. This work is licensed under the `GNU Affero General Public License v3 <https://www.gnu.org/licenses/agpl-3.0.en.html>`_.

.. moduleauthor:: tpltnt
"""
class Orgmode2json(object):
    """
    A pure python 3 class to parse `orgmode <http://orgmode.org/>`_ files and
    spit out `JSON <http://wwww.json.org>`_.

    .. moduleauthor:: tpltnt
    """
    from io import TextIOWrapper

    __orgmode_inputfile = None
    __json_outputfile = None

    def __init__(self):
        pass

    def open_orgmodefile(self, filename):
        """
        Open a orgmode file for reading. The file is identified by the given
        name.

        :param filename: name (path) of the file to open
        :type filename: str
        :returns: file object associated with the file
        :raises: TypeError
        """

        if not isinstance(filename,str):
            raise TypeError("given filename is not a string")

        __ofile = open(filename,'r')
        return __ofile


    def open_jsonfile(self, filename):
        """
        Open a JSON file for reading. The file is identified by the given
        name.

        :param filename: name (path) of the file to open
        :type filename: str
        :returns: file object associated with the file
        :raises: TypeError
        """

        if not isinstance(filename,str):
            raise TypeError("given filename is not a string")

        __ofile = open(filename,'w')
        return __ofile


    def parse_and_write(self, orgmodefile, jsonfile):
        """
        Parse the given orgmode-file and write into the given JSON file.

        :param orgmodefile:
        :type orgmodefile: io.TextIOWrapper
        :param jsonfile:
        :type jsonfile: io.TextIOWrapper
        :raises: TypeError
        """

        if not isinstance(orgmodefile, TextIOWrapper):
            raise TypeError("orgmode file of wrong type")
        if not isinstance(jsonfile, TextIOWrapper):
            raise TypeError("JSON file of wrong type")

        pass
