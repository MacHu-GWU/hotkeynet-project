# -*- coding: utf-8 -*-

import pytest
from hotkeynet import keyname
from hotkeynet.script import Key, Mouse, SendLabel

test_dump_result = """
    <SendLabel w1, w2, w3>
        <Key 1>
        <Key 2>
        <Key 3>
""".strip()


class TestSendLabel:
    def test_dump(self):
        send_label = SendLabel(
            to=["w1", "w2", "w3"],
            actions=[
                Key(name=keyname.KEY_1),
                Key(name=keyname.KEY_2),
                Key(name=keyname.KEY_3),
            ]
        )
        assert send_label.dump().strip() == test_dump_result


if __name__ == "__main__":
    import os

    basename = os.path.basename(__file__)
    pytest.main([basename, "-s", "--tb=native"])
