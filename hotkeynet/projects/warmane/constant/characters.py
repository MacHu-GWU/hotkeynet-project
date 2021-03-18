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
            window_index=1,
        )

    @classmethod
    def make_char_fatmulti1_batlefury_pve_retri_pala(cls) -> Character:
        return Character(
            credential=Credentials.cred_fatmulti1.value,
            name="batlefury",
            talent=Talent.paladin_pve_retri,
            window_index=1,
        )

    @classmethod
    def make_char_fatmulti2_quentin_pve_elemental_shaman(cls) -> Character:
        return Character(
            credential=Credentials.cred_fatmulti2.value,
            name="quentin",
            talent=Talent.shaman_pve_elemental,
            window_index=2,
        )

    @classmethod
    def make_char_fatmulti2_quentin_pve_resto_shaman(cls) -> Character:
        return Character(
            credential=Credentials.cred_fatmulti2.value,
            name="quentin",
            talent=Talent.shaman_pve_resto,
            window_index=2,
        )

    @classmethod
    def make_char_fatmulti3_opiitou_pve_balance_druid(cls) -> Character:
        return Character(
            credential=Credentials.cred_fatmulti3.value,
            name="opiitou",
            talent=Talent.druid_pve_balance,
            window_index=3,
        )

    @classmethod
    def make_char_fatmulti3_opiitou_pve_bear_druid(cls) -> Character:
        return Character(
            credential=Credentials.cred_fatmulti3.value,
            name="opiitou",
            talent=Talent.druid_pve_resto,
            window_index=3,
        )

    @classmethod
    def make_char_fatmulti4_swagsonic_pve_arcane_mage(cls) -> Character:
        return Character(
            credential=Credentials.cred_fatmulti4.value,
            name="swagsonic",
            talent=Talent.mage_pve_arcane,
            window_index=4,
        )

    @classmethod
    def make_char_fatmulti4_swagsonic_pve_fire_mage(cls) -> Character:
        return Character(
            credential=Credentials.cred_fatmulti4.value,
            name="swagsonic",
            talent=Talent.mage_pve_fire,
            window_index=4,
        )

    @classmethod
    def make_char_fatmulti5_kangliu_pve_shadow_priest(cls) -> Character:
        return Character(
            credential=Credentials.cred_fatmulti5.value,
            name="kangliu",
            talent=Talent.priest_pve_shadow,
            window_index=5,
        )

    @classmethod
    def make_char_fatmulti5_kangliu_pve_disco_priest(cls) -> Character:
        return Character(
            credential=Credentials.cred_fatmulti5.value,
            name="kangliu",
            talent=Talent.priest_pve_disco,
            window_index=5,
        )

    @classmethod
    def make_char_fitsheep_kindhearted_pve_demonology_warlock(cls) -> Character:
        return Character(
            credential=Credentials.cred_fitsheep.value,
            name="kindhearted",
            talent=Talent.warlock_pve_demonology,
            window_index=6,
        )

    @classmethod
    def make_char_fitsheep_kindhearted_pvp_destruction_warlock(cls) -> Character:
        return Character(
            credential=Credentials.cred_fitsheep.value,
            name="kindhearted",
            talent=Talent.warlock_pvp_destruction,
            window_index=6,
        )

    @classmethod
    def make_char_fitsheep_bordercollie_pve_shadow_priest(cls) -> Character:
        return Character(
            credential=Credentials.cred_fitsheep.value,
            name="bordercollie",
            talent=Talent.priest_pve_shadow,
            window_index=6,
        )

    @classmethod
    def make_char_fitsheep_bordercollie_pve_disco_priest(cls) -> Character:
        return Character(
            credential=Credentials.cred_fitsheep.value,
            name="bordercollie",
            talent=Talent.priest_pve_disco,
            window_index=6,
        )

    @classmethod
    def make_char_fatmulti6_kapacuk_pve_marksman_hunter(cls) -> Character:
        return Character(
            credential=Credentials.cred_fatmulti6.value,
            name="kapacuk",
            talent=Talent.hunter_pve_marksman,
            window_index=7,
        )

    @classmethod
    def make_char_fatmulti6_kapacuk_pvp_beast_hunter(cls) -> Character:
        return Character(
            credential=Credentials.cred_fatmulti6.value,
            name="kapacuk",
            talent=Talent.hunter_pve_beast,
            window_index=7,
        )

    @classmethod
    def make_char_fatmulti8_bunnysisters_pve_resto_druid(cls) -> Character:
        return Character(
            credential=Credentials.cred_fatmulti8.value,
            name="bunnysisters",
            talent=Talent.druid_pve_resto,
            window_index=8,
        )

    @classmethod
    def make_char_fatmulti8_bunnysisters_pve_balance_druid(cls) -> Character:
        return Character(
            credential=Credentials.cred_fatmulti8.value,
            name="bunnysisters",
            talent=Talent.druid_pve_balance,
            window_index=8,
        )

    @classmethod
    def make_char_fatmulti9_glowyy_pve_holy_pala(cls) -> Character:
        return Character(
            credential=Credentials.cred_fatmulti9.value,
            name="glowyy",
            talent=Talent.paladin_pve_holy,
            window_index=9,
        )

    @classmethod
    def make_char_fatmulti9_glowyy_pve_protect_pala(cls) -> Character:
        return Character(
            credential=Credentials.cred_fatmulti9.value,
            name="glowyy",
            talent=Talent.paladin_pve_protect,
            window_index=9,
        )

    @classmethod
    def make_char_monkey130_flydps_pve_blood_tank_dk(cls) -> Character:
        return Character(
            credential=Credentials.cred_monkey130.value,
            name="flydps",
            talent=Talent.dk_pve_blood_tank,
            window_index=10,
        )

    @classmethod
    def make_char_makun7551_ganjj_pve_blood_tank_dk(cls) -> Character:
        return Character(
            credential=Credentials.cred_makun7551.value,
            name="ganjj",
            talent=Talent.dk_pve_blood_tank,
            window_index=10,
        )

    @classmethod
    def make_char_makun7551_laoshou_retri_paladin(cls) -> Character:
        return Character(
            credential=Credentials.cred_makun7551.value,
            name="laoshou",
            talent=Talent.paladin_pve_retri,
            window_index=10,
        )

    #--- litgoat ss
    @classmethod
    def make_char_fatmulti1_litgoatssa_pve_demo_warlock(cls) -> Character:
        return Character(
            credential=Credentials.cred_fatmulti1.value,
            name="litgoatssa",
            talent=Talent.warlock_pve_demonology,
            window_index=1,
        )

    @classmethod
    def make_char_fatmulti2_litgoatssb_pve_demo_warlock(cls) -> Character:
        return Character(
            credential=Credentials.cred_fatmulti2.value,
            name="litgoatssb",
            talent=Talent.warlock_pve_demonology,
            window_index=2,
        )

    @classmethod
    def make_char_fatmulti3_litgoatssc_pve_demo_warlock(cls) -> Character:
        return Character(
            credential=Credentials.cred_fatmulti3.value,
            name="litgoatssc",
            talent=Talent.warlock_pve_demonology,
            window_index=3,
        )

    @classmethod
    def make_char_fatmulti4_litgoatssd_pve_demo_warlock(cls) -> Character:
        return Character(
            credential=Credentials.cred_fatmulti4.value,
            name="litgoatssd",
            talent=Talent.warlock_pve_demonology,
            window_index=4,
        )

    @classmethod
    def make_char_fatmulti5_litgoatsse_pve_demo_warlock(cls) -> Character:
        return Character(
            credential=Credentials.cred_fatmulti5.value,
            name="litgoatsse",
            talent=Talent.warlock_pve_demonology,
            window_index=5,
        )

    #--- litgoat dk
    @classmethod
    def make_char_fatmulti1_litgoatdka_pvp_frost_dk(cls) -> Character:
        return Character(
            credential=Credentials.cred_fatmulti1.value,
            name="litgoatdka",
            talent=Talent.dk_pvp_frost,
            window_index=1,
        )

    @classmethod
    def make_char_fatmulti2_litgoatdkb_pvp_frost_dk(cls) -> Character:
        return Character(
            credential=Credentials.cred_fatmulti2.value,
            name="litgoatdkb",
            talent=Talent.dk_pvp_frost,
            window_index=2,
        )

    @classmethod
    def make_char_fatmulti3_litgoatdkc_pvp_frost_dk(cls) -> Character:
        return Character(
            credential=Credentials.cred_fatmulti3.value,
            name="litgoatdkc",
            talent=Talent.dk_pvp_frost,
            window_index=3,
        )

    @classmethod
    def make_char_fatmulti4_litgoatdkd_pvp_frost_dk(cls) -> Character:
        return Character(
            credential=Credentials.cred_fatmulti4.value,
            name="litgoatdkd",
            talent=Talent.dk_pvp_frost,
            window_index=4,
        )

    @classmethod
    def make_char_fatmulti5_litgoatdke_pvp_frost_dk(cls) -> Character:
        return Character(
            credential=Credentials.cred_fatmulti5.value,
            name="litgoatdke",
            talent=Talent.dk_pvp_frost,
            window_index=5,
        )

    @classmethod
    def make_char_fatmulti1_litgoatdka_pve_blood_dk(cls) -> Character:
        return Character(
            credential=Credentials.cred_fatmulti1.value,
            name="litgoatdka",
            talent=Talent.dk_pve_unholy_dps,
            window_index=1,
        )

    @classmethod
    def make_char_fatmulti2_litgoatdkb_pve_unholy_dk(cls) -> Character:
        return Character(
            credential=Credentials.cred_fatmulti2.value,
            name="litgoatdkb",
            talent=Talent.dk_pve_unholy_dps,
            window_index=2,
        )

    @classmethod
    def make_char_fatmulti3_litgoatdkc_pve_unholy_dk(cls) -> Character:
        return Character(
            credential=Credentials.cred_fatmulti3.value,
            name="litgoatdkc",
            talent=Talent.dk_pve_unholy_dps,
            window_index=3,
        )

    @classmethod
    def make_char_fatmulti4_litgoatdkd_pve_unholy_dk(cls) -> Character:
        return Character(
            credential=Credentials.cred_fatmulti4.value,
            name="litgoatdkd",
            talent=Talent.dk_pve_unholy_dps,
            window_index=4,
        )

    @classmethod
    def make_char_fatmulti5_litgoatdke_pve_unholy_dk(cls) -> Character:
        return Character(
            credential=Credentials.cred_fatmulti5.value,
            name="litgoatdke",
            talent=Talent.dk_pve_unholy_dps,
            window_index=5,
        )

    #--- litgugu abcd
    @classmethod
    def make_char_fatmulti11_litgugua_pvp_balance_druid(cls) -> Character:
        return Character(
            credential=Credentials.cred_fatmulti11.value,
            name="litgugua",
            talent=Talent.druid_pvp_balance,
            window_index=11,
        )

    @classmethod
    def make_char_fatmulti11_litgugua_pvp_resto_druid(cls) -> Character:
        return Character(
            credential=Credentials.cred_fatmulti11.value,
            name="litgugud",
            talent=Talent.druid_pvp_resto,
            window_index=14,
        )

    @classmethod
    def make_char_fatmulti11_litgugua_pve_balance_druid(cls) -> Character:
        return Character(
            credential=Credentials.cred_fatmulti11.value,
            name="litgugua",
            talent=Talent.druid_pve_balance,
            window_index=11,
        )

    @classmethod
    def make_char_fatmulti12_litgugub_pvp_balance_druid(cls) -> Character:
        return Character(
            credential=Credentials.cred_fatmulti12.value,
            name="litgugub",
            talent=Talent.druid_pvp_balance,
            window_index=12,
        )

    @classmethod
    def make_char_fatmulti12_litgugub_pvp_resto_druid(cls) -> Character:
        return Character(
            credential=Credentials.cred_fatmulti12.value,
            name="litgugub",
            talent=Talent.druid_pvp_resto,
            window_index=12,
        )

    @classmethod
    def make_char_fatmulti12_litgugub_pve_balance_druid(cls) -> Character:
        return Character(
            credential=Credentials.cred_fatmulti12.value,
            name="litgugub",
            talent=Talent.druid_pve_balance,
            window_index=12,
        )

    @classmethod
    def make_char_fatmulti13_litguguc_pvp_balance_druid(cls) -> Character:
        return Character(
            credential=Credentials.cred_fatmulti13.value,
            name="litguguc",
            talent=Talent.druid_pvp_balance,
            window_index=13,
        )

    @classmethod
    def make_char_fatmulti13_litguguc_pvp_resto_druid(cls) -> Character:
        return Character(
            credential=Credentials.cred_fatmulti13.value,
            name="litguguc",
            talent=Talent.druid_pvp_resto,
            window_index=13,
        )

    @classmethod
    def make_char_fatmulti13_litguguc_pve_balance_druid(cls) -> Character:
        return Character(
            credential=Credentials.cred_fatmulti13.value,
            name="litguguc",
            talent=Talent.druid_pve_balance,
            window_index=13,
        )

    @classmethod
    def make_char_fatmulti14_litgugud_pvp_balancce_druid(cls) -> Character:
        return Character(
            credential=Credentials.cred_fatmulti14.value,
            name="litgugud",
            talent=Talent.druid_pvp_balance,
            window_index=14,
        )

    @classmethod
    def make_char_fatmulti14_litgugud_pvp_resto_druid(cls) -> Character:
        return Character(
            credential=Credentials.cred_fatmulti14.value,
            name="litgugud",
            talent=Talent.druid_pvp_resto,
            window_index=14,
        )

    @classmethod
    def make_char_fatmulti14_litgugud_pve_balance_druid(cls) -> Character:
        return Character(
            credential=Credentials.cred_fatmulti14.value,
            name="litgugud",
            talent=Talent.druid_pve_balance,
            window_index=14,
        )

    #--- lg ms i, j, k, l
    @classmethod
    def make_char_fatmulti19_lgmsi_pve_shadow_priest(cls) -> Character:
        return Character(
            credential=Credentials.cred_fatmulti19.value,
            name="lgmsi",
            talent=Talent.priest_pve_shadow,
            window_index=15,
        )

    @classmethod
    def make_char_fatmulti20_lgmsj_pve_shadow_priest(cls) -> Character:
        return Character(
            credential=Credentials.cred_fatmulti20.value,
            name="lgmsj",
            talent=Talent.priest_pve_shadow,
            window_index=16,
        )

    @classmethod
    def make_char_fatmulti21_lgmsk_pve_shadow_priest(cls) -> Character:
        return Character(
            credential=Credentials.cred_fatmulti21.value,
            name="lgmsk",
            talent=Talent.priest_pve_shadow,
            window_index=17,
        )

    @classmethod
    def make_char_fatmulti22_lgmsl_pve_shadow_priest(cls) -> Character:
        return Character(
            credential=Credentials.cred_fatmulti22.value,
            name="lgmsl",
            talent=Talent.priest_pve_shadow,
            window_index=18,
        )

    #--- lg sm m, n, o, p
    @classmethod
    def make_char_fatmulti23_lgsmm_pve_elemental_shaman(cls) -> Character:
        return Character(
            credential=Credentials.cred_fatmulti23.value,
            name="lgsmm",
            talent=Talent.shaman_pve_elemental,
            window_index=19,
        )

    @classmethod
    def make_char_fatmulti23_lgsmm_pve_resto_shaman(cls) -> Character:
        return Character(
            credential=Credentials.cred_fatmulti23.value,
            name="lgsmm",
            talent=Talent.shaman_pve_resto,
            window_index=19,
        )

    @classmethod
    def make_char_fatmulti24_lgsmn_pve_elemental_shaman(cls) -> Character:
        return Character(
            credential=Credentials.cred_fatmulti24.value,
            name="lgsmn",
            talent=Talent.shaman_pve_elemental,
            window_index=20,
        )

    @classmethod
    def make_char_fatmulti24_lgsmn_pve_resto_shaman(cls) -> Character:
        return Character(
            credential=Credentials.cred_fatmulti24.value,
            name="lgsmn",
            talent=Talent.shaman_pve_resto,
            window_index=20,
        )

    @classmethod
    def make_char_fatmulti25_lgsmo_pve_elemental_shaman(cls) -> Character:
        return Character(
            credential=Credentials.cred_fatmulti25.value,
            name="lgsmo",
            talent=Talent.shaman_pve_elemental,
            window_index=21,
        )

    @classmethod
    def make_char_fatmulti25_lgsmo_pve_resto_shaman(cls) -> Character:
        return Character(
            credential=Credentials.cred_fatmulti25.value,
            name="lgsmo",
            talent=Talent.shaman_pve_resto,
            window_index=21,
        )

    @classmethod
    def make_char_fatmulti26_lgsmp_pve_elemental_shaman(cls) -> Character:
        return Character(
            credential=Credentials.cred_fatmulti26.value,
            name="lgsmp",
            talent=Talent.shaman_pve_elemental,
            window_index=22,
        )

    @classmethod
    def make_char_fatmulti26_lgsmp_pve_resto_shaman(cls) -> Character:
        return Character(
            credential=Credentials.cred_fatmulti26.value,
            name="lgsmp",
            talent=Talent.shaman_pve_resto,
            window_index=22,
        )
