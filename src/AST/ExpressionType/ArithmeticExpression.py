"""
# -*- coding: utf-8 -*-
# @FileName: ArithmeticExpression.py
# @Author  : Robin
# @Time    : 2019/10/31 18:48
"""
from src.AST.Expression import Expression
from src.Types.IntegerType import IntegerType
from src.Types.RealType import RealType


class ArithmeticExpression(Expression):
    def __init__(self, left_expression, right_expression, operation):
        Expression.__init__(self, None)
        self.operation = operation
        self.left_expression = left_expression
        self.right_expression = right_expression
        # Determine the type of the expression
        # check if types of 2 expressions are the same
        if self.left_expression.basetype != self.right_expression.basetype:
            raise RuntimeError("The two types of the expressions in the arithmetic expression should be the same")

        # if not isinstance(self.left_expression.basetype, IntegerType):
        #     raise RuntimeError("Left side of arithmetic expression should be an integer but now it is a: "
        #                        + str(type(self.left_expression.basetype)))
        #
        # if not isinstance(self.right_expression.basetype, IntegerType):
        #     raise RuntimeError("Right side of arithmetic expression should be an integer but now it is a: "
        #                        + str(type(self.right_expression.basetype)))
        # set the type of this expression
        self.basetype = self.left_expression.basetype

    def __str__(self):
        return str(self.left_expression) + " " + str(self.operation) + " " + str(self.right_expression)

    def compile(self):
        operations = {"+": "add", "-": "sub", "/": "div", "*": "mul"}
        left_compiled = self.left_expression.compile()
        right_compiled = self.right_expression.compile()
        if self.operation in ["+", "-", "/", "*"]:
            code = left_compiled + right_compiled
            code += "{} {}\n".format(operations[self.operation], self.basetype.get_pcode())
        elif self.operation == "%":
            # 求余的实现a % b = a - a / b * b，转为一个后缀式表示
            code = "{lc}{lc}{rc}div {c}\n{rc}mul {c}\nsub {c}\n".format(
                    lc=left_compiled, rc=right_compiled, c=self.basetype.get_pcode())
        else:
            code = None
        return code

    def serialize(self, level):
        return self.left_expression.serialize(0) + " " + str(self.operation) + " " + self.right_expression.serialize(0)
