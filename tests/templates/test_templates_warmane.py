# -*- coding: utf-8 -*-

import pytest
from pytest import raises, approx
from hotkeynet.templates import (
    warmane_5p_rdf,
)

def test():
    warmane_5p_rdf.script.dump()



if __name__ == "__main__":
    import os

    basename = os.path.basename(__file__)
    pytest.main([basename, "-s", "--tb=native"])
