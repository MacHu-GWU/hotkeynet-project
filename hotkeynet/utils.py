# -*- coding: utf-8 -*-

import jinja2


def render_template(content, **kwargs):
    """
    Render jinja2 string template
    """
    return jinja2.Template(content).render(**kwargs)


def remove_comments(content: str) -> str:
    """
    Remove all Comments from hotkeynet script
    """
    lines = content.split("\n")

    lines_new = list()

    for line in lines:
        line_striped = line.strip()
        if not line_striped:
            continue
        if line_striped.startswith("//"):
            continue
        # if line_striped.startswith("function"):
        #     continue
        # if line_striped.startswith("}"):
        #     continue
        line = line.split("//", 1)[0]
        lines_new.append(line)

    new_content = "\n".join(lines_new)
    return new_content


def remove_empty_line(content: str) -> str:
    """
    Remove all full empty line
    """
    lines = content.split("\n")

    lines_new = list()
    for line in lines:
        if line.strip():
            lines_new.append(line)

    new_content = "\n".join(lines_new)
    return new_content


def remove_indent(content: str) -> str:
    """
    Allow developer to write inline string like:

    content = '''
    <div>
        <strong></strong>
    </div>
    '''

    and remove left whitespace cased by python script indentation.
    """
    lines = content.split("\n")[1:-1]
    values = list()
    for line in lines:
        if line.strip():
            unindent = len(line) - len(line.lstrip())
            values.append(unindent)
    unindent = min(values)
    return "\n".join([line[unindent:] for line in lines])
