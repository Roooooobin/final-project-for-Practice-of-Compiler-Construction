"""
# -*- coding: utf-8 -*-
# @FileName: ASTBuilder.py
# @Author  : Robin
# @Time    : 2019/10/27 10:22
"""
from antlr4 import *

from antlr4_tools.CXLexer import CXLexer
from antlr4_tools.CXParser import CXParser
from src.AST.ExpressionType.ArithmeticExpression import ArithmeticExpression
from src.AST.ExpressionType.AssignExpression import AssignExpression
from src.AST.ExpressionType.ConstantExpression import ConstantExpression
from src.AST.ExpressionType.DecrementExpression import DecrementExpression
from src.AST.ExpressionType.IncrementExpression import IncrementExpression
from src.AST.ExpressionType.ComparisonExpression import ComparisonExpression
from src.AST.ExpressionType.LogicExpression import LogicExpression
from src.AST.ExpressionType.NegativeExpression import NegativeExpression
from src.AST.ExpressionType.NotExpression import NotExpression
from src.AST.ExpressionType.OddExpression import OddExpression
from src.AST.ExpressionType.VariableCallExpression import VariableCallExpression
from src.AST.ExpressionType.VariableDefineExpression import VariableDefineExpression
from src.AST.Program import Program
from src.AST.Statement import Statement
from src.AST.StatementType.BreakStatement import BreakStatement
from src.AST.StatementType.ContinueStatement import ContinueStatement
from src.AST.StatementType.WriteStatement import WriteStatement
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
            print(i)
            self.AST.add_statement(self.build_statement(tree.getChild(i)))

        return self.AST

    def build_statement(self, tree):
        if tree.getChildCount() == 0:
            raise RuntimeError("Invalid Statement: '{}'".format(tree.getText()))
        token = tree.getChild(0).getPayload()
        if isinstance(token, Token) and token == CXLexer.BREAK:
            token1 = tree.getChild(1).getPayload()
            if token == CXLexer.BREAK:
                if isinstance(token1, Token) and token1.type == CXLexer.SEMICOLON:
                    return BreakStatement()
                else:
                    RuntimeError("Wrong Break statement, error: '{}'".format(tree.getText()))
        if isinstance(token, Token) and token == CXLexer.CONTINUE:
            token1 = tree.getChild(1).getPayload()
            if isinstance(token1, Token) and token1.type == CXLexer.SEMICOLON:
                return ContinueStatement()
            else:
                RuntimeError("Wrong Continue statement, error: '{}'".format(tree.getText()))
        if isinstance(token, Token) and token.type == CXLexer.WRITE:
            token2 = tree.getChild(2).getPayload()
            if isinstance(token2, Token) and token2.type == CXLexer.SEMICOLON:
                return self.build_write_statement(tree)
            else:
                RuntimeError("Wrong Continue statement, error: '{}'".format(tree.getText()))
        if isinstance(token, Token) and token.type == CXLexer.WRITELN:
            token2 = tree.getChild(2).getPayload()
            if isinstance(token2, Token) and token2.type == CXLexer.SEMICOLON:
                return self.build_writeln_statement(tree)
            else:
                RuntimeError("Wrong Continue statement, error: '{}'".format(tree.getText()))
        if tree.getChildCount() >= 2:
            token1 = tree.getChild(1).getPayload()
            if isinstance(token1, Token) and token1.type == CXLexer.IDENTIFIER:
                return self.build_define_statement(tree)
        tree = tree.getChild(0)
        token = tree.getChild(0).getPayload()
        if token == CXLexer.LEFTBRACE:
            # 遇见左大括号，那么生成复合语句
            return self.build_compound_statement(tree)
        elif token == CXLexer.WHILE:
            return self.build_while_statement(tree)
        elif token == CXLexer.FOR:
            return self.build_for_statement(tree)
        elif token == CXLexer.IF:
            return self.build_if_statement(tree)
        elif token == CXLexer.DO:
            pass
            # return self.build_dowhile_statement(tree)
        else:
            return self.build_expression_statement(tree)

    def build_expression_statement(self, tree):
        if tree.getChildCount() == 2:
            return self.build_expression(tree.getChild(0))

    # TODO: odd grammar definition, not, -
    def build_expression(self, tree):
        return self.build_assignment_expression(tree.getChild(0))

    def build_variable_expression(self, tree):
        # 处理变量语句
        if tree.getChildCount() == 1:
            # 只有一个孩子，说明是直接调用的，去符号表中找
            identifier = tree.getChild(0).getText()
            symbol = self.symbol.get_symbol(identifier)
            return VariableCallExpression(symbol)
        elif tree.getChildCount() == 2:
            # 变量声明语句
            basetype = self.build_type(tree.getChild(0))
            identifier = tree.getChild(1).getText()
            # Register in Symbol Table
            symbol = self.symbol.register_symbol(identifier, basetype)
            return VariableDefineExpression(symbol)
        else:
            raise RuntimeError("Invalid Variable Expression: '" + tree.getText() + "'")

    def build_assignment_expression(self, tree):
        if tree.getChildCount() == 1:
            return self.build_condition_expression(tree.getChild(0))
        if tree.getChildCount() != 3:
            raise RuntimeError("Invalid Assignment Expression: '{}'".format(tree.getText()))
        # 孩子必须为3，中间的符号必须为等号（即赋值符号）
        token = tree.getChild(1).getPayload()
        if not isinstance(token, Token) or token.type != CXLexer.ASSIGN:
            raise RuntimeError("Invalid Assignment Expression: '{}'".format(tree.getText()))
        # 将identifier和"值"传入AssignmentExpression
        identifier = tree.getChild(0).getText()
        symbol = self.symbol.get_symbol(identifier)
        call_var = VariableCallExpression(symbol)
        # AssignExpression(define, self.build_expression(tree.getChild(3)))
        return AssignExpression(call_var, self.build_expression(tree.getChild(2)))

    def build_condition_expression(self, tree):
        if tree.getChildCount() == 1:
            return self.build_logic_or_expression(tree.getChild(0))

    def build_define_statement(self, tree):
        basetype = tree.getChild(0).getText()
        if basetype == "bool":
            basetype = BooleanType()
        elif basetype == "int":
            basetype = IntegerType()
        identifier = tree.getChild(1).getText()
        # Register in Symbol Table
        symbol = self.symbol.register_symbol(identifier, basetype)
        define_var = VariableDefineExpression(symbol)
        if tree.getChildCount() == 3:
            return AssignExpression(define_var, ConstantExpression(0, "int"))
        else:
            return AssignExpression(define_var, self.build_expression(tree.getChild(3)))

    def build_negative_expression(self, tree):
        if tree.getChildCount() != 2:
            raise RuntimeError("Invalid NegativeExpression: '" + tree.getText() + "'")

        token = tree.getChild(0).getPayload()
        if not isinstance(token, Token) or token.type != CXLexer.MINUS:
            raise RuntimeError("Invalid NegativeExpression: '" + tree.getText() + "'")

        return NegativeExpression(self.build_expression(tree.getChild(1)))

    def build_not_expression(self, tree):
        if tree.getChildCount() != 2:
            raise RuntimeError("Invalid NotExpression: '" + tree.getText() + "'")

        token = tree.getChild(0).getPayload()
        if not isinstance(token, Token) or token.type != CXLexer.NOT:
            raise RuntimeError("Invalid NotExpression: '" + tree.getText() + "'")

        return NotExpression(self.build_expression(tree.getChild(1)))

    def build_odd_expression(self, tree):
        if tree.getChildCount() != 2:
            raise RuntimeError("Invalid OddExpression: '" + tree.getText() + "'")

        token = tree.getChild(0).getPayload()
        if not isinstance(token, Token) or token.type != CXLexer.ODD:
            raise RuntimeError("Invalid OddExpression: '" + tree.getText() + "'")

        return OddExpression(self.build_expression(tree.getChild(1)))

    def build_logic_or_expression(self, tree):
        if tree.getChildCount() == 1:
            return self.build_logic_and_expression(tree.getChild(0))
        if tree.getChildCount() != 3:
            raise RuntimeError("Invalid LogicExpression: '" + tree.getText() + "'")
        token = tree.getChild(1).getPayload()
        if not isinstance(token, Token):
            raise RuntimeError("Invalid LogicExpression: '" + tree.getText() + "'")

        left_expression = self.build_logic_or_expression(tree.getChild(0))
        right_expression = self.build_logic_and_expression(tree.getChild(2))

        if token.type == CXLexer.OR:
            return LogicExpression(left_expression, right_expression, "||")
        else:
            raise RuntimeError("Invalid LogicExpression: '" + tree.getText() + "'")

    def build_logic_and_expression(self, tree):
        if tree.getChildCount() == 1:
            return self.build_logic_xor_expression(tree.getChild(0))
        if tree.getChildCount() != 3:
            raise RuntimeError("Invalid LogicExpression: '" + tree.getText() + "'")
        token = tree.getChild(1).getPayload()
        if not isinstance(token, Token):
            raise RuntimeError("Invalid LogicExpression: '" + tree.getText() + "'")

        left_expression = self.build_logic_and_expression(tree.getChild(0))
        right_expression = self.build_logic_xor_expression(tree.getChild(2))

        if token.type == CXLexer.AND:
            return LogicExpression(left_expression, right_expression, "&&")
        elif token.type == CXLexer.OR:
            return LogicExpression(left_expression, right_expression, "||")
        elif token.type == CXLexer.XOR:
            return LogicExpression(left_expression, right_expression, "^")
        else:
            raise RuntimeError("Invalid LogicExpression: '" + tree.getText() + "'")

    def build_logic_xor_expression(self, tree):
        if tree.getChildCount() == 1:
            return self.build_equal_expression(tree.getChild(0))
        if tree.getChildCount() != 3:
            raise RuntimeError("Invalid LogicExpression: '" + tree.getText() + "'")
        token = tree.getChild(1).getPayload()
        if not isinstance(token, Token):
            raise RuntimeError("Invalid LogicExpression: '" + tree.getText() + "'")

        left_expression = self.build_logic_xor_expression(tree.getChild(0))
        right_expression = self.build_equal_expression(tree.getChild(2))

        if token.type == CXLexer.XOR:
            return LogicExpression(left_expression, right_expression, "^")
        else:
            raise RuntimeError("Invalid LogicExpression: '" + tree.getText() + "'")

    def build_equal_expression(self, tree):
        if tree.getChildCount() == 1:
            return self.build_comparison_expression(tree.getChild(0))
        if tree.getChildCount() != 3:
            raise RuntimeError("Invalid ComparisonExpression: '" + tree.getText() + "'")

        token = tree.getChild(1).getPayload()
        if not isinstance(token, Token):
            raise RuntimeError("Invalid ComparisonExpression: '" + tree.getText() + "'")

        left_expression = self.build_equal_expression(tree.getChild(0))
        right_expression = self.build_comparison_expression(tree.getChild(2))

        if token.type == CXLexer.EQUAL:
            return ComparisonExpression(left_expression, right_expression, "==")
        elif token.type == CXLexer.NOTEQUAL:
            return ComparisonExpression(left_expression, right_expression, "!=")
        else:
            raise RuntimeError("Invalid ComparisonExpression: '" + tree.getText() + "'")

    def build_comparison_expression(self, tree):
        if tree.getChildCount() == 1:
            return self.build_additive_expression(tree.getChild(0))
        if tree.getChildCount() != 3:
            raise RuntimeError("Invalid ComparisonExpression: '" + tree.getText() + "'")

        token = tree.getChild(1).getPayload()
        if not isinstance(token, Token):
            raise RuntimeError("Invalid ComparisonExpression: '" + tree.getText() + "'")

        left_expression = self.build_comparison_expression(tree.getChild(0))
        right_expression = self.build_additive_expression(tree.getChild(2))

        if token.type == CXLexer.LESSTHAN:
            return ComparisonExpression(left_expression, right_expression, "<")
        elif token.type == CXLexer.GREATERTHAN:
            return ComparisonExpression(left_expression, right_expression, ">")
        elif token.type == CXLexer.LESSTHANOREQUAL:
            return ComparisonExpression(left_expression, right_expression, "<=")
        elif token.type == CXLexer.GREATERTHANOREQUAL:
            return ComparisonExpression(left_expression, right_expression, ">=")
        else:
            raise RuntimeError("Invalid ComparisonExpression: '" + tree.getText() + "'")

    def build_additive_expression(self, tree):
        if tree.getChildCount() == 1:
            return self.build_multiplicative_expression(tree.getChild(0))
        if tree.getChildCount() != 3:
            raise RuntimeError("Invalid ArithmeticExpression: '{}'".format(tree.getText()))

        token = tree.getChild(1).getPayload()
        if not isinstance(token, Token):
            raise RuntimeError("Invalid ArithmeticExpression: '{}'".format(tree.getText()))

        # 双目运算，先递归得到左右两个expression
        left_expression = self.build_additive_expression(tree.getChild(0))
        right_expression = self.build_multiplicative_expression(tree.getChild(2))

        if token.type == CXLexer.PLUS:
            return ArithmeticExpression(left_expression, right_expression, "+")
        elif token.type == CXLexer.MINUS:
            return ArithmeticExpression(left_expression, right_expression, "-")
        else:
            raise RuntimeError("Invalid ArithmeticExpression: '" + tree.getText() + "'")

    def build_multiplicative_expression(self, tree):
        if tree.getChildCount() == 1:
            return self.build_incremental_expression(tree.getChild(0))
        if tree.getChildCount() != 3:
            raise RuntimeError("Invalid ArithmeticExpression: '{}'".format(tree.getText()))

        token = tree.getChild(1).getPayload()
        if not isinstance(token, Token):
            raise RuntimeError("Invalid ArithmeticExpression: '{}'".format(tree.getText()))

        # 双目运算，先递归得到左右两个expression
        left_expression = self.build_multiplicative_expression(tree.getChild(0))
        right_expression = self.build_incremental_expression(tree.getChild(2))

        if token.type == CXLexer.STAR:
            return ArithmeticExpression(left_expression, right_expression, "*")
        elif token.type == CXLexer.SLASH:
            return ArithmeticExpression(left_expression, right_expression, "/")
        elif token.type == CXLexer.PLUS:
            return ArithmeticExpression(left_expression, right_expression, "+")
        elif token.type == CXLexer.MINUS:
            return ArithmeticExpression(left_expression, right_expression, "-")
        elif token.type == CXLexer.MOD:
            return ArithmeticExpression(left_expression, right_expression, "%")
        else:
            raise RuntimeError("Invalid ArithmeticExpression: '" + tree.getText() + "'")

    def build_incremental_expression(self, tree):
        if tree.getChildCount() == 1:
            return self.build_base_expression(tree.getChild(0))
        else:
            token1 = tree.getChild(1).getPayload()
            if token1.type == CXLexer.PLUSPLUS:
                return IncrementExpression(self.build_variable_expression(tree.getChild(0)))
            elif token1.type == CXLexer.MINUSMINUS:
                return DecrementExpression(self.build_variable_expression(tree.getChild(0)))
            else:
                raise RuntimeError("No such: {} incremental operation".format(tree.getText()))

    def build_base_expression(self, tree):
        if tree.getChildCount() == 1:
            token = tree.getChild(0).getPayload()
            if isinstance(token, Token) and token.type == CXLexer.IDENTIFIER:
                identifier = tree.getChild(0).getText()
                symbol = self.symbol.get_symbol(identifier)
                return VariableCallExpression(symbol)
            else:
                return self.build_constant_expression(tree.getChild(0))
        elif tree.getChildCount() == 3:
            token = tree.getChild(0).getPayload()
            if isinstance(token, Token) and token.type == CXLexer.LEFTPARENTHESIS:
                # print(tree.getChild(1).getText())
                return self.build_expression(tree.getChild(1))

    def build_constant_expression(self, tree):
        if tree.getChildCount() != 1:
            raise RuntimeError("Invalid ConstantExpression: '{}'".format(tree.getText()))
        token = tree.getChild(0).getPayload()
        if not isinstance(token, Token):
            raise RuntimeError("Invalid ConstantExpression: '" + tree.getText() + "'")
        # 根据常量类型做相应操作
        if token.type == CXLexer.TRUE:
            return ConstantExpression(True, "bool")
        elif token.type == CXLexer.FALSE:
            return ConstantExpression(False, "bool")
        elif token.type == CXLexer.NUMBER:
            return ConstantExpression(int(tree.getChild(0).getText()), "int")
        else:
            raise RuntimeError("Invalid ConstantExpression: '" + tree.getText() + "'")

    def build_compound_statement(self, tree):
        pass

    def build_while_statement(self, tree):
        pass

    def build_for_statement(self, tree):
        pass

    def build_if_statement(self, tree):
        pass

    def build_write_statement(self, tree):
        write_expr = self.build_expression(tree.getChild(1))
        return WriteStatement(write_expr, "write")

    def build_writeln_statement(self, tree):
        write_expr = self.build_expression(tree.getChild(1))
        return WriteStatement(write_expr, "writeln")

    def build_type(self, tree):
        token = None
        basetype = None

        if tree.getChildCount() == 1:
            token = tree.getChild(0).getPayload()

            if not isinstance(token, Token):
                raise RuntimeError("Invalid type identifier: '{}'".format(tree.getChild(0).getText()))

            # 仅支持bool和int
            if token.type == CXLexer.IDENTIFIER:
                if tree.getChild(0).getText() == "bool":
                    return BooleanType()
                elif tree.getChild(0).getText() == "int":
                    return IntegerType()
                else:
                    pass
            else:
                raise RuntimeError("Invalid type identifier: '{}'".format(tree.getText()))
        else:
            raise RuntimeError("Invalid type identifier: '{}'".format(tree.getText()))
