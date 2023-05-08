# -*- coding: utf-8 -*-

from hotkeynet import api


class TestScript:
    def test_render(self):
        with api.Script() as script:
            api.Label(name="w1", window="WoW1")
            api.Label(name="w2", window="WoW2")

            with api.Command(
                name="LaunchAndRenameGameClient",
            ) as cmd_launch_and_rename_game_client:
                with api.SendPC():
                    api.Run.make("C:\\Program Files (x86)\\World of Warcraft\\Wow.exe")
                    api.RenameWin(old="WoW", new=api.CommandArgEnum.Arg1)

            with api.Hotkey(key=api.KN.KEY_1) as hk_1:
                with api.SendLabel(to=["w1", "w2"]):
                    api.CAN.KEY_1()

        script.render()

        # print("=" * 80)
        # print(script.render())
        # print("=" * 80)


if __name__ == "__main__":
    from hotkeynet.tests import run_cov_test

    run_cov_test(__file__, "hotkeynet.script", preview=False)
