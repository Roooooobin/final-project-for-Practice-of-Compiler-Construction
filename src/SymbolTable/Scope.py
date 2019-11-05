"""
# -*- coding: utf-8 -*-
# @FileName: Scope.py
# @Author  : Robin
# @Time    : 2019/10/30 19:02
"""
from utils import padding


class Scope:
    """An Scope in the program"""
    def __init__(self, parent_scope):
        """Initializer with allocated(int) which represents from where in the memory the scope can start allocating"""
        self.parent_scope = parent_scope
        self.allocated = 0
        self.symbols = []
        self.scopes = []

    def open_scope(self):
        new_scope = Scope(self)
        self.scopes.append(new_scope)
        return self.scopes[-1]

    def add_symbol(self, symbol):
        """Add a Symbol to the Scope"""
        self.symbols.append(symbol)

    def get_allocated(self):
        """Returns how many memory was allocated in this scope"""
        return self.allocated

    def get_total_allocated(self):
        """Return how many memory was allocated in this scope and it's children scopes"""
        sum_memery = self.allocated
        scope = self.parent_scope
        while scope:
            print(scope.get_allocated())
            sum_memery += scope.get_allocated()
            scope = scope.parent_scope

        return sum_memery

    def symbol_is_in_scope(self, identifier):
        """Returns true if the scope has the symbol"""
        return True if self.get_symbol(identifier) else False

    def get_symbol(self, identifier):
        """Get the symbol in the scope"""
        for symbol in self.symbols:
            if symbol.identifier == identifier:
                return symbol

        return None

    def printer(self, level):
        output = padding(level) + "||SCOPE(" + str(self.allocated) + ")\n"

        # Symbols
        for symbol in self.symbols:
            output += padding(level) + "-> Symbol(" + symbol.identifier + ") : " + str(symbol.basetype) + "\n"

        for scope in self.scopes:
            output += scope.printer(level + 1)

        return output
