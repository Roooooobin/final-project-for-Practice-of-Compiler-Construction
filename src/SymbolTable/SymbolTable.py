"""
# -*- coding: utf-8 -*-
# @FileName: SymbolTable.py
# @Author  : Robin
# @Time    : 2019/10/30 19:01
"""
from src.SymbolTable import Scope


class SymbolTable:
    def __init__(self):
        """Initializer, will also open the global scope"""
        self.table = None
        self.scope = None
        self.loops = []
        self.labels = 0

        # Open the global scope
        # self.table = Scope(None)
        # self.scope = self.table
