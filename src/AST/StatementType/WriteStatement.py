"""
# -*- coding: utf-8 -*-
# @FileName: WriteStatement.py
# @Author  : Robin
# @Time    : 2019/11/4 23:54
"""
from src.AST.Statement import Statement


class WriteStatement(Statement):
    def __init__(self, expression, write_type):
        Statement.__init__(self)
        self.expression = expression
        self.basetype = expression.basetype
        self.write_type = write_type

    def __str__(self):
        return "statement"

    def compile(self):
        print(self.basetype)
        type_out_dic = {"int": "i", "bool": "b"}
        code = self.expression.compile()
        if self.write_type == "write":
            return "{}out {}\n".format(code, type_out_dic.get(str(self.basetype)))
        else:
            return "{}out {}\nldc c '\\n'\nout c\n".format(code, type_out_dic.get(str(self.basetype)))

    def serialize(self, level):
        return "statement"
