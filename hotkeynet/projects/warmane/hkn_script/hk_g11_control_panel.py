# -*- coding: utf-8 -*-

from pathlib_mate import PathCls as Path

from ._config_and_script import script
from ....script import Command

dir_project_root = Path(__file__).parent.parent.parent.parent.parent
assert Path(dir_project_root, "hotkeynet").exists()
dir_icon = Path(dir_project_root, "icons")

content = f"""
<CreatePanel MBControlPanel 0 0 120 1000>
    <CreateButton ButtonBar11 0 0 36 36 "Alt">
    <AddButtonToPanel ButtonBar11 MBControlPanel 0 0>

    <CreateButton ButtonBar12 0 0 36 36 "+">
    <AddButtonToPanel ButtonBar12 MBControlPanel 0 0>

    <CreateButton ButtonBar13 0 0 36 36 "N1-12">
    <AddButtonToPanel ButtonBar13 MBControlPanel 0 0>
    
    <CreatePictureButton Button1 0 0 "{Path(dir_icon, "ability_hunter_misdirection.jpg").abspath}">
    <AddButtonToPanel Button1 MBControlPanel 0 0>
    <SetButtonHotkey Button1 Hotkey ScrollLockOn Alt Numpad1>

    <CreatePictureButton Button2 0 0 "{Path(dir_icon, "ability_mount_whitetiger.jpg").abspath}">
    <AddButtonToPanel Button2 MBControlPanel 0 0>
    <SetButtonHotkey Button2 Hotkey ScrollLockOn Alt Numpad2>

    <CreatePictureButton Button3 0 0 "{Path(dir_icon, "ability_hunter_aspectoftheviper.jpg").abspath}">
    <AddButtonToPanel Button3 MBControlPanel 0 0>
    <SetButtonHotkey Button3 Hotkey ScrollLockOn Alt Numpad3>

    <CreatePictureButton Button4 0 0 "{Path(dir_icon, "ability_druid_starfall.jpg").abspath}">
    <AddButtonToPanel Button4 MBControlPanel 0 0>
    <SetButtonHotkey Button4 Hotkey ScrollLockOn Alt Numpad4>

    <CreatePictureButton Button5 0 0 "{Path(dir_icon, "spell_nature_wispheal.jpg").abspath}">
    <AddButtonToPanel Button5 MBControlPanel 0 0>
    <SetButtonHotkey Button5 Hotkey ScrollLockOn Alt Numpad5>

    <CreatePictureButton Button6 0 0 "{Path(dir_icon, "spell_nature_bloodlust.jpg").abspath}">
    <AddButtonToPanel Button6 MBControlPanel 0 0>
    <SetButtonHotkey Button6 Hotkey ScrollLockOn Alt Numpad6>

    <CreatePictureButton Button7 0 0 "{Path(dir_icon, "spell_holy_auramastery.jpg").abspath}">
    <AddButtonToPanel Button7 MBControlPanel 0 0>
    <SetButtonHotkey Button7 Hotkey ScrollLockOn Alt Numpad7>

    <CreatePictureButton Button8 0 0 "{Path(dir_icon, "spell_holy_powerwordbarrier.jpg").abspath}">
    <AddButtonToPanel Button8 MBControlPanel 0 0>
    <SetButtonHotkey Button8 Hotkey ScrollLockOn Alt Numpad8>

    <CreatePictureButton Button9 0 0 "{Path(dir_icon, "spell_holy_powerwordbarrier.jpg").abspath}">
    <AddButtonToPanel Button9 MBControlPanel 0 0>
    <SetButtonHotkey Button9 Hotkey ScrollLockOn Alt Numpad9>

    <CreatePictureButton Button10 0 0 "{Path(dir_icon, "spell_nature_diseasecleansingtotem.jpg").abspath}">
    <AddButtonToPanel Button10 MBControlPanel 0 0>
    <SetButtonHotkey Button10 Hotkey ScrollLockOn Alt Numpad0>

    <CreatePictureButton Button11 0 0 "{Path(dir_icon, "spell_nature_tremortotem.jpg").abspath}">
    <AddButtonToPanel Button11 MBControlPanel 0 0>
    <SetButtonHotkey Button11 Hotkey ScrollLockOn Alt Divide>

    <CreatePictureButton Button12 0 0 "{Path(dir_icon, "spell_nature_strengthofearthtotem02.jpg").abspath}">
    <AddButtonToPanel Button12 MBControlPanel 0 0>
    <SetButtonHotkey Button12 Hotkey ScrollLockOn Alt Multiply>

    <CreateButton ButtonBar21 0 0 36 36 "Ctrl">
    <AddButtonToPanel ButtonBar21 MBControlPanel 0 0>

    <CreateButton ButtonBar22 0 0 36 36 "+">
    <AddButtonToPanel ButtonBar22 MBControlPanel 0 0>

    <CreateButton ButtonBar23 0 0 36 36 "N1-12">
    <AddButtonToPanel ButtonBar23 MBControlPanel 0 0>
        
    <CreatePictureButton Button13 0 0 "{Path(dir_icon, "ability_theblackarrow.jpg").abspath}">
    <AddButtonToPanel Button13 MBControlPanel 0 0>
    <SetButtonHotkey Button13 Hotkey ScrollLockOn Ctrl Numpad1>

    <CreatePictureButton Button14 0 0 "{Path(dir_icon, "spell_frost_iceshock.jpg").abspath}">
    <AddButtonToPanel Button14 MBControlPanel 0 0>
    <SetButtonHotkey Button14 Hotkey ScrollLockOn Ctrl Numpad2>

    <CreatePictureButton Button15 0 0 "{Path(dir_icon, "spell_holy_dispelmagic.jpg").abspath}">
    <AddButtonToPanel Button15 MBControlPanel 0 0>
    <SetButtonHotkey Button15 Hotkey ScrollLockOn Ctrl Numpad3>

    <CreatePictureButton Button16 0 0 "{Path(dir_icon, "spell_shadow_psychicscream.jpg").abspath}">
    <AddButtonToPanel Button16 MBControlPanel 0 0>
    <SetButtonHotkey Button16 Hotkey ScrollLockOn Ctrl Numpad4>

    <CreatePictureButton Button17 0 0 "{Path(dir_icon, "ability_druid_typhoon.jpg").abspath}">
    <AddButtonToPanel Button17 MBControlPanel 0 0>
    <SetButtonHotkey Button17 Hotkey ScrollLockOn Ctrl Numpad5>

    <CreatePictureButton Button18 0 0 "{Path(dir_icon, "spell_shaman_thunderstorm.jpg").abspath}">
    <AddButtonToPanel Button18 MBControlPanel 0 0>
    <SetButtonHotkey Button18 Hotkey ScrollLockOn Ctrl Numpad6>

    <CreatePictureButton Button19 0 0 "{Path(dir_icon, "spell_holy_divinehymn.jpg").abspath}">
    <AddButtonToPanel Button19 MBControlPanel 0 0>
    <SetButtonHotkey Button19 Hotkey ScrollLockOn Ctrl Numpad7>

    <CreatePictureButton Button20 0 0 "{Path(dir_icon, "spell_nature_tranquility.jpg").abspath}">
    <AddButtonToPanel Button20 MBControlPanel 0 0>
    <SetButtonHotkey Button20 Hotkey ScrollLockOn Ctrl Numpad8>

    <CreatePictureButton Button21 0 0 "{Path(dir_icon, "spell_nature_tranquility.jpg").abspath}">
    <AddButtonToPanel Button21 MBControlPanel 0 0>
    <SetButtonHotkey Button21 Hotkey ScrollLockOn Ctrl Numpad9>

    <CreatePictureButton Button22 0 0 "{Path(dir_icon, "spell_holy_symbolofhope.jpg").abspath}">
    <AddButtonToPanel Button22 MBControlPanel 0 0>
    <SetButtonHotkey Button22 Hotkey ScrollLockOn Ctrl Numpad0>

    <CreatePictureButton Button23 0 0 "{Path(dir_icon, "spell_holy_unyieldingfaith.jpg").abspath}">
    <AddButtonToPanel Button23 MBControlPanel 0 0>
    <SetButtonHotkey Button23 Hotkey ScrollLockOn Ctrl Divide>

    <CreatePictureButton Button24 0 0 "{Path(dir_icon, "spell_nature_shamanrage.jpg").abspath}">
    <AddButtonToPanel Button24 MBControlPanel 0 0>
    <SetButtonHotkey Button24 Hotkey ScrollLockOn Ctrl Multiply>

    <CreateButton ButtonBar31 0 0 36 36 "Shift">
    <AddButtonToPanel ButtonBar31 MBControlPanel 0 0>

    <CreateButton ButtonBar32 0 0 36 36 "+">
    <AddButtonToPanel ButtonBar32 MBControlPanel 0 0>

    <CreateButton ButtonBar33 0 0 36 36 "N1-12">
    <AddButtonToPanel ButtonBar33 MBControlPanel 0 0>

    // syntax: <SetPanelLayout Panel RowLength Margin [ButtonWidth ButtonHeight]>
    // RowLength is the maximum number of buttons in a row
    <SetPanelLayout MBControlPanel 3 1 36 36>

    // Set MBControlPanel Always on Top
    <TargetWin MBControlPanel>
    <AlwaysOnTop on>
"""
command = Command(
    name="AutoExec",
    actions=[
        content,
    ],
    script=script,
)
