"""
# -*- coding: utf-8 -*-
# @FileName: SymbolTable.py
# @Author  : Robin
# @Time    : 2019/10/30 19:01
"""
from src.SymbolTable.Loop import Loop
from src.SymbolTable.Scope import Scope
from src.SymbolTable.Symbol import Symbol


class SymbolTable:
    def __init__(self):
        self.table = None
        self.scope = None
        self.loops = []
        self.labels = 0
        # Open the global scope
        self.table = Scope(None)
        self.scope = self.table

    def open_scope(self):
        self.scope = self.scope.open_scope()

    def close_scope(self):
        if not self.scope.parent_scope:
            raise RuntimeError("No scope opened previously")

        self.scope = self.scope.parent_scope

    # 在符号表中注册一个新symbol
    def register_symbol(self, identifier, basetype):
        if self.scope.symbol_is_in_scope(identifier):
            raise RuntimeError("Symbol '" + identifier + "' already registered in scope")
        if basetype.get_size() == 0:
            raise TypeError("Type should have a size greater then 0")

        symbol = Symbol(identifier, basetype, self.scope.get_total_allocated())
        self.scope.add_symbol(symbol)
        self.scope.allocated += basetype.get_size()
        return symbol

    # 在当前scope找，找不到一直往上(parent)中找，直到在main也没有
    def get_symbol(self, identifier):
        search_scope = self.scope
        while True:
            symbol = search_scope.get_symbol(identifier)
            if symbol:
                return symbol
            else:
                search_scope = search_scope.parent_scope
                if not search_scope:
                    break

        raise KeyError("Symbol '" + identifier + "' not registered")

    def open_loop(self):
        loop = Loop(self.labels + 1, self.labels + 2)
        self.labels += 2
        self.loops.append(loop)

    def close_loop(self):
        if len(self.loops) == 0:
            raise RuntimeError("No loops opened")
        self.loops.pop()

    def get_begin_loop(self):
        return "bl" + str(self.loops[-1].begin)

    def get_end_loop(self):
        return "el" + str(self.loops[-1].end)

    def create_label(self):
        self.labels += 1
        return "l" + str(self.labels)

    def get_allocated_space(self):
        return self.scope.allocated

    def __str__(self):
        output = "Symbol Table:\n" + "--------------\n" + self.scope.printer(0) + "\n" + "--------------\n"
        return output
