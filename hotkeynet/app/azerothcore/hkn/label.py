# -*- coding: utf-8 -*-

import typing as T

import hotkeynet as hk

if T.TYPE_CHECKING:
    from .script import HknScript


class LabelMixin:
    def build_labels(self: "HknScript"):
        self.labels: T.List[hk.Label] = [
            hk.Label.make(name=window.label, window=window.title)
            for window, _ in self.mode.login_window_and_account_pairs
        ]
        self.n_labels: int = len(self.labels)

    def build_label_mixin(self):
        self.build_labels()
