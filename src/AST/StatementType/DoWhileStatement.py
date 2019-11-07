"""
# -*- coding: utf-8 -*-
# @FileName: DoWhileStatement.py
# @Author  : Robin
# @Time    : 2019/11/6 22:28
"""
from src.AST.Statement import Statement
from utils import padding


class DoWhileStatement(Statement):
    def __init__(self, expression, statement, symbol_table):
        Statement.__init__(self)
        self.expression = expression
        self.statement = statement
        self.symbol_table = symbol_table

    def __str__(self):
        output = "Do (" + str(self.statement) + "\n"
        output += "While(" + str(self.expression) + ")\n"
        return output

    def compile(self):
        self.symbol_table.open_loop()
        # 获取开始和结束的label
        begin_label = self.symbol_table.get_begin_loop()
        end_label = self.symbol_table.get_end_loop()
        # 先编译statement
        # do-while do会先做一次
        compiled_stmt = self.statement.compile()
        code = compiled_stmt
        code += str(begin_label) + ":\n"
        # 编译expression，如果条件不成立则直接跳到结束label
        code += self.expression.compile() + "fjp " + str(end_label) + "\n"
        # 循环中执行statement
        code += compiled_stmt
        # 一次循环结束，跳到循环开始label
        code += "ujp " + str(begin_label) + "\n"
        code += str(end_label) + ":\n"
        self.symbol_table.close_loop()
        return code

    def serialize(self, level):
        output = ""
        if self.expression:
            output += padding(level) + "DO WHILE:\n"
            output += padding(level + 1) + self.expression.serialize(0)
        else:
            output += "DO WHILE"
        if self.statement:
            output += padding(level) + "THEN:\n"
            output += self.statement.serialize(level + 1)
        return output
