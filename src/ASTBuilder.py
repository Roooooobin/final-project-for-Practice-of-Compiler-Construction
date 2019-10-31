"""
# -*- coding: utf-8 -*-
# @FileName: ASTBuilder.py
# @Author  : Robin
# @Time    : 2019/10/27 10:22
"""
from antlr4 import *

from src.AST.ExpressionType.ArithmeticExpression import ArithmeticExpression
from src.AST.ExpressionType.VariableCallExpression import VariableCallExpression
from src.AST.ExpressionType.VariableDefineExpression import VariableDefineExpression
from src.AST.Program import Program
from antlr4_tools.CXLexer import CXLexer
from antlr4_tools.CXParser import CXParser
from src.AST.Statement import Statement
from src.AST.StatementType.BreakStatement import BreakStatement
from src.AST.StatementType.ContinueStatement import ContinueStatement
from src.Types.BooleanType import BooleanType
from src.Types.IntegerType import IntegerType


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
            self.AST.add_statement(self.build_statement(tree.getChild(i)))

        return self.AST

    def build_statement(self, tree):
        if tree.getChildCount() == 0:
            raise RuntimeError("Invalid Statement: '{}'".format(tree.getText()))
        elif tree.getChildCount() == 1:
            # AST只有一个孩子，应该为分号，否则出错
            token = tree.getChild(0).getPayload()
            if isinstance(token, Token) and token.type == CXLexer.SEMICOLON:
                return Statement()
            else:
                raise RuntimeError("Invalid Statement: '{}'".format(tree.getText()))
        else:
            token = tree.getChild(0).getPayload()
            token2 = tree.getChild(1).getPayload()
            if isinstance(token, Token):
                # break或continue后一定要接分号，否则就是错误的语句
                if token.type == CXLexer.BREAK:
                    if isinstance(token2, Token) and token2.type == CXLexer.SEMICOLON:
                        return BreakStatement()
                    else:
                        RuntimeError("Wrong Break statement, error: '{}'".format(tree.getText()))
                elif token.type == CXLexer.CONTINUE:
                    if isinstance(token2, Token) and token2.type == CXLexer.SEMICOLON:
                        return ContinueStatement()
                    else:
                        RuntimeError("Wrong Continue statement, error: '{}'".format(tree.getText()))
                elif token.type == CXLexer.LBRACE:
                    # 遇见左括号，那么生成复合语句
                    return self.build_compound_statement(tree)
                elif token.type == CXLexer.WHILE:
                    return self.build_while_statement(tree)
                elif token.type == CXLexer.FOR:
                    return self.build_for_statement(tree)
                elif token.type == CXLexer.IF:
                    return self.build_if_statement(tree)
                else:
                    raise RuntimeError("Invalid Statement: '{}'".format(tree.getText()))
            else:
                if not isinstance(token2, Token):
                    raise RuntimeError("Invalid Statement: '{}'".format(tree.getText()))
                if token.type == CXLexer.SEMICOLON:
                    return self.build_expression(tree.getChild(0))
                else:
                    raise RuntimeError("Invalid Statement: '" + tree.getText() + "'")

    def build_expression(self, tree):
        if tree.getChildCount() == 1:
            """
            AST仅有一个孩子的时候：
            1. 标识符Identifier
            2. TRUE|FALSE|NUM
            """
            token = tree.getChild(0).getPayload()
            if not isinstance(token, Token):    # 如果是一个token，则是identifier
                return self.build_variable_expression(tree.getChild(0))
            else:   # 否则是常量
                return self.build_constant_expression(tree)
        elif tree.getChildCount() == 2:
            """
            AST仅有两个孩子：
            1. int identifier
            2. MINUS|NOT expression
            """
            token = tree.getChild(0).getPayload()

            if isinstance(token, Token):
                if token.type == CXLexer.MINUS:
                    return self.build_negative_expression(tree)
                elif token.type == CXLexer.NOT:
                    return self.build_not_expression(tree)
                else:
                    raise RuntimeError("Invalid Expression: '{}'".format(tree.getText()))
            else:
                id_ = tree.getChild(1).getPayload()
                if isinstance(id_, Token) and id_.type == CXLexer.IDENTIFIER:
                    return self.build_variable_expression(tree)
                else:
                    raise RuntimeError("Invalid Expression: '{}'".format(tree.getText()))
        elif tree.getChildCount() == 3:
            """
            孩子数为3时，正常的双目运算或是++/--
            """
            token0 = tree.getChild(0).getPayload()
            token1 = tree.getChild(1).getPayload()
            token2 = tree.getChild(2).getPayload()
            if isinstance(token1, Token) and isinstance(token2, Token) and token1.type == CXLexer.PLUS and token2.type == CXLexer.PLUS:
                # variable (PLUS PLUS)|(MINUS MINUS)
                return self.build_increment_expression(tree)
            elif isinstance(token1, Token) and isinstance(token2, Token) and token1.type == CXLexer.MINUS and token2.type == CXLexer.MINUS:
                # variable (PLUS PLUS)|(MINUS MINUS)
                return self.build_decrement_expression(tree)
            elif isinstance(token0, Token) and isinstance(token2, Token) and token0.type == CXLexer.LPAREN and token2.type == CXLexer.RPAREN:
                # ( expression )
                return self.build_expression(tree.getChild(1))
            elif isinstance(token1, Token):
                if token1.type == CXLexer.ASSIGN:
                    return self.build_assignment_expression(tree)
                elif token1.type == CXLexer.STAR:
                    return self.build_arithmetic_expression(tree)
                elif token1.type == CXLexer.PLUS:
                    return self.build_arithmetic_expression(tree)
                elif token1.type == CXLexer.MINUS:
                    return self.build_arithmetic_expression(tree)
                elif token1.type == CXLexer.SLASH:
                    return self.build_arithmetic_expression(tree)
                elif token1.type == CXLexer.EQUAL:
                    return self.build_comparison_expression(tree)
                elif token1.type == CXLexer.NOTEQUAL:
                    return self.build_comparison_expression(tree)
                elif token1.type == CXLexer.LESSTHANOREQUAL:
                    return self.build_comparison_expression(tree)
                elif token1.type == CXLexer.GREATERTHANOREQUAL:
                    return self.build_comparison_expression(tree)
                elif token1.type == CXLexer.LESSTHAN:
                    return self.build_comparison_expression(tree)
                elif token1.type == CXLexer.GREATERTHAN:
                    return self.build_comparison_expression(tree)
                elif token1.type == CXLexer.AND:
                    return self.build_logic_expression(tree)
                elif token1.type == CXLexer.OR:
                    return self.build_logic_expression(tree)
                else:
                    raise RuntimeError("Invalid Expression: '{}'".format(tree.getText()))
        else:
            raise RuntimeError("Invalid Expression: '{}'".format(tree.getText()))

    def build_variable_expression(self, tree):
        # 处理变量语句
        if tree.getChildCount() == 1:
            # 只有一个孩子，说明是直接调用的，去符号表中找
            identifier = tree.getChild(0).getText()
            symbol = self.symbol.getSymbol(identifier)
            return VariableCallExpression(symbol)
        elif tree.getChildCount() == 2:
            # 变量声明语句
            basetype = self.build_type(tree.getChild(0))
            identifier = tree.getChild(1).getText()
            # Register in Symbol Table
            symbol = self.symbol.registerSymbol(identifier, basetype)
            return VariableDefineExpression(symbol)
        else:
            raise RuntimeError("Invalid Variable Expression: '" + tree.getText() + "'")

    def build_constant_expression(self, tree):
        pass

    def build_negative_expression(self, tree):
        pass

    def build_not_expression(self, tree):
        pass

    def build_increment_expression(self, tree):
        pass

    def build_decrement_expression(self, tree):
        pass

    def build_assignment_expression(self, tree):
        pass

    def build_arithmetic_expression(self, tree):
        # expects 3 children
        if tree.getChildCount() != 3:
            raise RuntimeError("Invalid ArithmeticExpression: '{}'".format(tree.getText()))

        token = tree.getChild(1).getPayload()
        if not isinstance(token, Token):
            raise RuntimeError("Invalid ArithmeticExpression: '{}'".format(tree.getText()))

        # 双目运算，先递归得到左右两个expression
        left_expression = self.build_expression(tree.getChild(0))
        right_expression = self.build_expression(tree.getChild(2))

        if token.type == CXLexer.STAR:
            return ArithmeticExpression(left_expression, right_expression, "*")
        elif token.type == CXLexer.SLASH:
            return ArithmeticExpression(left_expression, right_expression, "/")
        elif token.type == CXLexer.PLUS:
            return ArithmeticExpression(left_expression, right_expression, "+")
        elif token.type == CXLexer.MINUS:
            return ArithmeticExpression(left_expression, right_expression, "-")
        else:
            raise RuntimeError("Invalid ArithmeticExpression: '" + tree.getText() + "'")

    def build_comparison_expression(self, tree):
        pass

    def build_logic_expression(self, tree):
        pass

    def build_compound_statement(self, tree):
        pass

    def build_while_statement(self, tree):
        pass

    def build_for_statement(self, tree):
        pass

    def build_if_statement(self, tree):
        pass

    def build_type(self, tree):
        token = None
        basetype = None

        if tree.getChildCount() == 1:
            token = tree.getChild(0).getPayload()

            if not isinstance(token, Token):
                raise RuntimeError("Invalid type identifier: '{}'".format(tree.getText()))

            # 仅支持bool和int
            if token.type == CXLexer.IDENTIFIER:
                if tree.getChild(0).getText() == "bool":
                    return BooleanType()
                elif tree.getChild(0).getText() == "int":
                    return IntegerType()
                else:
                    # Alias, check the symbol Table
                    return self.symbol.getAlias(tree.getChild(0).getText()).basetype
            else:
                raise RuntimeError("Invalid type identifier: '{}'".format(tree.getText()))
        else:
            raise RuntimeError("Invalid type identifier: '{}'".format(tree.getText()))