#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 2017/7/18
import unittest


class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        self.tag, self.count = (1 << n) - 1, 0
        self.solve(0, 0, 0)
        return self.count

    def solve(self, row, bias, bias_anti):
        """
        :param row: if one bit is 1, the line (index of bit) has a queen.
        :param bias: for each line, show bias has a queen if bit is 1
        :param bias_anti: for each line, show bias_anti has a queen if bit is 1
        :return:
        """
        if row == self.tag:
            self.count += 1
        else:
            pos = self.tag & (~(row | bias | bias_anti))  # find place info of queen
            while pos:
                p = -pos & pos  # find most right place
                pos -= p  # remove the place, means a queen placed
                self.solve(row | p, (bias | p) << 1, (bias_anti | p) >> 1)


class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_count(self):
        self.assertEqual(Solution().totalNQueens(8), 92)


if __name__ == '__main__':
    unittest.main()
