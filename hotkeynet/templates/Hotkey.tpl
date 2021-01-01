{{ hotkey.title }}
    {%- for action in hotkey.actions %}
    {{ render_action(action) }}
    {%- endfor %}
