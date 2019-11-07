"""
# -*- coding: utf-8 -*-
# @FileName: Program.py
# @Author  : Robin
# @Time    : 2019/10/30 18:14
"""
from src.AST.Node import Node
from utils import padding


class Program(Node):
    def __init__(self, symbol):
        Node.__init__(self)
        self.statements = []    # 一个程序由若干语句组成
        self.symbol = symbol

    def __str__(self):
        output = "\n".join([str(stmt) for stmt in self.statements])
        output += "\n"  # 结尾还需要加一个换行
        return output

    # statements
    def add_statement(self, stmt):
        self.statements.append(stmt)

    def compile(self):
        # 翻译为p-code
        if not self.statements:
            return "hlt\n"
        # 初始设定数据区大小(static part)
        codes = "ssp 15\n"
        for stmt in self.statements:
            codes += stmt.compile()
        # 程序最后，终止
        codes += "hlt"
        return codes

    def serialize(self, level):
        output = "Program\n:"
        for statement in self.statements:
            output += padding(level + 1) + statement.serialize(1)
        return output
