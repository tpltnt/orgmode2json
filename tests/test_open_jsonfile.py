import sys
sys.path.append('../orgmode2json')
import pytest
from io import IOBase
from orgmode2json import *


def test_filename0():
    """
    Test to handle a valid filename. This should return a file object and not
    cause any trouble.
    """
    o2j = Orgmode2json()
    ofile = o2j.open_jsonfile('tests/test.json')
    if not isinstance(ofile, IOBase):
        pytest.fail("no file object returned")
    ofile.close()


def test_filename1():
    """
    Test to handle non-string (int) as filename. This should fail with a
    TypeError.
    """
    o2j = Orgmode2json()
    with pytest.raises(TypeError):
        o2j.open_jsonfile(23)
