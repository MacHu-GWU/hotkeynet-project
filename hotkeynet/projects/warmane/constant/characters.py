# -*- coding: utf-8 -*-

import attr

from .credentials import Credential, Credentials
from .talent import Talent
from .windows import window_index


@attr.s
class Character:
    """
    :param credential:
    :param window_index: 你将在哪个窗口玩这个人物
    :param leader1_window_index: 多开时模式 1 下的焦点角色所在的窗口序号
    :param leader2_window_index: 多开时模式 2 下的焦点角色所在的窗口序号
    """
    credential = attr.ib(default=None)  # type: Credential
    name = attr.ib(default=None)  # type: str
    talent = attr.ib(default=None)  # type: Talent
    window_index = attr.ib(default=None)  # type: int
    leader1_window_index = attr.ib(default=None)  # type: int
    leader2_window_index = attr.ib(default=None)  # type: int
    is_tank1 = attr.ib(default=False)  # type: bool
    is_tank2 = attr.ib(default=False)  # type: bool
    is_dr_pala1 = attr.ib(default=False)  # type: bool
    is_dr_pala2 = attr.ib(default=False)  # type: bool

    def evolve(self,
               window_index: int = None,
               leader1_window_index: int = None,
               leader2_window_index: int = None,
               credential: Credential = None,
               talent: Talent = None,
               is_tank1: bool = None,
               is_tank2: bool = None,
               is_dr_pala1: bool = None,
               is_dr_pala2: bool = None) -> 'Character':
        kwargs = dict(
            window_index=window_index,
            leader1_window_index=leader1_window_index,
            leader2_window_index=leader2_window_index,
            credential=credential,
            talent=talent,
            is_tank1=is_tank1,
            is_tank2=is_tank2,
            is_dr_pala1=is_dr_pala1,
            is_dr_pala2=is_dr_pala2,
        )
        kwargs = {
            k: v
            for k, v in kwargs.items() if v is not None
        }
        return attr.evolve(self, **kwargs)

    @property
    def window_title(self):
        return window_index[self.window_index].title

    @property
    def window_label(self):
        return window_index[self.window_index].label

    @property
    def leader1_window_label(self):
        return window_index[self.leader1_window_index].label

    @property
    def leader2_window_label(self):
        return window_index[self.leader2_window_index].label


class CharacterFactory:
    @classmethod
    def make_char_fatmulti1_batlefury_pve_protect_pala(cls) -> Character:
        return Character(
            credential=Credentials.cred_fatmulti1.value,
            name="batlefury",
            talent=Talent.paladin_pve_protect,
        )

    @classmethod
    def make_char_fatmulti1_batlefury_pve_retri_pala(cls) -> Character:
        return Character(
            credential=Credentials.cred_fatmulti1.value,
            name="batlefury",
            talent=Talent.paladin_pve_retri,
        )

    @classmethod
    def make_char_fatmulti2_quentin_pve_elemental_shaman(cls) -> Character:
        return Character(
            credential=Credentials.cred_fatmulti2.value,
            name="quentin",
            talent=Talent.shaman_pve_elemental,
        )

    @classmethod
    def make_char_fatmulti2_quentin_pve_resto_shaman(cls) -> Character:
        return Character(
            credential=Credentials.cred_fatmulti2.value,
            name="quentin",
            talent=Talent.shaman_pve_resto,
        )

    @classmethod
    def make_char_fatmulti3_opiitou_pve_balance_druid(cls) -> Character:
        return Character(
            credential=Credentials.cred_fatmulti3.value,
            name="opiitou",
            talent=Talent.druid_pve_balance,
        )

    @classmethod
    def make_char_fatmulti3_opiitou_pve_resto_druid(cls) -> Character:
        return Character(
            credential=Credentials.cred_fatmulti3.value,
            name="opiitou",
            talent=Talent.druid_pve_resto,
        )

    @classmethod
    def make_char_fatmulti4_swagsonic_pve_arcane_mage(cls) -> Character:
        return Character(
            credential=Credentials.cred_fatmulti4.value,
            name="swagsonic",
            talent=Talent.mage_pve_arcane,
        )

    @classmethod
    def make_char_fatmulti4_swagsonic_pve_fire_mage(cls) -> Character:
        return Character(
            credential=Credentials.cred_fatmulti4.value,
            name="swagsonic",
            talent=Talent.mage_pve_fire,
        )

    @classmethod
    def make_char_fatmulti5_kangliu_pve_shadow_priest(cls) -> Character:
        return Character(
            credential=Credentials.cred_fatmulti5.value,
            name="kangliu",
            talent=Talent.priest_pve_shadow,
        )

    @classmethod
    def make_char_fatmulti5_kangliu_pve_disco_priest(cls) -> Character:
        return Character(
            credential=Credentials.cred_fatmulti5.value,
            name="kangliu",
            talent=Talent.priest_pve_disco,
        )

    @classmethod
    def make_char_fitsheep_kindhearted_pve_demonology_warlock(cls) -> Character:
        return Character(
            credential=Credentials.cred_fitsheep.value,
            name="kindhearted",
            talent=Talent.warlock_pve_demonology,
        )

    @classmethod
    def make_char_fitsheep_kindhearted_pvp_destruction_warlock(cls) -> Character:
        return Character(
            credential=Credentials.cred_fitsheep.value,
            name="kindhearted",
            talent=Talent.warlock_pvp_destruction,
        )

    @classmethod
    def make_char_fatmulti6_kapacuk_pve_marksman_hunter(cls) -> Character:
        return Character(
            credential=Credentials.cred_fatmulti6.value,
            name="kapacuk",
            talent=Talent.hunter_pve_marksman,
        )

    @classmethod
    def make_char_fatmulti6_kapacuk_pvp_beast_hunter(cls) -> Character:
        return Character(
            credential=Credentials.cred_fatmulti6.value,
            name="kapacuk",
            talent=Talent.hunter_pve_beast,
        )

    @classmethod
    def make_char_fatmulti8_bunnysisters_pve_resto_druid(cls) -> Character:
        return Character(
            credential=Credentials.cred_fatmulti8.value,
            name="bunnysisters",
            talent=Talent.druid_pve_resto,
        )

    @classmethod
    def make_char_fatmulti8_bunnysisters_pve_balance_druid(cls) -> Character:
        return Character(
            credential=Credentials.cred_fatmulti8.value,
            name="bunnysisters",
            talent=Talent.druid_pve_balance,
        )

    @classmethod
    def make_char_fatmulti9_glowyy_pve_holy_pala(cls) -> Character:
        return Character(
            credential=Credentials.cred_fatmulti9.value,
            name="glowyy",
            talent=Talent.paladin_pve_holy,
        )

    @classmethod
    def make_char_fatmulti9_glowyy_pve_protect_pala(cls) -> Character:
        return Character(
            credential=Credentials.cred_fatmulti9.value,
            name="glowyy",
            talent=Talent.paladin_pve_protect,
        )

    @classmethod
    def make_char_monkey130_flydps_pve_blood_tank_dk(cls) -> Character:
        return Character(
            credential=Credentials.cred_monkey130.value,
            name="flydps",
            talent=Talent.dk_pve_blood_tank,
        )

    @classmethod
    def make_char_fatmulti1_litgoatssa_pve_demo_warlock(cls) -> Character:
        return Character(
            credential=Credentials.cred_fatmulti1.value,
            name="litgoatssa",
            talent=Talent.warlock_pve_demonology,
        )

    @classmethod
    def make_char_fatmulti2_litgoatssb_pve_demo_warlock(cls) -> Character:
        return Character(
            credential=Credentials.cred_fatmulti2.value,
            name="litgoatssb",
            talent=Talent.warlock_pve_demonology,
        )

    @classmethod
    def make_char_fatmulti3_litgoatssc_pve_demo_warlock(cls) -> Character:
        return Character(
            credential=Credentials.cred_fatmulti3.value,
            name="litgoatssc",
            talent=Talent.warlock_pve_demonology,
        )

    @classmethod
    def make_char_fatmulti4_litgoatssd_pve_demo_warlock(cls) -> Character:
        return Character(
            credential=Credentials.cred_fatmulti4.value,
            name="litgoatssd",
            talent=Talent.warlock_pve_demonology,
        )

    @classmethod
    def make_char_fatmulti5_litgoatsse_pve_demo_warlock(cls) -> Character:
        return Character(
            credential=Credentials.cred_fatmulti5.value,
            name="litgoatsse",
            talent=Talent.warlock_pve_demonology,
        )

    @classmethod
    def make_char_fatmulti1_litgoatdka_pvp_frost_dk(cls) -> Character:
        return Character(
            credential=Credentials.cred_fatmulti1.value,
            name="litgoatdka",
            talent=Talent.dk_pvp_frost,
        )

    @classmethod
    def make_char_fatmulti2_litgoatdkb_pvp_frost_dk(cls) -> Character:
        return Character(
            credential=Credentials.cred_fatmulti2.value,
            name="litgoatdkb",
            talent=Talent.dk_pvp_frost,
        )

    @classmethod
    def make_char_fatmulti3_litgoatdkc_pvp_frost_dk(cls) -> Character:
        return Character(
            credential=Credentials.cred_fatmulti3.value,
            name="litgoatdkc",
            talent=Talent.dk_pvp_frost,
        )

    @classmethod
    def make_char_fatmulti4_litgoatdkd_pvp_frost_dk(cls) -> Character:
        return Character(
            credential=Credentials.cred_fatmulti4.value,
            name="litgoatdkd",
            talent=Talent.dk_pvp_frost,
        )

    @classmethod
    def make_char_fatmulti5_litgoatdke_pvp_frost_dk(cls) -> Character:
        return Character(
            credential=Credentials.cred_fatmulti5.value,
            name="litgoatdke",
            talent=Talent.dk_pvp_frost,
        )
