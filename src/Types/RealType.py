"""
# -*- coding: utf-8 -*-
# @FileName: RealType.py
# @Author  : Robin
# @Time    : 2019/11/6 12:16
"""
from src.Types.BaseType import BaseType


class RealType(BaseType):
    def __init__(self):
        BaseType.__init__(self, 'r')

    def __str__(self):
        output = ""
        if self.is_const():
            output += "const "
        output += "real"
        return output

    def get_pcode(self):
        return "r"

    def serialize(self, level):
        return "RealType"

    def get_size(self):
        return 4
