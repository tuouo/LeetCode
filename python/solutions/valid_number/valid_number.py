#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 2017/8/17
import unittest


class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        import re
        return bool(re.match(r"^\s*[\+-]?((\d+(\.\d*)?)|\.\d+)([eE][\+-]?\d+)?\s*$", s))


class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_solution(self):
        self.assertEqual(Solution().isNumber("0"), True)
        self.assertEqual(Solution().isNumber(" 0.1"), True)
        self.assertEqual(Solution().isNumber("abc"), False)
        self.assertEqual(Solution().isNumber("1 a"), False)
        self.assertEqual(Solution().isNumber("3e10"), True)


if __name__ == '__main__':
    unittest.main()
