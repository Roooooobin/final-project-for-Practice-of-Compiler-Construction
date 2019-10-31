"""
# -*- coding: utf-8 -*-
# @FileName: Node.py
# @Author  : Robin
# @Time    : 2019/10/30 18:15
"""


class Node:
    """Node in AST 作为一个基类"""
    def __init__(self):
        """Constructor for AST Node """

    def __str__(self):
        """String representation of AST Node"""
        return "Node"

    def compile(self):
        """Compile node to p-code"""
        return ""

    def serialize(self, level):
        """Serialize this node, the level attribute specifies how much indentation is needed"""
        return "Node"
