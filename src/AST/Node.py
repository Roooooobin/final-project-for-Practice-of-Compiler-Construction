"""
# -*- coding: utf-8 -*-
# @FileName: Node.py
# @Author  : Robin
# @Time    : 2019/10/30 18:15
"""


class Node:
    """Node in AST 作为一个基类"""
    def __init__(self):
        """基类无初始"""

    def __str__(self):
        return "Node"

    # 编译
    def compile(self):
        return ""

    def serialize(self, level):
        return "Node"
