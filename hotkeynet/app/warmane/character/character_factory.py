# -*- coding: utf-8 -*-

from ordered_set import OrderedSet
from hotkeynet.game.wow.wlk import (
    Talent as TL,
    Window,
    Character,
)
from ..account import AccountEnum


class CharacterFactory:
    """
    枚举出所有账号下的所有角色的所有天赋. 每一个 @property 都代表: 一个账号下的一个角色的
    具体天赋配装. 同一个角色的双天赋需要创建两个 @property 函数.

    例如 fatmulti1 中有这些角色.

    1. batlefury, 防骑, 惩戒, 需要创建 2 个函数
    2. litgoatdka, DK, 坦克 和 冰AOE, 需要创建 2 个函数
    3. litgoatssa, 术士, PvP, 需要创建 1 个函数

    这样我们可以通过调用这些 可以被搜索定位, 名字人类可理解 的函数方便的创建游戏角色的实例.
    枚举出所有账号下的所有角色的所有天赋.
    """

    @property
    def fatmulti1_batlefury_pve_protect_pala(self) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti1.value,
            name="batlefury",
            nth_char=1,
            talent=TL.paladin_pve_protect,
            window=Window.make(1),
        )

    @property
    def fatmulti1_batlefury_pve_retri_pala(self) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti1.value,
            name="batlefury",
            nth_char=1,
            talent=TL.paladin_pve_retri,
            window=Window.make(1),
        )

    @property
    def fatmulti2_quentin_pve_elemental_shaman(self) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti2.value,
            name="quentin",
            nth_char=1,
            talent=TL.shaman_pve_elemental,
            window=Window.make(2),
        )

    @property
    def fatmulti2_quentin_pve_resto_shaman(self) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti2.value,
            name="quentin",
            nth_char=1,
            talent=TL.shaman_pve_resto,
            window=Window.make(2),
        )

    @property
    def fatmulti3_opiitou_pve_balance_druid(self) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti3.value,
            name="opiitou",
            nth_char=1,
            talent=TL.druid_pve_balance,
            window=Window.make(3),
        )

    @property
    def fatmulti3_opiitou_pve_bear_druid(self) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti3.value,
            name="opiitou",
            nth_char=1,
            talent=TL.druid_pve_resto,
            window=Window.make(3),
        )

    @property
    def fatmulti4_swagsonic_pve_arcane_mage(self) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti4.value,
            name="swagsonic",
            nth_char=1,
            talent=TL.mage_pve_arcane,
            window=Window.make(4),
        )

    @property
    def fatmulti4_swagsonic_pve_fire_mage(self) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti4.value,
            name="swagsonic",
            nth_char=1,
            talent=TL.mage_pve_fire,
            window=Window.make(4),
        )

    @property
    def fatmulti5_kangliu_pve_shadow_priest(self) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti5.value,
            name="kangliu",
            nth_char=1,
            talent=TL.priest_pve_shadow,
            window=Window.make(5),
        )

    @property
    def fatmulti5_kangliu_pve_disco_priest(self) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti5.value,
            name="kangliu",
            nth_char=1,
            talent=TL.priest_pve_disco,
            window=Window.make(5),
        )

    @property
    def fitsheep_kindhearted_pve_demonology_warlock(self) -> Character:
        return Character(
            account=AccountEnum.account_fitsheep.value,
            name="kindhearted",
            nth_char=1,
            talent=TL.warlock_pve_demonology,
            window=Window.make(6),
        )

    @property
    def fitsheep_kindhearted_pvp_destruction_warlock(self) -> Character:
        return Character(
            account=AccountEnum.account_fitsheep.value,
            name="kindhearted",
            nth_char=1,
            talent=TL.warlock_pvp_destruction,
            window=Window.make(6),
        )

    @property
    def fitsheep_bordercollie_pve_shadow_priest(self) -> Character:
        return Character(
            account=AccountEnum.account_fitsheep.value,
            name="bordercollie",
            nth_char=2,
            talent=TL.priest_pve_shadow,
            window=Window.make(6),
        )

    @property
    def fitsheep_bordercollie_pve_disco_priest(self) -> Character:
        return Character(
            account=AccountEnum.account_fitsheep.value,
            name="bordercollie",
            nth_char=2,
            talent=TL.priest_pve_disco,
            window=Window.make(6),
        )

    @property
    def fatmulti6_kapacuk_pve_marksman_hunter(self) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti6.value,
            name="kapacuk",
            nth_char=1,
            talent=TL.hunter_pve_marksman,
            window=Window.make(7),
        )

    @property
    def fatmulti6_kapacuk_pvp_beast_hunter(self) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti6.value,
            name="kapacuk",
            nth_char=1,
            talent=TL.hunter_pve_beast,
            window=Window.make(7),
        )

    @property
    def fatmulti8_bunnysisters_pve_resto_druid(self) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti8.value,
            name="bunnysisters",
            nth_char=1,
            talent=TL.druid_pve_resto,
            window=Window.make(8),
        )

    @property
    def fatmulti8_bunnysisters_pve_balance_druid(self) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti8.value,
            name="bunnysisters",
            nth_char=1,
            talent=TL.druid_pve_balance,
            window=Window.make(8),
        )

    @property
    def fatmulti9_glowyy_pve_holy_pala(self) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti9.value,
            name="glowyy",
            nth_char=1,
            talent=TL.paladin_pve_holy,
            window=Window.make(9),
        )

    @property
    def fatmulti9_glowyy_pve_protect_pala(self) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti9.value,
            name="glowyy",
            nth_char=1,
            talent=TL.paladin_pve_protect,
            window=Window.make(9),
        )

    @property
    def fatmulti10_luxiaofeng_pve_blood_tank_dk(self) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti10.value,
            name="luxiaofeng",
            nth_char=1,
            talent=TL.dk_pve_blood_tank,
            window=Window.make(10),
        )

    @property
    def fatmulti10_luxiaofeng_pve_unholy_tank_dk(self) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti10.value,
            name="luxiaofeng",
            nth_char=1,
            talent=TL.dk_pve_unholy_tank,
            window=Window.make(10),
        )

    @property
    def monkey130_flydps_pve_blood_tank_dk(self) -> Character:
        return Character(
            account=AccountEnum.account_monkey130.value,
            name="flydps",
            nth_char=1,
            talent=TL.dk_pve_blood_tank,
            window=Window.make(10),
        )

    @property
    def makun7551_ganjj_pve_blood_tank_dk(self) -> Character:
        return Character(
            account=AccountEnum.account_makun7551.value,
            name="ganjj",
            nth_char=2,
            talent=TL.dk_pve_blood_tank,
            window=Window.make(10),
        )

    @property
    def makun7551_ganjj_pve_unholy_dps_dk(self) -> Character:
        return Character(
            account=AccountEnum.account_makun7551.value,
            name="ganjj",
            nth_char=2,
            talent=TL.dk_pve_unholy_dps,
            window=Window.make(10),
        )

    @property
    def makun7551_ganjj_pve_unholy_dps_dk_at_window_22(self) -> Character:
        return Character(
            account=AccountEnum.account_makun7551.value,
            name="ganjj",
            nth_char=2,
            talent=TL.dk_pve_unholy_dps,
            window=Window.make(22),
        )

    @property
    def makun7551_laoshou_protect_paladin(self) -> Character:
        return Character(
            account=AccountEnum.account_makun7551.value,
            name="laoshou",
            nth_char=1,
            talent=TL.paladin_pve_protect,
            window=Window.make(10),
        )

    @property
    def makun7551_laoshou_retri_paladin(self) -> Character:
        return Character(
            account=AccountEnum.account_makun7551.value,
            name="laoshou",
            nth_char=1,
            talent=TL.paladin_pve_retri,
            window=Window.make(10),
        )

    @property
    def makun7551_laoshou_protect_paladin_at_window_9(self) -> Character:
        return Character(
            account=AccountEnum.account_makun7551.value,
            name="laoshou",
            nth_char=1,
            talent=TL.paladin_pve_protect,
            window=Window.make(9),
        )

    @property
    def makun7551_laoshou_retri_paladin_at_window_19(self) -> Character:
        return Character(
            account=AccountEnum.account_makun7551.value,
            name="laoshou",
            nth_char=1,
            talent=TL.paladin_pve_retri,
            window=Window.make(19),
        )

    @property
    def freiliheng_stophealing_pve_blood_tank_dk(self) -> Character:
        return Character(
            account=AccountEnum.account_freiliheng.value,
            name="stophealing",
            nth_char=1,
            talent=TL.dk_pve_blood_tank,
            window=Window.make(10),
        )

    @property
    def fatmulti1_litgoatssa_pve_demo_warlock(self) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti1.value,
            name="litgoatssa",
            nth_char=2,
            talent=TL.warlock_pve_demonology,
            window=Window.make(1),
        )

    @property
    def fatmulti2_litgoatssb_pve_demo_warlock(self) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti2.value,
            name="litgoatssb",
            nth_char=2,
            talent=TL.warlock_pve_demonology,
            window=Window.make(2),
        )

    @property
    def fatmulti3_litgoatssc_pve_demo_warlock(self) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti3.value,
            name="litgoatssc",
            nth_char=2,
            talent=TL.warlock_pve_demonology,
            window=Window.make(3),
        )

    @property
    def fatmulti4_litgoatssd_pve_demo_warlock(self) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti4.value,
            name="litgoatssd",
            nth_char=2,
            talent=TL.warlock_pve_demonology,
            window=Window.make(4),
        )

    @property
    def fatmulti5_litgoatsse_pve_demo_warlock(self) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti5.value,
            name="litgoatsse",
            nth_char=2,
            talent=TL.warlock_pve_demonology,
            window=Window.make(5),
        )

    @property
    def fatmulti1_litgoatdka_pvp_frost_dk(self) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti1.value,
            name="litgoatdka",
            nth_char=4,
            talent=TL.dk_pvp_frost,
            window=Window.make(1),
        )

    @property
    def fatmulti2_litgoatdkb_pvp_frost_dk(self) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti2.value,
            name="litgoatdkb",
            nth_char=4,
            talent=TL.dk_pvp_frost,
            window=Window.make(2),
        )

    @property
    def fatmulti3_litgoatdkc_pvp_frost_dk(self) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti3.value,
            name="litgoatdkc",
            nth_char=4,
            talent=TL.dk_pvp_frost,
            window=Window.make(3),
        )

    @property
    def fatmulti4_litgoatdkd_pvp_frost_dk(self) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti4.value,
            name="litgoatdkd",
            nth_char=4,
            talent=TL.dk_pvp_frost,
            window=Window.make(4),
        )

    @property
    def fatmulti5_litgoatdke_pvp_frost_dk(self) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti5.value,
            name="litgoatdke",
            nth_char=4,
            talent=TL.dk_pvp_frost,
            window=Window.make(5),
        )

    @property
    def fatmulti1_litgoatdka_pve_blood_dk(self) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti1.value,
            name="litgoatdka",
            nth_char=4,
            talent=TL.dk_pve_unholy_dps,
            window=Window.make(1),
        )

    @property
    def fatmulti2_litgoatdkb_pve_unholy_dk(self) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti2.value,
            name="litgoatdkb",
            nth_char=4,
            talent=TL.dk_pve_unholy_dps,
            window=Window.make(2),
        )

    @property
    def fatmulti3_litgoatdkc_pve_unholy_dk(self) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti3.value,
            name="litgoatdkc",
            nth_char=4,
            talent=TL.dk_pve_unholy_dps,
            window=Window.make(3),
        )

    @property
    def fatmulti4_litgoatdkd_pve_unholy_dk(self) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti4.value,
            name="litgoatdkd",
            nth_char=4,
            talent=TL.dk_pve_unholy_dps,
            window=Window.make(4),
        )

    @property
    def fatmulti5_litgoatdke_pve_unholy_dk(self) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti5.value,
            name="litgoatdke",
            nth_char=4,
            talent=TL.dk_pve_unholy_dps,
            window=Window.make(5),
        )

    @property
    def fatmulti11_litgugua_pvp_balance_druid(self) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti11.value,
            name="litgugua",
            nth_char=1,
            talent=TL.druid_pvp_balance,
            window=Window.make(11),
        )

    @property
    def fatmulti11_litgugua_pvp_resto_druid(self) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti11.value,
            name="litgugud",
            nth_char=1,
            talent=TL.druid_pvp_resto,
            window=Window.make(11),
        )

    @property
    def fatmulti11_litgugua_pve_balance_druid(self) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti11.value,
            name="litgugua",
            nth_char=1,
            talent=TL.druid_pve_balance,
            window=Window.make(11),
        )

    @property
    def fatmulti12_litgugub_pvp_balance_druid(self) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti12.value,
            name="litgugub",
            nth_char=1,
            talent=TL.druid_pvp_balance,
            window=Window.make(12),
        )

    @property
    def fatmulti12_litgugub_pvp_resto_druid(self) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti12.value,
            name="litgugub",
            nth_char=1,
            talent=TL.druid_pvp_resto,
            window=Window.make(12),
        )

    @property
    def fatmulti12_litgugub_pve_balance_druid(self) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti12.value,
            name="litgugub",
            nth_char=1,
            talent=TL.druid_pve_balance,
            window=Window.make(12),
        )

    @property
    def fatmulti13_litguguc_pvp_balance_druid(self) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti13.value,
            name="litguguc",
            nth_char=1,
            talent=TL.druid_pvp_balance,
            window=Window.make(13),
        )

    @property
    def fatmulti13_litguguc_pvp_resto_druid(self) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti13.value,
            name="litguguc",
            nth_char=1,
            talent=TL.druid_pvp_resto,
            window=Window.make(13),
        )

    @property
    def fatmulti13_litguguc_pve_balance_druid(self) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti13.value,
            name="litguguc",
            nth_char=1,
            talent=TL.druid_pve_balance,
            window=Window.make(13),
        )

    @property
    def fatmulti14_litgugud_pvp_balancce_druid(self) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti14.value,
            name="litgugud",
            nth_char=1,
            talent=TL.druid_pvp_balance,
            window=Window.make(14),
        )

    @property
    def fatmulti14_litgugud_pvp_resto_druid(self) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti14.value,
            name="litgugud",
            nth_char=1,
            talent=TL.druid_pvp_resto,
            window=Window.make(14),
        )

    @property
    def fatmulti14_litgugud_pve_balance_druid(self) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti14.value,
            name="litgugud",
            nth_char=1,
            talent=TL.druid_pve_balance,
            window=Window.make(14),
        )

    @property
    def fatmulti15_litgugue_pvp_balance_druid(self) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti15.value,
            name="litgugue",
            nth_char=1,
            talent=TL.druid_pvp_balance,
            window=Window.make(11),
        )

    @property
    def fatmulti16_litguguf_pvp_balance_druid(self) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti16.value,
            name="litguguf",
            nth_char=1,
            talent=TL.druid_pvp_balance,
            window=Window.make(12),
        )

    @property
    def fatmulti17_litgugug_pvp_balance_druid(self) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti17.value,
            name="litgugug",
            nth_char=1,
            talent=TL.druid_pvp_balance,
            window=Window.make(13),
        )

    @property
    def fatmulti18_litguguh_pvp_balance_druid(self) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti18.value,
            name="litguguh",
            nth_char=1,
            talent=TL.druid_pvp_balance,
            window=Window.make(14),
        )

    @property
    def fatmulti18_litguguh_pvp_resto_druid(self) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti18.value,
            name="litguguh",
            nth_char=1,
            talent=TL.druid_pvp_resto,
            window=Window.make(14),
        )

    @property
    def fatmulti19_lgmsi_pve_shadow_priest(self) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti19.value,
            name="lgmsi",
            nth_char=1,
            talent=TL.priest_pve_shadow,
            window=Window.make(15),
        )

    @property
    def fatmulti19_lgmsi_pve_disco_priest(self) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti19.value,
            name="lgmsi",
            nth_char=1,
            talent=TL.priest_pve_disco,
            window=Window.make(15),
        )

    @property
    def fatmulti20_lgmsj_pve_shadow_priest(self) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti20.value,
            name="lgmsj",
            nth_char=1,
            talent=TL.priest_pve_shadow,
            window=Window.make(16),
        )

    @property
    def fatmulti20_lgmsj_pve_disco_priest(self) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti20.value,
            name="lgmsj",
            nth_char=1,
            talent=TL.priest_pve_disco,
            window=Window.make(16),
        )

    @property
    def fatmulti21_lgmsk_pve_shadow_priest(self) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti21.value,
            name="lgmsk",
            nth_char=1,
            talent=TL.priest_pve_shadow,
            window=Window.make(17),
        )

    @property
    def fatmulti21_lgmsk_pve_holy_priest(self) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti21.value,
            name="lgmsk",
            nth_char=1,
            talent=TL.priest_pve_holy,
            window=Window.make(17),
        )

    @property
    def fatmulti22_lgmsl_pve_shadow_priest(self) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti22.value,
            name="lgmsl",
            nth_char=1,
            talent=TL.priest_pve_shadow,
            window=Window.make(18),
        )

    @property
    def fatmulti22_lgmsl_pve_holy_priest(self) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti22.value,
            name="lgmsl",
            nth_char=1,
            talent=TL.priest_pve_holy,
            window=Window.make(18),
        )

    @property
    def fatmulti23_lgsmm_pve_elemental_shaman(self) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti23.value,
            name="lgsmm",
            nth_char=1,
            talent=TL.shaman_pve_elemental,
            window=Window.make(19),
        )

    @property
    def fatmulti23_lgsmm_pve_resto_shaman(self) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti23.value,
            name="lgsmm",
            nth_char=1,
            talent=TL.shaman_pve_resto,
            window=Window.make(19),
        )

    @property
    def fatmulti24_lgsmn_pve_elemental_shaman(self) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti24.value,
            name="lgsmn",
            nth_char=1,
            talent=TL.shaman_pve_elemental,
            window=Window.make(20),
        )

    @property
    def fatmulti24_lgsmn_pve_resto_shaman(self) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti24.value,
            name="lgsmn",
            nth_char=1,
            talent=TL.shaman_pve_resto,
            window=Window.make(20),
        )

    @property
    def fatmulti25_lgsmo_pve_elemental_shaman(self) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti25.value,
            name="lgsmo",
            nth_char=1,
            talent=TL.shaman_pve_elemental,
            window=Window.make(21),
        )

    @property
    def fatmulti25_lgsmo_pve_resto_shaman(self) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti25.value,
            name="lgsmo",
            nth_char=1,
            talent=TL.shaman_pve_resto,
            window=Window.make(21),
        )

    @property
    def fatmulti26_lgsmp_pve_elemental_shaman(self) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti26.value,
            name="lgsmp",
            nth_char=1,
            talent=TL.shaman_pve_elemental,
            window=Window.make(22),
        )

    @property
    def fatmulti26_lgsmp_pve_resto_shaman(self) -> Character:
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
    @property
    def fatmulti1_lgqsa_pve_protect_pala(self) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti1.value,
            name="lgqsa",
            nth_char=1,
            talent=TL.paladin_pve_protect,
            window=Window.make(1),
        )

    @property
    def fatmulti2_lgqsb_pve_retri_pala(self) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti2.value,
            name="lgqsb",
            nth_char=1,
            talent=TL.paladin_pve_retri,
            window=Window.make(2),
        )

    @property
    def fatmulti3_lgqsc_pve_retri_pala(self) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti3.value,
            name="lgqsc",
            nth_char=1,
            talent=TL.paladin_pve_retri,
            window=Window.make(3),
        )

    @property
    def fatmulti4_lgqsd_pve_retri_pala(self) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti4.value,
            name="lgqsd",
            nth_char=1,
            talent=TL.paladin_pve_retri,
            window=Window.make(4),
        )

    @property
    def fatmulti5_lgqse_pve_holy_pala(self) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti5.value,
            name="lgqse",
            nth_char=1,
            talent=TL.paladin_pve_holy,
            window=Window.make(5),
        )


char_fact = CharacterFactory()


class CharacterGroup:
    @property
    def window_1_to_9_batlefury_to_glowyy(self) -> OrderedSet[Character]:
        return OrderedSet([
            char_fact.fatmulti1_batlefury_pve_protect_pala,
            char_fact.fatmulti2_quentin_pve_elemental_shaman,
            char_fact.fatmulti3_opiitou_pve_balance_druid,
            char_fact.fatmulti4_swagsonic_pve_arcane_mage,
            char_fact.fatmulti5_kangliu_pve_shadow_priest,
            char_fact.fitsheep_kindhearted_pve_demonology_warlock,
            char_fact.fatmulti6_kapacuk_pve_marksman_hunter,
            char_fact.fatmulti8_bunnysisters_pve_resto_druid,
            char_fact.fatmulti9_glowyy_pve_holy_pala,
        ])

    @property
    def window_10_luxiaofeng(self) -> OrderedSet[Character]:
        return OrderedSet([
            char_fact.fatmulti10_luxiaofeng_pve_blood_tank_dk,
        ])

    @property
    def window_10_ganjj(self) -> OrderedSet[Character]:
        return OrderedSet([
            char_fact.makun7551_ganjj_pve_blood_tank_dk,
        ])

    @property
    def window_10_flydps(self) -> OrderedSet[Character]:
        return OrderedSet([
            char_fact.monkey130_flydps_pve_blood_tank_dk,
        ])

    @property
    def window_11_to_14_litgugu_abcd(self) -> OrderedSet[Character]:
        return OrderedSet([
            char_fact.fatmulti11_litgugua_pve_balance_druid,
            char_fact.fatmulti12_litgugub_pve_balance_druid,
            char_fact.fatmulti13_litguguc_pve_balance_druid,
            char_fact.fatmulti14_litgugud_pve_balance_druid,
        ])

    @property
    def window_11_to_14_litgugu_efgh(self) -> OrderedSet[Character]:
        return OrderedSet([
            char_fact.fatmulti15_litgugue_pvp_balance_druid,
            char_fact.fatmulti16_litguguf_pvp_balance_druid,
            char_fact.fatmulti17_litgugug_pvp_balance_druid,
            char_fact.fatmulti18_litguguh_pvp_balance_druid,
        ])

    @property
    def window_15_to_18_lgms_ijkl(self) -> OrderedSet[Character]:
        return OrderedSet([
            char_fact.fatmulti19_lgmsi_pve_shadow_priest,
            char_fact.fatmulti20_lgmsj_pve_shadow_priest,
            char_fact.fatmulti21_lgmsk_pve_shadow_priest,
            char_fact.fatmulti22_lgmsl_pve_shadow_priest,
        ])

    @property
    def window_19_to_22_lgsm_mnop(self) -> OrderedSet[Character]:
        return OrderedSet([
            char_fact.fatmulti23_lgsmm_pve_elemental_shaman,
            char_fact.fatmulti24_lgsmn_pve_elemental_shaman,
            char_fact.fatmulti25_lgsmo_pve_elemental_shaman,
            char_fact.fatmulti26_lgsmp_pve_elemental_shaman,
        ])


char_group = CharacterGroup()
