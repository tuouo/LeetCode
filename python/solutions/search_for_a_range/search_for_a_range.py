#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 2017/6/19
import unittest


class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        length = len(nums) - 1
        left = self.bin_search_left(nums, target, 0, length)
        if left > length or nums[left] != target:
            return [-1, -1]
        right = self.bin_search_right(nums, target, left, length)
        return [left, right]

    def bin_search_left(self, arr, target, left, right):
        while left <= right:
            mid = (right + left) // 2
            if target > arr[mid]:
                left = mid + 1
            else:
                right = mid - 1
        return left

    def bin_search_right(self, arr, target, left, right):
        while left <= right:
            mid = (right + left) // 2
            if target < arr[mid]:
                right = mid - 1
            else:
                left = mid + 1
        return right


class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_search(self):
        self.assertEqual(Solution().searchRange([5, 7, 7, 8, 8, 10], 8), [3, 4])


if __name__ == '__main__':
    unittest.main()
