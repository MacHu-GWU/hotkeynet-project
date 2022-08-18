{%- for sub_block in block.blocks %}
{{ render(sub_block, verbose=verbose) }}
{%- endfor %}