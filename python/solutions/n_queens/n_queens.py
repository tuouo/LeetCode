#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 2017/7/16
import unittest


class Solution(object):
    def solveNQueens(self, n):  # 77.69(95ms, 201704)
        """
        :type n: int
        :rtype: List[List[str]]
        """
        self.n, self.result = n, []
        # Tags show no queen(empty) at postion of col, bias, bias_anti
        self.col, self.bias, self.bias_anti = [True] * n, [True] * (2 * n), [True] * (2 * n)
        self.solve(0, [0] * n)
        return self.result

    def solve(self, row, one):
        if row == self.n:
            self.result.append(["." * i + "Q" + "." * (self.n - i - 1) for i in one])
        else:
            for pos in range(self.n):
                if self.col[pos] and self.bias[pos + row] and self.bias_anti[self.n - pos + row]:
                    self.col[pos] = self.bias[pos + row] = self.bias_anti[self.n - pos + row] = False
                    one[row] = pos  # change 'one' after we deal with row & tags, doesn't matter what's initialized
                    self.solve(row + 1, one)
                    self.col[pos] = self.bias[pos + row] = self.bias_anti[self.n - pos + row] = True


class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_gen(self):
        self.assertEqual(Solution().solveNQueens(4), [[".Q..", "...Q", "Q...", "..Q."], ["..Q.", "Q...", "...Q", ".Q.."]])


if __name__ == '__main__':
    unittest.main()
