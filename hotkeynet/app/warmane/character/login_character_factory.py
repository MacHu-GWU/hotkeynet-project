# -*- coding: utf-8 -*-


from ordered_set import OrderedSet
from hotkeynet.game.wow.wlk import (
    Character,
    char_oset_helper,
)

from .character_factory import char_group


class LoginCharactersFactory:
    @property
    def group_core_10p(self) -> OrderedSet[Character]:
        return char_oset_helper.set_inactive(
            OrderedSet.union(
                char_group.window_1_to_9_batlefury_to_glowyy,
                char_group.window_10_luxiaofeng,
            )
        )

    @property
    def group_core_6p_alchemy_transmute(self) -> OrderedSet[Character]:
        return char_oset_helper.set_inactive(
            OrderedSet.union(
                char_group.window_1_to_5_batlefury_to_kangliu,
                char_group.window_6_angorarabbit,
            )
        )

    @property
    def group_14p_litgugu_abcd(self) -> OrderedSet[Character]:
        return char_oset_helper.set_inactive(
            OrderedSet.union(
                char_group.window_1_to_9_batlefury_to_glowyy,
                char_group.window_10_luxiaofeng,
                char_group.window_11_to_14_litgugu_abcd,
            )
        )

    @property
    def group_14p_litgugu_efgh(self) -> OrderedSet[Character]:
        return char_oset_helper.set_inactive(
            OrderedSet.union(
                char_group.window_1_to_9_batlefury_to_glowyy,
                char_group.window_10_luxiaofeng,
                char_group.window_11_to_14_litgugu_efgh,
            )
        )

    @property
    def group_22p_litgugu_abcd(self) -> OrderedSet[Character]:
        return char_oset_helper.set_inactive(
            OrderedSet.union(
                char_group.window_1_to_9_batlefury_to_glowyy,
                char_group.window_10_luxiaofeng,
                char_group.window_11_to_14_litgugu_abcd,
                char_group.window_15_to_18_lgms_ijkl,
                char_group.window_19_to_22_lgsm_mnop,
            )
        )

    @property
    def group_22p_litgugu_efgh(self) -> OrderedSet[Character]:
        return char_oset_helper.set_inactive(
            OrderedSet.union(
                char_group.window_1_to_9_batlefury_to_glowyy,
                char_group.window_10_luxiaofeng,
                char_group.window_11_to_14_litgugu_efgh,
                char_group.window_15_to_18_lgms_ijkl,
                char_group.window_19_to_22_lgsm_mnop,
            )
        )


login_char_fact = LoginCharactersFactory()
