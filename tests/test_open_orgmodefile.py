import sys
sys.path.append('../orgmode2json')
import pytest
from orgmode2json import *


def test_filename1():
    """
    Test to handle non-string (int) as filename. This should fail with a
    TypeError.
    """
    o2j = Orgmode2json()
    with pytest.raises(TypeError):
        o2j.open_orgmodefile(23)
