# -*- coding: utf-8 -*-

from .....script import Hotkey, Key, SendLabel
from ... import act
from ..... import keyname
from .._config_and_script import config, script
from ...config import Config, ActiveCharacterConfig
from ...constant.characters import CharacterFactory
from ...constant.talent_category_association import TC


class Mode:
    @classmethod
    def set_mode_icc_1_marrowgar(cls, config: Config):
        """
        Batlefury Retri paladin + 4 alts
        Opiitou Bear druid + 4 alts
        """
        config.game_client_config.use_1600_900_resolution()
        config.game_client_config.use_n_windows(22)
        config.game_client_config.use_credential_list_default()
        config.toggle_window_config.round_robin_window_index = list(range(1, 22 + 1))
        config.active_character_config = ActiveCharacterConfig(
            active_characters=[
                # team 1
                CharacterFactory.make_char_fatmulti1_batlefury_pve_retri_pala().evolve(),
                CharacterFactory.make_char_fatmulti19_lgmsi_pve_shadow_priest().evolve(leader1_window_index=1),
                CharacterFactory.make_char_fatmulti20_lgmsj_pve_shadow_priest().evolve(leader1_window_index=1),
                CharacterFactory.make_char_fatmulti21_lgmsk_pve_shadow_priest().evolve(leader1_window_index=1),
                CharacterFactory.make_char_fatmulti22_lgmsl_pve_shadow_priest().evolve(leader1_window_index=1),

                # team 2
                CharacterFactory.make_char_fatmulti3_opiitou_pve_bear_druid().evolve(),
                CharacterFactory.make_char_fatmulti23_lgsmm_pve_elemental_shaman().evolve(leader1_window_index=3),
                CharacterFactory.make_char_fatmulti24_lgsmn_pve_elemental_shaman().evolve(leader1_window_index=3),
                CharacterFactory.make_char_fatmulti25_lgsmo_pve_elemental_shaman().evolve(leader1_window_index=3),
                CharacterFactory.make_char_fatmulti26_lgsmp_pve_elemental_shaman().evolve(leader1_window_index=3),
            ]
        )
        config.active_character_config.set_leader1_window_index(1)

        hk_c = Hotkey(
            name="C",
            key=keyname.SCROLOCK_ON(keyname.C),
            actions=[
                SendLabel(
                    name=TC.shaman_resto.name,
                    to=config.lbs_by_tc(tc=TC.shaman_resto),
                    actions=[
                        act.Target.TARGET_PARTY,
                        act.Shaman.ALL_SPEC_CHAIN_HEAL,
                    ]
                ),
                SendLabel(
                    name=TC.paladin_holy.name,
                    to=config.lbs_by_tc(tc=TC.paladin_holy),
                    actions=[
                        act.Target.TARGET_PARTY,
                        act.Paladin.HOLY_SPEC_KEY_5_HOLY_LIGHT,
                    ]
                ),
                SendLabel(
                    name=TC.shaman_resto.name,
                    to=config.lbs_by_tc(tc=TC.shaman_resto),
                    actions=[
                        act.Target.TARGET_SELF,
                        act.Shaman.ALL_SPEC_CHAIN_HEAL,
                    ]
                ),
                SendLabel(
                    name=TC.shaman_resto.name,
                    to=config.lbs_by_tc(tc=TC.shaman_resto),
                    actions=[
                        act.Target.TARGET_SELF,
                        act.Shaman.ALL_SPEC_CHAIN_HEAL,
                    ]
                ),
            ],
            script=script,
        )


