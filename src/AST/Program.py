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

    def compile(self):
        # 翻译为p-code
        if not self.statements:
            return "hlt\n"

        # 类似于c语言的初始代码
        # init_codes = ["mst 0", "cup 0 init", "init:", "ssp 5", "mst 0", "cup 0 main0", "hlt\n", "main0:", "ssp 15"]
        # codes = "\n".join(init_codes)
        codes = "ssp 15\n"
        # print(self.statements)
        for stmt in self.statements:
            codes += stmt.compile()
        # 程序最后，终止
        codes += "hlt"
        return codes

    def add_statement(self, stmt):
        self.statements.append(stmt)

    def serialize(self, level):
        output = "Program\n:"
        for statement in self.statements:
            output += padding(level + 1) + statement.serialize(1)
        return output
