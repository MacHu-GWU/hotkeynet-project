{% for command in script.commands.values() %}
{{ command.dump() }}
{% endfor %}
