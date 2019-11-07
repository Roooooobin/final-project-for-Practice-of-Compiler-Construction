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
        out = "While(" + str(self.expression) + ")\n"
        out += "    " + str(self.statement) + "\n"

        return out

    def compile(self):
        # Check if expression is an boolean type
        self.symbol_table.open_loop()
        begin_label = self.symbol_table.get_begin_loop()
        end_label = self.symbol_table.get_end_loop()
        # mark the begin of the WHILE statement
        code = self.statement.compile()
        code += str(begin_label) + ":\n"
        # compile the expression to evaluate
        code += self.expression.compile() + "not\nfjp " + str(end_label) + "\n"
        # compile the statement to execute
        code += self.statement.compile()
        # end with an unconditional jump to the begin
        code += "ujp " + str(begin_label) + "\n"
        # mark the end of the WHILE statement
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

