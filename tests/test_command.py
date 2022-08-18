# # -*- coding: utf-8 -*-
#
# import pytest
#
# from hotkeynet import keyname
# from hotkeynet.script import Command, Key
# from hotkeynet.utils import remove_indent
#
# class TestCommand:
#     def test_title(self):
#         cmd = Command("MyCommand")
#         assert cmd.title == "<Command MyCommand>"
#
#     def test_call(self):
#         cmd = Command("MyCommand")
#         assert cmd.call() == "<MyCommand>"
#         assert cmd.call("arg1", "arg2") == "<MyCommand arg1 arg2>"
#
#     def test_dump_indent(self):
#         cmd = Command(
#             "MyCommand",
#             actions=[
#                 Key(name=keyname.KEY_1),
#                 "<Key 2>",
#             ],
#         )
#         assert cmd.dump() == remove_indent("""
#         <Command MyCommand>
#             <Key 1>
#             <Key 2>
#         """)
#
#
# if __name__ == "__main__":
#     import os
#
#     basename = os.path.basename(__file__)
#     pytest.main([basename, "-s", "--tb=native"])
