{{ hotkey.title }}
{%- for action in hotkey.actions %}
{{ render_action(action)|indent(4, True) }}
{%- endfor %}
