#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 2017/7/20
import unittest


class Solution(object):
    def spiralOrder(self, matrix):  # 82.77(32ms,170720)
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return matrix
        left, top, right, bottom, result = 0, 0, len(matrix[0]) - 1, len(matrix) - 1, []
        while left < right and top < bottom:
            result.extend(matrix[top][left:right + 1] +
                          [matrix[i][right] for i in range(top + 1, bottom)] +
                          matrix[bottom][left:right + 1][::-1] +
                          [matrix[i][left] for i in range(bottom - 1, top, -1)])
            left, top, right, bottom = left + 1, top + 1, right - 1, bottom - 1
        if left == right and top == bottom:
            result.append(matrix[top][left])
        elif left == right:
            result.extend([matrix[i][left] for i in range(top, bottom + 1)])
        elif top == bottom:
            result.extend(matrix[top][left:right + 1])
        return result


class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_pow(self):
        self.assertEqual(Solution().spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), [1, 2, 3, 6, 9, 8, 7, 4, 5])


if __name__ == '__main__':
    unittest.main()
