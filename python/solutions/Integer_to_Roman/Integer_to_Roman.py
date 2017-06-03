#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 2017/5/4
import unittest


class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        Also, you can made a hole map
        """
        return Solution.transform_each(num)

    @staticmethod
    def transform_add(num):
        nums = {1: "I", 4: "IV", 5: "V", 9: "IX", 10: "X", 40: "XL", 50: "L",
                90: "XC", 100: "C", 400: "CD", 500: "D", 900: "CM", 1000: "M"}
        result, parts = [], sorted(nums.keys(), reverse=True)
        for i in parts:
            while num >= i:
                num -= i
                result.append(nums[i])
        return "".join(result)

    @staticmethod
    def transform_each(num):
        nums = (("", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"),
                ("", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"),
                ("", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"),
                ("", "M", "MM", "MMM"),
                )
        return nums[3][num // 1000] + nums[2][(num % 1000) // 100] + nums[1][(num % 100) // 10] + nums[0][(num % 10)]


class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_transform(self):
        self.assertEqual(Solution().intToRoman(99), "XCIX")


if __name__ == '__main__':
    unittest.main()
