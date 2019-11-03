"""
# -*- coding: utf-8 -*-
# @FileName: DecrementExpression.py
# @Author  : Robin
# @Time    : 2019/11/3 9:30
"""
from src.AST.Expression import Expression
from utils import padding


class DecrementExpression(Expression):
    def __init__(self, variable):
        Expression.__init__(self, None)
        self.variable = variable
        self.basetype = self.variable.basetype

    def __str__(self):
        return str(self.variable) + "--"

    def compile(self):
        output = self.variable.compile()
        output += "dec " + self.basetype.get_pcode() + " 1\n"

        return output

    def serialize(self, level):
        output = padding(level) + "DecrementExpression\n"
        output += self.variable.serialize(level + 1)

        return output
