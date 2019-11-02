"""
# -*- coding: utf-8 -*-
# @FileName: ConstantExpression.py
# @Author  : Robin
# @Time    : 2019/11/2 21:14
"""
from src.AST.Expression import Expression
from src.Types.BooleanType import BooleanType
from src.Types.IntegerType import IntegerType
from utils import padding


class ConstantExpression(Expression):
    def __init__(self, value, basetype):
        Expression.__init__(self, None)
        self.basetype = basetype
        self.value = value
        self.compiled_codes = None
        if self.basetype == "bool":
            self.basetype = BooleanType()
            if self.value is True:
                self.compiled_codes = "ldc b t\n"
            elif self.value is False:
                self.compiled_codes = "ldc b f\n"
            else:
                raise RuntimeError("Wrong Boolean Value")
        elif self.basetype == "int":
            self.basetype = IntegerType()
            self.compiled_codes = "ldc i {}\n".format(str(self.value))
        else:
            raise RuntimeError("Type {} is not supported".format(self.basetype))

    def __str__(self):
        return "ConstantExpression"

    def compile(self):
        return self.compiled_codes

    def serialize(self, level):
        output = padding(level) + "ConstantExpression\n" + self.basetype.serialize(level+1)
        return output
