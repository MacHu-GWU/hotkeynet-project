# -*- coding: utf-8 -*-

import jinja2


def render_template(content, verbose=True, **kwargs):
    """
    Render jinja2 string template
    """
    return jinja2.Template(content).render(verbose=verbose, **kwargs)


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


def union_list(*lists) -> list:
    """
    Union elements in all given lists.
    """

    l = list(set.union(*[set(lst) for lst in lists]))
    l.sort()
    return l


def intersection_list(*lists) -> list:
    """
    Common elements in all given lists.
    """
    l = list(set.intersection(*[set(lst) for lst in lists]))
    l.sort()
    return l


def difference_list(lst, *other_lsts) -> list:
    """
    Remove all item in ``lst`` that exists in all ``other_lsts``
    """
    st = set(lst)
    for l in other_lsts:
        st.difference_update(l)
    l = list(st)
    l.sort()
    return l


def set_to_list(st) -> list:
    l = list(st)
    l.sort()
    return l
