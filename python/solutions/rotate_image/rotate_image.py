#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 2017/7/10
import unittest


class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for row in range(n):
            for col in range(row + 1, n):
                matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]
        for row in range(n):
            matrix[row] = matrix[row][::-1]
        # return matrix


class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_rotate(self):
        self.assertEqual(Solution().rotate([[1, 2, 3], [8, 9, 4], [7, 6, 5]]), [[7, 8, 1], [6, 9, 2], [5, 4, 3]])

if __name__ == '__main__':
    unittest.main()
