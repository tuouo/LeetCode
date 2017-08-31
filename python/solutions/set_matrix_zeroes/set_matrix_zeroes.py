#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 2017/8/31
import unittest


class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        col = 0 if 0 in matrix[0] else 1

        for i in range(1, len(matrix)):
            modify = 1
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    modify = matrix[0][j] = 0
            if modify == 0:
                matrix[i] = [0] * len(matrix[0])

        for j in range(len(matrix[0])):
            if matrix[0][j] == 0:
                for i in range(len(matrix)):
                    matrix[i][j] = 0

        if col == 0:
            matrix[0] = [0] * len(matrix[0])


class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_solution(self):
        matrix = [[1, 0, 1, 1], [1, 1, 0, 1], [1, 1, 1, 0], [1, 1, 1, 1]]
        result = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [1, 0, 0, 0]]
        Solution().setZeroes(matrix)
        self.assertEqual(matrix, result)


if __name__ == '__main__':
    unittest.main()
