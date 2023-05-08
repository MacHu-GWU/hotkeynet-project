# -*- coding: utf-8 -*-

from hotkeynet import keyname as KN

# from hotkeynet.maker import KeyMaker
from hotkeynet import canned


def test_resolve_key_liked_arg():
    assert canned._resolve_key_liked_arg(canned.KEY_1) == "1"
    assert canned._resolve_key_liked_arg(KN.KEY_1) == "1"


def test_key_with_modifier():
    assert canned.CTRL_(canned.KEY_1, KN.KEY_2)().key == "Ctrl 1, 2"
    assert canned.CTRL_ALT_(canned.KEY_1, KN.KEY_2)().key == "Ctrl Alt 1, 2"
    assert canned.CTRL_SHIFT_ALT(canned.KEY_1, KN.KEY_2)().key == "Ctrl Shift Alt 1, 2"
    assert canned.LWIN_(canned.KEY_1)().key == "LWin 1"
    assert canned.RWIN_(KN.KEY_1)().key == "RWin 1"

def test_modified_mouse_click():
    assert canned.MOUSE_LButton().button == "LButton"

    actions = canned.SHIFT_LEFT_CLICK()
    assert len(actions) == 4
    assert actions[0].__class__.__name__ == "KeyDown"
    assert actions[3].__class__.__name__ == "KeyUp"


if __name__ == "__main__":
    from hotkeynet.tests import run_cov_test

    run_cov_test(__file__, "hotkeynet.canned", preview=False)
