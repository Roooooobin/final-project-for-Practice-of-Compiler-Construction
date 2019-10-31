"""
# -*- coding: utf-8 -*-
# @FileName: Expression.py
# @Author  : Robin
# @Time    : 2019/10/31 15:24
"""
from src.AST.Statement import Statement


class Expression(Statement):
    """Node For Expression in AST"""

    def __init__(self, basetype):
        Statement.__init__(self)
        self.basetype = basetype

    def __str__(self):
        return "expression"

    def compile(self):
        return ""

    def serialize(self, level):
        return "expression"
