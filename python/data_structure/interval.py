#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 2017/7/26


class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    def __str__(self):
        return str([self.start, self.end])

    __repr__ = __str__

if __name__ == '__main__':
    i = Interval(3, 5)
    print(i)
