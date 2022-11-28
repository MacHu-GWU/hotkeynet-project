# -*- coding: utf-8 -*-

import typing as T

import attr
from attrs_mate import AttrsClass

import hotkeynet as hk
from hotkeynet import KN
from hotkeynet import utils
from hotkeynet.game.wow.wlk import (
    Character,
    Window,
    Talent as TL,
    TalentCategory as TC,
    char_oset_helper,
)

from . import act
from .icons import Icons

if T.TYPE_CHECKING:
    from .mode.base import Mode


@attr.s
class HknScript(AttrsClass):
    mode: 'Mode' = attr.ib(default=None)
    script: hk.Script = attr.ib(factory=hk.Script)

    def __attrs_post_init__(self):
        # 此时 Script 已经不再 context 中, 我们也不希望没定义一个 Hotkey 就一直用
        # with script 的语法. 所以我们手动将 script 对象设置为 Context 的顶层

        self.build_hk_group_10()
        self.build_hk_group_11_healbot()
        self.build_control_panel()

    # -------------------------------------------------------------------------
    # 实现使用图形界面上的按钮, 替代一些不常用, 或是紧急情况需要用到的快捷键,
    # 避免了记忆复杂快捷键的麻烦
    # -------------------------------------------------------------------------
    __anchor_control_panel = None

    # def build_control_panel(self):
    #     WIDTH = 36
    #     HEIGHT = 36
    #
    #     with hk.Command(name="AutoExec") as self.cmd_auto_exec:
    #         with hk.CreatePanel(name="MBControlPanel", x=0, y=60, width=120, height=960) as main_panel:
    #             def set_hotkey_or_command(
    #                 button,
    #                 hotkey: T.Optional[hk.Hotkey] = None,
    #                 command: T.Optional[hk.Command] = None,
    #                 command_args: T.Optional[tuple] = None,
    #             ):
    #                 if hotkey is not None:
    #                     hk.SetButtonHotkey(
    #                         button=button.name,
    #                         hotkey=hotkey,
    #                     )
    #                 if command is not None:
    #                     hk.SetButtonCommand(
    #                         button=button.name,
    #                         command=command,
    #                         args=command_args,
    #                     )
    #
    #             def create_button(
    #                 name: str,
    #                 text: str,
    #                 hotkey: T.Optional[hk.Hotkey] = None,
    #                 command: T.Optional[hk.Command] = None,
    #                 command_args: T.Optional[tuple] = None,
    #             ):
    #                 button = hk.CreateButton(
    #                     name=name,
    #                     x=0,
    #                     y=0,
    #                     width=WIDTH,
    #                     height=HEIGHT,
    #                     text=text,
    #                 )
    #                 hk.AddButtonToPanel(
    #                     button=button.name,
    #                     panel=main_panel.name,
    #                 )
    #                 set_hotkey_or_command(button, hotkey, command, command_args)
    #
    #             def create_picture_button(
    #                 name: str,
    #                 file: str,
    #                 hotkey: T.Optional[hk.Hotkey] = None,
    #                 command: T.Optional[hk.Command] = None,
    #                 command_args: T.Optional[tuple] = None,
    #             ):
    #                 button = hk.CreatePictureButton(
    #                     name=name,
    #                     x=0,
    #                     y=0,
    #                     file=file,
    #                 )
    #                 hk.AddButtonToPanel(
    #                     button=button.name,
    #                     panel=main_panel.name,
    #                 )
    #                 set_hotkey_or_command(button, hotkey, command, command_args)
    #
    #             def create_colored_button(
    #                 name: str,
    #                 bkcolor: str,
    #                 textcolor: str = "000000",
    #                 text: T.Optional[str] = None,
    #                 hotkey: T.Optional[hk.Hotkey] = None,
    #                 command: T.Optional[hk.Command] = None,
    #                 command_args: T.Optional[tuple] = None,
    #             ):
    #                 button = hk.CreateColoredButton(
    #                     name=name,
    #                     x=0,
    #                     y=0,
    #                     width=WIDTH,
    #                     height=HEIGHT,
    #                     bkcolor=f"0x{bkcolor}",
    #                     textcolor=f"0x{textcolor}",
    #                     text=text,
    #                 )
    #                 hk.AddButtonToPanel(
    #                     button=button.name,
    #                     panel=main_panel.name,
    #                 )
    #                 set_hotkey_or_command(button, hotkey, command, command_args)
    #
    #             create_picture_button(
    #                 name="ButtonA01",
    #                 file=Icons.wow,
    #                 command=self.cmd_launch_and_rename_all_game_client,
    #             )
    #
    #             create_picture_button(
    #                 name="ButtonA02",
    #                 file=Icons.log_in,
    #                 command=self.cmd_batch_login,
    #             )
    #
    #             create_picture_button(
    #                 name="ButtonA03",
    #                 file=Icons.resize_window,
    #                 command=self.cmd_center_overlap_layout,
    #             )
    #
    #             # -------------------------------------------------------------
    #             # Alt + Numpad 1 - 12
    #             # -------------------------------------------------------------
    #             create_colored_button(
    #                 name="ButtonBarAlt1To12a",
    #                 bkcolor="E75638",
    #                 text="Alt"
    #             )
    #             create_colored_button(
    #                 name="ButtonBarAlt1To12b",
    #                 bkcolor="E75638",
    #                 text="+Num"
    #             )
    #             create_colored_button(
    #                 name="ButtonBarAlt1To12c",
    #                 bkcolor="E75638",
    #                 text="1-12"
    #             )
    #
    #             create_picture_button(
    #                 name="Alt1",
    #                 file=Icons.ability_hunter_misdirection,
    #                 hotkey=self.hk_alt_numpad_1,
    #             )
    #             create_picture_button(
    #                 name="Alt2",
    #                 file=Icons.ability_mount_whitetiger,
    #                 hotkey=self.hk_alt_numpad_2,
    #             )
    #             create_picture_button(
    #                 name="Alt3",
    #                 file=Icons.ability_hunter_aspectoftheviper,
    #                 hotkey=self.hk_alt_numpad_3,
    #             )
    #             create_picture_button(
    #                 name="Alt4",
    #                 file=Icons.ability_druid_starfall,
    #                 hotkey=self.hk_alt_numpad_4,
    #             )
    #             create_picture_button(
    #                 name="Alt5",
    #                 file=Icons.spell_nature_wispheal,
    #                 hotkey=self.hk_alt_numpad_5,
    #             )
    #             create_picture_button(
    #                 name="Alt6",
    #                 file=Icons.spell_nature_bloodlust,
    #                 hotkey=self.hk_alt_numpad_6,
    #             )
    #             create_picture_button(
    #                 name="Alt7",
    #                 file=Icons.spell_holy_powerwordbarrier,
    #                 hotkey=self.hk_alt_numpad_7,
    #             )
    #             create_picture_button(
    #                 name="Alt8",
    #                 file=Icons.spell_holy_powerwordbarrier,
    #                 hotkey=self.hk_alt_numpad_8,
    #             )
    #             create_picture_button(
    #                 name="Alt9",
    #                 file=Icons.spell_holy_auramastery,
    #                 hotkey=self.hk_alt_numpad_9,
    #             )
    #             create_picture_button(
    #                 name="Alt10",
    #                 file=Icons.spell_nature_diseasecleansingtotem,
    #                 hotkey=self.hk_alt_numpad_10,
    #             )
    #             create_picture_button(
    #                 name="Alt11",
    #                 file=Icons.spell_nature_tremortotem,
    #                 hotkey=self.hk_alt_numpad_11,
    #             )
    #             create_picture_button(
    #                 name="Alt12",
    #                 file=Icons.spell_nature_strengthofearthtotem02,
    #                 hotkey=self.hk_alt_numpad_12,
    #             )
    #
    #             # -------------------------------------------------------------
    #             # Ctrl + Numpad 1 - 12
    #             # -------------------------------------------------------------
    #             create_colored_button(
    #                 name="ButtonBarCtrl1To12a",
    #                 bkcolor="E75638",
    #                 text="Ctrl"
    #             )
    #             create_colored_button(
    #                 name="ButtonBarCtrl1To12b",
    #                 bkcolor="E75638",
    #                 text="+Num"
    #             )
    #             create_colored_button(
    #                 name="ButtonBarCtrl1To12c",
    #                 bkcolor="E75638",
    #                 text="1-12"
    #             )
    #
    #             create_picture_button(
    #                 name="CtrlNumpad1",
    #                 file=Icons.ability_theblackarrow,
    #                 hotkey=self.hk_ctrl_numpad_1,
    #             )
    #             create_picture_button(
    #                 name="CtrlNumpad2",
    #                 file=Icons.spell_frost_iceshock,
    #                 hotkey=self.hk_ctrl_numpad_2,
    #             )
    #             create_picture_button(
    #                 name="CtrlNumpad3",
    #                 file=Icons.spell_holy_dispelmagic,
    #                 hotkey=self.hk_ctrl_numpad_3,
    #             )
    #             create_picture_button(
    #                 name="CtrlNumpad4",
    #                 file=Icons.spell_shadow_psychicscream,
    #                 hotkey=self.hk_ctrl_numpad_4,
    #             )
    #             create_picture_button(
    #                 name="CtrlNumpad5",
    #                 file=Icons.ability_druid_typhoon,
    #                 hotkey=self.hk_ctrl_numpad_5,
    #             )
    #             create_picture_button(
    #                 name="CtrlNumpad6",
    #                 file=Icons.spell_shaman_thunderstorm,
    #                 hotkey=self.hk_ctrl_numpad_6,
    #             )
    #             create_picture_button(
    #                 name="CtrlNumpad7",
    #                 file=Icons.spell_holy_divinehymn,
    #                 hotkey=self.hk_ctrl_numpad_7,
    #             )
    #             create_picture_button(
    #                 name="CtrlNumpad8",
    #                 file=Icons.spell_nature_tranquility,
    #                 hotkey=self.hk_ctrl_numpad_7,
    #             )
    #             create_picture_button(
    #                 name="CtrlNumpad9",
    #                 file=Icons.spell_nature_tranquility,
    #                 hotkey=self.hk_ctrl_numpad_7,
    #             )
    #             create_picture_button(
    #                 name="CtrlNumpad10",
    #                 file=Icons.spell_holy_symbolofhope,
    #                 hotkey=self.hk_ctrl_numpad_10,
    #             )
    #             create_picture_button(
    #                 name="CtrlNumpad11",
    #                 file=Icons.spell_holy_unyieldingfaith,
    #                 hotkey=self.hk_ctrl_numpad_11,
    #             )
    #             create_picture_button(
    #                 name="CtrlNumpad12",
    #                 file=Icons.spell_nature_shamanrage,
    #                 hotkey=self.hk_ctrl_numpad_12,
    #             )
    #
    #             # -------------------------------------------------------------
    #             # Shift + Numpad 1 - 9
    #             # -------------------------------------------------------------
    #             create_colored_button(
    #                 name="ButtonBarShift1To9a",
    #                 bkcolor="E75638",
    #                 text="Shift"
    #             )
    #             create_colored_button(
    #                 name="ButtonBarShift1To9b",
    #                 bkcolor="E75638",
    #                 text="+Num"
    #             )
    #             create_colored_button(
    #                 name="ButtonBarShift1To9c",
    #                 bkcolor="E75638",
    #                 text="1-9"
    #             )
    #
    #             hk.SetPanelLayout(
    #                 panel=main_panel.name,
    #                 row_length=3,
    #                 margin=1,
    #                 button_width=36,
    #                 button_height=36,
    #             )
    #
    #             hk.TargetWin(window=main_panel.name)
    #             hk.AlwaysOnTop()

    def build_control_panel(self):
        WIDTH = 24
        HEIGHT = 24

        with hk.Command(name="AutoExec") as self.cmd_auto_exec:
            with hk.CreatePanel(name="MBControlPanel", x=0, y=60, width=120, height=960) as main_panel:
                # Define three temp utility function
                def set_hotkey_or_command(
                    button,
                    hotkey: T.Optional[hk.Hotkey] = None,
                    command: T.Optional[hk.Command] = None,
                    command_args: T.Optional[tuple] = None,
                ):
                    if hotkey is not None:
                        hk.SetButtonHotkey(
                            button=button.name,
                            hotkey=hotkey,
                        )
                    if command is not None:
                        hk.SetButtonCommand(
                            button=button.name,
                            command=command,
                            args=command_args,
                        )

                def create_button(
                    name: str,
                    text: str,
                    hotkey: T.Optional[hk.Hotkey] = None,
                    command: T.Optional[hk.Command] = None,
                    command_args: T.Optional[tuple] = None,
                ):
                    button = hk.CreateButton(
                        name=name,
                        x=0,
                        y=0,
                        width=WIDTH,
                        height=HEIGHT,
                        text=text,
                    )
                    hk.AddButtonToPanel(
                        button=button.name,
                        panel=main_panel.name,
                    )
                    set_hotkey_or_command(button, hotkey, command, command_args)

                def create_picture_button(
                    name: str,
                    file: str,
                    hotkey: T.Optional[hk.Hotkey] = None,
                    command: T.Optional[hk.Command] = None,
                    command_args: T.Optional[tuple] = None,
                ):
                    button = hk.CreatePictureButton(
                        name=name,
                        x=0,
                        y=0,
                        file=file,
                    )
                    hk.AddButtonToPanel(
                        button=button.name,
                        panel=main_panel.name,
                    )
                    set_hotkey_or_command(button, hotkey, command, command_args)

                def create_colored_button(
                    name: str,
                    bkcolor: str,
                    textcolor: str = "000000",
                    text: T.Optional[str] = None,
                    hotkey: T.Optional[hk.Hotkey] = None,
                    command: T.Optional[hk.Command] = None,
                    command_args: T.Optional[tuple] = None,
                ):
                    button = hk.CreateColoredButton(
                        name=name,
                        x=0,
                        y=0,
                        width=WIDTH,
                        height=HEIGHT,
                        bkcolor=f"0x{bkcolor}",
                        textcolor=f"0x{textcolor}",
                        text=text,
                    )
                    hk.AddButtonToPanel(
                        button=button.name,
                        panel=main_panel.name,
                    )
                    set_hotkey_or_command(button, hotkey, command, command_args)

                create_picture_button(
                    name="ButtonLaunchAndRenameAllGameClient",
                    file=Icons.wow,
                    command=self.cmd_launch_and_rename_all_game_client,
                )

                create_picture_button(
                    name="ButtonBatchLogin",
                    file=Icons.log_in,
                    command=self.cmd_batch_login_and_enter_game,
                )

                create_picture_button(
                    name="ButtonResizeWindow",
                    file=Icons.resize_window,
                    command=self.cmd_center_overlap_layout,
                )

                create_picture_button(
                    name="ButtonLogOut",
                    file=Icons.log_out,
                    hotkey=self.hk_batch_logout,
                )

                create_picture_button(
                    name="ButtonVolumeDown",
                    file=Icons.vol_down,
                    hotkey=self.hk_volumn_down,
                )

                counter = 0
                index_mapper = dict()
                for window, account in self.mode.login_window_and_account_pairs:
                    index_mapper[window.index] = (window, account)
                for i in range(1, 1 + 25):
                    if i in index_mapper:
                        window, account = index_mapper[i]
                        create_button(
                            name=f"ButtonLogin{str(i).zfill(2)}",
                            text=window.label,
                            command=self.cmd_enter_username_and_password,
                            command_args=(
                                window.title,
                                account.username,
                                account.password,
                            )
                        )
                    else:
                        create_button(
                            name=f"ButtonLogin{str(i).zfill(2)}",
                            text="NA",
                        )

                create_picture_button(
                    name="RDFConfirmRoleAndEnterDungeon",
                    file=Icons.spell_holy_summonchampion,
                    hotkey=self.hk_rdf_confirm_role_and_enter_dungeon,
                )

                # -------------------------------------------------------------
                # Login
                # -------------------------------------------------------------
                # for self.mode.

                # -------------------------------------------------------------
                # Alt + Numpad 1 - 12
                # -------------------------------------------------------------
                for id, text in enumerate([
                    "Alt",
                    "+",
                    "Num",
                    "Pad",
                    "1-12",
                ], start=1):
                    create_colored_button(
                        name=f"ButtonBarAlt1To12B{id}",
                        bkcolor="E75638",
                        text=text
                    )

                create_picture_button(
                    name="Alt1",
                    file=Icons.ability_hunter_misdirection,
                    hotkey=self.hk_alt_numpad_1,
                )
                create_picture_button(
                    name="Alt2",
                    file=Icons.ability_mount_whitetiger,
                    hotkey=self.hk_alt_numpad_2,
                )
                create_picture_button(
                    name="Alt3",
                    file=Icons.ability_hunter_aspectoftheviper,
                    hotkey=self.hk_alt_numpad_3,
                )
                create_button(
                    name=f"Alt3B1",
                    text="NA",
                )
                create_button(
                    name=f"Alt3B2",
                    text="NA",
                )

                create_picture_button(
                    name="Alt4",
                    file=Icons.ability_druid_starfall,
                    hotkey=self.hk_alt_numpad_4,
                )
                create_picture_button(
                    name="Alt5",
                    file=Icons.spell_nature_wispheal,
                    hotkey=self.hk_alt_numpad_5,
                )
                create_picture_button(
                    name="Alt6",
                    file=Icons.spell_nature_bloodlust,
                    hotkey=self.hk_alt_numpad_6,
                )
                create_button(
                    name=f"Alt6B1",
                    text="NA",
                )
                create_button(
                    name=f"Alt6B2",
                    text="NA",
                )

                create_picture_button(
                    name="Alt7",
                    file=Icons.spell_holy_powerwordbarrier,
                    hotkey=self.hk_alt_numpad_7,
                )
                create_picture_button(
                    name="Alt8",
                    file=Icons.spell_holy_powerwordbarrier,
                    hotkey=self.hk_alt_numpad_8,
                )
                create_picture_button(
                    name="Alt9",
                    file=Icons.spell_holy_auramastery,
                    hotkey=self.hk_alt_numpad_9,
                )
                create_button(
                    name=f"Alt9B1",
                    text="NA",
                )
                create_button(
                    name=f"Alt9B2",
                    text="NA",
                )

                create_picture_button(
                    name="Alt10",
                    file=Icons.spell_nature_diseasecleansingtotem,
                    hotkey=self.hk_alt_numpad_10,
                )
                create_picture_button(
                    name="Alt11",
                    file=Icons.spell_nature_tremortotem,
                    hotkey=self.hk_alt_numpad_11,
                )
                create_picture_button(
                    name="Alt12",
                    file=Icons.spell_nature_strengthofearthtotem02,
                    hotkey=self.hk_alt_numpad_12,
                )
                create_button(
                    name=f"Alt12B1",
                    text="NA",
                )
                create_button(
                    name=f"Alt12B2",
                    text="NA",
                )

                # -------------------------------------------------------------
                # Ctrl + Numpad 1 - 12
                # -------------------------------------------------------------
                for id, text in enumerate([
                    "Ctrl",
                    "+",
                    "Num",
                    "Pad",
                    "1-12",
                ], start=1):
                    create_colored_button(
                        name=f"ButtonBarCtrl1To12B{id}",
                        bkcolor="E75638",
                        text=text
                    )

                create_picture_button(
                    name="CtrlNumpad1",
                    file=Icons.ability_theblackarrow,
                    hotkey=self.hk_ctrl_numpad_1,
                )
                create_picture_button(
                    name="CtrlNumpad2",
                    file=Icons.spell_frost_iceshock,
                    hotkey=self.hk_ctrl_numpad_2,
                )
                create_picture_button(
                    name="CtrlNumpad3",
                    file=Icons.spell_holy_dispelmagic,
                    hotkey=self.hk_ctrl_numpad_3,
                )
                create_button(
                    name=f"Ctrl3B1",
                    text="NA",
                )
                create_button(
                    name=f"Ctrl3B2",
                    text="NA",
                )

                create_picture_button(
                    name="CtrlNumpad4",
                    file=Icons.spell_shadow_psychicscream,
                    hotkey=self.hk_ctrl_numpad_4,
                )
                create_picture_button(
                    name="CtrlNumpad5",
                    file=Icons.ability_druid_typhoon,
                    hotkey=self.hk_ctrl_numpad_5,
                )
                create_picture_button(
                    name="CtrlNumpad6",
                    file=Icons.spell_shaman_thunderstorm,
                    hotkey=self.hk_ctrl_numpad_6,
                )
                create_button(
                    name=f"Ctrl6B1",
                    text="NA",
                )
                create_button(
                    name=f"Ctrl6B2",
                    text="NA",
                )

                create_picture_button(
                    name="CtrlNumpad7",
                    file=Icons.spell_holy_divinehymn,
                    hotkey=self.hk_ctrl_numpad_7,
                )
                create_picture_button(
                    name="CtrlNumpad8",
                    file=Icons.spell_nature_tranquility,
                    hotkey=self.hk_ctrl_numpad_7,
                )
                create_picture_button(
                    name="CtrlNumpad9",
                    file=Icons.spell_nature_tranquility,
                    hotkey=self.hk_ctrl_numpad_7,
                )
                create_button(
                    name=f"Ctrl9B1",
                    text="NA",
                )
                create_button(
                    name=f"Ctrl9B2",
                    text="NA",
                )

                create_picture_button(
                    name="CtrlNumpad10",
                    file=Icons.spell_holy_symbolofhope,
                    hotkey=self.hk_ctrl_numpad_10,
                )
                create_picture_button(
                    name="CtrlNumpad11",
                    file=Icons.spell_holy_unyieldingfaith,
                    hotkey=self.hk_ctrl_numpad_11,
                )
                create_picture_button(
                    name="CtrlNumpad12",
                    file=Icons.spell_nature_shamanrage,
                    hotkey=self.hk_ctrl_numpad_12,
                )
                create_button(
                    name=f"Ctrl12B1",
                    text="NA",
                )
                create_button(
                    name=f"Ctrl12B2",
                    text="NA",
                )

                # # -------------------------------------------------------------
                # # Shift + Numpad 1 - 9
                # # -------------------------------------------------------------
                # create_colored_button(
                #     name="ButtonBarShift1To9a",
                #     bkcolor="E75638",
                #     text="Shift"
                # )
                # create_colored_button(
                #     name="ButtonBarShift1To9b",
                #     bkcolor="E75638",
                #     text="+Num"
                # )
                # create_colored_button(
                #     name="ButtonBarShift1To9c",
                #     bkcolor="E75638",
                #     text="1-9"
                # )

                hk.SetPanelLayout(
                    panel=main_panel.name,
                    row_length=5,
                    margin=1,
                    button_width=24,
                    button_height=24,
                )

                hk.TargetWin(window=main_panel.name)
                hk.AlwaysOnTop()
