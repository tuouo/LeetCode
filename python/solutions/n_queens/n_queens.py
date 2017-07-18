#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 2017/7/16
import unittest


class Solution(object):
    def solveNQueens(self, n):  # 100(62ms,20170717)
        """
        :type n: int
        :rtype: List[List[str]]
        """
        self.result, self.arr, self.n, self.tag, count = [], {}, n, (1 << n) - 1, 1
        for i in range(n):
            self.arr[count] = n - 1 - i
            count *= 2
        self.solve(0, 0, 0, [])
        return self.result

    def solve(self, row, bias, bias_anti, one):
        """
        :param row: if one bit is 1, the line (index of bit) has a queen.
        :param bias: for each line, show bias has a queen if bit is 1
        :param bias_anti: for each line, show bias_anti has a queen if bit is 1
        :return:
        """
        if row == self.tag:
            self.result.append(["." * i + "Q" + "." * (self.n - i - 1) for i in one])
        else:
            pos = self.tag & (~(row | bias | bias_anti))  # find place info of queen
            while pos:
                p = -pos & pos  # find most right place
                pos -= p  # remove the place, means a queen placed
                one.append(self.arr[p])
                self.solve(row | p, (bias | p) << 1, (bias_anti | p) >> 1, one)
                one.pop()

    # def solveNQueens(self, n):  # 77.69(95ms, 201704)
    #     """
    #     :type n: int
    #     :rtype: List[List[str]]
    #     """
    #     self.n, self.result = n, []
    #     # Tags show no queen(empty) at postion of col, bias, bias_anti
    #     self.col, self.bias, self.bias_anti = [True] * n, [True] * (2 * n), [True] * (2 * n)
    #     self.solve(0, [0] * n)
    #     return self.result
    #
    # def solve(self, row, one):
    #     if row == self.n:
    #         self.result.append(["." * i + "Q" + "." * (self.n - i - 1) for i in one])
    #     else:
    #         for pos in range(self.n):
    #             if self.col[pos] and self.bias[pos + row] and self.bias_anti[self.n - pos + row]:
    #                 self.col[pos] = self.bias[pos + row] = self.bias_anti[self.n - pos + row] = False
    #                 one[row] = pos  # change 'one' after we deal with row & tags, doesn't matter what's initialized
    #                 self.solve(row + 1, one)
    #                 self.col[pos] = self.bias[pos + row] = self.bias_anti[self.n - pos + row] = True

    # def solveNQueens(self, n):  # 70.54(102ms, 20170716)
    #     from copy import deepcopy
    #     """
    #     :type n: int
    #     :rtype: List[List[str]]
    #     """
    #     self.n, self.result, self.deepcopy = n, [], deepcopy
    #     # Tags show no queen(empty) at postion of col, bias, bias_anti
    #     self.col, self.bias, self.bias_anti = [True] * n, [True] * (2 * n), [True] * (2 * n)
    #     self.solve(0, [0] * n)
    #     return [["." * i + "Q" + "." * (n - i - 1) for i in one] for one in self.result]
    #
    # def solve(self, row, one):
    #     if row == self.n:
    #         self.result.append(self.deepcopy(one))
    #     else:
    #         for pos in range(self.n):
    #             if self.col[pos] and self.bias[pos + row] and self.bias_anti[self.n - pos + row]:
    #                 self.col[pos] = self.bias[pos + row] = self.bias_anti[self.n - pos + row] = False
    #                 one[row] = pos  # change 'one' after we deal with row & tags, doesn't matter what's initialized
    #                 self.solve(row + 1, one)
    #                 self.col[pos] = self.bias[pos + row] = self.bias_anti[self.n - pos + row] = True


class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_gen(self):
        self.assertEqual(Solution().solveNQueens(4), [[".Q..", "...Q", "Q...", "..Q."], ["..Q.", "Q...", "...Q", ".Q.."]])


if __name__ == '__main__':
    unittest.main()
