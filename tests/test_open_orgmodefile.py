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
    ofile = o2j.open_orgmodefile('tests/test.org')
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
        o2j.open_orgmodefile(23)


def test_filename2():
    """
    Test to handle non-existing file. This should fail with a
    FileNotFoundError.
    """
    o2j = Orgmode2json()
    with pytest.raises(FileNotFoundError):
        o2j.open_orgmodefile('foobar.baz')
