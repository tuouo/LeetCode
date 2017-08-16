#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 2017/8/16
import unittest


class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return
        len_row, len_col = len(grid), len(grid[0])
        dp = [0] * len_col
        dp[0] = grid[0][0]
        for i in range(1, len_col):
            dp[i] = dp[i - 1] + grid[0][i]
        for i in range(1, len_row):
            dp[0] += grid[i][0]
            for j in range(1, len_col):
                dp[j] = min(dp[j - 1], dp[j]) + grid[i][j]
        return dp[-1]

    def change(self, grid):
        len_row, len_col = len(grid), len(grid[0])
        for i in range(len_col - 1):
            grid[0][i + 1] += grid[0][i]
        for i in range(len_row - 1):
            grid[i + 1][0] += grid[i][0]
        for i in range(1, len_row):
            for j in range(1, len_col):
                grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])
        return grid[-1][-1]


class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_solution(self):
        self.assertEqual(Solution().minPathSum([[0, 0, 0], [0, 1, 0], [0, 0, 0]]), 0)

if __name__ == '__main__':
    unittest.main()
