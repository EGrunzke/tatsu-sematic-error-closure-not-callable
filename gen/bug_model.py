#!/usr/bin/env python
# -*- coding: utf-8 -*-

# CAVEAT UTILITOR
#
# This file was automatically generated by TatSu.
#
#    https://pypi.python.org/pypi/tatsu/
#
# Any changes you make to it will be overwritten the next time
# the file is generated.

from __future__ import print_function, division, absolute_import, unicode_literals

from tatsu.objectmodel import Node
from tatsu.semantics import ModelBuilderSemantics


class ModelBase(Node):
    pass


class BugModelBuilderSemantics(ModelBuilderSemantics):
    def __init__(self, context=None, types=None):
        types = [
            t for t in globals().values()
            if type(t) is type and issubclass(t, ModelBase)
        ] + (types or [])
        super(BugModelBuilderSemantics, self).__init__(context=context, types=types)


class Sequence(ModelBase):
    children = None


class Word(ModelBase):
    val = None
