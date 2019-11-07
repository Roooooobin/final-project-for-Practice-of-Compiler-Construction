"""
# -*- coding: utf-8 -*-
# @FileName: WhileStatement.py
# @Author  : Robin
# @Time    : 2019/11/2 8:58
"""
from src.AST.Statement import Statement
from utils import padding


class WhileStatement(Statement):
    def __init__(self, expression, statement, symbol_table):
        Statement.__init__(self)
        self.expression = expression
        self.statement = statement
        self.symbol_table = symbol_table

    def __str__(self):
        out = "While(" + str(self.expression) + ")\n"
        out += "    " + str(self.statement) + "\n"

        return out

    def compile(self):
        # 符号表中开一个loop
        self.symbol_table.open_loop()
        begin_label = self.symbol_table.get_begin_loop()
        end_label = self.symbol_table.get_end_loop()
        code = str(begin_label) + ":\n"
        # while中的条件不成立则调至结束label
        code += self.expression.compile() + "fjp " + str(end_label) + "\n"
        # 执行statement
        code += self.statement.compile()
        code += "ujp " + str(begin_label) + "\n"
        code += str(end_label) + ":\n"
        self.symbol_table.close_loop()
        return code

    def serialize(self, level):
        output = ""
        if self.expression:
            output += padding(level) + "WHILE:\n"
            output += padding(level + 1) + self.expression.serialize(0)
        else:
            output += "WHILE"
        if self.statement:
            output += padding(level) + "THEN:\n"
            output += self.statement.serialize(level + 1)
        return output
