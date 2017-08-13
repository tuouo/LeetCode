#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 2017/8/13
import unittest


class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        # if m == 1 or n == 1:
        #     return 1
        from functools import reduce
        import operator
        if m < n:
            m, n = n, m
        return reduce(operator.mul, range(m, m + n - 1), 1) // reduce(operator.mul, range(1, n), 1)


class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_solution(self):
        self.assertEqual(Solution().uniquePaths(3, 7), 28)


if __name__ == '__main__':
    unittest.main()
