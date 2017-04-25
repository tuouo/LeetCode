#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 2017/4/24
import unittest


class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        return Solution.my_atoi_re(s)

    @classmethod
    def my_atoi_1(cls, s):
        if not s:
            return 0

        INI_MAX = 0x7fffffff
        INI_MIN = -1 - INI_MAX
        i, sign, result = 0, 1, 0
        while i < len(s) and s[i] == " ":
            i += 1

        if s[i] == "+":
            i += 1
        elif s[i] == "-":
            sign = -1
            i += 1

        while i < len(s) and s[i] in "0123456789":
            if result > (INI_MAX - int(s[i])) / 10:
                return INI_MAX if sign > 0 else INI_MIN
            result = result * 10 + int(s[i])
            i += 1

        return sign * result

    @classmethod
    def my_atoi_2(cls, s):
        if not s:
            return 0
        i, sign, result = 0, 1, 0
        while i < len(s) and s[i] == " ":
            i += 1

        if s[i] == "+":
            i += 1
        elif s[i] == "-":
            sign = -1
            i += 1

        while i < len(s) and s[i].isdigit():
            result = result * 10 + int(s[i])
            i += 1

        INI_MAX = 0x7fffffff
        INI_MIN = -1 - INI_MAX
        return max(INI_MIN, min(sign * result, INI_MAX))

    @classmethod
    def my_atoi_re(cls, s):
        import re
        s = re.findall(r'(^[+-0]*\d+)\D*', s.strip())
        try:
            result = int("".join(s))
            INI_MAX = 0x7fffffff
            INI_MIN = -1 - INI_MAX
            return max(INI_MIN, min(result, INI_MAX))
        except:
            return 0


class TestCase(unittest.TestCase):
    def setUp(self):
        self.num, self.result = "-00124", -124
        self.s = Solution()

    def tearDown(self):
        del self.num
        del self.result

    def test_solution(self):
        self.assertEqual(self.s.myAtoi(self.num), self.result)
        self.assertEqual(Solution.my_atoi_1(self.num), self.result)
        self.assertEqual(Solution.my_atoi_2(self.num), self.result)
        self.assertEqual(Solution.my_atoi_re(self.num), self.result)


if __name__ == '__main__':
    unittest.main()
