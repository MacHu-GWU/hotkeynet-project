{{ command.title }}
{%- for block in command.blocks %}
{{ render(block)|indent(4, True) }}
{%- endfor %}