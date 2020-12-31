# -*- coding: utf-8 -*-

import pytest
from hotkeynet.script import Command


test_dump_result_1 = """
<Command MyCommand>
    <Key 1>
""".strip()

class TestCommand:
    def test_call(self):
        cmd = Command("MyCommand", content="")
        assert cmd.call() == "<MyCommand>"
        assert cmd.call("arg1", "arg2") == "<MyCommand arg1 arg2>"

    def test_dump(self):
        cmd = Command("MyCommand", content="    <Key 1>")
        assert cmd.dump().strip() == test_dump_result_1.strip()


if __name__ == "__main__":
    import os

    basename = os.path.basename(__file__)
    pytest.main([basename, "-s", "--tb=native"])
