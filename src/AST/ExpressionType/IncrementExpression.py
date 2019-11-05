"""
# -*- coding: utf-8 -*-
# @FileName: IncrementExpression.py
# @Author  : Robin
# @Time    : 2019/11/3 9:30
"""
from src.AST.Expression import Expression
from utils import padding


class IncrementExpression(Expression):
    def __init__(self, variable):
        Expression.__init__(self, None)
        self.variable = variable
        self.basetype = self.variable.basetype

    def __str__(self):
        return str(self.variable) + "++"

    def compile(self):
        output = self.variable.compile()
        output += "inc " + self.basetype.get_pcode() + " 1\n"
        output += self.variable.compile().replace("lod", "str")
        return output

    def serialize(self, level):
        output = padding(level) + "IncrementExpression\n"
        output += self.variable.serialize(level + 1)

        return output
