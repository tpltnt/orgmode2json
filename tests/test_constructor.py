import sys
sys.path.append('../orgmode2json')
import pytest
from orgmode2json import *


def test_empty_call():
    foo = Orgmode2json
