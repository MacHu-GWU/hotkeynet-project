# -*- coding: utf-8 -*-

import os
from hotkeynet import keyname
from hotkeynet.script import Command, Hotkey, Key, SendLabel


# from hotkeynet.utils import remove_indent


class TestHotkey:
    # def test_title(self):
    #     hk = Hotkey(
    #         name="Test",
    #         key=keyname.SCROLOCK_ON(keyname.KEY_1)
    #     )
    #     assert hk.title == "<Hotkey ScrollLockOn 1>"

    # def test_render(self):
    #     cmd = Command(name="MyCommand")
    #
    #     hk = Hotkey(
    #         name="Test",
    #         key=keyname.SCROLOCK_ON(keyname.SPACE),
    #         actions=[
    #             SendLabel(
    #                 to=["w1", ],
    #                 actions=[
    #                     Key(keyname.NUMPAD_1),
    #                     Key(keyname.KEY_1),
    #                 ]
    #             ),
    #             SendLabel(
    #                 to=["w2", ],
    #                 actions=[
    #                     Key(keyname.NUMPAD_2),
    #                     Key(keyname.KEY_2),
    #                 ]
    #             ),
    #             CallCommand(cmd=cmd),
    #             cmd.call(),
    #             "<MyCommand>",
    #         ]
    #     )
    #     assert hk.dump().strip() == remove_indent("""
    #     <Hotkey ScrollLockOn Space>
    #         <SendLabel w1>
    #             <Key Numpad1>
    #             <Key 1>
    #         <SendLabel w2>
    #             <Key Numpad2>
    #             <Key 2>
    #         <MyCommand>
    #         <MyCommand>
    #         <MyCommand>
    #     """)

    def test_render_edge_case_no_sub_blocks(self):
        # just no sub block
        hk = Hotkey(
            key=keyname.KEY_1,
        )
        assert hk.render() == ""

        # has sub block, but all element in sub block is also empty
        hk = Hotkey(
            key=keyname.KEY_1,
            blocks=[
                SendLabel(
                    to=[],
                    blocks=[
                        Key(key=keyname.KEY_1)
                    ]
                )
            ]
        )
        assert hk.render() == ""


if __name__ == "__main__":
    import sys
    import subprocess

    abspath = os.path.abspath(__file__)
    dir_project_root = os.path.dirname(abspath)
    for _ in range(10):
        if os.path.exists(os.path.join(dir_project_root, ".git")):
            break
        else:
            dir_project_root = os.path.dirname(dir_project_root)
    else:
        raise FileNotFoundError("cannot find project root dir!")
    dir_htmlcov = os.path.join(dir_project_root, "htmlcov")
    bin_pytest = os.path.join(os.path.dirname(sys.executable), "pytest")

    args = [
        bin_pytest,
        "-s", "--tb=native", "-vv",
        f"--rootdir={dir_project_root}",
        "--cov=hotkeynet.script",
        "--cov-report", "term-missing",
        "--cov-report", f"html:{dir_htmlcov}",
        abspath,
    ]
    subprocess.run(args)
