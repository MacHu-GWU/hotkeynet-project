# -*- coding: utf-8 -*-

import typing as T

from rich import print
from hotkeynet.game.wow.wlk import (
    Talent as TL,
    TalentCategory as TC,
    Window,
    Character,
)

from .account import AccountEnum, AccountHelper


class CharacterFactory:
    """
    枚举出所有账号下的所有角色的所有天赋.

    例如 fatmulti1 中有这些角色.

    1. batlefury, 防骑, 惩戒, 需要创建 2 个函数
    2. litgoatdka, DK, 坦克 和 冰AOE, 需要创建 2 个函数
    3. litgoatssa, 术士, PvP, 需要创建 1 个函数

    这样我们可以通过调用这些 可以被搜索定位, 名字人类可理解 的函数方便的创建游戏角色的实例.
    """

    @classmethod
    def make_char_fatmulti1_batlefury_pve_protect_pala(cls) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti1.value,
            name="batlefury",
            talent=TL.paladin_pve_protect,
            window=Window.make(1),
        )

    @classmethod
    def make_char_fatmulti1_batlefury_pve_retri_pala(cls) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti1.value,
            name="batlefury",
            talent=TL.paladin_pve_retri,
            window=Window.make(1),
        )

    @classmethod
    def make_char_fatmulti2_quentin_pve_elemental_shaman(cls) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti2.value,
            name="quentin",
            talent=TL.shaman_pve_elemental,
            window=Window.make(2),
        )

    @classmethod
    def make_char_fatmulti2_quentin_pve_resto_shaman(cls) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti2.value,
            name="quentin",
            talent=TL.shaman_pve_resto,
            window=Window.make(2),
        )

    @classmethod
    def make_char_fatmulti3_opiitou_pve_balance_druid(cls) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti3.value,
            name="opiitou",
            talent=TL.druid_pve_balance,
            window=Window.make(3),
        )

    @classmethod
    def make_char_fatmulti3_opiitou_pve_bear_druid(cls) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti3.value,
            name="opiitou",
            talent=TL.druid_pve_resto,
            window=Window.make(3),
        )

    @classmethod
    def make_char_fatmulti4_swagsonic_pve_arcane_mage(cls) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti4.value,
            name="swagsonic",
            talent=TL.mage_pve_arcane,
            window=Window.make(4),
        )

    @classmethod
    def make_char_fatmulti4_swagsonic_pve_fire_mage(cls) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti4.value,
            name="swagsonic",
            talent=TL.mage_pve_fire,
            window=Window.make(4),
        )

    @classmethod
    def make_char_fatmulti5_kangliu_pve_shadow_priest(cls) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti5.value,
            name="kangliu",
            talent=TL.priest_pve_shadow,
            window=Window.make(5),
        )

    @classmethod
    def make_char_fatmulti5_kangliu_pve_disco_priest(cls) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti5.value,
            name="kangliu",
            talent=TL.priest_pve_disco,
            window=Window.make(5),
        )

    @classmethod
    def make_char_fitsheep_kindhearted_pve_demonology_warlock(cls) -> Character:
        return Character(
            account=AccountEnum.account_fitsheep.value,
            name="kindhearted",
            talent=TL.warlock_pve_demonology,
            window=Window.make(6),
        )

    @classmethod
    def make_char_fitsheep_kindhearted_pvp_destruction_warlock(cls) -> Character:
        return Character(
            account=AccountEnum.account_fitsheep.value,
            name="kindhearted",
            talent=TL.warlock_pvp_destruction,
            window=Window.make(6),
        )

    @classmethod
    def make_char_fitsheep_bordercollie_pve_shadow_priest(cls) -> Character:
        return Character(
            account=AccountEnum.account_fitsheep.value,
            name="bordercollie",
            talent=TL.priest_pve_shadow,
            window=Window.make(6),
        )

    @classmethod
    def make_char_fitsheep_bordercollie_pve_disco_priest(cls) -> Character:
        return Character(
            account=AccountEnum.account_fitsheep.value,
            name="bordercollie",
            talent=TL.priest_pve_disco,
            window=Window.make(6),
        )

    @classmethod
    def make_char_fatmulti6_kapacuk_pve_marksman_hunter(cls) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti6.value,
            name="kapacuk",
            talent=TL.hunter_pve_marksman,
            window=Window.make(7),
        )

    @classmethod
    def make_char_fatmulti6_kapacuk_pvp_beast_hunter(cls) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti6.value,
            name="kapacuk",
            talent=TL.hunter_pve_beast,
            window=Window.make(7),
        )

    @classmethod
    def make_char_fatmulti8_bunnysisters_pve_resto_druid(cls) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti8.value,
            name="bunnysisters",
            talent=TL.druid_pve_resto,
            window=Window.make(8),
        )

    @classmethod
    def make_char_fatmulti8_bunnysisters_pve_balance_druid(cls) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti8.value,
            name="bunnysisters",
            talent=TL.druid_pve_balance,
            window=Window.make(8),
        )

    @classmethod
    def make_char_fatmulti9_glowyy_pve_holy_pala(cls) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti9.value,
            name="glowyy",
            talent=TL.paladin_pve_holy,
            window=Window.make(9),
        )

    @classmethod
    def make_char_fatmulti9_glowyy_pve_protect_pala(cls) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti9.value,
            name="glowyy",
            talent=TL.paladin_pve_protect,
            window=Window.make(9),
        )

    @classmethod
    def make_char_fatmulti10_luxiaofeng_pve_blood_tank_dk(cls) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti10.value,
            name="luxiaofeng",
            talent=TL.dk_pve_blood_tank,
            window=Window.make(10),
        )

    @classmethod
    def make_char_fatmulti10_luxiaofeng_pve_unholy_tank_dk(cls) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti10.value,
            name="luxiaofeng",
            talent=TL.dk_pve_unholy_tank,
            window=Window.make(10),
        )

    @classmethod
    def make_char_monkey130_flydps_pve_blood_tank_dk(cls) -> Character:
        return Character(
            account=AccountEnum.account_monkey130.value,
            name="flydps",
            talent=TL.dk_pve_blood_tank,
            window=Window.make(10),
        )

    @classmethod
    def make_char_makun7551_ganjj_pve_blood_tank_dk(cls) -> Character:
        return Character(
            account=AccountEnum.account_makun7551.value,
            name="ganjj",
            talent=TL.dk_pve_blood_tank,
            window=Window.make(10),
        )

    @classmethod
    def make_char_makun7551_ganjj_pve_unholy_dps_dk(cls) -> Character:
        return Character(
            account=AccountEnum.account_makun7551.value,
            name="ganjj",
            talent=TL.dk_pve_unholy_dps,
            window=Window.make(10),
        )

    @classmethod
    def make_char_makun7551_ganjj_pve_unholy_dps_dk_at_window_22(cls) -> Character:
        return Character(
            account=AccountEnum.account_makun7551.value,
            name="ganjj",
            talent=TL.dk_pve_unholy_dps,
            window=Window.make(22),
        )

    @classmethod
    def make_char_makun7551_laoshou_protect_paladin(cls) -> Character:
        return Character(
            account=AccountEnum.account_makun7551.value,
            name="laoshou",
            talent=TL.paladin_pve_protect,
            window=Window.make(10),
        )

    @classmethod
    def make_char_makun7551_laoshou_retri_paladin(cls) -> Character:
        return Character(
            account=AccountEnum.account_makun7551.value,
            name="laoshou",
            talent=TL.paladin_pve_retri,
            window=Window.make(10),
        )

    @classmethod
    def make_char_makun7551_laoshou_protect_paladin_at_window_9(cls) -> Character:
        return Character(
            account=AccountEnum.account_makun7551.value,
            name="laoshou",
            talent=TL.paladin_pve_protect,
            window=Window.make(9),
        )

    @classmethod
    def make_char_makun7551_laoshou_retri_paladin_at_window_19(cls) -> Character:
        return Character(
            account=AccountEnum.account_makun7551.value,
            name="laoshou",
            talent=TL.paladin_pve_retri,
            window=Window.make(19),
        )

    @classmethod
    def make_char_freiliheng_stophealing_pve_blood_tank_dk(cls) -> Character:
        return Character(
            account=AccountEnum.account_freiliheng.value,
            name="stophealing",
            talent=TL.dk_pve_blood_tank,
            window=Window.make(10),
        )

    # --- litgoat ss
    @classmethod
    def make_char_fatmulti1_litgoatssa_pve_demo_warlock(cls) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti1.value,
            name="litgoatssa",
            talent=TL.warlock_pve_demonology,
            window=Window.make(1),
        )

    @classmethod
    def make_char_fatmulti2_litgoatssb_pve_demo_warlock(cls) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti2.value,
            name="litgoatssb",
            talent=TL.warlock_pve_demonology,
            window=Window.make(2),
        )

    @classmethod
    def make_char_fatmulti3_litgoatssc_pve_demo_warlock(cls) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti3.value,
            name="litgoatssc",
            talent=TL.warlock_pve_demonology,
            window=Window.make(3),
        )

    @classmethod
    def make_char_fatmulti4_litgoatssd_pve_demo_warlock(cls) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti4.value,
            name="litgoatssd",
            talent=TL.warlock_pve_demonology,
            window=Window.make(4),
        )

    @classmethod
    def make_char_fatmulti5_litgoatsse_pve_demo_warlock(cls) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti5.value,
            name="litgoatsse",
            talent=TL.warlock_pve_demonology,
            window=Window.make(5),
        )

    # --- litgoat dk
    @classmethod
    def make_char_fatmulti1_litgoatdka_pvp_frost_dk(cls) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti1.value,
            name="litgoatdka",
            talent=TL.dk_pvp_frost,
            window=Window.make(1),
        )

    @classmethod
    def make_char_fatmulti2_litgoatdkb_pvp_frost_dk(cls) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti2.value,
            name="litgoatdkb",
            talent=TL.dk_pvp_frost,
            window=Window.make(2),
        )

    @classmethod
    def make_char_fatmulti3_litgoatdkc_pvp_frost_dk(cls) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti3.value,
            name="litgoatdkc",
            talent=TL.dk_pvp_frost,
            window=Window.make(3),
        )

    @classmethod
    def make_char_fatmulti4_litgoatdkd_pvp_frost_dk(cls) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti4.value,
            name="litgoatdkd",
            talent=TL.dk_pvp_frost,
            window=Window.make(4),
        )

    @classmethod
    def make_char_fatmulti5_litgoatdke_pvp_frost_dk(cls) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti5.value,
            name="litgoatdke",
            talent=TL.dk_pvp_frost,
            window=Window.make(5),
        )

    @classmethod
    def make_char_fatmulti1_litgoatdka_pve_blood_dk(cls) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti1.value,
            name="litgoatdka",
            talent=TL.dk_pve_unholy_dps,
            window=Window.make(1),
        )

    @classmethod
    def make_char_fatmulti2_litgoatdkb_pve_unholy_dk(cls) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti2.value,
            name="litgoatdkb",
            talent=TL.dk_pve_unholy_dps,
            window=Window.make(2),
        )

    @classmethod
    def make_char_fatmulti3_litgoatdkc_pve_unholy_dk(cls) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti3.value,
            name="litgoatdkc",
            talent=TL.dk_pve_unholy_dps,
            window=Window.make(3),
        )

    @classmethod
    def make_char_fatmulti4_litgoatdkd_pve_unholy_dk(cls) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti4.value,
            name="litgoatdkd",
            talent=TL.dk_pve_unholy_dps,
            window=Window.make(4),
        )

    @classmethod
    def make_char_fatmulti5_litgoatdke_pve_unholy_dk(cls) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti5.value,
            name="litgoatdke",
            talent=TL.dk_pve_unholy_dps,
            window=Window.make(5),
        )

    # --- litgugu abcd
    @classmethod
    def make_char_fatmulti11_litgugua_pvp_balance_druid(cls) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti11.value,
            name="litgugua",
            talent=TL.druid_pvp_balance,
            window=Window.make(11),
        )

    @classmethod
    def make_char_fatmulti11_litgugua_pvp_resto_druid(cls) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti11.value,
            name="litgugud",
            talent=TL.druid_pvp_resto,
            window=Window.make(11),
        )

    @classmethod
    def make_char_fatmulti11_litgugua_pve_balance_druid(cls) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti11.value,
            name="litgugua",
            talent=TL.druid_pve_balance,
            window=Window.make(11),
        )

    @classmethod
    def make_char_fatmulti12_litgugub_pvp_balance_druid(cls) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti12.value,
            name="litgugub",
            talent=TL.druid_pvp_balance,
            window=Window.make(12),
        )

    @classmethod
    def make_char_fatmulti12_litgugub_pvp_resto_druid(cls) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti12.value,
            name="litgugub",
            talent=TL.druid_pvp_resto,
            window=Window.make(12),
        )

    @classmethod
    def make_char_fatmulti12_litgugub_pve_balance_druid(cls) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti12.value,
            name="litgugub",
            talent=TL.druid_pve_balance,
            window=Window.make(12),
        )

    @classmethod
    def make_char_fatmulti13_litguguc_pvp_balance_druid(cls) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti13.value,
            name="litguguc",
            talent=TL.druid_pvp_balance,
            window=Window.make(13),
        )

    @classmethod
    def make_char_fatmulti13_litguguc_pvp_resto_druid(cls) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti13.value,
            name="litguguc",
            talent=TL.druid_pvp_resto,
            window=Window.make(13),
        )

    @classmethod
    def make_char_fatmulti13_litguguc_pve_balance_druid(cls) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti13.value,
            name="litguguc",
            talent=TL.druid_pve_balance,
            window=Window.make(13),
        )

    @classmethod
    def make_char_fatmulti14_litgugud_pvp_balancce_druid(cls) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti14.value,
            name="litgugud",
            talent=TL.druid_pvp_balance,
            window=Window.make(14),
        )

    @classmethod
    def make_char_fatmulti14_litgugud_pvp_resto_druid(cls) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti14.value,
            name="litgugud",
            talent=TL.druid_pvp_resto,
            window=Window.make(14),
        )

    @classmethod
    def make_char_fatmulti14_litgugud_pve_balance_druid(cls) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti14.value,
            name="litgugud",
            talent=TL.druid_pve_balance,
            window=Window.make(14),
        )

    # --- litgugu e, f, g, h
    @classmethod
    def make_char_fatmulti15_litgugue_pvp_balance_druid(cls) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti15.value,
            name="litgugue",
            talent=TL.druid_pvp_balance,
            window=Window.make(11),
        )

    @classmethod
    def make_char_fatmulti16_litguguf_pvp_balance_druid(cls) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti16.value,
            name="litguguf",
            talent=TL.druid_pvp_balance,
            window=Window.make(12),
        )

    @classmethod
    def make_char_fatmulti17_litgugug_pvp_balance_druid(cls) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti17.value,
            name="litgugug",
            talent=TL.druid_pvp_balance,
            window=Window.make(13),
        )

    @classmethod
    def make_char_fatmulti18_litguguh_pvp_balance_druid(cls) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti18.value,
            name="litguguh",
            talent=TL.druid_pvp_balance,
            window=Window.make(14),
        )

    @classmethod
    def make_char_fatmulti18_litguguh_pvp_resto_druid(cls) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti18.value,
            name="litguguh",
            talent=TL.druid_pvp_resto,
            window=Window.make(14),
        )

    # --- lg ms i, j, k, l
    @classmethod
    def make_char_fatmulti19_lgmsi_pve_shadow_priest(cls) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti19.value,
            name="lgmsi",
            talent=TL.priest_pve_shadow,
            window=Window.make(15),
        )

    @classmethod
    def make_char_fatmulti19_lgmsi_pve_disco_priest(cls) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti19.value,
            name="lgmsi",
            talent=TL.priest_pve_disco,
            window=Window.make(15),
        )

    @classmethod
    def make_char_fatmulti20_lgmsj_pve_shadow_priest(cls) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti20.value,
            name="lgmsj",
            talent=TL.priest_pve_shadow,
            window=Window.make(16),
        )

    @classmethod
    def make_char_fatmulti20_lgmsj_pve_disco_priest(cls) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti20.value,
            name="lgmsj",
            talent=TL.priest_pve_disco,
            window=Window.make(16),
        )

    @classmethod
    def make_char_fatmulti21_lgmsk_pve_shadow_priest(cls) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti21.value,
            name="lgmsk",
            talent=TL.priest_pve_shadow,
            window=Window.make(17),
        )

    @classmethod
    def make_char_fatmulti21_lgmsk_pve_holy_priest(cls) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti21.value,
            name="lgmsk",
            talent=TL.priest_pve_holy,
            window=Window.make(17),
        )

    @classmethod
    def make_char_fatmulti22_lgmsl_pve_shadow_priest(cls) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti22.value,
            name="lgmsl",
            talent=TL.priest_pve_shadow,
            window=Window.make(18),
        )

    @classmethod
    def make_char_fatmulti22_lgmsl_pve_holy_priest(cls) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti22.value,
            name="lgmsl",
            talent=TL.priest_pve_holy,
            window=Window.make(18),
        )

    # --- lg sm m, n, o, p
    @classmethod
    def make_char_fatmulti23_lgsmm_pve_elemental_shaman(cls) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti23.value,
            name="lgsmm",
            talent=TL.shaman_pve_elemental,
            window=Window.make(19),
        )

    @classmethod
    def make_char_fatmulti23_lgsmm_pve_resto_shaman(cls) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti23.value,
            name="lgsmm",
            talent=TL.shaman_pve_resto,
            window=Window.make(19),
        )

    @classmethod
    def make_char_fatmulti24_lgsmn_pve_elemental_shaman(cls) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti24.value,
            name="lgsmn",
            talent=TL.shaman_pve_elemental,
            window=Window.make(20),
        )

    @classmethod
    def make_char_fatmulti24_lgsmn_pve_resto_shaman(cls) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti24.value,
            name="lgsmn",
            talent=TL.shaman_pve_resto,
            window=Window.make(20),
        )

    @classmethod
    def make_char_fatmulti25_lgsmo_pve_elemental_shaman(cls) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti25.value,
            name="lgsmo",
            talent=TL.shaman_pve_elemental,
            window=Window.make(21),
        )

    @classmethod
    def make_char_fatmulti25_lgsmo_pve_resto_shaman(cls) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti25.value,
            name="lgsmo",
            talent=TL.shaman_pve_resto,
            window=Window.make(21),
        )

    @classmethod
    def make_char_fatmulti26_lgsmp_pve_elemental_shaman(cls) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti26.value,
            name="lgsmp",
            talent=TL.shaman_pve_elemental,
            window=Window.make(22),
        )

    @classmethod
    def make_char_fatmulti26_lgsmp_pve_resto_shaman(cls) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti26.value,
            name="lgsmp",
            talent=TL.shaman_pve_resto,
            window=Window.make(22),
        )


class ActiveCharactersFactory:
    @classmethod
    def _set_5p_team_leader(cls, chars: T.List[Character]):
        if len(chars) != 5:
            raise ValueError("solo dungeon team has to be 5 member!")

        # find leader char window
        leader_char_window: T.Optional[Window] = None

        # try to find the leader if explicitly defined
        if leader_char_window is None:
            for char in chars:
                if char.is_tank1:
                    leader_char_window = char.window

        # try to find the leader if it is tank talent
        if leader_char_window is None:
            for char in chars:
                if TC.tank in char.talent.categories:
                    tank_char_window = char.window

        # try to find a plate char
        if leader_char_window is None:
            for char in chars:
                categories = char.talent.categories
                if (
                    TC.warrior in categories
                    or TC.dk in categories
                    or TC.paladin in categories
                ):
                    tank_char_window = char.window

        if leader_char_window is None:
            raise ValueError("you have to define at least one TANK or one Plate char")

        # set other char leader1 as the tank
        for char in chars:
            if char.window.label != leader_char_window.label:
                char.set_leader1_window(leader_char_window)

        return chars

    @classmethod
    def make_team_solo_dungeon_batlefury_quentin_opiitou_swagsonic_kangliu(cls) -> T.List[Character]:
        """
        主力 5 人组
        """
        return cls._set_5p_team_leader(chars=[
            CharacterFactory.make_char_fatmulti1_batlefury_pve_protect_pala().set_tank1().set_dr_pala1(),
            CharacterFactory.make_char_fatmulti2_quentin_pve_elemental_shaman(),
            CharacterFactory.make_char_fatmulti3_opiitou_pve_balance_druid(),
            CharacterFactory.make_char_fatmulti4_swagsonic_pve_arcane_mage(),
            CharacterFactory.make_char_fatmulti5_kangliu_pve_shadow_priest(),
        ])

    @classmethod
    def make_team_solo_dungeon_1_tank_3_dps_1_healer(cls) -> T.List[Character]:
        """
        该模式用于 1 个坦克 带着 3 个 DPS, 1 个治疗 打 5 人小副本.
        """
        return cls._set_5p_team_leader(chars=[
            # =================================================================
            # === Tank 部分 ===
            # --- Paladin
            # CharacterFactory.make_char_fatmulti1_batlefury_pve_retri_pala().set_tank1(),
            CharacterFactory.make_char_fatmulti1_batlefury_pve_protect_pala().set_tank1().set_dr_pala1(),
            # CharacterFactory.make_char_fatmulti9_glowyy_pve_protect_pala().set_tank1().set_dr_pala1(),
            # CharacterFactory.make_char_makun7551_laoshou_retri_paladin().set_tank1().set_dr_pala1(),

            # --- DK
            # CharacterFactory.make_char_fatmulti10_luxiaofeng_pve_unholy_tank_dk().set_tank1(),
            # CharacterFactory.make_char_fatmulti1_litgoatdka_pve_blood_dk().set_tank1(),
            # CharacterFactory.make_char_makun7551_ganjj_pve_blood_tank_dk().set_tank1(),

            # --- Druid
            # CharacterFactory.make_char_fatmulti3_opiitou_pve_bear_druid().set_tank1(),

            # === DPS 部分 ===
            CharacterFactory.make_char_fatmulti11_litgugua_pve_balance_druid(),
            CharacterFactory.make_char_fatmulti12_litgugub_pve_balance_druid(),
            CharacterFactory.make_char_fatmulti13_litguguc_pve_balance_druid(),

            # CharacterFactory.make_char_fatmulti15_litgugue_pvp_balance_druid(),
            # CharacterFactory.make_char_fatmulti16_litguguf_pvp_balance_druid(),
            # CharacterFactory.make_char_fatmulti17_litgugug_pvp_balance_druid(),

            # === 治疗部分 ===
            # CharacterFactory.make_char_fatmulti8_bunnysisters_pve_resto_druid(),

            CharacterFactory.make_char_fatmulti14_litgugud_pvp_resto_druid(),

            # CharacterFactory.make_char_fatmulti18_litguguh_pvp_resto_druid(),
        ])

    # === 情人节 2 月中, 美酒节 9 月中, 万圣节 10 月中, 节日刷牌子 ===
    # 把 DK 5 人组 和 术士 5 人组 加上 Ganjj 和 Laoshou 分成 3 队 分别刷节日任务
    @classmethod
    def make_team_solo_dungeon_festival_team_1_dk(cls) -> T.List[Character]:
        return cls._set_5p_team_leader(chars=[
            CharacterFactory.make_char_fatmulti1_litgoatdka_pve_blood_dk().set_tank1(),
            CharacterFactory.make_char_fatmulti2_litgoatdkb_pve_unholy_dk(),
            CharacterFactory.make_char_fatmulti3_litgoatdkc_pve_unholy_dk(),
            CharacterFactory.make_char_fatmulti4_litgoatdkd_pve_unholy_dk(),
            CharacterFactory.make_char_fatmulti8_bunnysisters_pve_resto_druid(),
        ])

    @classmethod
    def make_team_solo_dungeon_festival_team_2_ss(cls) -> T.List[Character]:
        return cls._set_5p_team_leader(chars=[
            CharacterFactory.make_char_fatmulti3_litgoatssc_pve_demo_warlock(),
            CharacterFactory.make_char_fatmulti4_litgoatssd_pve_demo_warlock(),
            CharacterFactory.make_char_fatmulti5_litgoatsse_pve_demo_warlock(),
            CharacterFactory.make_char_makun7551_ganjj_pve_blood_tank_dk().set_tank1(),
            CharacterFactory.make_char_fatmulti13_litguguc_pvp_resto_druid(),
        ])

    @classmethod
    def make_team_solo_dungeon_festival_team_3_mix(cls) -> T.List[Character]:
        return cls._set_5p_team_leader(chars=[
            CharacterFactory.make_char_fatmulti1_litgoatssa_pve_demo_warlock(),
            CharacterFactory.make_char_fatmulti2_litgoatssb_pve_demo_warlock(),
            CharacterFactory.make_char_fatmulti5_litgoatdke_pve_unholy_dk(),
            CharacterFactory.make_char_makun7551_laoshou_protect_paladin().set_tank1().set_dr_pala1(),
            CharacterFactory.make_char_fatmulti14_litgugud_pvp_resto_druid(),
        ])

    # 把 牧师 4 人组 和 萨满 4 人组 加上 Ganjj 和 Laoshou 分成 2 队分别刷节日任务
    @classmethod
    def make_team_solo_dungeon_festival_team_4_ms_sm(cls) -> T.List[Character]:
        return cls._set_5p_team_leader(chars=[
            CharacterFactory.make_char_makun7551_ganjj_pve_blood_tank_dk().set_tank1(),
            CharacterFactory.make_char_fatmulti19_lgmsi_pve_shadow_priest(),
            CharacterFactory.make_char_fatmulti20_lgmsj_pve_shadow_priest(),
            CharacterFactory.make_char_fatmulti23_lgsmm_pve_elemental_shaman(),
            CharacterFactory.make_char_fatmulti24_lgsmn_pve_resto_shaman(),
        ])

    @classmethod
    def make_team_solo_dungeon_festival_team_5_ms_sm(cls) -> T.List[Character]:
        return cls._set_5p_team_leader(chars=[
            CharacterFactory.make_char_makun7551_laoshou_protect_paladin().set_tank1().set_dr_pala1(),
            CharacterFactory.make_char_fatmulti21_lgmsk_pve_shadow_priest(),
            CharacterFactory.make_char_fatmulti22_lgmsl_pve_shadow_priest(),
            CharacterFactory.make_char_fatmulti25_lgsmo_pve_elemental_shaman(),
            CharacterFactory.make_char_fatmulti26_lgsmp_pve_resto_shaman(),
        ])

    # === 灰熊丘陵日常刷金 ===
    @classmethod
    def make_team_daily_gold_farm_team_1_druid(cls) -> T.List[Character]:
        """
        灰熊秋林日常刷金 - 防骑 + 3 鸟德 + 1 奶德
        """
        return cls._set_5p_team_leader(chars=[
            CharacterFactory.make_char_fatmulti9_glowyy_pve_protect_pala().set_tank1().set_dr_pala1(),
            CharacterFactory.make_char_fatmulti15_litgugue_pvp_balance_druid(),
            CharacterFactory.make_char_fatmulti16_litguguf_pvp_balance_druid(),
            CharacterFactory.make_char_fatmulti17_litgugug_pvp_balance_druid(),
            CharacterFactory.make_char_fatmulti18_litguguh_pvp_resto_druid(),
        ])

    @classmethod
    def make_team_daily_gold_farm_team_2_druid(cls) -> T.List[Character]:
        """
        灰熊秋林日常刷金 - 4 鸟德 + 1 奶德
        """
        return cls._set_5p_team_leader(chars=[
            CharacterFactory.make_char_fatmulti8_bunnysisters_pve_balance_druid().set_tank1(),
            CharacterFactory.make_char_fatmulti11_litgugua_pve_balance_druid(),
            CharacterFactory.make_char_fatmulti12_litgugub_pve_balance_druid(),
            CharacterFactory.make_char_fatmulti13_litguguc_pve_balance_druid(),
            CharacterFactory.make_char_fatmulti14_litgugud_pvp_resto_druid(),
        ])

    @classmethod
    def make_team_daily_gold_farm_team_3_dk(cls) -> T.List[Character]:
        """
        灰熊秋林日常刷金 - 5 DK
        """
        return cls._set_5p_team_leader(chars=[
            CharacterFactory.make_char_fatmulti1_litgoatdka_pvp_frost_dk().set_tank1(),
            CharacterFactory.make_char_fatmulti2_litgoatdkb_pvp_frost_dk(),
            CharacterFactory.make_char_fatmulti3_litgoatdkc_pvp_frost_dk(),
            CharacterFactory.make_char_fatmulti4_litgoatdkd_pvp_frost_dk(),
            CharacterFactory.make_char_fatmulti5_litgoatdke_pvp_frost_dk(),
        ])

    @classmethod
    def make_team_daily_gold_farm_team_4_ss(cls) -> T.List[Character]:
        """
        灰熊秋林日常刷金 - 5 SS
        """
        return cls._set_5p_team_leader(chars=[
            CharacterFactory.make_char_fatmulti1_litgoatssa_pve_demo_warlock().set_tank1(),
            CharacterFactory.make_char_fatmulti2_litgoatssb_pve_demo_warlock(),
            CharacterFactory.make_char_fatmulti3_litgoatssc_pve_demo_warlock(),
            CharacterFactory.make_char_fatmulti4_litgoatssd_pve_demo_warlock(),
            CharacterFactory.make_char_fatmulti5_litgoatsse_pve_demo_warlock(),
        ])

    @classmethod
    def make_team_daily_gold_farm_team_5_ms(cls) -> T.List[Character]:
        """
        灰熊秋林日常刷金 - DK + 4 暗牧
        """
        return cls._set_5p_team_leader(chars=[
            CharacterFactory.make_char_makun7551_ganjj_pve_unholy_dps_dk().set_tank1(),
            CharacterFactory.make_char_fatmulti19_lgmsi_pve_shadow_priest(),
            CharacterFactory.make_char_fatmulti20_lgmsj_pve_shadow_priest(),
            CharacterFactory.make_char_fatmulti21_lgmsk_pve_shadow_priest(),
            CharacterFactory.make_char_fatmulti22_lgmsl_pve_shadow_priest(),
        ])

    @classmethod
    def make_team_daily_gold_farm_team_6_sm(cls) -> T.List[Character]:
        """
        灰熊秋林日常刷金 - DK + 4 萨满
        """
        return cls._set_5p_team_leader(chars=[
            CharacterFactory.make_char_makun7551_laoshou_retri_paladin().set_tank1(),
            CharacterFactory.make_char_fatmulti23_lgsmm_pve_elemental_shaman(),
            CharacterFactory.make_char_fatmulti24_lgsmn_pve_elemental_shaman(),
            CharacterFactory.make_char_fatmulti25_lgsmo_pve_elemental_shaman(),
            CharacterFactory.make_char_fatmulti26_lgsmp_pve_elemental_shaman(),
        ])

    @classmethod
    def make_team_daily_gold_farm_team_7(cls) -> T.List[Character]:
        """
        灰熊秋林日常刷金 - Batlefury 黄金组合
        """
        return cls._set_5p_team_leader(chars=[
            CharacterFactory.make_char_fatmulti1_batlefury_pve_retri_pala().set_tank1(),
            CharacterFactory.make_char_fatmulti2_quentin_pve_elemental_shaman(),
            CharacterFactory.make_char_fatmulti3_opiitou_pve_balance_druid(),
            CharacterFactory.make_char_fatmulti4_swagsonic_pve_arcane_mage(),
            CharacterFactory.make_char_fatmulti5_kangliu_pve_shadow_priest(),
        ])
