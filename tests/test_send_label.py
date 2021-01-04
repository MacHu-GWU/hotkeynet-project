# -*- coding: utf-8 -*-

import pytest
from hotkeynet.script import SendLabel, Key
from hotkeynet import keyname


class TestSendLabel:
    def test_normal_case(self):
        sl = SendLabel(
            to=["w1", "w2"],
            actions=[
                Key(name=keyname.KEY_1),
                "<Key 2>",
            ]
        )
        assert sl.dump() == "\n".join([
            "<SendLabel w1, w2>",
            "    <Key 1>",
            "    <Key 2>",
        ])

    def test_edge_case_no_target(self):
        sl = SendLabel(
            actions=[Key(name=keyname.KEY_1)],
        )
        assert sl.dump() == ""

    def test_edge_case_no_action(self):
        sl = SendLabel(
            to=["w1", "w2"],
        )
        assert sl.dump() == ""


if __name__ == "__main__":
    import os

    basename = os.path.basename(__file__)
    pytest.main([basename, "-s", "--tb=native"])
