#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 2017/8/24
import unittest


class Solution(object):
    def mySqrt(self, x):  # 42ms 77.55
        """
        :type x: int
        :rtype: int
        """
        if x < 16:
            result = 3
        else:
            result = x // 2
        while result * result > x:
            result = (result + x / result) // 2
        return int(result)

    def sqrt_1(self, x):  # 62ms 14.56
        result = 1.0
        while abs(result * result - x) > 0.1:
            result = (result + x / result) / 2
        return int(result)


class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_solution(self):
        self.assertEqual(Solution().mySqrt(123), 11)


if __name__ == '__main__':
    unittest.main()
