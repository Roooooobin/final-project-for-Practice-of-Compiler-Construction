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
        # Compile expression and jump if needed
        code = self.expression.compile()
        code += "fjp " + str(end_if_label) + "\n"
        # compile the statement to execute if existing
        if self.statement:
            code += self.statement.compile()
        # need to jump to the end of ELSE if there's an alternative
        if self.alternativeStatement:
            code += "ujp " + str(end_else_label) + "\n"
        # Mark end if code
        code += str(end_if_label) + ":\n"
        # end scope if
        self.symbol_table.close_scope()
        # Stop if no alternative statement
        if not self.alternativeStatement:
            return code
        # Compile alternative statement
        self.symbol_table.open_scope()
        code += self.alternativeStatement.compile()
        code += str(end_else_label) + ":\n"
        self.symbol_table.close_scope()
        return code

    def serialize(self, level):
        return ""
