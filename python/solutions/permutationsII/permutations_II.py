#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 2017/7/7
import unittest


class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        perms = [[]]
        for k, n in enumerate(nums):
            new_perms = []
            for perm in perms:
                for i in range(k + 1):  # 51.34(122ms) 换成 xrange 94.36（99ms）
                    new_perms.append(perm[:i] + [n] + perm[i:])
                    if i < k and perm[i] == n:
                        break
            perms = new_perms
        return perms


class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
