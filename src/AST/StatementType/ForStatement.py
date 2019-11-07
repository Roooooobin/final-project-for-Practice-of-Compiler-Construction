"""
# -*- coding: utf-8 -*-
# @FileName: ForStatement.py
# @Author  : Robin
# @Time    : 2019/11/2 8:58
"""
from src.AST.Statement import Statement
from src.Types.BooleanType import BooleanType
from src.utils import padding


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
        begin_label = self.symbol_table.get_begin_loop()
        end_label = self.symbol_table.get_end_loop()
        code = ""
        # 初始语句
        if self.init_expr:
            code += self.init_expr.compile()
        code += str(begin_label) + ":\n"
        if not isinstance(self.condition_expr.basetype, BooleanType):
            raise RuntimeError("Check condition in for loop should be of boolean type")
        code += self.condition_expr.compile()
        code += "fjp " + str(end_label) + "\n"
        code += self.statement.compile()
        code += self.update_expr.compile()
        code += "ujp " + str(begin_label) + "\n"
        code += str(end_label) + ":\n"
        self.symbol_table.close_loop()
        return code

    def serialize(self, level):
        output = padding(level) + "ForStatement\n"
        if self.init_expr:
            output += padding(level + 1) + "->init: \n" + self.init_expr.serialize(level + 1) + "\n"
        if self.condition_expr:
            output += padding(level + 1) + "->condition: \n" + self.condition_expr.serialize(level + 1) + "\n"
        if self.update_expr:
            output += padding(level + 1) + "->update: \n" + self.update_expr.serialize(level + 1) + "\n"
        if self.statement is not None:
            output += padding(level + 1) + "->statements: \n" + self.statement.serialize(level + 1)
        return output
