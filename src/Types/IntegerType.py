"""
# -*- coding: utf-8 -*-
# @FileName: IntegerType.py
# @Author  : Robin
# @Time    : 2019/10/31 17:54
"""
from src.Types.BaseType import BaseType


class IntegerType(BaseType):
    """Integer Type"""
    def __init__(self):
        BaseType.__init__(self, 'i')    # int的p-code是'i'

    def __str__(self):
        output = ""
        if self.is_const():
            output += "const "
        output += "int"
        return output

    def get_pcode(self):
        return "i"

    def serialize(self, level):
        return "IntegerType"

    def get_size(self):
        return 4
