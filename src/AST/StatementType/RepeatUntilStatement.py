"""
# -*- coding: utf-8 -*-
# @FileName: RepeatUntilStatement.py
# @Author  : Robin
# @Time    : 2019/11/6 22:44
"""
from src.AST.Statement import Statement
from utils import padding


class RepeatUntilStatement(Statement):
    def __init__(self, expression, statement, symbol_table):
        Statement.__init__(self)
        self.expression = expression
        self.statement = statement
        self.symbol_table = symbol_table

    def __str__(self):
        output = "repeat" + str(self.statement) + "\n"
        output += "until not (" + str(self.expression) + ")\n"
        return output

    def compile(self):
        self.symbol_table.open_loop()
        begin_label = self.symbol_table.get_begin_loop()
        end_label = self.symbol_table.get_end_loop()
        compiled_stmt = self.statement.compile()
        # repeat until也先会执行一次
        code = compiled_stmt
        code += str(begin_label) + ":\n"
        # 当expression不成立时结束
        code += self.expression.compile() + "not\nfjp " + str(end_label) + "\n"
        code += compiled_stmt
        code += "ujp " + str(begin_label) + "\n"
        code += str(end_label) + ":\n"
        self.symbol_table.close_loop()
        return code

    def serialize(self, level):
        output = ""
        if self.expression:
            output += padding(level) + "UNTIL NOT:\n"
            output += padding(level + 1) + self.expression.serialize(0)
        else:
            output += "Until"
        if self.statement:
            output += padding(level) + "REPEAT:\n"
            output += self.statement.serialize(level + 1)
        return output


