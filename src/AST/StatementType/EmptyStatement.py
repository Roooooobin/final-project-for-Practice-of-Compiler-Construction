"""
# -*- coding: utf-8 -*-
# @FileName: EmptyStatement.py
# @Author  : Robin
# @Time    : 2019/11/7 15:20
"""
from src.AST.Statement import Statement
from utils import padding


class EmptyStatement(Statement):
    def __init__(self):
        Statement.__init__(self)

    def __str__(self):
        return "Empty\n"

    def compile(self):
        return ""

    def serialize(self, level):
        output = padding(level) + "EmptyStatement\n"
        return output
