#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 2017/4/25
import unittest


class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        return Solution.is_palindrome_compare(x)

    @classmethod
    def is_palindrome_log(cls, x):
        if x < 0:
            return False
        elif x < 10:
            return True
        elif x % 10 == 0:
            return False

        import math
        base = 10 ** int(math.log10(x))
        while x > 0:
            if x / base != x % 10:
                return False
            x = (x % base) / 10
            base /= 100
        return True

    @classmethod
    def is_palindrome_compare(cls, x):
        if x < 0:
            return False
        elif x < 10:
            return True
        elif x % 10 == 0:
            return False
        x, get = x // 10, x % 10
        while x > get:
            x, get = x // 10, 10 * get + x % 10
        if get > x:
            get //= 10
        return get == x


class TestCase(unittest.TestCase):
    def setUp(self):
        self.num = 12421
        self.s = Solution()

    def tearDown(self):
        del self.num

    def test_solution(self):
        self.assertTrue(self.s.isPalindrome(self.nums))


if __name__ == '__main__':
    unittest.main()
