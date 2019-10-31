"""
# -*- coding: utf-8 -*-
# @FileName: CompoundStatement.py
# @Author  : Robin
# @Time    : 2019/11/2 8:58
"""
from src.AST.Statement import Statement
from utils import padding


class CompoundStatement(Statement):
    def __init__(self):
        Statement.__init__(self)

    def __str__(self):
        return "Compound\n"

    def compile(self):
        pass

    def serialize(self, level):
        output = padding(level) + "CompoundStatement\n"

        return output
