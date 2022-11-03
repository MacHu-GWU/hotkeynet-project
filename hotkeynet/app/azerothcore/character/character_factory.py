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

    这样我们可以通过调用这些 可以被搜索定位, 名字人类可理解 的函数方便的创建游戏角色的实例.
    """

    @property
    def ra_pve_protect_pala(self) -> Character:
        return Character(
            account=AccountEnum.account_fat01.value,
            name="ra",
            talent=TL.paladin_pve_protect,
            window=Window.make(1),
            nth_char=1,
        )

    @property
    def rb_pve_elemental_shaman(self) -> Character:
        return Character(
            account=AccountEnum.account_fat02.value,
            name="rb",
            talent=TL.shaman_pve_elemental,
            window=Window.make(2),
            nth_char=1,
        )

    @property
    def rc_pve_balance_druid(self) -> Character:
        return Character(
            account=AccountEnum.account_fat03.value,
            name="rc",
            talent=TL.druid_pve_balance,
            window=Window.make(3),
            nth_char=1,
        )

    @property
    def rd_pve_arcane_mage(self) -> Character:
        return Character(
            account=AccountEnum.account_fat04.value,
            name="rd",
            talent=TL.mage_pve_arcane,
            window=Window.make(4),
            nth_char=1,
        )

    @property
    def re_pve_shadow_priest(self) -> Character:
        return Character(
            account=AccountEnum.account_fat05.value,
            name="re",
            talent=TL.priest_pve_shadow,
            window=Window.make(5),
            nth_char=1,
        )

    @property
    def re_pve_holy_priest(self) -> Character:
        return Character(
            account=AccountEnum.account_fat05.value,
            name="re",
            talent=TL.priest_pve_holy,
            window=Window.make(5),
            nth_char=1,
        )

    @property
    def rf_pve_demon_warlock(self) -> Character:
        return Character(
            account=AccountEnum.account_fat06.value,
            name="rf",
            talent=TL.warlock_pve_demonology,
            window=Window.make(6),
            nth_char=1,
        )

    @property
    def rg_pve_marksman_hunter(self) -> Character:
        return Character(
            account=AccountEnum.account_fat07.value,
            name="rg",
            talent=TL.hunter_pve_marksman,
            window=Window.make(7),
            nth_char=1,
        )

    @property
    def rh_pve_resto_druid(self) -> Character:
        return Character(
            account=AccountEnum.account_fat08.value,
            name="rh",
            talent=TL.druid_pve_resto,
            window=Window.make(8),
            nth_char=1,
        )

    @property
    def ri_pve_holy_paladin(self) -> Character:
        return Character(
            account=AccountEnum.account_fat09.value,
            name="ri",
            talent=TL.paladin_pve_holy,
            window=Window.make(9),
            nth_char=1,
        )

    @property
    def rj_pve_blood_tank_dk(self) -> Character:
        return Character(
            account=AccountEnum.account_fat10.value,
            name="rj",
            talent=TL.dk_pve_blood_tank,
            window=Window.make(10),
            nth_char=1,
        )

    @property
    def rk_pve_balance_druid(self) -> Character:
        return Character(
            account=AccountEnum.account_fat11.value,
            name="rk",
            talent=TL.druid_pve_balance,
            window=Window.make(11),
            nth_char=1,
        )

    @property
    def rl_pve_balance_druid(self) -> Character:
        return Character(
            account=AccountEnum.account_fat12.value,
            name="rl",
            talent=TL.druid_pve_balance,
            window=Window.make(12),
            nth_char=1,
        )

    @property
    def rm_pve_balance_druid(self) -> Character:
        return Character(
            account=AccountEnum.account_fat13.value,
            name="rm",
            talent=TL.druid_pve_balance,
            window=Window.make(13),
            nth_char=1,
        )

    @property
    def rn_pve_shadow_priest(self) -> Character:
        return Character(
            account=AccountEnum.account_fat14.value,
            name="rn",
            talent=TL.priest_pve_shadow,
            window=Window.make(14),
            nth_char=1,
        )

    @property
    def ro_pve_shadow_priest(self) -> Character:
        return Character(
            account=AccountEnum.account_fat15.value,
            name="ro",
            talent=TL.priest_pve_shadow,
            window=Window.make(15),
            nth_char=1,
        )

    @property
    def rp_pve_shadow_priest(self) -> Character:
        return Character(
            account=AccountEnum.account_fat16.value,
            name="rp",
            talent=TL.priest_pve_shadow,
            window=Window.make(16),
            nth_char=1,
        )

    @property
    def rq_pve_shadow_priest(self) -> Character:
        return Character(
            account=AccountEnum.account_fat17.value,
            name="rq",
            talent=TL.priest_pve_shadow,
            window=Window.make(17),
            nth_char=1,
        )

    @property
    def rr_pve_shadow_priest(self) -> Character:
        return Character(
            account=AccountEnum.account_fat18.value,
            name="rr",
            talent=TL.priest_pve_shadow,
            window=Window.make(18),
            nth_char=1,
        )

    @property
    def rs_pve_shadow_priest(self) -> Character:
        return Character(
            account=AccountEnum.account_fat19.value,
            name="rs",
            talent=TL.priest_pve_shadow,
            window=Window.make(19),
            nth_char=1,
        )

    @property
    def rt_pve_shadow_priest(self) -> Character:
        return Character(
            account=AccountEnum.account_fat20.value,
            name="rt",
            talent=TL.priest_pve_shadow,
            window=Window.make(20),
            nth_char=1,
        )

    @property
    def ru_pve_shadow_priest(self) -> Character:
        return Character(
            account=AccountEnum.account_fat21.value,
            name="ru",
            talent=TL.priest_pve_shadow,
            window=Window.make(21),
            nth_char=1,
        )

    @property
    def rv_pve_shadow_priest(self) -> Character:
        return Character(
            account=AccountEnum.account_fat22.value,
            name="rv",
            talent=TL.priest_pve_shadow,
            window=Window.make(22),
            nth_char=1,
        )

    @property
    def rw_pve_resto_shaman(self) -> Character:
        return Character(
            account=AccountEnum.account_fat23.value,
            name="rw",
            talent=TL.shaman_pve_resto,
            window=Window.make(23),
            nth_char=1,
        )

    @property
    def rx_pve_holy_paladin(self) -> Character:
        return Character(
            account=AccountEnum.account_fat24.value,
            name="rx",
            talent=TL.paladin_pve_holy,
            window=Window.make(24),
            nth_char=1,
        )

    @property
    def ry_pve_disco_priest(self) -> Character:
        return Character(
            account=AccountEnum.account_fat25.value,
            name="ry",
            talent=TL.priest_pve_disco,
            window=Window.make(25),
            nth_char=1,
        )

    @property
    def sa_pve_protect_paladin(self) -> Character:
        return Character(
            account=AccountEnum.account_rab01.value,
            name="sa",
            talent=TL.paladin_pve_protect,
            window=Window.make(1),
            nth_char=1,
        )

    @property
    def sb_pve_elemental_shaman(self) -> Character:
        return Character(
            account=AccountEnum.account_rab02.value,
            name="sb",
            talent=TL.shaman_pve_elemental,
            window=Window.make(2),
            nth_char=1,
        )

    @property
    def sc_pve_elemental_shaman(self) -> Character:
        return Character(
            account=AccountEnum.account_rab03.value,
            name="sc",
            talent=TL.shaman_pve_elemental,
            window=Window.make(3),
            nth_char=1,
        )

    @property
    def sd_pve_elemental_shaman(self) -> Character:
        return Character(
            account=AccountEnum.account_rab04.value,
            name="sd",
            talent=TL.shaman_pve_elemental,
            window=Window.make(4),
            nth_char=1,
        )

    @property
    def se_pve_resto_shaman(self) -> Character:
        return Character(
            account=AccountEnum.account_rab05.value,
            name="se",
            talent=TL.shaman_pve_resto,
            window=Window.make(5),
            nth_char=1,
        )


char_fact = CharacterFactory()


class CharacterGroup:
    @property
    def r_abcde_fghij(self) -> OrderedSet[Character]:
        return OrderedSet([
            char_fact.ra_pve_protect_pala,
            char_fact.rb_pve_elemental_shaman,
            char_fact.rc_pve_balance_druid,
            char_fact.rd_pve_arcane_mage,
            char_fact.re_pve_shadow_priest,
            char_fact.rf_pve_demon_warlock,
            char_fact.rg_pve_marksman_hunter,
            char_fact.rh_pve_resto_druid,
            char_fact.ri_pve_holy_paladin,
            char_fact.rj_pve_blood_tank_dk,
        ])

    @property
    def r_a_to_y(self) -> OrderedSet[Character]:
        return OrderedSet([
            char_fact.ra_pve_protect_pala,
            char_fact.rb_pve_elemental_shaman,
            char_fact.rc_pve_balance_druid,
            char_fact.rd_pve_arcane_mage,
            char_fact.re_pve_shadow_priest,
            char_fact.rf_pve_demon_warlock,
            char_fact.rg_pve_marksman_hunter,
            char_fact.rh_pve_resto_druid,
            char_fact.ri_pve_holy_paladin,
            char_fact.rj_pve_blood_tank_dk,
            char_fact.rk_pve_balance_druid,
            char_fact.rl_pve_balance_druid,
            char_fact.rm_pve_balance_druid,
            char_fact.rn_pve_shadow_priest,
            char_fact.ro_pve_shadow_priest,
            char_fact.rp_pve_shadow_priest,
            char_fact.rq_pve_shadow_priest,
            char_fact.rr_pve_shadow_priest,
            char_fact.rs_pve_shadow_priest,
            char_fact.rt_pve_shadow_priest,
            char_fact.ru_pve_shadow_priest,
            char_fact.rv_pve_shadow_priest,
            char_fact.rw_pve_resto_shaman,
            char_fact.rx_pve_holy_paladin,
            char_fact.ry_pve_disco_priest,
        ])

    @property
    def s_abcde(self) -> OrderedSet[Character]:
        return OrderedSet([
            char_fact.sa_pve_protect_paladin,
            char_fact.sb_pve_elemental_shaman,
            char_fact.sc_pve_elemental_shaman,
            char_fact.sd_pve_elemental_shaman,
            char_fact.se_pve_resto_shaman,
        ])


char_group = CharacterGroup()
