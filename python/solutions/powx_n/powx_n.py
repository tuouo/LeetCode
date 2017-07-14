#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 2017/7/14
import unittest


class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        Cos the leetcode Runtime, this code can get the best 74.33(39ns, 1705)
        """
        abs_n, result = abs(n), 1
        while abs_n > 0:
            if abs_n % 2:
                result *= x
            abs_n //= 2
            x *= x
        return 1.0 / result if n < 0 else result


class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_pow(self):
        # self.assertEqual(Solution().myPow(8.88023, 3), 700.28148)
        self.assertEqual(Solution().myPow(8.88023, 3), 700.2814829452681)


if __name__ == '__main__':
    unittest.main()
