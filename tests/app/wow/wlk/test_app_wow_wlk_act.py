# -*- coding: utf-8 -*-

import pytest
from hotkeynet.app.wow.wlk import act


class TestPaladin:
    def test_common(self):
        _ = act.movement.MOVE_LEFT()
        _ = act.movement.MOVE_LEFT_TOP()

    def test_class(self):
        _ = act.paladin_protection.Hammer_of_the_Righteous()
        _ = act.paladin_retribution.Divine_Storm()
        _ = act.paladin_holy.Holy_Shock()

        with pytest.raises(ValueError):
            act.paladin_holy.Blessing_of_Sanctuary()


if __name__ == "__main__":
    from hotkeynet.tests import run_cov_test

    run_cov_test(__file__, "hotkeynet.app.wow.wlk.act")
