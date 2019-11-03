"""
# -*- coding: utf-8 -*-
# @FileName: ComparisonExpression.py
# @Author  : Robin
# @Time    : 2019/11/3 9:54
"""
from src.AST.Expression import Expression
from src.Types.BooleanType import BooleanType


class ComparisonExpression(Expression):
    def __init__(self, left_expression, right_expression, operation):
        Expression.__init__(self, None)
        self.operation = operation
        self.leftExpression = left_expression
        self.rightExpression = right_expression
        # 比较两边的类型必须相同
        if self.leftExpression.basetype != self.rightExpression.basetype:
            raise RuntimeError("The two types of the expressions in the arithmetic expression should be the same")
        self.basetype = BooleanType()

    def __str__(self):
        return str(self.leftExpression) + " " + str(self.operation) + " " + str(self.rightExpression)

    def compile(self):
        operations = {'==': 'equ', '!=': 'neq', '>': 'grt', '<': 'les', '>=': 'geq', '<=': 'leq'}
        code = self.leftExpression.compile()
        code += self.rightExpression.compile()
        code += operations[self.operation] + " " + self.leftExpression.basetype.get_pcode() + "\n"

        return code

    def serialize(self, level):
        return self.leftExpression.serialize(0) + " " + self.operation + " " + self.rightExpression.serialize(0)
