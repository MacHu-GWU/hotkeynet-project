# -*- coding: utf-8 -*-


import pytest
from pytest import raises, approx
from hotkeynet.script import Command

class TestCommand:
    def test_call(self):
        cmd = Command("MyCommand", content="")
        assert cmd.call() == "<MyCommand>"
        assert cmd.call("arg1", "arg2") == "<MyCommand arg1 arg2>"

if __name__ == "__main__":
    import os

    basename = os.path.basename(__file__)
    pytest.main([basename, "-s", "--tb=native"])
