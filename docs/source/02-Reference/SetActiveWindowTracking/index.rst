.. _SetActiveWindowTracking:

SetActiveWindowTracking
==============================================================================
This command is new in build 107.

Enables, disables, or toggles active window tracking (also known as "activation follows mouse").

**Syntax**

::

    <SetActiveWindowTracking Switch>

**Parameters**

    Switch must be either On, Off , or Toggle.

**Remarks**

    Turning this on has the same effect as enabling "activation follows mouse" in Microsoft's PowerToys TweakUI.

    This command does not write to the registry. The new setting lasts until you reboot.

**Example**

::

    <hotkey F1>
       <SetActiveWindowTrackingDelay 0>
       <SetActiveWindowTracking on>

**Related topics**

- :ref:`SetActiveWindowTrackingDelay`
