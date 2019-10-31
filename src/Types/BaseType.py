"""
# -*- coding: utf-8 -*-
# @FileName: BaseType.py
# @Author  : Robin
# @Time    : 2019/10/31 17:55
"""


class BaseType:
    """Representation of Type Node in AST"""
    def __init__(self, code):
        """Initialize, size = 1"""
        self.const = False
        self.size = 1
        self.code = code

    def __eq__(self, other):
        """Check if 2 types are the same"""
        if not isinstance(other, BaseType):
            return False
        else:
            return self.code == other.code

    def get_size(self):
        """Returns the size of the type"""
        return self.size

    def is_const(self):
        """Check if type is constant"""
        return self.const

    def set_const(self, const):
        """set type const"""
        self.const = const
        return self

    def serialize(self, level):
        """serialize Type"""
        return "BaseType"

    def __str__(self):
        """String representation"""
        return "BaseType"
