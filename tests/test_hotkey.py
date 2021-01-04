# -*- coding: utf-8 -*-

import pytest
from hotkeynet.script import Hotkey, Key, SendLabel, Command
from hotkeynet import keyname


test_dump_result_1 = """
<Hotkey ScrollLockOn Space>
    <SendLabel w1>
        <Key Numpad1>
        <Key 1>
    <SendLabel w2>
        <Key Numpad2>
        <Key 2>
    <Key 3>
""".strip()


test_dump_result_2 = """
<Hotkey ScrollLockOn Space>
    <TestCommand>
""".strip()


class TestHotkey:
    def test_title(self):
        hk = Hotkey(
            name="Test",
            key=keyname.SCROLOCK_ON(keyname.KEY_1)
        )
        assert hk.title == "<Hotkey ScrollLockOn 1>"

    def test_dump(self):
        hk = Hotkey(
            name="Test",
            key=keyname.SCROLOCK_ON(keyname.SPACE),
            actions=[
                SendLabel(
                    to=["w1",],
                    actions=[
                        Key(keyname.NUMPAD_1),
                        Key(keyname.KEY_1),
                    ]
                ),
                SendLabel(
                    to=["w2",],
                    actions=[
                        Key(keyname.NUMPAD_2),
                        Key(keyname.KEY_2),
                    ]
                ),
                "<Key 3>"
            ]
        )
        assert hk.dump().strip() == test_dump_result_1

        cmd = Command(
            name="TestCommand",
            content=""
        )
        hk = Hotkey(
            name="Test",
            key=keyname.SCROLOCK_ON(keyname.SPACE),
            actions=[
                cmd.call(),
            ]
        )

        assert hk.dump().strip() == test_dump_result_2


if __name__ == "__main__":
    import os

    basename = os.path.basename(__file__)
    pytest.main([basename, "-s", "--tb=native"])
