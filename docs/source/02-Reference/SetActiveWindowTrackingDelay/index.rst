.. _SetActiveWindowTrackingDelay:

SetActiveWindowTrackingDelay
==============================================================================
This command is new in build 175

Sets the active window tracking delay.

**Syntax**

::

    <SetActiveWindowTrackingDelay milliseconds>

**Parameters**

    Miilliseconds is the length of the delay in thousandths of a second.

**Remarks**

    Usually when people turn on active window tracking, they want it to work as fast as possible. With XP this happens automatically. But in Vista, by default, Microsoft inserts a delay, making active window tracking work very slowly. This function allows you to set the delay to zero so active window tracking works as fast in Vista as it does in XP.

**Example**

::

    <hotkey F1>
       <SetActiveWindowTrackingDelay 0>
       <SetActiveWindowTracking on>

**Related topics**

- :ref:`SetActiveWindowTracking`
