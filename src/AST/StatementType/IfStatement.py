"""
# -*- coding: utf-8 -*-
# @FileName: IfStatement.py
# @Author  : Robin
# @Time    : 2019/11/2 8:58
"""
from src.AST.Statement import Statement


class IfStatement(Statement):
    def __init__(self, expression, statement, alternative_statement, symbol_table):
        Statement.__init__(self)
        self.expression = expression
        self.statement = statement
        self.alternativeStatement = alternative_statement
        self.symbol_table = symbol_table

    def __str__(self):
        out = "If(" + str(self.expression) + ")\n"
        out += "    " + str(self.statement) + "\n"
        if self.alternativeStatement:
            out += "Else\n"
            out += "    " + str(self.alternativeStatement) + "\n"
        return out

    def compile(self):
        self.symbol_table.open_scope()
        end_if_label = self.symbol_table.create_label()
        end_else_label = self.symbol_table.create_label()
        code = self.expression.compile()
        code += "fjp " + str(end_if_label) + "\n"
        if self.statement:
            code += self.statement.compile()
        # 如果有else
        if self.alternativeStatement:
            code += "ujp " + str(end_else_label) + "\n"
        code += str(end_if_label) + ":\n"
        self.symbol_table.close_scope()
        if not self.alternativeStatement:
            return code
        self.symbol_table.open_scope()
        code += self.alternativeStatement.compile()
        code += str(end_else_label) + ":\n"
        self.symbol_table.close_scope()
        return code

    def serialize(self, level):
        return ""
