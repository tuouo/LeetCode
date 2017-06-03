#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 2017/5/4
import unittest


class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        return Solution.after_add_pos(s)

    @staticmethod
    def check_add(s):
        result, roman_int = 0, {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}
        for i in range(len(s) - 1):
            if roman_int[s[i]] >= roman_int[s[i + 1]]:
                result += roman_int[s[i]]
            else:
                result -= roman_int[s[i]]
        return result + roman_int[s[-1]]

    @staticmethod
    def lambda_add(s):
        roman_int = {"I": lambda i: -1 if s[i + 1] in ("V", "X") else 1,
                     "X": lambda i: -10 if s[i + 1] in ("L", "C") else 10,
                     "C": lambda i: -100 if s[i + 1] in ("D", "M") else 100,
                     "V": lambda i: 5,
                     "L": lambda i: 50,
                     "D": lambda i: 500,
                     "M": lambda i: 1000}
        result, s = 0, s + "@"
        for index, v in enumerate(s[:-1]):
            result += roman_int[v](index)
        return result

    @staticmethod
    def after_add(s):
        result, roman_int = 0, {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}
        for i in s:
            result += roman_int[i]
        if s.find("IV") != -1:
            result -= 2
        if s.find("IX") != -1:
            result -= 2
        if s.find("XL") != -1:
            result -= 20
        if s.find("XC") != -1:
            result -= 20
        if s.find("CD") != -1:
            result -= 200
        if s.find("CM") != -1:
            result -= 200
        return result

    @staticmethod
    def after_add_pos(s):
        result, roman_int = 0, {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}
        for i in range(len(s)):
            result += roman_int[s[i]]
        # for i in s:
        #     result += roman_int[i]
        pre, pos = 0, s.find("CM")
        if pos == -1:
            pos = s.find("CD", pre)
        if pos != -1:
            result -= 200
            pre = pos

        pos = s.find("XC", pre)
        if pos == -1:
            pos = s.find("XL", pre)
        if pos != -1:
            result -= 20
            pre = pos

        pos = s.find("IX", pre)
        if pos == -1:
            pos = s.find("IV", pre)
        if pos != -1:
            result -= 2
        return result


class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_transform(self):
        self.assertEqual(Solution().romanToInt("MDCCCLXXXIV"), 1884)


if __name__ == '__main__':
    unittest.main()
