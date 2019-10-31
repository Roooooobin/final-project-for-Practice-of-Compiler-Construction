"""
# -*- coding: utf-8 -*-
# @FileName: WhileStatement.py
# @Author  : Robin
# @Time    : 2019/11/2 8:58
"""
from src.AST.Statement import Statement


class WhileStatement(Statement):
    def __init__(self):
        Statement.__init__(self)

    def __str__(self):
        return "While"

    def compile(self):
        pass

    def serialize(self, level):
        return ""
