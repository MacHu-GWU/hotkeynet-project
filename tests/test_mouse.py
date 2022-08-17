# -*- coding: utf-8 -*-

import pytest
from hotkeynet import keyname
from hotkeynet.script import Mouse


class TestMouse:
    def test_dump(self):
        assert Mouse(button=keyname.MOUSE_LButton).dump() == "<ClickMouse LButton>"
        assert Mouse(button=keyname.MOUSE_LButton, restore="NoRestore").dump() == "<ClickMouse LButton NoRestore>"


if __name__ == "__main__":
    import os

    basename = os.path.basename(__file__)
    pytest.main([basename, "-s", "--tb=native"])
