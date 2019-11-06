"""
# -*- coding: utf-8 -*-
# @FileName: CastExpression.py
# @Author  : Robin
# @Time    : 2019/11/6 16:49
"""
from src.AST.Expression import Expression
from src.Types.IntegerType import IntegerType
from src.Types.RealType import RealType


class CastExpression(Expression):
    def __init__(self, basetype, expression):
        Expression.__init__(self, None)
        self.expression = expression
        if basetype == "int":
            self.basetype = IntegerType()
        elif basetype == "real":
            self.basetype = RealType()
        else:
            pass

    def __str__(self):
        return str(self.basetype) + " " + str(self.expression)

    def compile(self):
        code = self.expression.compile() + "conv {} {}\n".format(self.expression.basetype.get_pcode(),
                                                                 self.basetype.get_pcode())
        return code

    def serialize(self, level):
        return str(self.basetype) + " " + str(self.expression)