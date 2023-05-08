# -*- coding: utf-8 -*-

import os
import typing as T

from rich import print

from hotkeynet.script import (
    context,
    Script,
    Label,
    Hotkey,
    SendLabel,
    Key,
)
from hotkeynet import keyname


def test_context():
    context.reset()
    assert len(context.stack) == 0
    script = Script()
    assert len(context.stack) == 0
    with script():
        assert len(context.stack) == 1
        assert context.current is script
        labels: T.List[Label] = list()
        for i in range(1, 1 + 5):
            labels.append(
                Label(name=f"w{i}", window=f"WoW{i}")
            )
            assert len(context.stack) == 1
            assert context.current is script

    with script():
        with Hotkey(
            id="Key1",
            key=keyname.SCROLOCK_ON(keyname.KEY_1),
        ) as hk_1:
            assert len(context.stack) == 2
            assert context.current is hk_1
            with SendLabel(
                name="",
                to=[label.name for label in labels],
            ) as hk_1_send_label:
                Key(key=keyname.KEY_1)

    with hk_1_send_label():
        assert len(context.stack) == 1
        assert context.current is hk_1_send_label
        Key(key=keyname.KEY_2)

    # print(my_script.script)

    assert len(script.blocks) == 5 + 1
    assert len(script.iter_label()) == 5
    assert len(script.iter_hotkey()) == 1

    assert isinstance(hk_1, Hotkey)
    assert len(hk_1.blocks) == 1

    assert isinstance(hk_1.blocks[0], SendLabel)
    assert len(hk_1.blocks[0].to) == 5
    assert len(hk_1.blocks[0].blocks) == 2

    assert isinstance(hk_1.blocks[0].blocks[0], Key)
    assert isinstance(hk_1.blocks[0].blocks[1], Key)


if __name__ == "__main__":
    from hotkeynet.tests import run_cov_test

    run_cov_test(__file__, "hotkeynet.script", preview=False)
