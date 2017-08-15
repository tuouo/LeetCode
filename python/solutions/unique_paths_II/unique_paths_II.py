#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 2017/8/15
import unittest


class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if obstacleGrid[0][0] == 1:
            return 0
        len_row, len_col = len(obstacleGrid), len(obstacleGrid[0])
        result = [0] * len_col
        result[0] = 1
        for i in range(1, len_col):
            if obstacleGrid[0][i] == 1:
                result[i] = 0
                break
            else:
                result[i] = result[i - 1]

        for i in range(1, len_row):
            if obstacleGrid[i][0] == 1:
                result[0] = 0
            for j in range(1, len_col):
                if obstacleGrid[i][j] == 1:
                    result[j] = 0
                else:
                    result[j] += result[j - 1]
        return result[-1]

    def uniquePathsWithObstacles2(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if obstacleGrid[0][0] == 1:
            return 0
        len_row, len_col = len(obstacleGrid), len(obstacleGrid[0])
        result = [[0] * (len_col + 1) for _ in range(len_row + 1)]
        result[0][1] = 1
        for i in range(len_row):
            for j in range(len_col):
                if not obstacleGrid[i][j]:
                    result[i + 1][j + 1] = result[i][j + 1] + result[i + 1][j]
        return result[-1][-1]


class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_solution(self):
        self.assertEqual(Solution().uniquePathsWithObstacles([[0, 0, 0], [0, 1, 0], [0, 0, 0]]), 2)


if __name__ == '__main__':
    unittest.main()
