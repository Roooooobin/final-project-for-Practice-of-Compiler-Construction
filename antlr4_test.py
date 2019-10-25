from antlr4_tools.CXLexer import CXLexer
from antlr4_tools.CXParser import CXParser
from antlr4_tools.CXListener import CXListener


class CXPrintListener(CXListener):
    def enterR(self, ctx):
        # 函数名enterR的R指的是非终结符r
        print("CX: {}" % ctx.INT())


def main():
    lexer = CXLexer(StdinStream())
    stream = CommonTokenStream(lexer)
    parser = CXParser(stream)
    tree = parser.program()
    child_cnt = tree.getChildCount()
    print(child_cnt)
    for i in range(child_cnt):
        new_tree = tree.getChild(i)
        for j in range(new_tree.getChildCount()):
            print(new_tree.getChild(j))
    # printer = CXPrintListener()
    # walker = ParseTreeWalker()
    # walker.walk(printer, tree)


if __name__ == '__main__':
    main()
