"""
# -*- coding: utf-8 -*-
# @FileName: VariableDefineExpression.py
# @Author  : Robin
# @Time    : 2019/10/31 15:33
"""
from src.AST.Expression import Expression
from utils import padding


class VariableDefineExpression(Expression):
    def __init__(self, symbol):
        """Create variable call with symbol(Symbol)"""
        Expression.__init__(self, None)
        self.symbol = symbol
        self.basetype = symbol.basetype

    def __str__(self):
        output = "Define " + str(self.basetype) + ":" + str(self.symbol.identifier) + "\n"
        return output

    # TODO: no return?
    def compile(self):
        code = "lod " + str(self.symbol.basetype.get_pcode()) + " 0 " + str(self.symbol.address) + "\n"
        return code

    def serialize(self, level):
        return padding(level) + "VariableExpression(" + self.symbol.identifier + ")\n"
