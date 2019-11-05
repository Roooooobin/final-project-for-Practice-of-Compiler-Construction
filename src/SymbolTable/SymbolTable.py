"""
# -*- coding: utf-8 -*-
# @FileName: SymbolTable.py
# @Author  : Robin
# @Time    : 2019/10/30 19:01
"""
from src.SymbolTable.Scope import Scope
from src.SymbolTable.Symbol import Symbol


class SymbolTable:
    def __init__(self):
        """Initializer, will also open the global scope"""
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
        """Close Scope"""
        if not self.scope.parent_scope:
            raise ScopeError("No scope opened previously")

        self.scope = self.scope.parent_scope

    def register_symbol(self, identifier, basetype):
        """Register a Symbol in the current scope with an identifier(string) and basetype(Type) is an array(bool)"""
        if self.scope.symbol_is_in_scope(identifier):
            raise SymbolAlreadyRegisteredError("Symbol '" + identifier + "' already registered in scope")

        if basetype.get_size() == 0:
            raise TypeError("Type should have a size greater then 0")

        symbol = Symbol(identifier, basetype, self.scope.get_total_allocated())

        self.scope.add_symbol(symbol)
        self.scope.allocated += basetype.get_size()

        return symbol

    def get_symbol(self, identifier):
        """Get a symbol from the Symbol Table with an identifier(string)"""
        search_scope = self.scope

        while True:
            symbol = search_scope.get_symbol(identifier)

            if symbol:
                return symbol
            else:
                search_scope = search_scope.parent_scope
                if not search_scope:
                    # Stop in main scope
                    break

        raise SymbolNotRegisteredError("Symbol '" + identifier + "' not registered")

    def open_loop(self):
        """Open a loop"""
        loop = Loop(self.labels + 1, self.labels + 2)
        self.labels += 2

        self.loops.append(loop)

    def close_loop(self):
        """Close a loop"""
        if len(self.loops) == 0:
            raise ScopeError("No loops opened")

        self.loops.pop()

    def get_begin_loop(self):
        """Get the start label of the loop"""
        return "bl" + str(self.loops[-1].begin)

    def get_end_loop(self):
        """Get the end label of the loop"""
        return "el" + str(self.loops[-1].end)

    def create_label(self):
        """Create a label"""
        self.labels += 1
        return "l" + str(self.labels)

    def get_allocated_space(self):
        """Get the size of the address space in use"""
        return self.scope.allocated

    def __str__(self):
        """String Representation"""
        output = "Symbol Table:\n" + "--------------\n" + self.scope.printer(0) + "\n" + "--------------\n"
        return output
