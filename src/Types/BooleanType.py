"""
# -*- coding: utf-8 -*-
# @FileName: BooleanType.py
# @Author  : Robin
# @Time    : 2019/10/31 17:54
"""
from src.Types.BaseType import BaseType


class BooleanType(BaseType):
    def __init__(self):
        BaseType.__init__(self, 'b')    # bool的p-code为'b'

    def __str__(self):
        output = ""
        if self.is_const():
            output += "const "
        output += "bool"
        return output

    def get_pcode(self):
        return "b"

    def serialize(self, level):
        return "BooleanType"

    def get_size(self):
        return 1
