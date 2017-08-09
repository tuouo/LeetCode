#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 2017/8/9
import unittest


class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        nums = {1: 1, 2: 2, 3: 6, 4: 24, 5: 120, 6: 720, 7: 5040, 8: 40320}
        digitals = list(range(1, n + 1))  # nums in set
        result, k = [], k - 1  # index begin from 0
        while n > 1:
            n -= 1
            pos, k = divmod(k, nums[n])
            result.append(digitals[pos])
            digitals.remove(digitals[pos])
        result.append(digitals[0])
        return "".join(map(str, result))


class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_solution(self):
        self.assertEqual(Solution().getPermutation(5, 4), "12453")


if __name__ == '__main__':
    unittest.main()
