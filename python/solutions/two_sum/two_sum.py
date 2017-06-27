#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 2017/4/19
import unittest


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        return Solution.two_sum_c(nums, target)

    @staticmethod
    def two_sum_a(nums, target):
        end_l, end = len(nums) - 1, len(nums)
        for i in range(end_l):
            for j in range(i + 1, end):
                if nums[i] + nums[j] == target:
                    return [i, j]

    @staticmethod
    def two_sum_b(nums, target):
        if len(nums) < 1:
            return
        tmp = {}
        for i in range(len(nums)):
            if nums[i] in tmp:
                return [tmp[nums[i]], i]
            else:
                tmp[target - nums[i]] = i

    @staticmethod
    def two_sum_c(nums, target):
        if len(nums) < 1:
            return
        tmp = {}
        for i in range(len(nums)):
            this = nums[i]
            if this in tmp:
                return [tmp[this], i]
            else:
                tmp[target - this] = i


class TestCase(unittest.TestCase):
    def setUp(self):
        self.nums, self.target, self.result = [2, 7, 11, 15], 9, [0, 1]
        self.s = Solution()

    def tearDown(self):
        del self.nums
        del self.target

    def test_solution(self):
        self.assertEqual(self.s.twoSum(self.nums, self.target), self.result)
        self.assertEqual(Solution.two_sum_a(self.nums, self.target), self.result)
        self.assertEqual(Solution.two_sum_b(self.nums, self.target), self.result)


if __name__ == '__main__':
    unittest.main()
