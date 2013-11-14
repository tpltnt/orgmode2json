import sys
sys.path.append('../orgmode2json')
import pytest
from io import TextIOWrapper
from orgmode2json import *


def test_parse_and_write0():
    """
    Test plain conversion.
    """
    o2j = Orgmode2json()
    jfile = o2j.open_jsonfile('tests/test.json')
    ofile = o2j.open_orgmodefile('tests/test.org')
    o2j.parse_and_write(ofile, jfile)
    ofile.close()
    jfile.close()


def test_parse_and_write1():
    """
    Test non-file-object (int) for orgmode-file.
    """
    o2j = Orgmode2json()
    jfile = o2j.open_jsonfile('tests/test.json')
    ofile = 5
    with pytest.raises(TypeError):
        o2j.parse_and_write(ofile, jfile)
    jfile.close()


def test_parse_and_write2():
    """
    Test non-file-object (int) for json-file.
    """
    o2j = Orgmode2json()
    jfile = 23
    ofile = o2j.open_orgmodefile('tests/test.org')
    with pytest.raises(TypeError):
        o2j.parse_and_write(ofile, jfile)
    ofile.close()


def test_parse_and_write3():
    """
    Test non-file-objects for files.
    """
    o2j = Orgmode2json()
    jfile = 23
    ofile = 42
    with pytest.raises(TypeError):
        o2j.parse_and_write(ofile, jfile)
