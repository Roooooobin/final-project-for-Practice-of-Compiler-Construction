"""
# -*- coding: utf-8 -*-
# @FileName: ReadStatement.py
# @Author  : Robin
# @Time    : 2019/11/6 18:35
"""
from src.AST.Statement import Statement


class ReadStatement(Statement):
    def __init__(self, expression):
        Statement.__init__(self)
        self.identifier = expression
        self.basetype = expression.basetype

    def __str__(self):
        return "read"

    def compile(self):
        load_code = self.identifier.compile()
        store_code = load_code.replace("lod", "str")
        code = load_code + "in {}\n".format(self.basetype.get_pcode()) + store_code
        return code

    def serialize(self, level):
        return "read"
