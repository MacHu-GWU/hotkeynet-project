# -*- coding: utf-8 -*-

import attr
from attrs_mate import AttrsClass

from hotkeynet.game.wow.wlk import coordinator

from .config import config


@attr.s
class GameClient(AttrsClass):
    """
    定义了你所使用的游戏客户端的详细信息. 以下坐标的单位都为 pixel, 像素.

    下面四个坐标是从整个桌面的视角看的绝对坐标:

    :param window_left_top_x: 游戏窗口左上角的 x 坐标
    :param window_left_top_y: 游戏窗口左上角的 y 坐标
    :param window_width: 游戏窗口的宽度
    :param window_height: 游戏窗口的高度

    下面的坐标都是从游戏客户端内看的相对坐标:

    :param wrong_password_pop_up_x: 输入错误的账号密码后的对话框的确认按钮的 x 坐标
    :param wrong_password_pop_up_y: 输入错误的账号密码后的对话框的确认按钮的 y 坐标
    :param username_input_box_x: 输入账号的文本框的 x 坐标
    :param username_input_box_y: 输入账号的文本框的 y 坐标
    :param log_out_button_x: 游戏内按 ESC 打开系统菜单后, 登出按钮 的 x 坐标
    :param log_out_button_y: 游戏内按 ESC 打开系统菜单后, 登出按钮 的 y 坐标
    :param exit_game_button_x: 游戏内按 ESC 打开系统菜单后, 退出游戏 的 x 坐标
    :param exit_game_button_y: 游戏内按 ESC 打开系统菜单后, 退出游戏 的 y 坐标
    :param return_to_game_button_x: 游戏内按 ESC 打开系统菜单后, 返回游戏 的 x 坐标
    :param return_to_game_button_y: 游戏内按 ESC 打开系统菜单后, 返回游戏 的 x 坐标
    :param pass_item_button_x: 游戏内按 roll 装备的弹出框的取消按钮的 x 坐标
    :param pass_item_button_1_y: 游戏内按 roll 装备的 1 号弹出框的取消按钮的 y 坐标
    :param pass_item_button_2_y: 游戏内按 roll 装备的 2 号弹出框的取消按钮的 y 坐标
    :param pass_item_button_3_y: 游戏内按 roll 装备的 3 号弹出框的取消按钮的 y 坐标
    :param pass_item_button_4_y: 游戏内按 roll 装备的 4 号弹出框的取消按钮的 y 坐标
    :param rdf_confirm_role_accept_button_x: RDS 排本时选择自己的角色的确认按钮的 x 坐标
    :param rdf_confirm_role_accept_button_y: RDS 排本时选择自己的角色的确认按钮的 y 坐标
    :param rdf_enter_dungeon_button_x: RDS 确认进入副本按钮的 x 坐标
    :param rdf_enter_dungeon_button_y: RDS 确认进入副本按钮的 y 坐标
    """
    wow_exe_path: str = attr.ib(default=config.wow_exe_path)

    window_left_top_x: int = attr.ib(default=None)
    window_left_top_y: int = attr.ib(default=None)
    window_width: int = attr.ib(default=None)
    window_height: int = attr.ib(default=None)
    wrong_password_pop_up_x: int = attr.ib(default=None)
    wrong_password_pop_up_y: int = attr.ib(default=None)
    username_input_box_x: int = attr.ib(default=None)
    username_input_box_y: int = attr.ib(default=None)
    log_out_button_x: int = attr.ib(default=None)
    log_out_button_y: int = attr.ib(default=None)
    exit_game_button_x: int = attr.ib(default=None)
    exit_game_button_y: int = attr.ib(default=None)
    return_to_game_button_x: int = attr.ib(default=None)
    return_to_game_button_y: int = attr.ib(default=None)
    pass_item_button_x: int = attr.ib(default=None)
    pass_item_button_1_y: int = attr.ib(default=None)
    pass_item_button_2_y: int = attr.ib(default=None)
    pass_item_button_3_y: int = attr.ib(default=None)
    pass_item_button_4_y: int = attr.ib(default=None)
    rdf_confirm_role_accept_button_x: int = attr.ib(default=None)
    rdf_confirm_role_accept_button_y: int = attr.ib(default=None)
    rdf_enter_dungeon_button_x: int = attr.ib(default=None)
    rdf_enter_dungeon_button_y: int = attr.ib(default=None)

    def _use_resolution(self, resolution: str) -> 'GameClient':
        keyword = f"_at_{resolution}"
        for attr in coordinator.__dict__:
            if keyword in attr:
                setattr(
                    self,
                    attr.replace(keyword, ""),
                    getattr(coordinator, attr)
                )
        return self

    def use_1920_1080_resolution(self):
        return self._use_resolution("1920_1080")

    def use_1600_900_resolution(self):
        return self._use_resolution("1600_900")

    def use_1176_664_resolution(self):
        return self._use_resolution("1176_664")
