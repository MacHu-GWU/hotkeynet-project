# -*- coding: utf-8 -*-

import pytest

from hotkeynet import keyname
from hotkeynet.script import Command, Hotkey, Key, SendLabel, CallCommand
from hotkeynet.utils import remove_indent


class TestHotkey:
    def test_title(self):
        hk = Hotkey(
            name="Test",
            key=keyname.SCROLOCK_ON(keyname.KEY_1)
        )
        assert hk.title == "<Hotkey ScrollLockOn 1>"

    def test_dump(self):
        cmd = Command(name="MyCommand")

        hk = Hotkey(
            name="Test",
            key=keyname.SCROLOCK_ON(keyname.SPACE),
            actions=[
                SendLabel(
                    to=["w1", ],
                    actions=[
                        Key(keyname.NUMPAD_1),
                        Key(keyname.KEY_1),
                    ]
                ),
                SendLabel(
                    to=["w2", ],
                    actions=[
                        Key(keyname.NUMPAD_2),
                        Key(keyname.KEY_2),
                    ]
                ),
                CallCommand(cmd=cmd),
                cmd.call(),
                "<MyCommand>",
            ]
        )
        assert hk.dump().strip() == remove_indent("""
        <Hotkey ScrollLockOn Space>
            <SendLabel w1>
                <Key Numpad1>
                <Key 1>
            <SendLabel w2>
                <Key Numpad2>
                <Key 2>
            <MyCommand>
            <MyCommand>
            <MyCommand>
        """)

    def test_dump_no_action(self):
        hk = Hotkey(
            name="Test",
            key=keyname.KEY_1,
        )
        assert hk.dump() == ""

        hk = Hotkey(
            name="Test",
            key=keyname.KEY_1,
            actions=[
                SendLabel(
                    to=[],
                    actions=[
                        Key(name=keyname.KEY_1)
                    ]
                )
            ]
        )
        assert hk.dump() == ""


if __name__ == "__main__":
    import os

    basename = os.path.basename(__file__)
    pytest.main([basename, "-s", "--tb=native"])
