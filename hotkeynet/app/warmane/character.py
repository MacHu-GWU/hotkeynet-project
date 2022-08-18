# -*- coding: utf-8 -*-

import enum

from hotkeynet.game.wow.wlk.talent_category_association import (
    Talent as TL,
    TalentCategory as TC,
    get_talent_by_category,
    get_category_by_talent,
)
from hotkeynet.game.wow.model import Character

from .account import AccountEnum, AccountHelper
from .window import WindowEnum, WindowHelper


class CharacterFactory:
    @classmethod
    def make_char_fatmulti1_batlefury_pve_protect_pala(cls) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti1.value,
            name="batlefury",
            talent=TL.paladin_pve_protect,
            window=WindowHelper.get_window(1),
        )

    @classmethod
    def make_char_fatmulti1_batlefury_pve_retri_pala(cls) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti1.value,
            name="batlefury",
            talent=TL.paladin_pve_retri,
            window=WindowHelper.get_window(1),
        )

    @classmethod
    def make_char_fatmulti2_quentin_pve_elemental_shaman(cls) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti2.value,
            name="quentin",
            talent=TL.shaman_pve_elemental,
            window=WindowHelper.get_window(2),
        )

    @classmethod
    def make_char_fatmulti2_quentin_pve_resto_shaman(cls) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti2.value,
            name="quentin",
            talent=TL.shaman_pve_resto,
            window=WindowHelper.get_window(2),
        )

    @classmethod
    def make_char_fatmulti3_opiitou_pve_balance_druid(cls) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti3.value,
            name="opiitou",
            talent=TL.druid_pve_balance,
            window=WindowHelper.get_window(3),
        )

    @classmethod
    def make_char_fatmulti3_opiitou_pve_bear_druid(cls) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti3.value,
            name="opiitou",
            talent=TL.druid_pve_resto,
            window=WindowHelper.get_window(3),
        )

    @classmethod
    def make_char_fatmulti4_swagsonic_pve_arcane_mage(cls) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti4.value,
            name="swagsonic",
            talent=TL.mage_pve_arcane,
            window=WindowHelper.get_window(4),
        )

    @classmethod
    def make_char_fatmulti4_swagsonic_pve_fire_mage(cls) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti4.value,
            name="swagsonic",
            talent=TL.mage_pve_fire,
            window=WindowHelper.get_window(4),
        )

    @classmethod
    def make_char_fatmulti5_kangliu_pve_shadow_priest(cls) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti5.value,
            name="kangliu",
            talent=TL.priest_pve_shadow,
            window=WindowHelper.get_window(5),
        )

    @classmethod
    def make_char_fatmulti5_kangliu_pve_disco_priest(cls) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti5.value,
            name="kangliu",
            talent=TL.priest_pve_disco,
            window=WindowHelper.get_window(5),
        )

    @classmethod
    def make_char_fitsheep_kindhearted_pve_demonology_warlock(cls) -> Character:
        return Character(
            account=AccountEnum.account_fitsheep.value,
            name="kindhearted",
            talent=TL.warlock_pve_demonology,
            window=WindowHelper.get_window(6),
        )

    @classmethod
    def make_char_fitsheep_kindhearted_pvp_destruction_warlock(cls) -> Character:
        return Character(
            account=AccountEnum.account_fitsheep.value,
            name="kindhearted",
            talent=TL.warlock_pvp_destruction,
            window=WindowHelper.get_window(6),
        )

    @classmethod
    def make_char_fitsheep_bordercollie_pve_shadow_priest(cls) -> Character:
        return Character(
            account=AccountEnum.account_fitsheep.value,
            name="bordercollie",
            talent=TL.priest_pve_shadow,
            window=WindowHelper.get_window(6),
        )

    @classmethod
    def make_char_fitsheep_bordercollie_pve_disco_priest(cls) -> Character:
        return Character(
            account=AccountEnum.account_fitsheep.value,
            name="bordercollie",
            talent=TL.priest_pve_disco,
            window=WindowHelper.get_window(6),
        )

    @classmethod
    def make_char_fatmulti6_kapacuk_pve_marksman_hunter(cls) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti6.value,
            name="kapacuk",
            talent=TL.hunter_pve_marksman,
            window=WindowHelper.get_window(7),
        )

    @classmethod
    def make_char_fatmulti6_kapacuk_pvp_beast_hunter(cls) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti6.value,
            name="kapacuk",
            talent=TL.hunter_pve_beast,
            window=WindowHelper.get_window(7),
        )

    @classmethod
    def make_char_fatmulti8_bunnysisters_pve_resto_druid(cls) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti8.value,
            name="bunnysisters",
            talent=TL.druid_pve_resto,
            window=WindowHelper.get_window(8),
        )

    @classmethod
    def make_char_fatmulti8_bunnysisters_pve_balance_druid(cls) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti8.value,
            name="bunnysisters",
            talent=TL.druid_pve_balance,
            window=WindowHelper.get_window(8),
        )

    @classmethod
    def make_char_fatmulti9_glowyy_pve_holy_pala(cls) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti9.value,
            name="glowyy",
            talent=TL.paladin_pve_holy,
            window=WindowHelper.get_window(9),
        )

    @classmethod
    def make_char_fatmulti9_glowyy_pve_protect_pala(cls) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti9.value,
            name="glowyy",
            talent=TL.paladin_pve_protect,
            window=WindowHelper.get_window(9),
        )

    @classmethod
    def make_char_fatmulti10_luxiaofeng_pve_blood_tank_dk(cls) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti10.value,
            name="luxiaofeng",
            talent=TL.dk_pve_blood_tank,
            window=WindowHelper.get_window(10),
        )

    @classmethod
    def make_char_fatmulti10_luxiaofeng_pve_unholy_tank_dk(cls) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti10.value,
            name="luxiaofeng",
            talent=TL.dk_pve_unholy_tank,
            window=WindowHelper.get_window(10),
        )

    @classmethod
    def make_char_monkey130_flydps_pve_blood_tank_dk(cls) -> Character:
        return Character(
            account=AccountEnum.account_monkey130.value,
            name="flydps",
            talent=TL.dk_pve_blood_tank,
            window=WindowHelper.get_window(10),
        )

    @classmethod
    def make_char_makun7551_ganjj_pve_blood_tank_dk(cls) -> Character:
        return Character(
            account=AccountEnum.account_makun7551.value,
            name="ganjj",
            talent=TL.dk_pve_blood_tank,
            window=WindowHelper.get_window(10),
        )

    @classmethod
    def make_char_makun7551_ganjj_pve_unholy_dps_dk(cls) -> Character:
        return Character(
            account=AccountEnum.account_makun7551.value,
            name="ganjj",
            talent=TL.dk_pve_unholy_dps,
            window=WindowHelper.get_window(10),
        )

    @classmethod
    def make_char_makun7551_ganjj_pve_unholy_dps_dk_at_window_22(cls) -> Character:
        return Character(
            account=AccountEnum.account_makun7551.value,
            name="ganjj",
            talent=TL.dk_pve_unholy_dps,
            window=WindowHelper.get_window(22),
        )

    @classmethod
    def make_char_makun7551_laoshou_protect_paladin(cls) -> Character:
        return Character(
            account=AccountEnum.account_makun7551.value,
            name="laoshou",
            talent=TL.paladin_pve_protect,
            window=WindowHelper.get_window(10),
        )

    @classmethod
    def make_char_makun7551_laoshou_retri_paladin(cls) -> Character:
        return Character(
            account=AccountEnum.account_makun7551.value,
            name="laoshou",
            talent=TL.paladin_pve_retri,
            window=WindowHelper.get_window(10),
        )

    @classmethod
    def make_char_makun7551_laoshou_protect_paladin_at_window_9(cls) -> Character:
        return Character(
            account=AccountEnum.account_makun7551.value,
            name="laoshou",
            talent=TL.paladin_pve_protect,
            window=WindowHelper.get_window(9),
        )

    @classmethod
    def make_char_makun7551_laoshou_retri_paladin_at_window_19(cls) -> Character:
        return Character(
            account=AccountEnum.account_makun7551.value,
            name="laoshou",
            talent=TL.paladin_pve_retri,
            window=WindowHelper.get_window(19),
        )

    @classmethod
    def make_char_freiliheng_stophealing_pve_blood_tank_dk(cls) -> Character:
        return Character(
            account=AccountEnum.account_freiliheng.value,
            name="stophealing",
            talent=TL.dk_pve_blood_tank,
            window=WindowHelper.get_window(10),
        )

    # --- litgoat ss
    @classmethod
    def make_char_fatmulti1_litgoatssa_pve_demo_warlock(cls) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti1.value,
            name="litgoatssa",
            talent=TL.warlock_pve_demonology,
            window=WindowHelper.get_window(1),
        )

    @classmethod
    def make_char_fatmulti2_litgoatssb_pve_demo_warlock(cls) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti2.value,
            name="litgoatssb",
            talent=TL.warlock_pve_demonology,
            window=WindowHelper.get_window(2),
        )

    @classmethod
    def make_char_fatmulti3_litgoatssc_pve_demo_warlock(cls) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti3.value,
            name="litgoatssc",
            talent=TL.warlock_pve_demonology,
            window=WindowHelper.get_window(3),
        )

    @classmethod
    def make_char_fatmulti4_litgoatssd_pve_demo_warlock(cls) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti4.value,
            name="litgoatssd",
            talent=TL.warlock_pve_demonology,
            window=WindowHelper.get_window(4),
        )

    @classmethod
    def make_char_fatmulti5_litgoatsse_pve_demo_warlock(cls) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti5.value,
            name="litgoatsse",
            talent=TL.warlock_pve_demonology,
            window=WindowHelper.get_window(5),
        )

    # --- litgoat dk
    @classmethod
    def make_char_fatmulti1_litgoatdka_pvp_frost_dk(cls) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti1.value,
            name="litgoatdka",
            talent=TL.dk_pvp_frost,
            window=WindowHelper.get_window(1),
        )

    @classmethod
    def make_char_fatmulti2_litgoatdkb_pvp_frost_dk(cls) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti2.value,
            name="litgoatdkb",
            talent=TL.dk_pvp_frost,
            window=WindowHelper.get_window(2),
        )

    @classmethod
    def make_char_fatmulti3_litgoatdkc_pvp_frost_dk(cls) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti3.value,
            name="litgoatdkc",
            talent=TL.dk_pvp_frost,
            window=WindowHelper.get_window(3),
        )

    @classmethod
    def make_char_fatmulti4_litgoatdkd_pvp_frost_dk(cls) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti4.value,
            name="litgoatdkd",
            talent=TL.dk_pvp_frost,
            window=WindowHelper.get_window(4),
        )

    @classmethod
    def make_char_fatmulti5_litgoatdke_pvp_frost_dk(cls) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti5.value,
            name="litgoatdke",
            talent=TL.dk_pvp_frost,
            window=WindowHelper.get_window(5),
        )

    @classmethod
    def make_char_fatmulti1_litgoatdka_pve_blood_dk(cls) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti1.value,
            name="litgoatdka",
            talent=TL.dk_pve_unholy_dps,
            window=WindowHelper.get_window(1),
        )

    @classmethod
    def make_char_fatmulti2_litgoatdkb_pve_unholy_dk(cls) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti2.value,
            name="litgoatdkb",
            talent=TL.dk_pve_unholy_dps,
            window=WindowHelper.get_window(2),
        )

    @classmethod
    def make_char_fatmulti3_litgoatdkc_pve_unholy_dk(cls) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti3.value,
            name="litgoatdkc",
            talent=TL.dk_pve_unholy_dps,
            window=WindowHelper.get_window(3),
        )

    @classmethod
    def make_char_fatmulti4_litgoatdkd_pve_unholy_dk(cls) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti4.value,
            name="litgoatdkd",
            talent=TL.dk_pve_unholy_dps,
            window=WindowHelper.get_window(4),
        )

    @classmethod
    def make_char_fatmulti5_litgoatdke_pve_unholy_dk(cls) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti5.value,
            name="litgoatdke",
            talent=TL.dk_pve_unholy_dps,
            window=WindowHelper.get_window(5),
        )

    # --- litgugu abcd
    @classmethod
    def make_char_fatmulti11_litgugua_pvp_balance_druid(cls) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti11.value,
            name="litgugua",
            talent=TL.druid_pvp_balance,
            window=WindowHelper.get_window(11),
        )

    @classmethod
    def make_char_fatmulti11_litgugua_pvp_resto_druid(cls) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti11.value,
            name="litgugud",
            talent=TL.druid_pvp_resto,
            window=WindowHelper.get_window(11),
        )

    @classmethod
    def make_char_fatmulti11_litgugua_pve_balance_druid(cls) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti11.value,
            name="litgugua",
            talent=TL.druid_pve_balance,
            window=WindowHelper.get_window(11),
        )

    @classmethod
    def make_char_fatmulti12_litgugub_pvp_balance_druid(cls) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti12.value,
            name="litgugub",
            talent=TL.druid_pvp_balance,
            window=WindowHelper.get_window(12),
        )

    @classmethod
    def make_char_fatmulti12_litgugub_pvp_resto_druid(cls) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti12.value,
            name="litgugub",
            talent=TL.druid_pvp_resto,
            window=WindowHelper.get_window(12),
        )

    @classmethod
    def make_char_fatmulti12_litgugub_pve_balance_druid(cls) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti12.value,
            name="litgugub",
            talent=TL.druid_pve_balance,
            window=WindowHelper.get_window(12),
        )

    @classmethod
    def make_char_fatmulti13_litguguc_pvp_balance_druid(cls) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti13.value,
            name="litguguc",
            talent=TL.druid_pvp_balance,
            window=WindowHelper.get_window(13),
        )

    @classmethod
    def make_char_fatmulti13_litguguc_pvp_resto_druid(cls) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti13.value,
            name="litguguc",
            talent=TL.druid_pvp_resto,
            window=WindowHelper.get_window(13),
        )

    @classmethod
    def make_char_fatmulti13_litguguc_pve_balance_druid(cls) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti13.value,
            name="litguguc",
            talent=TL.druid_pve_balance,
            window=WindowHelper.get_window(13),
        )

    @classmethod
    def make_char_fatmulti14_litgugud_pvp_balancce_druid(cls) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti14.value,
            name="litgugud",
            talent=TL.druid_pvp_balance,
            window=WindowHelper.get_window(14),
        )

    @classmethod
    def make_char_fatmulti14_litgugud_pvp_resto_druid(cls) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti14.value,
            name="litgugud",
            talent=TL.druid_pvp_resto,
            window=WindowHelper.get_window(14),
        )

    @classmethod
    def make_char_fatmulti14_litgugud_pve_balance_druid(cls) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti14.value,
            name="litgugud",
            talent=TL.druid_pve_balance,
            window=WindowHelper.get_window(14),
        )

    # --- litgugu e, f, g, h
    @classmethod
    def make_char_fatmulti15_litgugue_pvp_balance_druid(cls) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti15.value,
            name="litgugue",
            talent=TL.druid_pvp_balance,
            window=WindowHelper.get_window(11),
        )

    @classmethod
    def make_char_fatmulti16_litguguf_pvp_balance_druid(cls) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti16.value,
            name="litguguf",
            talent=TL.druid_pvp_balance,
            window=WindowHelper.get_window(12),
        )

    @classmethod
    def make_char_fatmulti17_litgugug_pvp_balance_druid(cls) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti17.value,
            name="litgugug",
            talent=TL.druid_pvp_balance,
            window=WindowHelper.get_window(13),
        )

    @classmethod
    def make_char_fatmulti18_litguguh_pvp_balance_druid(cls) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti18.value,
            name="litguguh",
            talent=TL.druid_pvp_balance,
            window=WindowHelper.get_window(14),
        )

    @classmethod
    def make_char_fatmulti18_litguguh_pvp_resto_druid(cls) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti18.value,
            name="litguguh",
            talent=TL.druid_pvp_resto,
            window=WindowHelper.get_window(14),
        )

    # --- lg ms i, j, k, l
    @classmethod
    def make_char_fatmulti19_lgmsi_pve_shadow_priest(cls) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti19.value,
            name="lgmsi",
            talent=TL.priest_pve_shadow,
            window=WindowHelper.get_window(15),
        )

    @classmethod
    def make_char_fatmulti19_lgmsi_pve_disco_priest(cls) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti19.value,
            name="lgmsi",
            talent=TL.priest_pve_disco,
            window=WindowHelper.get_window(15),
        )

    @classmethod
    def make_char_fatmulti20_lgmsj_pve_shadow_priest(cls) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti20.value,
            name="lgmsj",
            talent=TL.priest_pve_shadow,
            window=WindowHelper.get_window(16),
        )

    @classmethod
    def make_char_fatmulti20_lgmsj_pve_disco_priest(cls) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti20.value,
            name="lgmsj",
            talent=TL.priest_pve_disco,
            window=WindowHelper.get_window(16),
        )

    @classmethod
    def make_char_fatmulti21_lgmsk_pve_shadow_priest(cls) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti21.value,
            name="lgmsk",
            talent=TL.priest_pve_shadow,
            window=WindowHelper.get_window(17),
        )

    @classmethod
    def make_char_fatmulti21_lgmsk_pve_holy_priest(cls) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti21.value,
            name="lgmsk",
            talent=TL.priest_pve_holy,
            window=WindowHelper.get_window(17),
        )

    @classmethod
    def make_char_fatmulti22_lgmsl_pve_shadow_priest(cls) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti22.value,
            name="lgmsl",
            talent=TL.priest_pve_shadow,
            window=WindowHelper.get_window(18),
        )

    @classmethod
    def make_char_fatmulti22_lgmsl_pve_holy_priest(cls) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti22.value,
            name="lgmsl",
            talent=TL.priest_pve_holy,
            window=WindowHelper.get_window(18),
        )

    # --- lg sm m, n, o, p
    @classmethod
    def make_char_fatmulti23_lgsmm_pve_elemental_shaman(cls) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti23.value,
            name="lgsmm",
            talent=TL.shaman_pve_elemental,
            window=WindowHelper.get_window(19),
        )

    @classmethod
    def make_char_fatmulti23_lgsmm_pve_resto_shaman(cls) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti23.value,
            name="lgsmm",
            talent=TL.shaman_pve_resto,
            window=WindowHelper.get_window(19),
        )

    @classmethod
    def make_char_fatmulti24_lgsmn_pve_elemental_shaman(cls) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti24.value,
            name="lgsmn",
            talent=TL.shaman_pve_elemental,
            window=WindowHelper.get_window(20),
        )

    @classmethod
    def make_char_fatmulti24_lgsmn_pve_resto_shaman(cls) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti24.value,
            name="lgsmn",
            talent=TL.shaman_pve_resto,
            window=WindowHelper.get_window(20),
        )

    @classmethod
    def make_char_fatmulti25_lgsmo_pve_elemental_shaman(cls) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti25.value,
            name="lgsmo",
            talent=TL.shaman_pve_elemental,
            window=WindowHelper.get_window(21),
        )

    @classmethod
    def make_char_fatmulti25_lgsmo_pve_resto_shaman(cls) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti25.value,
            name="lgsmo",
            talent=TL.shaman_pve_resto,
            window=WindowHelper.get_window(21),
        )

    @classmethod
    def make_char_fatmulti26_lgsmp_pve_elemental_shaman(cls) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti26.value,
            name="lgsmp",
            talent=TL.shaman_pve_elemental,
            window=WindowHelper.get_window(22),
        )

    @classmethod
    def make_char_fatmulti26_lgsmp_pve_resto_shaman(cls) -> Character:
        return Character(
            account=AccountEnum.account_fatmulti26.value,
            name="lgsmp",
            talent=TL.shaman_pve_resto,
            window=WindowHelper.get_window(22),
        )
