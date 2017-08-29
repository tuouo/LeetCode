#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 2017/8/29
import unittest


class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        len_1, len_2 = len(word1) + 1, len(word2) + 1
        pre, dp = 0, [i for i in range(len_2)]
        for i in range(1, len_1):
            pre, dp[0] = i - 1, i
            for j in range(1, len_2):
                pre, dp[j] = dp[j], min(dp[j] + 1, dp[j - 1] + 1, pre + (0 if word1[i - 1] == word2[j - 1] else 1))
        return dp[-1]

    def two(self, word1, word2):
        len_1, len_2 = len(word1) + 1, len(word2) + 1
        dp = [[0] * len_1 for _ in range(len_2)]
        dp[0] = [i for i in range(len_1)]
        for j in range(len_2):
            dp[j][0] = j
        for i in range(1, len_2):
            for j in range(1, len_1):
                dp[i][j] = min(dp[i - 1][j - 1] + (0 if word2[i - 1] == word1[j - 1] else 1),
                               dp[i - 1][j] + 1, dp[i][j - 1] + 1)
        return dp[-1][-1]


class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_solution(self):
        self.assertEqual(Solution().minDistance("adsgarg", "sgdge"), 5)


if __name__ == '__main__':
    unittest.main()
