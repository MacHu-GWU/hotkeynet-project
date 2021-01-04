# -*- coding: utf-8 -*-

import pytest
from hotkeynet.script import Command, Key
from hotkeynet import keyname

class TestCommand:
    def test_call(self):
        cmd = Command("MyCommand", content="")
        assert cmd.call() == "<MyCommand>"
        assert cmd.call("arg1", "arg2") == "<MyCommand arg1 arg2>"

    def test_dump_indent(self):
        cmd = Command(
            "MyCommand",
            actions=[
                Key(name=keyname.KEY_1),
                "<Key 2>",
            ],
        )

        print(cmd.dump())
        # assert cmd.dump() == "\n".join([
        #     "<Command MyCommand>",
        #     "    <Key 1>",
        #     "    <Key 2>",
        # ])


if __name__ == "__main__":
    import os

    basename = os.path.basename(__file__)
    pytest.main([basename, "-s", "--tb=native"])
