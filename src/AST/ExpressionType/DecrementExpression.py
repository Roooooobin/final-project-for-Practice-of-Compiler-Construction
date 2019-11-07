"""
# -*- coding: utf-8 -*-
# @FileName: DecrementExpression.py
# @Author  : Robin
# @Time    : 2019/11/3 9:30
"""
from src.AST.Expression import Expression
from src.utils import padding


class DecrementExpression(Expression):
    def __init__(self, variable):
        Expression.__init__(self, None)
        self.variable = variable
        self.basetype = self.variable.basetype

    def __str__(self):
        return str(self.variable) + "--"

    # 因为Pmachine对于自增自减是原地执行，所以会影响后续操作，做完后str一下
    def compile(self):
        code = self.variable.compile()
        code += "dec " + self.basetype.get_pcode() + " 1\n"
        code += self.variable.compile().replace("lod", "str")
        return code

    def serialize(self, level):
        output = padding(level) + "DecrementExpression\n"
        output += self.variable.serialize(level + 1)
        return output
