"""
# -*- coding: utf-8 -*-
# @FileName: main.py
# @Author  : Robin
# @Time    : 2019/10/27 13:32
"""
import os
from src.ASTBuilder import ASTBuilder
from src.SymbolTable.SymbolTable import SymbolTable

basics = ["and_or", "arithmetic", "bool", "if", "read_write", "while"]
bonus = ["break", "continue", "dowhile", "for", "odd", "real", "repeatuntil", "xor"]
required = ["factorial", "LCM", "prime numbers"]

if __name__ == "__main__":
    test_basic_path = os.getcwd() + r"\tests\tests_basic\test_" + basics[0] + ".txt"
    test_bonus_path = os.getcwd() + r"\tests\tests_bonus\test_" + bonus[0] + ".txt"
    test_required_path = os.getcwd() + r"\tests\tests_required" + "\\" + required[0] + ".txt"
    test_path = os.getcwd() + r"\test.txt"
    symbol_table = SymbolTable()
    ast = ASTBuilder(test_basic_path, symbol_table)
    ast = ast.build()
    compiled_codes = ast.compile()
    output_path = r"C:\Users\robin\Desktop\CX_compiler\tests\out.p"
    output_file = open(output_path, "w")
    print(compiled_codes, file=output_file)
