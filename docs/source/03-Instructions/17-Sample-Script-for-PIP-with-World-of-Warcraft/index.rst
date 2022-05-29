.. _pip-for-wow:

Sample Script for PIP with World of Warcraft
==============================================================================
Sample Script for PIP with World of Warcraft

Here's a basic script for picture-in-picture with World of Warcraft.

Requires build 139 or higher. Toggle scroll lock to turn hotkeys off and on.

You can toggle between these two pictures with a key press. The sample script (below) shows how. You can modify the script to toggle any number of WoW's in any configuration you like::

    //================================================================
    // PIP TOGGLING WITH WORLD OF WARCRAFT
    //
    // Requires HotkeyNet build 139 or higher.
    //
    // This sample shows how to place one WoW window inside another.
    //
    // Each time you press F1 the two windows switch positions.
    //
    // WoW must be set to windowed mode on video options in game.
    //
    // Toggle Scroll Lock to enable and disable the hotkey
    //
    //================================================================

    //----------------------------------------------------------------
    // RENAME WINDOWS AND REMOVE BORDERS
    //----------------------------------------------------------------
    <Hotkey Ctrl R>
       <RenameWin World WoW1>
       <RemoveWinFrame>
       <RenameWin World WoW2>
       <RemoveWinFrame>

    //----------------------------------------------------------------
    // SET PIP CONFIGURATION
    // Usage: <SetPip BigWindowName LittleWindowName>
    // This command is called by <Hotkey F1> which is defined below.
    //----------------------------------------------------------------
    <Command SetPip>
       <TargetWin %2%>
          <SetWinSize 400 300>
          <SetWinPos 775 515>
       <TargetWin %1%>
          <SetWinPos 0 0>
          <SetWinSize 1200 900>
       <TargetWin %2%>
          <SetForegroundWin>
          <UpdateWin>
       <TargetWin %1%>
          <SetWinRegion 775 515 400 300>
          <SetForegroundWin>

    //----------------------------------------------------------------
    // TOGGLE PIP CONFIG WITH HOTKEY
    //----------------------------------------------------------------
    <Hotkey ScrollLockOn F1>
       <Toggle>
          <SetPip WoW1 WoW2>
       <Toggle>
          <SetPip WoW2 WoW1>

    //================================================================
    // END OF FILE
    //================================================================
