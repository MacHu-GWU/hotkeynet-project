# -*- coding: utf-8 -*-

import attr

from .credentials import Credential, Credentials
from .talent import Talent


@attr.s
class Character:
    """
    :param credential:
    :param window_index: 你将在哪个窗口玩这个人物
    :param leader1_window_index: 多开时模式 1 下的焦点角色所在的窗口序号
    :param leader2_window_index: 多开时模式 2 下的焦点角色所在的窗口序号
    """
    credential = attr.ib(default=None)  # type: Credential
    talent = attr.ib(default=None)  # type: Talent
    window_index = attr.ib(default=None)  # type: int
    leader1_window_index = attr.ib(default=None)  # type: int
    leader2_window_index = attr.ib(default=None)  # type: int

    def evolve(self,
               window_index: int=None,
               leader1_window_index: int=None,
               leader2_window_index: int=None,
               credential: Credential=None,
               talent: Talent=None) -> 'Character':
        kwargs = dict(
            window_index=window_index,
            leader1_window_index=leader1_window_index,
            leader2_window_index=leader2_window_index,
            credential=credential,
            talent=talent,
        )
        kwargs = {
            k: v
            for k, v in kwargs.items() if v is not None
        }
        return attr.evolve(self, **kwargs)


class CharacterFactory:
    @classmethod
    def make_char_fatmulti1_batlefury_pve_protect_pala(cls) -> Character:
        return Character(
            credential=Credentials.cred_fatmulti1,
            talent=Talent.paladin_pve_protect,
        )

    @classmethod
    def make_char_fatmulti1_batlefury_pve_retri_pala(cls) -> Character:
        return Character(
            credential=Credentials.cred_fatmulti1,
            talent=Talent.paladin_pve_retri,
        )

    @classmethod
    def make_char_fatmulti2_quentin_pve_elemental_shaman(cls) -> Character:
        return Character(
            credential=Credentials.cred_fatmulti2,
            talent=Talent.shaman_pve_elemental,
        )

    @classmethod
    def make_char_fatmulti2_quentin_pve_resto_shaman(cls) -> Character:
        return Character(
            credential=Credentials.cred_fatmulti2,
            talent=Talent.shaman_pve_resto,
        )

    @classmethod
    def make_char_fatmulti3_opiitou_pve_balance_druid(cls) -> Character:
        return Character(
            credential=Credentials.cred_fatmulti3,
            talent=Talent.druid_pve_balance,
        )

    @classmethod
    def make_char_fatmulti3_opiitou_pve_resto_druid(cls) -> Character:
        return Character(
            credential=Credentials.cred_fatmulti3,
            talent=Talent.druid_pve_resto,
        )

    @classmethod
    def make_char_fatmulti4_swagsonic_pve_arcane_mage(cls) -> Character:
        return Character(
            credential=Credentials.cred_fatmulti4,
            talent=Talent.mage_pve_arcane,
        )

    @classmethod
    def make_char_fatmulti4_swagsonic_pve_fire_mage(cls) -> Character:
        return Character(
            credential=Credentials.cred_fatmulti4,
            talent=Talent.mage_pve_fire,
        )

    @classmethod
    def make_char_fatmulti5_kangliu_pve_shadow_priest(cls) -> Character:
        return Character(
            credential=Credentials.cred_fatmulti5,
            talent=Talent.priest_pve_shadow,
        )

    @classmethod
    def make_char_fatmulti5_kangliu_pve_disco_priest(cls) -> Character:
        return Character(
            credential=Credentials.cred_fatmulti5,
            talent=Talent.priest_pve_disco,
        )

    @classmethod
    def make_char_fitsheep_kindhearted_pve_demonology_warlock(cls) -> Character:
        return Character(
            credential=Credentials.cred_fitsheep,
            talent=Talent.warlock_pve_demonology,
        )

    @classmethod
    def make_char_fitsheep_kindhearted_pvp_destruction_warlock(cls) -> Character:
        return Character(
            credential=Credentials.cred_fitsheep,
            talent=Talent.warlock_pvp_destruction,
        )

    @classmethod
    def make_char_fatmulti6_kapacuk_pve_marksman_hunter(cls) -> Character:
        return Character(
            credential=Credentials.cred_fatmulti6,
            talent=Talent.hunter_pve_marksman,
        )

    @classmethod
    def make_char_fatmulti6_kapacuk_pvp_beast_hunter(cls) -> Character:
        return Character(
            credential=Credentials.cred_fatmulti6,
            talent=Talent.hunter_pve_beast,
        )

    @classmethod
    def make_char_fatmulti8_bunnysisters_pve_resto_druid(cls) -> Character:
        return Character(
            credential=Credentials.cred_fatmulti8,
            talent=Talent.druid_pve_resto,
        )

    @classmethod
    def make_char_fatmulti8_bunnysisters_pve_balance_druid(cls) -> Character:
        return Character(
            credential=Credentials.cred_fatmulti8,
            talent=Talent.druid_pve_balance,
        )

    @classmethod
    def make_char_fatmulti9_glowyy_pve_holy_pala(cls) -> Character:
        return Character(
            credential=Credentials.cred_fatmulti9,
            talent=Talent.paladin_pve_holy,
        )

    @classmethod
    def make_char_fatmulti9_glowyy_pve_protect_pala(cls) -> Character:
        return Character(
            credential=Credentials.cred_fatmulti9,
            talent=Talent.paladin_pve_protect,
        )

    @classmethod
    def make_char_monkey130_flydps_pve_blood_tank_dk(cls) -> Character:
        return Character(
            credential=Credentials.cred_monkey130,
            talent=Talent.dk_pve_blood_tank,
        )

    @classmethod
    def make_char_fatmulti1_litgoatssa_pve_demo_warlock(cls) -> Character:
        return Character(
            credential=Credentials.cred_fatmulti1,
            talent=Talent.warlock_pve_demonology,
        )

    @classmethod
    def make_char_fatmulti2_litgoatssb_pve_demo_warlock(cls) -> Character:
        return Character(
            credential=Credentials.cred_fatmulti2,
            talent=Talent.warlock_pve_demonology,
        )

    @classmethod
    def make_char_fatmulti3_litgoatssc_pve_demo_warlock(cls) -> Character:
        return Character(
            credential=Credentials.cred_fatmulti3,
            talent=Talent.warlock_pve_demonology,
        )

    @classmethod
    def make_char_fatmulti4_litgoatssd_pve_demo_warlock(cls) -> Character:
        return Character(
            credential=Credentials.cred_fatmulti4,
            talent=Talent.warlock_pve_demonology,
        )

    @classmethod
    def make_char_fatmulti5_litgoatsse_pve_demo_warlock(cls) -> Character:
        return Character(
            credential=Credentials.cred_fatmulti5,
            talent=Talent.warlock_pve_demonology,
        )

    @classmethod
    def make_char_fatmulti1_litgoatdka_pvp_frost_dk(cls) -> Character:
        return Character(
            credential=Credentials.cred_fatmulti1,
            talent=Talent.dk_pvp_frost,
        )

    @classmethod
    def make_char_fatmulti2_litgoatdkb_pvp_frost_dk(cls) -> Character:
        return Character(
            credential=Credentials.cred_fatmulti2,
            talent=Talent.dk_pvp_frost,
        )

    @classmethod
    def make_char_fatmulti3_litgoatdkc_pvp_frost_dk(cls) -> Character:
        return Character(
            credential=Credentials.cred_fatmulti3,
            talent=Talent.dk_pvp_frost,
        )

    @classmethod
    def make_char_fatmulti4_litgoatdkd_pvp_frost_dk(cls) -> Character:
        return Character(
            credential=Credentials.cred_fatmulti4,
            talent=Talent.dk_pvp_frost,
        )

    @classmethod
    def make_char_fatmulti5_litgoatdke_pvp_frost_dk(cls) -> Character:
        return Character(
            credential=Credentials.cred_fatmulti5,
            talent=Talent.dk_pvp_frost,
        )
