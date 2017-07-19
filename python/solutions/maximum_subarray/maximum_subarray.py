#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 2017/7/19
import unittest


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = total_all = nums[0]
        for num in nums[1:]:
            total = max(num, total + num)
            if total_all < total:
                total_all = total
        return total_all


class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_add(self):
        self.assertEqual(Solution().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]), 6)


if __name__ == '__main__':
    unittest.main()
