"""
# -*- coding: utf-8 -*-
# @FileName: Symbol.py
# @Author  : Robin
# @Time    : 2019/11/2 14:38
"""


class Symbol:
    """Representation of a Symbol"""
    def __init__(self, identifier, basetype, address):
        self.identifier = identifier
        self.basetype = basetype
        self.address = address
