"""
# -*- coding: utf-8 -*-
# @FileName: main.py
# @Author  : Robin
# @Time    : 2019/10/27 13:32
"""
import os
import argparse
from src.ASTBuilder import ASTBuilder
from src.SymbolTable.SymbolTable import SymbolTable

basics = ["and_or", "arithmetic", "bool", "if", "read_write", "while"]
bonus = ["break", "continue", "dowhile", "for", "odd", "real", "repeatuntil", "xor"]
program = ["factorial", "LCM", "prime"]

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("type", type=str, help="type in the func kind you want to test")
    parser.add_argument("test", type=str, help="type in which func you want to test")
    args = parser.parse_args()
    test_path = r"C:\Users\robin\Desktop\CX_compiler\tests\tests_" + args.type + r"\test_" + args.test + ".txt"
    # test_bonus_path = r"C:\Users\robin\Desktop\CX_compiler\tests\tests_bonus\test_" + args.test + ".txt"
    # test_program_path = r"C:\Users\robin\Desktop\CX_compiler\tests\tests_program" + "\\" + args.test + ".txt"
    symbol_table = SymbolTable()
    ast = ASTBuilder(test_path, symbol_table)
    ast = ast.build()
    compiled_codes = ast.compile()
    output_path = r"C:\Users\robin\Desktop\CX_compiler\tests\out.p"
    output_file = open(output_path, "w")
    print(compiled_codes, file=output_file)
