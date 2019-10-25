# Generated from CX.g4 by ANTLR 4.7.2
if __name__ is not None and "." in __name__:
    from .CXParser import CXParser
else:
    from antlr4_tools.CXParser import CXParser

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


    # Enter a parse tree produced by CXParser#expression.
    def enterExpression(self, ctx:CXParser.ExpressionContext):
        pass

    # Exit a parse tree produced by CXParser#expression.
    def exitExpression(self, ctx:CXParser.ExpressionContext):
        pass


    # Enter a parse tree produced by CXParser#variable.
    def enterVariable(self, ctx:CXParser.VariableContext):
        pass

    # Exit a parse tree produced by CXParser#variable.
    def exitVariable(self, ctx:CXParser.VariableContext):
        pass


    # Enter a parse tree produced by CXParser#basetype.
    def enterBasetype(self, ctx:CXParser.BasetypeContext):
        pass

    # Exit a parse tree produced by CXParser#basetype.
    def exitBasetype(self, ctx:CXParser.BasetypeContext):
        pass


