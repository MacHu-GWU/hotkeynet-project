# -*- coding: utf-8 -*-

"""
该模块定义了在 Warmane 服务器上所拥有的角色. 并且提供了一系列函数方便于我们对角色进行排列组合.

这个模块里的所有类都是一个 namespace, 仅仅是为了方便引用而提供的类. 这些类下面的方法其实
都可以是 ``staticmethod``. 但是为了免去为每个方法写 ``@staticmethod`` 的麻烦, 我们就
把类名起一个以下划线开头的名字, 然后创建一个名称像类名的实例.
"""

import typing as T

from hotkeynet.game.wow.wlk import (
    Talent as TL,
    TalentCategory as TC,
    Window,
    Character,
)

from .account import AccountEnum


class _CharacterFactory:
    """
    枚举出所有账号下的所有角色的所有天赋.

    例如 fatmulti1 中有这些角色.

    1. batlefury, 防骑, 惩戒, 需要创建 2 个函数
    2. litgoatdka, DK, 坦克 和 冰AOE, 需要创建 2 个函数
    3. litgoatssa, 术士, PvP, 需要创建 1 个函数

    这样我们可以通过调用这些 可以被搜索定位, 名字人类可理解 的函数方便的创建游戏角色的实例.
    """

    def make_char_fatmulti1_batlefury_pve_protect_pala(self) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti1.value,
            name="batlefury",
            nth_char=1,
            talent=TL.paladin_pve_protect,
            window=Window.make(1),
        )

    def make_char_fatmulti1_batlefury_pve_retri_pala(self) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti1.value,
            name="batlefury",
            nth_char=1,
            talent=TL.paladin_pve_retri,
            window=Window.make(1),
        )

    def make_char_fatmulti2_quentin_pve_elemental_shaman(self) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti2.value,
            name="quentin",
            nth_char=1,
            talent=TL.shaman_pve_elemental,
            window=Window.make(2),
        )

    def make_char_fatmulti2_quentin_pve_resto_shaman(self) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti2.value,
            name="quentin",
            nth_char=1,
            talent=TL.shaman_pve_resto,
            window=Window.make(2),
        )

    def make_char_fatmulti3_opiitou_pve_balance_druid(self) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti3.value,
            name="opiitou",
            nth_char=1,
            talent=TL.druid_pve_balance,
            window=Window.make(3),
        )

    def make_char_fatmulti3_opiitou_pve_bear_druid(self) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti3.value,
            name="opiitou",
            nth_char=1,
            talent=TL.druid_pve_resto,
            window=Window.make(3),
        )

    def make_char_fatmulti4_swagsonic_pve_arcane_mage(self) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti4.value,
            name="swagsonic",
            nth_char=1,
            talent=TL.mage_pve_arcane,
            window=Window.make(4),
        )

    def make_char_fatmulti4_swagsonic_pve_fire_mage(self) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti4.value,
            name="swagsonic",
            nth_char=1,
            talent=TL.mage_pve_fire,
            window=Window.make(4),
        )

    def make_char_fatmulti5_kangliu_pve_shadow_priest(self) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti5.value,
            name="kangliu",
            nth_char=1,
            talent=TL.priest_pve_shadow,
            window=Window.make(5),
        )

    def make_char_fatmulti5_kangliu_pve_disco_priest(self) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti5.value,
            name="kangliu",
            nth_char=1,
            talent=TL.priest_pve_disco,
            window=Window.make(5),
        )

    def make_char_fitsheep_kindhearted_pve_demonology_warlock(self) -> Character:
        return Character(
            account=AccountEnum.account_fitsheep.value,
            name="kindhearted",
            nth_char=1,
            talent=TL.warlock_pve_demonology,
            window=Window.make(6),
        )

    def make_char_fitsheep_kindhearted_pvp_destruction_warlock(self) -> Character:
        return Character(
            account=AccountEnum.account_fitsheep.value,
            name="kindhearted",
            nth_char=1,
            talent=TL.warlock_pvp_destruction,
            window=Window.make(6),
        )

    def make_char_fitsheep_bordercollie_pve_shadow_priest(self) -> Character:
        return Character(
            account=AccountEnum.account_fitsheep.value,
            name="bordercollie",
            nth_char=2,
            talent=TL.priest_pve_shadow,
            window=Window.make(6),
        )

    def make_char_fitsheep_bordercollie_pve_disco_priest(self) -> Character:
        return Character(
            account=AccountEnum.account_fitsheep.value,
            name="bordercollie",
            nth_char=2,
            talent=TL.priest_pve_disco,
            window=Window.make(6),
        )

    def make_char_fatmulti6_kapacuk_pve_marksman_hunter(self) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti6.value,
            name="kapacuk",
            nth_char=1,
            talent=TL.hunter_pve_marksman,
            window=Window.make(7),
        )

    def make_char_fatmulti6_kapacuk_pvp_beast_hunter(self) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti6.value,
            name="kapacuk",
            nth_char=1,
            talent=TL.hunter_pve_beast,
            window=Window.make(7),
        )

    def make_char_fatmulti8_bunnysisters_pve_resto_druid(self) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti8.value,
            name="bunnysisters",
            nth_char=1,
            talent=TL.druid_pve_resto,
            window=Window.make(8),
        )

    def make_char_fatmulti8_bunnysisters_pve_balance_druid(self) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti8.value,
            name="bunnysisters",
            nth_char=1,
            talent=TL.druid_pve_balance,
            window=Window.make(8),
        )

    def make_char_fatmulti9_glowyy_pve_holy_pala(self) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti9.value,
            name="glowyy",
            nth_char=1,
            talent=TL.paladin_pve_holy,
            window=Window.make(9),
        )

    def make_char_fatmulti9_glowyy_pve_protect_pala(self) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti9.value,
            name="glowyy",
            nth_char=1,
            talent=TL.paladin_pve_protect,
            window=Window.make(9),
        )

    def make_char_fatmulti10_luxiaofeng_pve_blood_tank_dk(self) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti10.value,
            name="luxiaofeng",
            nth_char=1,
            talent=TL.dk_pve_blood_tank,
            window=Window.make(10),
        )

    def make_char_fatmulti10_luxiaofeng_pve_unholy_tank_dk(self) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti10.value,
            name="luxiaofeng",
            nth_char=1,
            talent=TL.dk_pve_unholy_tank,
            window=Window.make(10),
        )

    def make_char_monkey130_flydps_pve_blood_tank_dk(self) -> Character:
        return Character(
            account=AccountEnum.account_monkey130.value,
            name="flydps",
            nth_char=1,
            talent=TL.dk_pve_blood_tank,
            window=Window.make(10),
        )

    def make_char_makun7551_ganjj_pve_blood_tank_dk(self) -> Character:
        return Character(
            account=AccountEnum.account_makun7551.value,
            name="ganjj",
            nth_char=2,
            talent=TL.dk_pve_blood_tank,
            window=Window.make(10),
        )

    def make_char_makun7551_ganjj_pve_unholy_dps_dk(self) -> Character:
        return Character(
            account=AccountEnum.account_makun7551.value,
            name="ganjj",
            nth_char=2,
            talent=TL.dk_pve_unholy_dps,
            window=Window.make(10),
        )

    def make_char_makun7551_ganjj_pve_unholy_dps_dk_at_window_22(self) -> Character:
        return Character(
            account=AccountEnum.account_makun7551.value,
            name="ganjj",
            nth_char=2,
            talent=TL.dk_pve_unholy_dps,
            window=Window.make(22),
        )

    def make_char_makun7551_laoshou_protect_paladin(self) -> Character:
        return Character(
            account=AccountEnum.account_makun7551.value,
            name="laoshou",
            nth_char=1,
            talent=TL.paladin_pve_protect,
            window=Window.make(10),
        )

    def make_char_makun7551_laoshou_retri_paladin(self) -> Character:
        return Character(
            account=AccountEnum.account_makun7551.value,
            name="laoshou",
            nth_char=1,
            talent=TL.paladin_pve_retri,
            window=Window.make(10),
        )

    def make_char_makun7551_laoshou_protect_paladin_at_window_9(self) -> Character:
        return Character(
            account=AccountEnum.account_makun7551.value,
            name="laoshou",
            nth_char=1,
            talent=TL.paladin_pve_protect,
            window=Window.make(9),
        )

    def make_char_makun7551_laoshou_retri_paladin_at_window_19(self) -> Character:
        return Character(
            account=AccountEnum.account_makun7551.value,
            name="laoshou",
            nth_char=1,
            talent=TL.paladin_pve_retri,
            window=Window.make(19),
        )

    def make_char_freiliheng_stophealing_pve_blood_tank_dk(self) -> Character:
        return Character(
            account=AccountEnum.account_freiliheng.value,
            name="stophealing",
            nth_char=1,
            talent=TL.dk_pve_blood_tank,
            window=Window.make(10),
        )

    def make_char_fatmulti1_litgoatssa_pve_demo_warlock(self) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti1.value,
            name="litgoatssa",
            nth_char=2,
            talent=TL.warlock_pve_demonology,
            window=Window.make(1),
        )

    def make_char_fatmulti2_litgoatssb_pve_demo_warlock(self) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti2.value,
            name="litgoatssb",
            nth_char=2,
            talent=TL.warlock_pve_demonology,
            window=Window.make(2),
        )

    def make_char_fatmulti3_litgoatssc_pve_demo_warlock(self) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti3.value,
            name="litgoatssc",
            nth_char=2,
            talent=TL.warlock_pve_demonology,
            window=Window.make(3),
        )

    def make_char_fatmulti4_litgoatssd_pve_demo_warlock(self) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti4.value,
            name="litgoatssd",
            nth_char=2,
            talent=TL.warlock_pve_demonology,
            window=Window.make(4),
        )

    def make_char_fatmulti5_litgoatsse_pve_demo_warlock(self) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti5.value,
            name="litgoatsse",
            nth_char=2,
            talent=TL.warlock_pve_demonology,
            window=Window.make(5),
        )

    def make_char_fatmulti1_litgoatdka_pvp_frost_dk(self) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti1.value,
            name="litgoatdka",
            nth_char=4,
            talent=TL.dk_pvp_frost,
            window=Window.make(1),
        )

    def make_char_fatmulti2_litgoatdkb_pvp_frost_dk(self) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti2.value,
            name="litgoatdkb",
            nth_char=4,
            talent=TL.dk_pvp_frost,
            window=Window.make(2),
        )

    def make_char_fatmulti3_litgoatdkc_pvp_frost_dk(self) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti3.value,
            name="litgoatdkc",
            nth_char=4,
            talent=TL.dk_pvp_frost,
            window=Window.make(3),
        )

    def make_char_fatmulti4_litgoatdkd_pvp_frost_dk(self) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti4.value,
            name="litgoatdkd",
            nth_char=4,
            talent=TL.dk_pvp_frost,
            window=Window.make(4),
        )

    def make_char_fatmulti5_litgoatdke_pvp_frost_dk(self) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti5.value,
            name="litgoatdke",
            nth_char=4,
            talent=TL.dk_pvp_frost,
            window=Window.make(5),
        )

    def make_char_fatmulti1_litgoatdka_pve_blood_dk(self) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti1.value,
            name="litgoatdka",
            nth_char=4,
            talent=TL.dk_pve_unholy_dps,
            window=Window.make(1),
        )

    def make_char_fatmulti2_litgoatdkb_pve_unholy_dk(self) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti2.value,
            name="litgoatdkb",
            nth_char=4,
            talent=TL.dk_pve_unholy_dps,
            window=Window.make(2),
        )

    def make_char_fatmulti3_litgoatdkc_pve_unholy_dk(self) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti3.value,
            name="litgoatdkc",
            nth_char=4,
            talent=TL.dk_pve_unholy_dps,
            window=Window.make(3),
        )

    def make_char_fatmulti4_litgoatdkd_pve_unholy_dk(self) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti4.value,
            name="litgoatdkd",
            nth_char=4,
            talent=TL.dk_pve_unholy_dps,
            window=Window.make(4),
        )

    def make_char_fatmulti5_litgoatdke_pve_unholy_dk(self) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti5.value,
            name="litgoatdke",
            nth_char=4,
            talent=TL.dk_pve_unholy_dps,
            window=Window.make(5),
        )

    def make_char_fatmulti11_litgugua_pvp_balance_druid(self) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti11.value,
            name="litgugua",
            nth_char=1,
            talent=TL.druid_pvp_balance,
            window=Window.make(11),
        )

    def make_char_fatmulti11_litgugua_pvp_resto_druid(self) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti11.value,
            name="litgugud",
            nth_char=1,
            talent=TL.druid_pvp_resto,
            window=Window.make(11),
        )

    def make_char_fatmulti11_litgugua_pve_balance_druid(self) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti11.value,
            name="litgugua",
            nth_char=1,
            talent=TL.druid_pve_balance,
            window=Window.make(11),
        )

    def make_char_fatmulti12_litgugub_pvp_balance_druid(self) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti12.value,
            name="litgugub",
            nth_char=1,
            talent=TL.druid_pvp_balance,
            window=Window.make(12),
        )

    def make_char_fatmulti12_litgugub_pvp_resto_druid(self) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti12.value,
            name="litgugub",
            nth_char=1,
            talent=TL.druid_pvp_resto,
            window=Window.make(12),
        )

    def make_char_fatmulti12_litgugub_pve_balance_druid(self) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti12.value,
            name="litgugub",
            nth_char=1,
            talent=TL.druid_pve_balance,
            window=Window.make(12),
        )

    def make_char_fatmulti13_litguguc_pvp_balance_druid(self) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti13.value,
            name="litguguc",
            nth_char=1,
            talent=TL.druid_pvp_balance,
            window=Window.make(13),
        )

    def make_char_fatmulti13_litguguc_pvp_resto_druid(self) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti13.value,
            name="litguguc",
            nth_char=1,
            talent=TL.druid_pvp_resto,
            window=Window.make(13),
        )

    def make_char_fatmulti13_litguguc_pve_balance_druid(self) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti13.value,
            name="litguguc",
            nth_char=1,
            talent=TL.druid_pve_balance,
            window=Window.make(13),
        )

    def make_char_fatmulti14_litgugud_pvp_balancce_druid(self) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti14.value,
            name="litgugud",
            nth_char=1,
            talent=TL.druid_pvp_balance,
            window=Window.make(14),
        )

    def make_char_fatmulti14_litgugud_pvp_resto_druid(self) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti14.value,
            name="litgugud",
            nth_char=1,
            talent=TL.druid_pvp_resto,
            window=Window.make(14),
        )

    def make_char_fatmulti14_litgugud_pve_balance_druid(self) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti14.value,
            name="litgugud",
            nth_char=1,
            talent=TL.druid_pve_balance,
            window=Window.make(14),
        )

    def make_char_fatmulti15_litgugue_pvp_balance_druid(self) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti15.value,
            name="litgugue",
            nth_char=1,
            talent=TL.druid_pvp_balance,
            window=Window.make(11),
        )

    def make_char_fatmulti16_litguguf_pvp_balance_druid(self) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti16.value,
            name="litguguf",
            nth_char=1,
            talent=TL.druid_pvp_balance,
            window=Window.make(12),
        )

    def make_char_fatmulti17_litgugug_pvp_balance_druid(self) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti17.value,
            name="litgugug",
            nth_char=1,
            talent=TL.druid_pvp_balance,
            window=Window.make(13),
        )

    def make_char_fatmulti18_litguguh_pvp_balance_druid(self) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti18.value,
            name="litguguh",
            nth_char=1,
            talent=TL.druid_pvp_balance,
            window=Window.make(14),
        )

    def make_char_fatmulti18_litguguh_pvp_resto_druid(self) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti18.value,
            name="litguguh",
            nth_char=1,
            talent=TL.druid_pvp_resto,
            window=Window.make(14),
        )

    def make_char_fatmulti19_lgmsi_pve_shadow_priest(self) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti19.value,
            name="lgmsi",
            nth_char=1,
            talent=TL.priest_pve_shadow,
            window=Window.make(15),
        )

    def make_char_fatmulti19_lgmsi_pve_disco_priest(self) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti19.value,
            name="lgmsi",
            nth_char=1,
            talent=TL.priest_pve_disco,
            window=Window.make(15),
        )

    def make_char_fatmulti20_lgmsj_pve_shadow_priest(self) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti20.value,
            name="lgmsj",
            nth_char=1,
            talent=TL.priest_pve_shadow,
            window=Window.make(16),
        )

    def make_char_fatmulti20_lgmsj_pve_disco_priest(self) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti20.value,
            name="lgmsj",
            nth_char=1,
            talent=TL.priest_pve_disco,
            window=Window.make(16),
        )

    def make_char_fatmulti21_lgmsk_pve_shadow_priest(self) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti21.value,
            name="lgmsk",
            nth_char=1,
            talent=TL.priest_pve_shadow,
            window=Window.make(17),
        )

    def make_char_fatmulti21_lgmsk_pve_holy_priest(self) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti21.value,
            name="lgmsk",
            nth_char=1,
            talent=TL.priest_pve_holy,
            window=Window.make(17),
        )

    def make_char_fatmulti22_lgmsl_pve_shadow_priest(self) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti22.value,
            name="lgmsl",
            nth_char=1,
            talent=TL.priest_pve_shadow,
            window=Window.make(18),
        )

    def make_char_fatmulti22_lgmsl_pve_holy_priest(self) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti22.value,
            name="lgmsl",
            nth_char=1,
            talent=TL.priest_pve_holy,
            window=Window.make(18),
        )

    def make_char_fatmulti23_lgsmm_pve_elemental_shaman(self) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti23.value,
            name="lgsmm",
            nth_char=1,
            talent=TL.shaman_pve_elemental,
            window=Window.make(19),
        )

    def make_char_fatmulti23_lgsmm_pve_resto_shaman(self) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti23.value,
            name="lgsmm",
            nth_char=1,
            talent=TL.shaman_pve_resto,
            window=Window.make(19),
        )

    def make_char_fatmulti24_lgsmn_pve_elemental_shaman(self) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti24.value,
            name="lgsmn",
            nth_char=1,
            talent=TL.shaman_pve_elemental,
            window=Window.make(20),
        )

    def make_char_fatmulti24_lgsmn_pve_resto_shaman(self) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti24.value,
            name="lgsmn",
            nth_char=1,
            talent=TL.shaman_pve_resto,
            window=Window.make(20),
        )

    def make_char_fatmulti25_lgsmo_pve_elemental_shaman(self) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti25.value,
            name="lgsmo",
            nth_char=1,
            talent=TL.shaman_pve_elemental,
            window=Window.make(21),
        )

    def make_char_fatmulti25_lgsmo_pve_resto_shaman(self) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti25.value,
            name="lgsmo",
            nth_char=1,
            talent=TL.shaman_pve_resto,
            window=Window.make(21),
        )

    def make_char_fatmulti26_lgsmp_pve_elemental_shaman(self) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti26.value,
            name="lgsmp",
            nth_char=1,
            talent=TL.shaman_pve_elemental,
            window=Window.make(22),
        )

    def make_char_fatmulti26_lgsmp_pve_resto_shaman(self) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti26.value,
            name="lgsmp",
            nth_char=1,
            talent=TL.shaman_pve_resto,
            window=Window.make(22),
        )

    # --------------------------------------------------------------------------
    # Lordaeron
    # --------------------------------------------------------------------------
    def make_char_fatmulti1_lgqsa_pve_protect_pala(self) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti1.value,
            name="lgqsa",
            nth_char=1,
            talent=TL.paladin_pve_protect,
            window=Window.make(1),
        )

    def make_char_fatmulti2_lgqsb_pve_retri_pala(self) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti2.value,
            name="lgqsb",
            nth_char=1,
            talent=TL.paladin_pve_retri,
            window=Window.make(2),
        )

    def make_char_fatmulti3_lgqsc_pve_retri_pala(self) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti3.value,
            name="lgqsc",
            nth_char=1,
            talent=TL.paladin_pve_retri,
            window=Window.make(3),
        )

    def make_char_fatmulti4_lgqsd_pve_retri_pala(self) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti4.value,
            name="lgqsd",
            nth_char=1,
            talent=TL.paladin_pve_retri,
            window=Window.make(4),
        )

    def make_char_fatmulti5_lgqse_pve_holy_pala(self) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti5.value,
            name="lgqse",
            nth_char=1,
            talent=TL.paladin_pve_holy,
            window=Window.make(5),
        )


CharacterFactory = _CharacterFactory()


class _LoginCharactersFactory:
    def _make_chars_1_to_9(self) -> T.List[Character]:
        return [
            CharacterFactory.make_char_fatmulti1_batlefury_pve_protect_pala().set_inactive(),
            CharacterFactory.make_char_fatmulti2_quentin_pve_elemental_shaman().set_inactive(),
            CharacterFactory.make_char_fatmulti3_opiitou_pve_balance_druid().set_inactive(),
            CharacterFactory.make_char_fatmulti4_swagsonic_pve_arcane_mage().set_inactive(),
            CharacterFactory.make_char_fatmulti5_kangliu_pve_shadow_priest().set_inactive(),
            CharacterFactory.make_char_fitsheep_kindhearted_pve_demonology_warlock().set_inactive(),
            CharacterFactory.make_char_fatmulti6_kapacuk_pve_marksman_hunter().set_inactive(),
            CharacterFactory.make_char_fatmulti8_bunnysisters_pve_resto_druid().set_inactive(),
            CharacterFactory.make_char_fatmulti9_glowyy_pve_holy_pala().set_inactive(),
        ]

    def _make_chars_10_luxiaofeng(self) -> T.List[Character]:
        return [
            CharacterFactory.make_char_fatmulti10_luxiaofeng_pve_blood_tank_dk().set_inactive(),
        ]

    def _make_chars_10_ganjj(self) -> T.List[Character]:
        return [
            CharacterFactory.make_char_makun7551_ganjj_pve_blood_tank_dk().set_inactive(),
        ]

    def _make_chars_10_flydps(self) -> T.List[Character]:
        return [
            CharacterFactory.make_char_monkey130_flydps_pve_blood_tank_dk().set_inactive(),
        ]

    def _make_chars_11_to_14_litgugu_abcd(self) -> T.List[Character]:
        return [
            CharacterFactory.make_char_fatmulti11_litgugua_pve_balance_druid().set_inactive(),
            CharacterFactory.make_char_fatmulti12_litgugub_pve_balance_druid().set_inactive(),
            CharacterFactory.make_char_fatmulti13_litguguc_pve_balance_druid().set_inactive(),
            CharacterFactory.make_char_fatmulti14_litgugud_pve_balance_druid().set_inactive(),
        ]

    def _make_chars_11_to_14_litgugu_efgh(self) -> T.List[Character]:
        return [
            CharacterFactory.make_char_fatmulti15_litgugue_pvp_balance_druid().set_inactive(),
            CharacterFactory.make_char_fatmulti16_litguguf_pvp_balance_druid().set_inactive(),
            CharacterFactory.make_char_fatmulti17_litgugug_pvp_balance_druid().set_inactive(),
            CharacterFactory.make_char_fatmulti18_litguguh_pvp_balance_druid().set_inactive(),
        ]

    def _make_chars_15_to_22(self) -> T.List[Character]:
        return [
            CharacterFactory.make_char_fatmulti19_lgmsi_pve_shadow_priest().set_inactive(),
            CharacterFactory.make_char_fatmulti20_lgmsj_pve_shadow_priest().set_inactive(),
            CharacterFactory.make_char_fatmulti21_lgmsk_pve_shadow_priest().set_inactive(),
            CharacterFactory.make_char_fatmulti22_lgmsl_pve_shadow_priest().set_inactive(),
            CharacterFactory.make_char_fatmulti23_lgsmm_pve_elemental_shaman().set_inactive(),
            CharacterFactory.make_char_fatmulti24_lgsmn_pve_elemental_shaman().set_inactive(),
            CharacterFactory.make_char_fatmulti25_lgsmo_pve_elemental_shaman().set_inactive(),
            CharacterFactory.make_char_fatmulti26_lgsmp_pve_elemental_shaman().set_inactive(),
        ]

    def make_chars_10p(self) -> T.List[Character]:
        return (
            self._make_chars_1_to_9()
            + self._make_chars_10_luxiaofeng()
        )

    def make_chars_14p_litgugu_abcd(self) -> T.List[Character]:
        return (
            self._make_chars_1_to_9()
            + self._make_chars_10_luxiaofeng()
            + self._make_chars_11_to_14_litgugu_abcd()
        )

    def make_chars_14p_litgugu_efgh(self) -> T.List[Character]:
        return (
            self._make_chars_1_to_9()
            + self._make_chars_10_luxiaofeng()
            + self._make_chars_11_to_14_litgugu_efgh()
        )

    def make_chars_22p_litgugu_abcd(self) -> T.List[Character]:
        return (
            self._make_chars_1_to_9()
            + self._make_chars_10_luxiaofeng()
            + self._make_chars_11_to_14_litgugu_abcd()
            + self._make_chars_15_to_22()
        )

    def make_chars_22p_litgugu_efgh(self) -> T.List[Character]:
        return (
            self._make_chars_1_to_9()
            + self._make_chars_10_luxiaofeng()
            + self._make_chars_11_to_14_litgugu_efgh()
            + self._make_chars_15_to_22()
        )

    def make_chars_5p_ganjj_laoshou_lgms_and_lssm(self) -> T.List[Character]:
        return (
            self._make_chars_10_ganjj()
            + self._make_chars_15_to_22()
        )

LoginCharactersFactory = _LoginCharactersFactory()


class _ActiveCharactersFactory:
    def _set_5p_team_leader(self, chars: T.List[Character]):  # pragma: no cover
        if len(chars) != 5:
            raise ValueError("solo dungeon team has to be 5 member!")

        # find leader char window
        leader_char_window: T.Optional[Window] = None

        # try to find the leader if explicitly defined
        if leader_char_window is None:
            for char in chars:
                if char.is_tank_1:
                    leader_char_window = char.window

        # try to find the leader if it is tank talent
        if leader_char_window is None:
            for char in chars:
                if TC.tank in char.talent.categories:
                    leader_char_window = char.window

        # try to find a plate char
        if leader_char_window is None:
            for char in chars:
                categories = char.talent.categories
                if (
                    TC.warrior in categories
                    or TC.dk in categories
                    or TC.paladin in categories
                ):
                    leader_char_window = char.window

        if leader_char_window is None:
            raise ValueError("you have to define at least one TANK or one Plate char")

        # set other char leader1 as the tank
        for char in chars:
            if char.window.label != leader_char_window.label:
                char.set_leader_1_window(leader_char_window)

        return chars

    def _find_key_char_window(
        self,
        chars: T.List[Character],
        attr: str,
    ) -> T.Optional[Window]:
        """
        从一堆 Character 当中找到那个扮演某个特定队伍角色的人所在的窗口.

        例如找到 1 号司机, 1 号坦克.

        如果一个队伍里有多个人被设为 1 号司机, 那么就设为自然顺序遇到的第一个 1 号司机.
        """
        window: T.Optional[Window] = None
        for char in chars:
            if getattr(char, attr):
                return char.window
        return window

    def _set_key_char_window(
        self,
        chars: T.List[Character],
        attr: str,
        window: Window,
    ):
        """
        例如将指定的窗口设为所有人的 1 号司机.

        这里要注意的是 1 号司机本人不会将自己设为一号司机. 因为司机通常会要绑定焦点. 司机
        本人不需要吧自己设为焦点.
        """
        for char in chars:
            if char.window.label != window.label:
                setattr(char, attr, window)

    def _set_team_leader_and_tank(self, chars: T.List[Character]):  # pragma: no cover
        """
        在定义队伍时, 我们希望能简化操作. 只要在一堆角色中指定谁是 1 号司机, 谁是 2 号司机,
        那么其他人就自动将他们的 Character.leader_1_window, Character.leader_2_window
        设置好.
        """
        # find leader char window
        leader_1_window: T.Optional[Window] = self._find_key_char_window(chars, "is_leader_1")
        leader_2_window: T.Optional[Window] = self._find_key_char_window(chars, "is_leader_2")
        tank_1_window: T.Optional[Window] = self._find_key_char_window(chars, "is_tank_1")
        tank_2_window: T.Optional[Window] = self._find_key_char_window(chars, "is_tank_2")

        if leader_1_window is not None:
            self._set_key_char_window(chars, "leader_1_window", leader_1_window)
        else:
            raise ValueError("At least one char has to be the leader 1")

        if leader_2_window is not None:
            self._set_key_char_window(chars, "leader_2_window", leader_2_window)

        if tank_1_window is not None:
            self._set_key_char_window(chars, "tank_1_window", tank_1_window)

        if tank_2_window is not None:
            self._set_key_char_window(chars, "leader_1_window", tank_2_window)

        return chars

    __anchor_make_team_warmane_solo_dungeon = None

    def make_team_solo_dungeon_batlefury_quentin_opiitou_swagsonic_kangliu(self) -> T.List[Character]:
        """
        主力 5 人组
        """
        return self._set_team_leader_and_tank(chars=[
            CharacterFactory.make_char_fatmulti1_batlefury_pve_protect_pala().set_is_leader_1().set_tank_1().set_dr_pala_1(),
            CharacterFactory.make_char_fatmulti2_quentin_pve_elemental_shaman(),
            CharacterFactory.make_char_fatmulti3_opiitou_pve_balance_druid(),
            CharacterFactory.make_char_fatmulti4_swagsonic_pve_arcane_mage(),
            CharacterFactory.make_char_fatmulti5_kangliu_pve_shadow_priest(),
        ])

    def make_team_solo_dungeon_1_tank_3_dps_1_healer(self) -> T.List[Character]:
        """
        该模式用于 1 个坦克 带着 3 个 DPS, 1 个治疗 打 5 人小副本.
        """
        return self._set_team_leader_and_tank(chars=[
            # =================================================================
            # === Tank 部分 ===
            # --- Paladin
            # CharacterFactory.make_char_fatmulti1_batlefury_pve_retri_pala().set_is_leader_1(),
            CharacterFactory.make_char_fatmulti1_batlefury_pve_protect_pala().set_is_leader_1().set_tank_1().set_dr_pala_1(),
            # CharacterFactory.make_char_fatmulti9_glowyy_pve_protect_pala().set_is_leader_1().set_tank_1().set_dr_pala_1(),
            # CharacterFactory.make_char_makun7551_laoshou_retri_paladin().set_is_leader_1(),

            # --- DK
            # CharacterFactory.make_char_fatmulti10_luxiaofeng_pve_unholy_tank_dk().set_is_leader_1().set_tank_1(),
            # CharacterFactory.make_char_fatmulti1_litgoatdka_pve_blood_dk().set_is_leader_1().set_tank_1(),
            # CharacterFactory.make_char_makun7551_ganjj_pve_blood_tank_dk().set_is_leader_1().set_tank_1(),

            # --- Druid
            # CharacterFactory.make_char_fatmulti3_opiitou_pve_bear_druid().set_is_leader_1().set_tank_1(),

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
    def make_team_solo_dungeon_festival_team_1_dk(self) -> T.List[Character]:
        return self._set_team_leader_and_tank(chars=[
            CharacterFactory.make_char_fatmulti1_litgoatdka_pve_blood_dk().set_leader_12_and_tank_12(),
            CharacterFactory.make_char_fatmulti2_litgoatdkb_pve_unholy_dk(),
            CharacterFactory.make_char_fatmulti3_litgoatdkc_pve_unholy_dk(),
            CharacterFactory.make_char_fatmulti4_litgoatdkd_pve_unholy_dk(),
            CharacterFactory.make_char_fatmulti8_bunnysisters_pve_resto_druid(),
        ])

    def make_team_solo_dungeon_festival_team_2_ss(self) -> T.List[Character]:
        return self._set_team_leader_and_tank(chars=[
            CharacterFactory.make_char_fatmulti3_litgoatssc_pve_demo_warlock(),
            CharacterFactory.make_char_fatmulti4_litgoatssd_pve_demo_warlock(),
            CharacterFactory.make_char_fatmulti5_litgoatsse_pve_demo_warlock(),
            CharacterFactory.make_char_fatmulti1_batlefury_pve_protect_pala().set_leader_12_and_tank_12(),
            CharacterFactory.make_char_fatmulti13_litguguc_pvp_resto_druid(),
        ])

    def make_team_solo_dungeon_festival_team_3_mix(self) -> T.List[Character]:
        return self._set_team_leader_and_tank(chars=[
            CharacterFactory.make_char_fatmulti1_litgoatssa_pve_demo_warlock(),
            CharacterFactory.make_char_fatmulti2_litgoatssb_pve_demo_warlock(),
            CharacterFactory.make_char_fatmulti5_litgoatdke_pve_unholy_dk(),
            CharacterFactory.make_char_fatmulti9_glowyy_pve_protect_pala().set_leader_12_and_tank_12(),
            CharacterFactory.make_char_fatmulti14_litgugud_pvp_resto_druid(),
        ])

    # 把 牧师 4 人组 和 萨满 4 人组 加上 Ganjj 和 Laoshou 分成 2 队分别刷节日任务
    def make_team_solo_dungeon_festival_team_4_ms_sm(self) -> T.List[Character]:
        return self._set_team_leader_and_tank(chars=[
            CharacterFactory.make_char_makun7551_ganjj_pve_blood_tank_dk().set_leader_12_and_tank_12(),
            CharacterFactory.make_char_fatmulti19_lgmsi_pve_shadow_priest(),
            CharacterFactory.make_char_fatmulti20_lgmsj_pve_shadow_priest(),
            CharacterFactory.make_char_fatmulti23_lgsmm_pve_elemental_shaman(),
            CharacterFactory.make_char_fatmulti24_lgsmn_pve_resto_shaman(),
        ])

    def make_team_solo_dungeon_festival_team_5_ms_sm(self) -> T.List[Character]:
        return self._set_team_leader_and_tank(chars=[
            CharacterFactory.make_char_makun7551_laoshou_protect_paladin().set_leader_12_and_tank_12(),
            CharacterFactory.make_char_fatmulti21_lgmsk_pve_shadow_priest(),
            CharacterFactory.make_char_fatmulti22_lgmsl_pve_shadow_priest(),
            CharacterFactory.make_char_fatmulti25_lgsmo_pve_elemental_shaman(),
            CharacterFactory.make_char_fatmulti26_lgsmp_pve_resto_shaman(),
        ])

    def make_team_solo_dungeon_festival_team_6_litgugu_efgh(self) -> T.List[Character]:
        return self._set_team_leader_and_tank(chars=[
            CharacterFactory.make_char_fatmulti10_luxiaofeng_pve_blood_tank_dk().set_leader_12_and_tank_12(),
            CharacterFactory.make_char_fatmulti15_litgugue_pvp_balance_druid(),
            CharacterFactory.make_char_fatmulti16_litguguf_pvp_balance_druid(),
            CharacterFactory.make_char_fatmulti17_litgugug_pvp_balance_druid(),
            CharacterFactory.make_char_fatmulti18_litguguh_pvp_resto_druid(),
        ])

    __anchore_make_team_warmane_daily_quest = None

    # === 灰熊丘陵日常刷金 ===
    def make_team_daily_gold_farm_team_1_druid(self) -> T.List[Character]:
        """
        灰熊秋林日常刷金 - 防骑 + 3 鸟德 + 1 奶德
        """
        return self._set_team_leader_and_tank(chars=[
            CharacterFactory.make_char_fatmulti9_glowyy_pve_protect_pala().set_is_leader_1().set_tank_1().set_dr_pala_1(),
            CharacterFactory.make_char_fatmulti15_litgugue_pvp_balance_druid(),
            CharacterFactory.make_char_fatmulti16_litguguf_pvp_balance_druid(),
            CharacterFactory.make_char_fatmulti17_litgugug_pvp_balance_druid(),
            CharacterFactory.make_char_fatmulti18_litguguh_pvp_resto_druid(),
        ])

    def make_team_daily_gold_farm_team_2_druid(self) -> T.List[Character]:
        """
        灰熊秋林日常刷金 - 4 鸟德 + 1 奶德
        """
        return self._set_team_leader_and_tank(chars=[
            CharacterFactory.make_char_fatmulti8_bunnysisters_pve_balance_druid().set_is_leader_1(),
            CharacterFactory.make_char_fatmulti11_litgugua_pve_balance_druid(),
            CharacterFactory.make_char_fatmulti12_litgugub_pve_balance_druid(),
            CharacterFactory.make_char_fatmulti13_litguguc_pve_balance_druid(),
            CharacterFactory.make_char_fatmulti14_litgugud_pvp_resto_druid(),
        ])

    def make_team_daily_gold_farm_team_3_dk(self) -> T.List[Character]:
        """
        灰熊秋林日常刷金 - 5 DK
        """
        return self._set_team_leader_and_tank(chars=[
            CharacterFactory.make_char_fatmulti1_litgoatdka_pvp_frost_dk().set_is_leader_1(),
            CharacterFactory.make_char_fatmulti2_litgoatdkb_pvp_frost_dk(),
            CharacterFactory.make_char_fatmulti3_litgoatdkc_pvp_frost_dk(),
            CharacterFactory.make_char_fatmulti4_litgoatdkd_pvp_frost_dk(),
            CharacterFactory.make_char_fatmulti5_litgoatdke_pvp_frost_dk(),
        ])

    def make_team_daily_gold_farm_team_4_ss(self) -> T.List[Character]:
        """
        灰熊秋林日常刷金 - 5 SS
        """
        return self._set_team_leader_and_tank(chars=[
            CharacterFactory.make_char_fatmulti1_litgoatssa_pve_demo_warlock().set_is_leader_1(),
            CharacterFactory.make_char_fatmulti2_litgoatssb_pve_demo_warlock(),
            CharacterFactory.make_char_fatmulti3_litgoatssc_pve_demo_warlock(),
            CharacterFactory.make_char_fatmulti4_litgoatssd_pve_demo_warlock(),
            CharacterFactory.make_char_fatmulti5_litgoatsse_pve_demo_warlock(),
        ])

    def make_team_daily_gold_farm_team_5_ms(self) -> T.List[Character]:
        """
        灰熊秋林日常刷金 - DK + 4 暗牧
        """
        return self._set_team_leader_and_tank(chars=[
            CharacterFactory.make_char_makun7551_ganjj_pve_unholy_dps_dk().set_is_leader_1(),
            CharacterFactory.make_char_fatmulti19_lgmsi_pve_shadow_priest(),
            CharacterFactory.make_char_fatmulti20_lgmsj_pve_shadow_priest(),
            CharacterFactory.make_char_fatmulti21_lgmsk_pve_shadow_priest(),
            CharacterFactory.make_char_fatmulti22_lgmsl_pve_shadow_priest(),
        ])

    def make_team_daily_gold_farm_team_6_sm(self) -> T.List[Character]:
        """
        灰熊秋林日常刷金 - DK + 4 萨满
        """
        return self._set_team_leader_and_tank(chars=[
            CharacterFactory.make_char_makun7551_laoshou_retri_paladin().set_is_leader_1(),
            CharacterFactory.make_char_fatmulti23_lgsmm_pve_elemental_shaman(),
            CharacterFactory.make_char_fatmulti24_lgsmn_pve_elemental_shaman(),
            CharacterFactory.make_char_fatmulti25_lgsmo_pve_elemental_shaman(),
            CharacterFactory.make_char_fatmulti26_lgsmp_pve_elemental_shaman(),
        ])

    def make_team_daily_gold_farm_team_7(self) -> T.List[Character]:
        """
        灰熊秋林日常刷金 - Batlefury 黄金组合
        """
        return self._set_team_leader_and_tank(chars=[
            CharacterFactory.make_char_fatmulti1_batlefury_pve_retri_pala().set_is_leader_1(),
            CharacterFactory.make_char_fatmulti2_quentin_pve_elemental_shaman(),
            CharacterFactory.make_char_fatmulti3_opiitou_pve_balance_druid(),
            CharacterFactory.make_char_fatmulti4_swagsonic_pve_arcane_mage(),
            CharacterFactory.make_char_fatmulti5_kangliu_pve_shadow_priest(),
        ])

    __anchor_make_team_warmane_raid_10 = None

    def make_team_solo_raid_10p_batlefury_luxiaofeng_core_team(self) -> T.List[Character]:
        return self._set_team_leader_and_tank(chars=[
            CharacterFactory.make_char_fatmulti1_batlefury_pve_protect_pala().set_is_leader_1().set_tank_1().set_dr_pala_1(),
            CharacterFactory.make_char_fatmulti2_quentin_pve_elemental_shaman(),
            CharacterFactory.make_char_fatmulti3_opiitou_pve_balance_druid(),
            CharacterFactory.make_char_fatmulti4_swagsonic_pve_arcane_mage(),
            CharacterFactory.make_char_fatmulti5_kangliu_pve_shadow_priest(),
            CharacterFactory.make_char_fitsheep_kindhearted_pve_demonology_warlock(),
            CharacterFactory.make_char_fatmulti6_kapacuk_pve_marksman_hunter(),
            CharacterFactory.make_char_fatmulti8_bunnysisters_pve_resto_druid(),
            CharacterFactory.make_char_fatmulti9_glowyy_pve_holy_pala().set_dr_pala_2(),
            CharacterFactory.make_char_fatmulti10_luxiaofeng_pve_unholy_tank_dk().set_is_leader_2().set_tank_2(),
        ])

    __anchor_make_team_warmane_monthly_login = None

    def make_team_22p_monthly_login_1(self) -> T.List[Character]:
        """
        由于 Warmane 角色很久不登录的话, 名字就要被收回. 所以隔 1 - 2 个月就要登录一次.

        这事第一批次.
        """
        return self._set_team_leader_and_tank(chars=[
            (
                CharacterFactory.make_char_fatmulti1_batlefury_pve_protect_pala()
                    .set_is_leader_1().set_tank_1().set_dr_pala_1()
                    .set_is_leader_2().set_tank_2().set_dr_pala_2()
            ),
            CharacterFactory.make_char_fatmulti2_quentin_pve_elemental_shaman(),
            CharacterFactory.make_char_fatmulti3_opiitou_pve_balance_druid(),
            CharacterFactory.make_char_fatmulti4_swagsonic_pve_arcane_mage(),
            CharacterFactory.make_char_fatmulti5_kangliu_pve_shadow_priest(),
            CharacterFactory.make_char_fitsheep_kindhearted_pve_demonology_warlock(),
            CharacterFactory.make_char_fatmulti6_kapacuk_pve_marksman_hunter(),
            CharacterFactory.make_char_fatmulti8_bunnysisters_pve_resto_druid(),
            CharacterFactory.make_char_fatmulti9_glowyy_pve_holy_pala().set_dr_pala_2(),
            CharacterFactory.make_char_fatmulti10_luxiaofeng_pve_unholy_tank_dk(),
            CharacterFactory.make_char_fatmulti11_litgugua_pve_balance_druid(),
            CharacterFactory.make_char_fatmulti16_litguguf_pvp_balance_druid(),
            CharacterFactory.make_char_fatmulti13_litguguc_pve_balance_druid(),
            CharacterFactory.make_char_fatmulti14_litgugud_pve_balance_druid(),
            CharacterFactory.make_char_fatmulti19_lgmsi_pve_shadow_priest(),
            CharacterFactory.make_char_fatmulti20_lgmsj_pve_shadow_priest(),
            CharacterFactory.make_char_fatmulti21_lgmsk_pve_shadow_priest(),
            CharacterFactory.make_char_fatmulti22_lgmsl_pve_shadow_priest(),
            CharacterFactory.make_char_fatmulti23_lgsmm_pve_elemental_shaman(),
            CharacterFactory.make_char_fatmulti24_lgsmn_pve_elemental_shaman(),
            CharacterFactory.make_char_fatmulti25_lgsmo_pve_elemental_shaman(),
            CharacterFactory.make_char_fatmulti26_lgsmp_pve_elemental_shaman(),
        ])

    def make_team_22p_monthly_login_2(self) -> T.List[Character]:
        """
        由于 Warmane 角色很久不登录的话, 名字就要被收回. 所以隔 1 - 2 个月就要登录一次.

        这事第二批次.
        """
        return self._set_team_leader_and_tank(chars=[
            (
                CharacterFactory.make_char_makun7551_ganjj_pve_blood_tank_dk()
                    .set_is_leader_1().set_tank_1().set_dr_pala_1()
                    .set_is_leader_2().set_tank_2().set_dr_pala_2()
            ),
            CharacterFactory.make_char_fatmulti15_litgugue_pvp_balance_druid(),
            CharacterFactory.make_char_fatmulti16_litguguf_pvp_balance_druid(),
            CharacterFactory.make_char_fatmulti17_litgugug_pvp_balance_druid(),
            CharacterFactory.make_char_fatmulti18_litguguh_pvp_balance_druid(),
        ])

    # --------------------------------------------------------------------------
    # Lordaeron
    # --------------------------------------------------------------------------
    __anchor_make_team_lordaeron_server = None

    def make_team_solo_dungeon_lgqs_abcde(self) -> T.List[Character]:
        return self._set_team_leader_and_tank(chars=[
            (
                CharacterFactory.make_char_fatmulti1_lgqsa_pve_protect_pala()
                    .set_is_leader_1().set_tank_1().set_dr_pala_1()
                    .set_is_leader_2().set_tank_2().set_dr_pala_2()
            ),
            CharacterFactory.make_char_fatmulti2_lgqsb_pve_retri_pala(),
            CharacterFactory.make_char_fatmulti3_lgqsc_pve_retri_pala(),
            CharacterFactory.make_char_fatmulti4_lgqsd_pve_retri_pala(),
            CharacterFactory.make_char_fatmulti5_lgqse_pve_holy_pala(),
        ])


ActiveCharactersFactory = _ActiveCharactersFactory()

class MyClass(_ActiveCharactersFactory):
    pass

class _CharacterHelper:
    """
    这个类有很多
    """
    def sort_chars_by_window_label(
        self,
        chars: T.Iterable[Character],
    ) -> T.List[Character]:
        """
        将许多角色按照所在的窗口编号排序.
        """
        return list(sorted(chars, key=lambda char: char.window.label))

    def sort_chars_by_window_title(
        self,
        chars: T.Iterable[Character],
    ) -> T.List[Character]:
        """
        将许多角色按照所在的窗口名称排序.
        """
        return list(sorted(chars, key=lambda char: char.window.title))

    def filter_by_talent(
        self,
        chars: T.Iterable[Character],
        tl: TL,
    ) -> T.List[Character]:
        """
        筛选出属于某个天赋的所有角色.

        例如你可以选出所有 PvE DK 血坦克 ``Talent.dk_pve_blood_tank`` 的角色.
        """
        return [
            char
            for char in chars
            if char.talent is tl
        ]

    def filter_by_talent_category(
        self,
        chars: T.Iterable[Character],
        tc: TC,
    ) -> T.List[Character]:
        """
        筛选出天赋属于某个天赋类别的所有角色.

        例如你可以选出所有 PvE Tank 类别的角色. 实际上是先根据类别找出所有对应的天赋的集合,
        然后一一判断这个角色的天赋在不在集合中.
        """
        talent_set = tc.talents
        return [
            char
            for char in chars
            if char.talent in talent_set
        ]


CharacterHelper = _CharacterHelper()
