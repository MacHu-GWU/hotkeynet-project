# -*- coding: utf-8 -*-

import pytest
from hotkeynet import keyname
from hotkeynet.script import Key


class TestSendKey:
    def test_dump(self):
        assert Key(name=keyname.ALT_(keyname.KEY_1)).dump() == "<Key Alt 1>"


if __name__ == "__main__":
    import os

    basename = os.path.basename(__file__)
    pytest.main([basename, "-s", "--tb=native"])
