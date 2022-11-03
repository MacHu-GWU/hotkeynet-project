# -*- coding: utf-8 -*-

"""
该模块枚举了我们可能会用到的魔兽世界客户端程序的配置.
"""

from hotkeynet.game.wow.wlk import coordinator
from hotkeynet.game.wow.wlk.game_client import GameClient
from .config import config


class GameClientFactory:
    """

    """

    def _use_resolution(self, resolution: str) -> 'GameClient':
        """
        一个工厂函数.
        """
        game_client = GameClient(
            wow_exe_path=config.wow_exe_path,
            locale=config.locale,
        )
        keyword = f"_at_{resolution}"
        for attr in coordinator.__dict__:
            if keyword in attr:
                setattr(
                    game_client,
                    attr.replace(keyword, ""),
                    getattr(coordinator, attr)
                )
        return game_client

    @property
    def resolution_1920_1080(self):
        return self._use_resolution("1920_1080")

    @property
    def resolution_1600_900(self):
        return self._use_resolution("1600_900")

    @property
    def resolution_1176_664(self):
        return self._use_resolution("1176_664")


game_client_fact = GameClientFactory()
