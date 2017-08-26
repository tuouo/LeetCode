#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 2017/8/26
import unittest


class Solution(object):
    def climbStairs(self, n):  # 25.10(39ms)
        """
        :type n: int
        :rtype: int
        """
        return int((((1 + 5 ** 0.5) / 2) ** (n + 1) - ((1 - 5 ** 0.5) / 2) ** (n + 1)) / 5 ** 0.5)

    def add_step(self, n):  # 0.97（68ms)
        a, b = 1, 1
        for _ in range(n):
            a, b = b, a + b
        return a

    def add_step2(self, n):  # 38.2（36ms)
        if n <= 2:
            return n
        a, b = 2, 3
        for _ in range(2, n):
            a, b = b, a + b
        return a


class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_solution(self):
        self.assertEqual(Solution().climbStairs(2), 2)


if __name__ == '__main__':
    unittest.main()
