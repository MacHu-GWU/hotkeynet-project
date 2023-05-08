# -*- coding: utf-8 -*-

from hotkeynet import keyname as KN


def test():
    assert KN.CTRL_(KN.C) == "Ctrl C"
    assert KN.SHIFT_(KN.C) == "Shift C"
    assert KN.ALT_(KN.C) == "Alt C"
    assert KN.CTRL_ALT_(KN.C) == "Ctrl Alt C"
    assert KN.CTRL_SHIFT_(KN.C) == "Ctrl Shift C"
    assert KN.ALT_SHIFT_(KN.C) == "Alt Shift C"
    assert KN.CTRL_SHIFT_ALT(KN.C) == "Ctrl Shift Alt C"
    assert KN.SCROLOCK_ON(KN.C) == "ScrollLockOn C"
    assert KN.CAPSLOCK_ON(KN.C) == "CapsLockOn C"
    assert KN.LWIN_(KN.C) == "LWin C"
    assert KN.RWIN_(KN.C) == "RWin C"


if __name__ == "__main__":
    from hotkeynet.tests import run_cov_test

    run_cov_test(__file__, "hotkeynet.keyname", preview=False)
