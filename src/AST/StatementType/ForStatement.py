"""
# -*- coding: utf-8 -*-
# @FileName: ForStatement.py
# @Author  : Robin
# @Time    : 2019/11/2 8:58
"""
from src.AST.Statement import Statement
from src.Types.BooleanType import BooleanType
from utils import padding


class ForStatement(Statement):
    def __init__(self, init_expr, condition_expr, update_expr, statement, symbol_table):
        Statement.__init__(self)
        self.init_expr = init_expr
        self.condition_expr = condition_expr
        self.update_expr = update_expr
        self.statement = statement
        self.symbol_table = symbol_table

    def __str__(self):
        out = "For(" + str(self.init_expr) + ", " + str(self.condition_expr) + ", " + str(self.update_expr) + ")\n"
        out += "    " + str(self.statement)

        return out

    def compile(self):
        self.symbol_table.open_loop()
        # Get begin and end label
        begin_label = self.symbol_table.get_begin_loop()
        end_label = self.symbol_table.get_end_loop()
        code = ""
        # compile the initial expression
        if self.init_expr:
            code += self.init_expr.compile()
        # Mark begin of loop
        code += str(begin_label) + ":\n"
        # Check if check is an boolean Expression
        if not isinstance(self.condition_expr.basetype, BooleanType):
            raise RuntimeError("Check condition in for loop should be of boolean type")
        # Compile check
        code += self.condition_expr.compile()
        code += "fjp " + str(end_label) + "\n"
        # Compile the statement
        code += self.statement.compile()
        # compile the update
        code += self.update_expr.compile()
        # Jump to begin with unconditional Jump
        code += "ujp " + str(begin_label) + "\n"
        # Mark end of for loop
        code += str(end_label) + ":\n"
        self.symbol_table.close_loop()

        return code

    def serialize(self, level):
        out = padding(level) + "ForStatement\n"
        if self.init_expr:
            out += padding(level + 1) + "->init: \n" + self.init_expr.serialize(level + 1) + "\n"
        if self.condition_expr:
            out += padding(level + 1) + "->condition: \n" + self.condition_expr.serialize(level + 1) + "\n"
        if self.update_expr:
            out += padding(level + 1) + "->update: \n" + self.update_expr.serialize(level + 1) + "\n"
        if self.statement is not None:
            out += padding(level + 1) + "->statements: \n" + self.statement.serialize(level + 1)

        return out
