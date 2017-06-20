#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 2017/6/20
import unittest


class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # return bisect.bisect_left(nums, target)
        left, right = 0, len(nums) - 1
        if target > nums[right]:
            return right + 1
        if target <= nums[0]:
            return 0

        while left <= right:
            mid = (right + left) // 2
            if nums[mid] >= target:
                right = mid - 1
            else:
                left = mid + 1

        return left


class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_search(self):
        self.assertEqual(Solution().searchInsert([1, 3, 5, 6], 5), 2)
        self.assertEqual(Solution().searchInsert([1, 3, 5, 6], 2), 1)
        self.assertEqual(Solution().searchInsert([1, 3, 5, 6], 7), 4)
        self.assertEqual(Solution().searchInsert([1, 3, 5, 6], 0), 0)

if __name__ == '__main__':
    unittest.main()
