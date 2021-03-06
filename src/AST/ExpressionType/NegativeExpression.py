"""
# -*- coding: utf-8 -*-
# @FileName: NegativeExpression.py
# @Author  : Robin
# @Time    : 2019/11/3 10:12
"""
from src.AST.Expression import Expression
from src.utils import padding


class NegativeExpression(Expression):
    def __init__(self, expression):
        Expression.__init__(self, None)
        self.expression = expression
        self.basetype = self.expression.basetype

    def __str__(self):
        return "-" + str(self.expression)

    def compile(self):
        code = self.expression.compile()
        code += "neg " + self.basetype.get_pcode() + "\n"
        return code

    def serialize(self, level):
        output = padding(level) + "NegateExpression\n"
        output += self.expression.serialize(level + 1)
        return output
