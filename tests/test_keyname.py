# -*- coding: utf-8 -*-

import pytest

from hotkeynet import keyname


def test():
    _ = keyname.UP


def test_modifier():
    assert keyname.CTRL_(keyname.C) == "Ctrl C"
    assert keyname.ALT_(keyname.C) == "Alt C"
    assert keyname.SHIFT_(keyname.C) == "Shift C"

    assert keyname.CTRL_(keyname.C, keyname.V) == "Ctrl C, V"
    assert keyname.ALT_(keyname.C, keyname.V) == "Alt C, V"
    assert keyname.SHIFT_(keyname.C, keyname.V) == "Shift C, V"
    assert keyname.CTRL_ALT_(keyname.C, keyname.V) == "Ctrl Alt C, V"
    assert keyname.CTRL_SHIFT_(keyname.C, keyname.V) == "Ctrl Shift C, V"
    assert keyname.ALT_SHIFT_(keyname.C, keyname.V) == "Alt Shift C, V"

    assert keyname.CTRL_SHIFT_ALT(keyname.C, keyname.V) == "Ctrl Shift Alt C, V"


if __name__ == "__main__":
    import os

    basename = os.path.basename(__file__)
    pytest.main([basename, "-s", "--tb=native"])
