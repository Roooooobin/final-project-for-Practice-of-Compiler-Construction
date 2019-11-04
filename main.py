"""
# -*- coding: utf-8 -*-
# @FileName: main.py
# @Author  : Robin
# @Time    : 2019/10/27 13:32
"""


from src.ASTBuilder import ASTBuilder
from src.SymbolTable.SymbolTable import SymbolTable

if __name__ == "__main__":
    file = r"C:\Users\robin\Desktop\CX_compiler\tests\test1.txt"
    symbol_table = SymbolTable()
    ast = ASTBuilder(file, symbol_table)
    ast = ast.build()
    # print(ast.statements[0].variable)
    compiled_codes = ast.compile()
    file_path_output = r"C:\Users\robin\Desktop\CX_compiler\tests\1.p"
    file_output = open(file_path_output, "w")
    print(compiled_codes, file=file_output)
