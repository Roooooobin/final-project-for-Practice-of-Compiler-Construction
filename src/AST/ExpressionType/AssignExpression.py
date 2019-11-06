"""
# -*- coding: utf-8 -*-
# @FileName: AssignExpression.py
# @Author  : Robin
# @Time    : 2019/11/2 20:41
"""
from src.AST.Expression import Expression
from src.AST.ExpressionType.VariableDefineExpression import VariableDefineExpression
from src.AST.ExpressionType.VariableCallExpression import VariableCallExpression


class AssignExpression(Expression):

    def __init__(self, variable, expression):
        Expression.__init__(self, None)
        self.variable = variable
        self.expression = expression
        self.basetype = self.expression.basetype

    def __str__(self):
        return str(self.variable) + " = " + str(self.expression) + "\n"

    def compile(self):
        if self.variable.basetype != self.expression.basetype:
            raise RuntimeError("Different type between variable({}) and assigned expression({})"
                               .format(self.variable.basetype, self.expression.basetype))

        code = self.expression.compile()
        if type(self.variable) is VariableDefineExpression or type(self.variable) is VariableCallExpression:
            code += "str {} 0 {}\n".format(self.variable.symbol.basetype.get_pcode(), self.variable.symbol.address)
        else:
            raise RuntimeError("Assignment Failure")
        return code

    def serialize(self, level):
        return "Assign {} -> {}".format(self.expression.serialize(0), self.variable.serialize(0))
