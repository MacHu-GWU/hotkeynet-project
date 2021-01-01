{% for command in script.commands.values() %}
{{ command.dump() }}
{% endfor %}

{% for hotkey in script.hotkeys.values() %}
{{ hotkey.dump() }}
{% endfor %}
