"""
# -*- coding: utf-8 -*-
# @FileName: OddExpression.py
# @Author  : Robin
# @Time    : 2019/11/4 12:37
"""
from src.AST.Expression import Expression
from src.AST.ExpressionType.ComparisonExpression import ComparisonExpression
from src.AST.ExpressionType.ConstantExpression import ConstantExpression
from src.AST.ExpressionType.ArithmeticExpression import ArithmeticExpression
from utils import padding


class OddExpression(Expression):
    def __init__(self, expression):
        Expression.__init__(self, None)
        self.expression = expression
        self.basetype = self.expression.basetype

    def __str__(self):
        return "odd" + str(self.expression)

    def compile(self):
        mod_compiled = ArithmeticExpression(self.expression, ConstantExpression(2, "int"), "%")
        code = ComparisonExpression(mod_compiled, ConstantExpression(1, "int"), "==").compile()
        return code

    def serialize(self, level):
        output = padding(level) + "NegateExpression\n"
        output += self.expression.serialize(level + 1)

        return output
