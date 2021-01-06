# -*- coding: utf-8 -*-

import pytest
from hotkeynet import keyname
from hotkeynet.script import Hotkey, SendLabel, ModifiedMouseClick
from hotkeynet.utils import remove_indent

class TestModifiedMouseClick:
    def test_dump_minimal(self):
        assert ModifiedMouseClick.shift_left_click().dump() == remove_indent("""
        <KeyDown Shift>
        <ClickMouse LButton Down>
        <ClickMouse LButton Up>
        <KeyUp Shift>
        """)

    def test_dump_with_hotkey_and_send_label(self):
        hk = Hotkey(
            name="Test",
            key=keyname.SCROLOCK_ON(keyname.KEY_1),
            actions=[
                SendLabel(
                    to=["w1",],
                    actions=[
                        ModifiedMouseClick.shift_left_click(),
                    ]
                )
            ]
        )
        assert hk.dump() == remove_indent("""
        <Hotkey ScrollLockOn 1>
            <SendLabel w1>
                <KeyDown Shift>
                <ClickMouse LButton Down>
                <ClickMouse LButton Up>
                <KeyUp Shift>
        """)


if __name__ == "__main__":
    import os

    basename = os.path.basename(__file__)
    pytest.main([basename, "-s", "--tb=native"])
