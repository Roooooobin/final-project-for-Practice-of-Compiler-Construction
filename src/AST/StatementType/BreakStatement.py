"""
# -*- coding: utf-8 -*-
# @FileName: BreakStatement.py
# @Author  : Robin
# @Time    : 2019/11/2 8:57
"""
from src.AST.Statement import Statement
from src.utils import padding


class BreakStatement(Statement):
    def __init__(self, symbol_table):
        Statement.__init__(self)
        self.symbol_table = symbol_table

    def __str__(self):
        return "Break\n"

    # break直接跳出循环
    def compile(self):
        return "ujp " + self.symbol_table.get_end_loop() + "\n"

    def serialize(self, level):
        output = padding(level) + "BreakStatement\n"
        return output
