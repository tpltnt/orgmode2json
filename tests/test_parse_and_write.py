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
