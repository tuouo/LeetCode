#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 2017/6/8
import unittest


class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        return self.sub_3(dividend, divisor)

    def sub_1(self, dividend, divisor):
        sign = (dividend < 0) is (divisor < 0)
        result, rate, tmp, divisor, dividend = 0, 1, abs(divisor), abs(divisor), abs(dividend)
        while tmp <= dividend:
            rate, tmp = rate << 1, tmp << 1
        while divisor <= dividend:
            rate, tmp = rate >> 1, tmp >> 1
            if dividend >= tmp:
                dividend, result = dividend - tmp, result + rate
        if sign:
            return min(result, 2147483647)
        return max(-result, -2147483648)

    def sub_2(self, dividend, divisor):
        sign = (dividend < 0) is (divisor < 0)
        result, rate, tmp, divisor, dividend = 0, 1, abs(divisor), abs(divisor), abs(dividend)

        while divisor <= dividend:
            if tmp <= dividend:
                dividend, result = dividend - tmp, result + rate
                rate, tmp = rate << 1, tmp << 1
            else:
                rate, tmp = rate >> 1, tmp >> 1
                if tmp <= dividend:
                    dividend, result = dividend - tmp, result + rate
        if sign:
            return min(result, 2147483647)
        return max(-result, -2147483648)

    def sub_3(self, dividend, divisor):
        sign = (dividend < 0) is (divisor < 0)
        result, rate, tmp, divisor, dividend = 0, 1, abs(divisor), abs(divisor), abs(dividend)
        while dividend >= divisor:
            dividend, result = dividend - tmp, result + rate
            rate, tmp = rate << 1, tmp << 1
            if dividend < tmp:
                tmp, rate = divisor, 1
        if sign:
            return min(result, 2147483647)
        return max(-result, -2147483648)


class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_divide(self):
        self.assertEqual(Solution().divide(123432, -3), -41144)


if __name__ == '__main__':
    unittest.main()
