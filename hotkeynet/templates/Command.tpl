<Command {{ command.name }}>
    {%- for action in command.actions %}
    {{ render_action(action) }}
    {%- endfor %}