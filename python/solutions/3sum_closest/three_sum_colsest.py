#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 2017/5/17
import unittest


class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        first, differ = 0, sum(nums[:3]) - target
        while first < len(nums) - 2:
            second, third = first + 1, len(nums) - 1
            if sum(nums[first:first+3]) > target:
                if abs(differ) > abs(sum(nums[first:first+3]) - target):
                    differ = sum(nums[first:first+3]) - target
                return differ + target
            flag = nums[first] + nums[second] + nums[third] < target
            while second < third:
                add = nums[first] + nums[second] + nums[third]
                if abs(differ) > abs(add - target):
                    differ = add - target
                if target == add:
                    return target
                elif target < add:
                    third -= 1
                    if flag:
                        second, third = second + 1, third + 1
                        flag = nums[first] + nums[second] + nums[third] < target
                    else:
                        flag = False
                else:
                    second += 1
                    flag = nums[first] + nums[second] + nums[third] < target
            first += 1
            while nums[first] == nums[first - 1] and first < len(nums) - 2:
                first += 1
        return differ + target


class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_find(self):
        print(Solution().threeSumClosest([-1, 1, 2, -4], 1))


if __name__ == '__main__':
    unittest.main()
