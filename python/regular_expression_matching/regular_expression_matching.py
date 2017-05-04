#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 2017/4/25
import unittest


class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str  # p should not start with "*"
        :rtype: bool
        """
        return Solution.match_dp(s, p)

    @classmethod
    def recursion(cls, s, p):
        if not p:
            return not s
        if len(p) == 1 or p[1] != "*":  # p will not start with "*"
            return cls.recursion(s[1:], p[1:]) if len(s) > 0 and (p[0] == s[0] or s[0] == ".") else False
        else:
            while len(s) > 0 and (p[0] == s[0] or p[0] == "."):
                if cls.recursion(s, p[2:]):
                    return True
                s = s[1:]
            return cls.recursion(s, p[2:])

    @staticmethod
    def match_dp_pre(s, p):
        len_s, len_p = len(s), len(p)
        dp = [[False] * (len_p + 1) for _ in range(len_s + 1)]
        dp[0][0] = True
        for pos in range(2, len_p + 1):
            dp[0][pos] = dp[0][pos - 2] and p[pos - 1] == "*"

        for i in range(1, len_s + 1):
            for j in range(1, len_p + 1):
                dp[i][j] = dp[i][j - 2] or (p[j - 2] in (".", s[i - 1]) and dp[i - 1][j]) if p[j - 1] == "*" \
                    else dp[i - 1][j - 1] and p[j - 1] in (".", s[i - 1])
        return dp[len_s][len_p]

    @staticmethod
    def match_dp(s, p):
        len_s, len_p = len(s), len(p)
        dp = [[False] * (len_p + 1) for _ in range(len_s + 1)]
        dp[0][0] = True
        for pos in range(1, len_p):
            dp[0][pos + 1] = dp[0][pos - 1] and p[pos] == "*"

        for i in range(len_s):
            for j in range(len_p):
                dp[i + 1][j + 1] = dp[i + 1][j - 1] or (p[j - 1] in (".", s[i]) and dp[i][j + 1]) if p[j] == "*" \
                    else dp[i][j] and p[j] in (".", s[i])
        return dp[len_s][len_p]


class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_match(self):
        self.assertEqual(Solution().isMatch("aa", "a"), False)
        self.assertEqual(Solution().isMatch("aa", "aa"), True)
        self.assertEqual(Solution().isMatch("aaa", "aa"), False)
        self.assertEqual(Solution().isMatch("aa", "a*"), True)
        self.assertEqual(Solution().isMatch("aa", ".*"), True)
        self.assertEqual(Solution().isMatch("ab", ".*"), True)
        self.assertEqual(Solution().isMatch("aab", "c*a*b"), True)

if __name__ == '__main__':
    unittest.main()
