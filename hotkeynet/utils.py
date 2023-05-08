# -*- coding: utf-8 -*-

import typing as T
import jinja2


def render_template(content: str, data: dict, verbose=True) -> str:
    """
    Render jinja2 string template
    """
    return jinja2.Template(content).render(verbose=verbose, **data)


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


def union_list(*lists: T.Iterable) -> list:
    """
    Union elements in all given lists.
    """
    l = list(set.union(*[set(lst) for lst in lists]))
    l.sort()
    return l


def intersection_list(*lists: T.Iterable) -> list:
    """
    Common elements in all given lists.
    """
    l = list(set.intersection(*[set(lst) for lst in lists]))
    l.sort()
    return l


def difference_list(lst: T.Iterable, *other_lsts: T.Iterable) -> list:
    """
    Remove all item in ``lst`` that exists in all ``other_lsts``
    """
    st = set(lst)
    for l in other_lsts:
        st.difference_update(l)
    l = list(st)
    l.sort()
    return l


def set_to_list(st: set, reverse=False) -> list:
    """
    Convert a set to sorted list
    """
    l = list(st)
    l.sort(reverse=reverse)
    return l


def has_duplicate(lst: list) -> bool:
    """
    Test if there is duplicate items in this list.
    """
    return len(lst) != len(set(lst))