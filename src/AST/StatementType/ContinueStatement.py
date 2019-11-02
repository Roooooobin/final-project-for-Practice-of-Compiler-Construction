"""
# -*- coding: utf-8 -*-
# @FileName: ContinueStatement.py
# @Author  : Robin
# @Time    : 2019/11/2 8:58
"""
from src.AST.Statement import Statement


class ContinueStatement(Statement):
    def __init__(self):
        Statement.__init__(self)

    def __str__(self):
        return "Continue\n"

    def compile(self):
        return "ujp " + self.symbol.get_begin_loop() + "\n"

    def serialize(self, level):
        output = padding(level) + "ContinueStatement\n"

        return output
