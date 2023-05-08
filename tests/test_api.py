# -*- coding: utf-8 -*-


def test():
    from hotkeynet import api

    _ = api.KN
    _ = api.CAN
    _ = api.context
    _ = api.Block
    _ = api.Script
    _ = api.SendModeEnum
    _ = api.Label
    _ = api.Command
    _ = api.CommandArgEnum
    _ = api.CallCommand
    _ = api.SendPC
    _ = api.Run
    _ = api.Hotkey
    _ = api.MovementHotkey
    _ = api.Key
    _ = api.KeyUp
    _ = api.KeyDown
    _ = api.SendLabel
    _ = api.MouseButtonEnum
    _ = api.MouseStrokeEnum
    _ = api.MouseTargetEnum
    _ = api.MouseModeEnum
    _ = api.ClickMouse
    _ = api.MoveMouse
    _ = api.RenameWin
    _ = api.TargetWin
    _ = api.Wait
    _ = api.WaitForWin
    _ = api.WaitForWinEnabled
    _ = api.SetForegroundWin
    _ = api.SetActiveWin
    _ = api.Toggle
    _ = api.ToggleHotkeys
    _ = api.ToggleWin
    _ = api.SendWin
    _ = api.SendWinM
    _ = api.SendWinMF
    _ = api.SendWinS
    _ = api.SendWinSF
    _ = api.SendFocusWin
    _ = api.SetWinPos
    _ = api.SetWinSize
    _ = api.SetWinRect
    _ = api.Text
    _ = api.CreatePanel
    _ = api.CreateButton
    _ = api.CreatePictureButton
    _ = api.CreateColoredButton
    _ = api.AddButtonToPanel
    _ = api.SetButtonHotkey
    _ = api.SetButtonCommand
    _ = api.AlwaysOnTop
    _ = api.SetPanelLayout


if __name__ == "__main__":
    from hotkeynet.tests import run_cov_test

    run_cov_test(__file__, "hotkeynet.api", preview=False)
