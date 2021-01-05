{{ send_label.title }}
{%- for action in send_label.actions %}
{{ render_action(action)|indent(4, True) }}
{%- endfor %}