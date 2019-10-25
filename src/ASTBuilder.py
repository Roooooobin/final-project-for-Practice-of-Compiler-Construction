"""
# -*- coding: utf-8 -*-
# @FileName: ASTBuilder.py
# @Author  : Robin
# @Time    : 2019/10/27 10:22
"""
from antlr4 import *

from src.AST.Program import Program
from antlr4_tools.CXLexer import CXLexer
from antlr4_tools.CXParser import CXParser
from src.AST.Statement import Statement


class ASTBuilder:
    def __init__(self, file_path, symbol_table):
        self.AST = None
        self.file_path = file_path
        self.symbol = symbol_table

    def build(self):
        # 输入测试文件路径
        input_file = FileStream(self.file_path)
        lexer = CXLexer(input_file)
        stream = CommonTokenStream(lexer)
        parser = CXParser(stream)
        # 经过antlr4词法语法分析之后得到抽象语法树
        tree = parser.program()
        # child_cnt = tree.getChildCount()
        # print(child_cnt)
        # for i in range(child_cnt):
        #     new_tree = tree.getChild(i)
        #     for j in range(new_tree.getChildCount()):
        #         print(new_tree.getChild(j))
        self.AST = Program(self.symbol)

        child_count = tree.getChildCount()
        for i in range(child_count):
            self.AST.add_statement(self.create_statement(tree.getChild(i)))

        return self.AST

    def create_statement(self, tree):
        pass


