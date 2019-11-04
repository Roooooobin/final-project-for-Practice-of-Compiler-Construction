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
        self.left_expression = left_expression
        self.right_expression = right_expression
        # 比较两边的类型必须相同
        if self.left_expression.basetype != self.right_expression.basetype:
            raise RuntimeError("The two types of the expressions in the comparison expression should be the same"
                               " now: left: {}, right: {}".format(
                                str(self.left_expression.basetype), str(self.right_expression)))
        self.basetype = BooleanType()

    def __str__(self):
        return str(self.left_expression) + " " + str(self.operation) + " " + str(self.right_expression)

    def compile(self):
        operations = {'==': 'equ', '!=': 'neq', '>': 'grt', '<': 'les', '>=': 'geq', '<=': 'leq'}
        code = self.left_expression.compile()
        code += self.right_expression.compile()
        code += operations[self.operation] + " " + self.left_expression.basetype.get_pcode() + "\n"

        return code

    def serialize(self, level):
        return self.left_expression.serialize(0) + " " + self.operation + " " + self.right_expression.serialize(0)
