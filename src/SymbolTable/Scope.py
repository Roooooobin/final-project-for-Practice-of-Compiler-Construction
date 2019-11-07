"""
# -*- coding: utf-8 -*-
# @FileName: Scope.py
# @Author  : Robin
# @Time    : 2019/10/30 19:02
"""
from utils import padding


# 作用域，包括开启新作用域，加入新symbol到作用域等
class Scope:
    def __init__(self, parent_scope):
        self.parent_scope = parent_scope
        self.allocated = 0
        self.symbols = []
        self.scopes = []

    def open_scope(self):
        new_scope = Scope(self)
        self.scopes.append(new_scope)
        return self.scopes[-1]

    def add_symbol(self, symbol):
        self.symbols.append(symbol)

    # 返回作用域的占用空间
    def get_allocated(self):
        return self.allocated

    # 返回此前的全部占用过的空间，以给scope中的局部变量附上正确的地址
    def get_total_allocated(self):
        sum_memery = self.allocated
        scope = self.parent_scope
        while scope:
            sum_memery += scope.get_allocated()
            scope = scope.parent_scope
        return sum_memery

    def symbol_is_in_scope(self, identifier):
        return True if self.get_symbol(identifier) else False

    def get_symbol(self, identifier):
        for symbol in self.symbols:
            if symbol.identifier == identifier:
                return symbol
        return None

    def printer(self, level):
        output = padding(level) + "||SCOPE(" + str(self.allocated) + ")\n"
        for symbol in self.symbols:
            output += padding(level) + "-> Symbol(" + symbol.identifier + ") : " + str(symbol.basetype) + "\n"
        for scope in self.scopes:
            output += scope.printer(level + 1)
        return output
