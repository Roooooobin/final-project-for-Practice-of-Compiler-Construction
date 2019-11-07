"""
# -*- coding: utf-8 -*-
# @FileName: Statement.py
# @Author  : Robin
# @Time    : 2019/10/30 19:15
"""
from src.AST.Node import Node


# 语句
class Statement(Node):
    def __init__(self):
        Node.__init__(self)

    def __str__(self):
        return "statement"

    def compile(self):
        return ""

    def serialize(self, level):
        return "statement"
