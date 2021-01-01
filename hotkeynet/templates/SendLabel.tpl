{{ send_label.title }}
    {%- for action in send_label.actions %}
        {{ action.dump() }}
    {%- endfor %}