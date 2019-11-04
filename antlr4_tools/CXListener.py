# Generated from CX.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .CXParser import CXParser
else:
    from CXParser import CXParser

# This class defines a complete listener for a parse tree produced by CXParser.
class CXListener(ParseTreeListener):

    # Enter a parse tree produced by CXParser#program.
    def enterProgram(self, ctx:CXParser.ProgramContext):
        pass

    # Exit a parse tree produced by CXParser#program.
    def exitProgram(self, ctx:CXParser.ProgramContext):
        pass


    # Enter a parse tree produced by CXParser#statement.
    def enterStatement(self, ctx:CXParser.StatementContext):
        pass

    # Exit a parse tree produced by CXParser#statement.
    def exitStatement(self, ctx:CXParser.StatementContext):
        pass


    # Enter a parse tree produced by CXParser#compoundstatement.
    def enterCompoundstatement(self, ctx:CXParser.CompoundstatementContext):
        pass

    # Exit a parse tree produced by CXParser#compoundstatement.
    def exitCompoundstatement(self, ctx:CXParser.CompoundstatementContext):
        pass


    # Enter a parse tree produced by CXParser#expressionstatement.
    def enterExpressionstatement(self, ctx:CXParser.ExpressionstatementContext):
        pass

    # Exit a parse tree produced by CXParser#expressionstatement.
    def exitExpressionstatement(self, ctx:CXParser.ExpressionstatementContext):
        pass


    # Enter a parse tree produced by CXParser#selectionstatement.
    def enterSelectionstatement(self, ctx:CXParser.SelectionstatementContext):
        pass

    # Exit a parse tree produced by CXParser#selectionstatement.
    def exitSelectionstatement(self, ctx:CXParser.SelectionstatementContext):
        pass


    # Enter a parse tree produced by CXParser#iterationstatement.
    def enterIterationstatement(self, ctx:CXParser.IterationstatementContext):
        pass

    # Exit a parse tree produced by CXParser#iterationstatement.
    def exitIterationstatement(self, ctx:CXParser.IterationstatementContext):
        pass


    # Enter a parse tree produced by CXParser#expression.
    def enterExpression(self, ctx:CXParser.ExpressionContext):
        pass

    # Exit a parse tree produced by CXParser#expression.
    def exitExpression(self, ctx:CXParser.ExpressionContext):
        pass


    # Enter a parse tree produced by CXParser#assignmentexpression.
    def enterAssignmentexpression(self, ctx:CXParser.AssignmentexpressionContext):
        pass

    # Exit a parse tree produced by CXParser#assignmentexpression.
    def exitAssignmentexpression(self, ctx:CXParser.AssignmentexpressionContext):
        pass


    # Enter a parse tree produced by CXParser#conditionalexpression.
    def enterConditionalexpression(self, ctx:CXParser.ConditionalexpressionContext):
        pass

    # Exit a parse tree produced by CXParser#conditionalexpression.
    def exitConditionalexpression(self, ctx:CXParser.ConditionalexpressionContext):
        pass


    # Enter a parse tree produced by CXParser#logicorexpression.
    def enterLogicorexpression(self, ctx:CXParser.LogicorexpressionContext):
        pass

    # Exit a parse tree produced by CXParser#logicorexpression.
    def exitLogicorexpression(self, ctx:CXParser.LogicorexpressionContext):
        pass


    # Enter a parse tree produced by CXParser#logicandexpression.
    def enterLogicandexpression(self, ctx:CXParser.LogicandexpressionContext):
        pass

    # Exit a parse tree produced by CXParser#logicandexpression.
    def exitLogicandexpression(self, ctx:CXParser.LogicandexpressionContext):
        pass


    # Enter a parse tree produced by CXParser#logicxorexpression.
    def enterLogicxorexpression(self, ctx:CXParser.LogicxorexpressionContext):
        pass

    # Exit a parse tree produced by CXParser#logicxorexpression.
    def exitLogicxorexpression(self, ctx:CXParser.LogicxorexpressionContext):
        pass


    # Enter a parse tree produced by CXParser#equalityexpression.
    def enterEqualityexpression(self, ctx:CXParser.EqualityexpressionContext):
        pass

    # Exit a parse tree produced by CXParser#equalityexpression.
    def exitEqualityexpression(self, ctx:CXParser.EqualityexpressionContext):
        pass


    # Enter a parse tree produced by CXParser#comparisonexpression.
    def enterComparisonexpression(self, ctx:CXParser.ComparisonexpressionContext):
        pass

    # Exit a parse tree produced by CXParser#comparisonexpression.
    def exitComparisonexpression(self, ctx:CXParser.ComparisonexpressionContext):
        pass


    # Enter a parse tree produced by CXParser#additiveexpression.
    def enterAdditiveexpression(self, ctx:CXParser.AdditiveexpressionContext):
        pass

    # Exit a parse tree produced by CXParser#additiveexpression.
    def exitAdditiveexpression(self, ctx:CXParser.AdditiveexpressionContext):
        pass


    # Enter a parse tree produced by CXParser#multiplicativeexpression.
    def enterMultiplicativeexpression(self, ctx:CXParser.MultiplicativeexpressionContext):
        pass

    # Exit a parse tree produced by CXParser#multiplicativeexpression.
    def exitMultiplicativeexpression(self, ctx:CXParser.MultiplicativeexpressionContext):
        pass


    # Enter a parse tree produced by CXParser#incrementalexpression.
    def enterIncrementalexpression(self, ctx:CXParser.IncrementalexpressionContext):
        pass

    # Exit a parse tree produced by CXParser#incrementalexpression.
    def exitIncrementalexpression(self, ctx:CXParser.IncrementalexpressionContext):
        pass


    # Enter a parse tree produced by CXParser#primaryexpression.
    def enterPrimaryexpression(self, ctx:CXParser.PrimaryexpressionContext):
        pass

    # Exit a parse tree produced by CXParser#primaryexpression.
    def exitPrimaryexpression(self, ctx:CXParser.PrimaryexpressionContext):
        pass


    # Enter a parse tree produced by CXParser#constant.
    def enterConstant(self, ctx:CXParser.ConstantContext):
        pass

    # Exit a parse tree produced by CXParser#constant.
    def exitConstant(self, ctx:CXParser.ConstantContext):
        pass


    # Enter a parse tree produced by CXParser#basetype.
    def enterBasetype(self, ctx:CXParser.BasetypeContext):
        pass

    # Exit a parse tree produced by CXParser#basetype.
    def exitBasetype(self, ctx:CXParser.BasetypeContext):
        pass


