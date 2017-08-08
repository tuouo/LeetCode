#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 2017/8/2
import unittest


class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        result = [[0] * n for _ in range(n)]
        num, left, top, right, button = 1, 0, 0, n - 1, n - 1
        while left < right and top < button:
            for i in range(left, right):
                result[top][i] = num
                num += 1
            for i in range(top, button):
                result[i][right] = num
                num += 1
            for i in range(right, left, -1):
                result[button][i] = num
                num += 1
            for i in range(button, top, -1):
                result[i][left] = num
                num += 1
            left, top, right, button = left + 1, top + 1, right - 1, button - 1
        if left == right:
            result[top][left] = num
        return result

    def interesting(self, n):
        result = [[0] * n for _ in range(n)]
        coord = [[(i, j) for j in range(n)] for i in range(n)]
        count = 1
        while coord:
            for x, y in coord.pop(0):
                result[x][y] = count
                count += 1
            coord = list(zip(*coord))[::-1]

        return result

    def ha(self, n):
        result, num = [], n * n + 1
        while num > 1:
            num, end = num - len(result), num
            result = [list(range(num, end))] + list(zip(*result[::-1]))
        return result

    def interesting2(self, n):
        num = n * n
        result = [[num]]
        while num > 1:
            num, old = num - len(result), num
            result = [list(range(num, old))] + list(zip(*result[::-1]))
            print(result)
        return result


class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_gen(self):
        self.assertEqual(Solution().ha(3), [[1, 2, 3], [8, 9, 4], [7, 6, 5]])

if __name__ == '__main__':
    unittest.main()
