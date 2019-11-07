"""
# -*- coding: utf-8 -*-
# @FileName: unittests.py
# @Author  : Robin
# @Time    : 2019/11/6 13:05
"""
import os
import unittest

from src.ASTBuilder import ASTBuilder
from src.SymbolTable.SymbolTable import SymbolTable


class TestCx(unittest.TestCase):
    def setUp(self):
        self.path = r"C:\Users\robin\Desktop\CX_compiler\tests\test_if_simple.txt"
        self.out_path = r"C:\Users\robin\Desktop\CX_compiler\tests\out.p"
        self.symbol_table = SymbolTable()
        self.file_path_output = r"C:\Users\robin\Desktop\CX_compiler\tests\out.p"

    def test_if_else_simple(self):
        ast = ASTBuilder(self.path, self.symbol_table)
        ast = ast.build()
        compiled_codes = ast.compile()
        file_output = open(self.file_path_output, "w")
        print(compiled_codes, file=file_output)
        f = os.popen(r"Pmachine C:\Users\robin\Desktop\CX_compiler\tests\out.p", "r")
        out = f.read()
        print(out)
        # self.assertEqual(out, "0")
