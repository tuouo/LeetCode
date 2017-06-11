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
        return self.dp_doing(s)

    def count_left(self, s):
        pre, result, items = -1, 0, []
        for i in range(len(s)):
            if s[i] == '(':
                if pre != -1:
                    items.append(pre)
                    pre = -1
                else:
                    items.append(i)
            else:
                if items:
                    start = items.pop()
                    if i - start + 1 > result:
                        result = i - start + 1
                    pre = start
                else:
                    pre = -1
        return result

    def dp_no_check(self, s):
        if not s:
            return 0
        s = ")" + s
        lengths = [0 for _ in range(len(s))]
        for pos in range(1, len(s)):
            if s[pos] == ")":
                pre = pos - 1 - lengths[pos - 1]
                if s[pre] == "(":
                    lengths[pos] = lengths[pos - 1] + 2 + lengths[pre - 1]
        return max(lengths)

    def dp_doing(self, s):
        if not s:
            return 0
        lengths = [0 for _ in range(len(s))]
        for pos in range(1, len(s)):
            if s[pos] == ")":
                pre = pos - 1 - lengths[pos - 1]
                if pre >= 0 and s[pre] == "(":
                    lengths[pos] = lengths[pos - 1] + 2
                    if pre >= 1:
                        lengths[pos] += lengths[pre - 1]
        return max(lengths)

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
