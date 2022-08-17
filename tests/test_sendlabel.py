# -*- coding: utf-8 -*-

import pytest

from hotkeynet import keyname
from hotkeynet.script import SendLabel, Key
from hotkeynet.utils import remove_indent


class TestSendLabel:
    def test_dump_indent(self):
        sl = SendLabel(
            to=["w1", "w2"],
            actions=[
                Key(name=keyname.KEY_1),
                "<Key 2>",
            ]
        )
        assert sl.dump() == remove_indent("""
        <SendLabel w1, w2>
            <Key 1>
            <Key 2>
        """)

    def test_dump_edge_case_no_target(self):
        sl = SendLabel(
            actions=[Key(name=keyname.KEY_1)],
        )
        assert sl.dump() == ""

    def test_dump_edge_case_no_action(self):
        sl = SendLabel(
            to=["w1", "w2"],
        )
        assert sl.dump() == ""


if __name__ == "__main__":
    import os

    basename = os.path.basename(__file__)
    pytest.main([basename, "-s", "--tb=native"])
