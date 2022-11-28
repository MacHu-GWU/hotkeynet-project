# -*- coding: utf-8 -*-

"""
实现组队以及系统功能性的按键.
"""

import typing as T

import hotkeynet as hk
from hotkeynet import KN
from hotkeynet.game.wow.wlk import (
    Character,
    Window,
    Talent as TL,
    TalentCategory as TC,
    char_oset_helper,
)
from hotkeynet.app.wow.wlk.servers.acore import act

if T.TYPE_CHECKING:
    from .script import HknScript


class HotkeyGroup06PartyAndSystemMixin:
    def build_hk_confirm(self: "HknScript"):
        with hk.Hotkey(
            id="Confirm",
            key=KN.SCROLOCK_ON(KN.CTRL_(KN.Y)),
        ) as self.hk_confirm:
            with hk.SendLabel(
                id="all",
                to=self.mode.lbs_all,
            ):
                act.general.CONFIRM_MACRO_KEY_NUMPAD_5()

    def build_hk_leave_party(self: "HknScript"):
        with hk.Hotkey(
            id="LeaveParty",
            key=KN.SCROLOCK_ON(KN.CTRL_(KN.L)),
        ) as self.hk_leave_party:
            with hk.SendLabel(
                name="all",
                to=self.mode.lbs_all,
            ):
                act.general.LEAVE_PARTY_MACRO_KEY_ALT_END()

    def build_hk_all_pass_item(self: "HknScript"):
        """
        所有的角色放弃拾取物品.
        """
        with hk.Hotkey(
            id="All Pass Item",
            key=KN.SCROLOCK_ON(KN.CTRL_ALT_(KN.Q)),
        ) as self.hk_all_pass_item:
            with hk.SendLabel(
                id="pass_item_button",
                to=self.mode.lbs_all,
            ):
                hk.ClickMouse(button=KN.MOUSE_LButton).set_mode_as_x_y(
                    x=self.mode.game_client.pass_item_button_x,
                    y=self.mode.game_client.pass_item_button_1_y,
                )
                hk.ClickMouse(button=KN.MOUSE_LButton).set_mode_as_x_y(
                    x=self.mode.game_client.pass_item_button_x,
                    y=self.mode.game_client.pass_item_button_2_y,
                )
                hk.ClickMouse(button=KN.MOUSE_LButton).set_mode_as_x_y(
                    x=self.mode.game_client.pass_item_button_x,
                    y=self.mode.game_client.pass_item_button_3_y,
                )
                hk.ClickMouse(button=KN.MOUSE_LButton).set_mode_as_x_y(
                    x=self.mode.game_client.pass_item_button_x,
                    y=self.mode.game_client.pass_item_button_4_y,
                )

    def build_hk_volume_down(self: "HknScript"):
        with hk.Hotkey(
            id="Volume Down",
            key=KN.SCROLOCK_ON(KN.CTRL_SHIFT_ALT(KN.M)),
        ) as self.hk_volumn_down:
            with hk.SendLabel(
                id="all",
                to=self.mode.lbs_all,
            ):
                act.system.MASTER_VOLUME_DOWN()

    def build_hk_rdf_confirm_role_and_enter_dungeon(self: "HknScript"):
        with hk.Hotkey(
            id="RDFConfirmRoleAndEnterDungeon",
            key=KN.SCROLOCK_ON(KN.CTRL_SHIFT_ALT(KN.Y)),
        ) as self.hk_rdf_confirm_role_and_enter_dungeon:
            with hk.SendLabel(
                id="all",
                to=self.mode.lbs_all,
            ):
                hk.ClickMouse(button=KN.MOUSE_LButton).set_mode_as_x_y(
                    x=self.mode.game_client.rdf_confirm_role_accept_button_x,
                    y=self.mode.game_client.rdf_confirm_role_accept_button_y,
                )
                hk.ClickMouse(button=KN.MOUSE_LButton).set_mode_as_x_y(
                    x=self.mode.game_client.rdf_enter_dungeon_button_x,
                    y=self.mode.game_client.rdf_enter_dungeon_button_y,
                )

    def build_hk_group_06_party_and_system_mixin(self: "HknScript"):
        self.build_hk_confirm()
        self.build_hk_leave_party()
        self.build_hk_all_pass_item()
        self.build_hk_volume_down()
        self.build_hk_rdf_confirm_role_and_enter_dungeon()
