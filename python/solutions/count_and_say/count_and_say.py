#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 2017/6/23
import unittest


class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        from itertools import groupby
        a = '1'
        for i in range(n-1):
            a = ''.join(str(len(list(v))) + k for k, v in groupby(a))
        return a

    def re_do(self, n):
        import re
        a, reg = "1", re.compile(r"((?P<w>\d)(?P=w)*)")
        for i in range(n - 1):
            a = "".join(list(map(lambda x: '{}{}'.format(len(x[0]), x[1]), reg.findall(a))))
        return a


class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_count(self):
        self.assertEqual(Solution().countAndSay(5), "111221")


if __name__ == '__main__':
    unittest.main()
