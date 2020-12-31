    <SendLabel {{ send_label.targets }}>
    {%- for action in send_label.actions %}
        {{ action.dump() }}
    {%- endfor %}
