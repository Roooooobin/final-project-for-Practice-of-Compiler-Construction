"""
# -*- coding: utf-8 -*-
# @FileName: Scope.py
# @Author  : Robin
# @Time    : 2019/10/30 19:02
"""


class Scope:
    """An Scope in the program"""
    def __init__(self, parent_scope):
        """Initializer with allocated(int) which represents from where in the memory the scope can start allocating"""
        self.parent_scope = parent_scope
        self.allocated = 0
        self.symbols = []
        self.aliases = []
        self.functions = []
        self.scopes = []