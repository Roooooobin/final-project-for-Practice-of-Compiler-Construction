"""
# -*- coding: utf-8 -*-
# @FileName: ContinueStatement.py
# @Author  : Robin
# @Time    : 2019/11/2 8:58
"""
from src.AST.Statement import Statement
from src.utils import padding


class ContinueStatement(Statement):
    def __init__(self, symbol_table):
        Statement.__init__(self)
        self.symbol_table = symbol_table

    def __str__(self):
        return "Continue\n"

    # continue跳到循环最前面
    def compile(self):
        return "ujp " + self.symbol_table.get_begin_loop() + "\n"

    def serialize(self, level):
        output = padding(level) + "ContinueStatement\n"

        return output
