"""
# -*- coding: utf-8 -*-
# @FileName: CompoundStatement.py
# @Author  : Robin
# @Time    : 2019/11/2 8:58
"""
from src.AST.Statement import Statement
from src.utils import padding


class CompoundStatement(Statement):
    def __init__(self, statements):
        Statement.__init__(self)
        self.statements = statements

    def __str__(self):
        out = ""
        for statement in self.statements:
            out += "   " + str(statement) + "\n"

        return out

    def compile(self):
        if not self.statements:
            return ""
        code = ""
        for statement in self.statements:
            code += statement.compile()
        return code

    def serialize(self, level):
        out = ""
        for statement in self.statements:
            out += padding(level) + statement.serialize(level + 1) + "\n"
        return out
