"""
# -*- coding: utf-8 -*-
# @FileName: VariableCallExpression.py
# @Author  : Robin
# @Time    : 2019/10/31 15:23
"""
from src.AST.Expression import Expression
from utils import padding


class VariableCallExpression(Expression):
    def __init__(self, symbol):
        """Call variable call with symbol(Symbol)"""
        Expression.__init__(self, None)
        self.symbol = symbol
        self.basetype = symbol.basetype

    def __str__(self):
        output = "Call " + str(self.symbol.identifier) + "\n"
        return output

    def compile(self):
        code = "lod " + str(self.symbol.basetype.get_pcode()) + " 0 " + str(self.symbol.address) + "\n"
        return code

    def serialize(self, level):
        return padding(level) + "VariableExpression(" + self.symbol.identifier + ")\n"
