{{ command.title }}
{%- for action in command.actions %}
{{ render_action(action)|indent(4, True) }}
{%- endfor %}