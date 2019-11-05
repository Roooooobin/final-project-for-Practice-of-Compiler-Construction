"""
# -*- coding: utf-8 -*-
# @FileName: LogicExpression.py
# @Author  : Robin
# @Time    : 2019/11/4 10:51
"""
from src.AST.Expression import Expression
from src.Types.BooleanType import BooleanType


class LogicExpression(Expression):
    def __init__(self, left_expression, right_expression, operation):
        Expression.__init__(self, None)
        self.left_expression = left_expression
        self.right_expression = right_expression
        self.operation = operation
        # print(self.left_expression.basetype, self.right_expression.basetype)
        if self.left_expression.basetype != self.right_expression.basetype:
            raise RuntimeError("left and right expression must be of the same type")
        if not isinstance(self.left_expression.basetype, BooleanType):
            raise RuntimeError("logic expression must be bool op bool, but now is {}"
                               .format(self.left_expression.basetype))
        if not isinstance(self.right_expression.basetype, BooleanType):
            raise RuntimeError("logic expression must be bool op bool, but now is {}"
                               .format(self.left_expression.basetype))
        self.basetype = BooleanType

    def __str__(self):
        return str(self.left_expression) + " " + str(self.right_expression) + " " + self.operation

    def compile(self):
        operations = {"&&": "and", "||": "or"}
        left_compiled = self.left_expression.compile()
        right_compiled = self.right_expression.compile()
        if self.operation in ["&&", "||"]:
            code = left_compiled + right_compiled + operations[self.operation] + "\n"
        elif self.operation == "^":
            # 异或通过与、或来实现
            code = "{lc}not\n{rc}and\n{rc}not\n{lc}and\nor\n".format(lc=left_compiled, rc=right_compiled)
        else:
            code = None
        return code

    def serialize(self, level):
        return self.left_expression.serialize(0) + " " + self.operation + " " + self.right_expression.serialize(0)