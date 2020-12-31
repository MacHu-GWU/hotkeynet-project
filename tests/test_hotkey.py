# -*- coding: utf-8 -*-

import pytest
from hotkeynet.script import Hotkey
from hotkeynet import keyname

class TestHotkey:
    def test_title(self):
        hk = Hotkey(
            name="Test",
            key=keyname.SCROLOCK_ON(keyname.KEY_1)
        )
        assert hk.title == "<Hotkey ScrollLockOn 1>"


if __name__ == "__main__":
    import os

    basename = os.path.basename(__file__)
    pytest.main([basename, "-s", "--tb=native"])
