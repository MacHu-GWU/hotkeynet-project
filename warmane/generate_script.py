# -*- coding: utf-8 -*-

from hotkeynet import Script, Command, Hotkey
from hotkeynet.templates import warmane


print(warmane.cmd_LaunchAndRenameWoW1ToWoW10.dump())

# WOW_EXE_PATH = r"D:\HSH\Games\WOW Private\Client\World of Warcraft 3.3.5 enUS (Warman wod models)\Wow.exe"
#
# cmd_LaunchAndRename = Command(
#     name="LaunchAndRename",
#     content=f"""
#         <SendPC %1%>
#             <Run "{WOW_EXE_PATH}">
#                 <RenameWin "World of Warcraft" %2%>
#     """
# )
#
# cmd_LaunchAndRenameWoW1ToWoW10 = Command()
#
#
#
# print(cmd_LaunchAndRename.call())

