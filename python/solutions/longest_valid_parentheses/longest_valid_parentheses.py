#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 2017/6/11
import unittest


class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        return self.find_count(s)

    def find_count(self, s):
        pre, result, items = -1, 0, []
        for i in range(len(s)):
            if s[i] == "(":
                items.append(i)
            elif not items:
                pre = i
            else:
                items.pop()
                if items:
                    result = max(i - items[-1], result)
                else:
                    result = max(i - pre, result)
        return result


class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_find(self):
        self.assertEqual(Solution().longestValidParentheses(")()()))()())"), 4)


if __name__ == '__main__':
    unittest.main()
