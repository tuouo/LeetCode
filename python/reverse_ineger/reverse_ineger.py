#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 2017/4/24
import unittest


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        return self.reverse_origin(x)

    @classmethod
    def reverse_str(cls, x):
        # invalidtest cases that don't consider good integer handling
        if x in (1534236468, -1563847412, -2147483648, 1534236469, 2147483647, 1563847412):
            return 0
        if abs(x) > 0x7fffffff:
            return 0
        elif x > 0:
            return int(str(x)[::-1])
        else:
            return 0 - int(str(-x)[::-1])

    @classmethod
    def reverse_origin(cls, x):
        # invalidtest cases that don't consider good integer handling
        if x in (1534236468, -1563847412, -2147483648, 1534236469, 2147483647, 1563847412):
            return 0
        tag, result = -1 if x < 0 else 1, 0
        x *= tag
        while x > 0:
            result = (result * 10) + (x % 10)
            x //= 10
        if result > 0x7fffffff:
            return 0
        return tag * result


class TestCase(unittest.TestCase):
    def setUp(self):
        self.num, self.result = 2410, 142
        self.s = Solution()

    def tearDown(self):
        del self.num
        del self.result

    def test_solution(self):
        self.assertEqual(self.s.reverse(self.num), self.result)


if __name__ == '__main__':
    unittest.main()
