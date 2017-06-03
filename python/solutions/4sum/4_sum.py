#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 2017/5/19
import unittest


class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        result = []
        for i in range(len(nums) - 3):
            if nums[i] * 4 > target:
                break
            if i and nums[i] == nums[i-1]:
                continue
            target2 = target - nums[i]
            for j in range(i+1, len(nums) - 2):
                if nums[j] * 3 > target2:
                    break
                if j != i+1 and nums[j] == nums[j-1]:
                    continue
                m, n = j+1, len(nums) - 1
                target3 = target - nums[i] - nums[j]
                if nums[m] * 2 > target3 or nums[n] * 2 < target3:
                    continue
                while m < n:
                    add = nums[m] + nums[n]
                    if target3 == add:
                        result.append((nums[i], nums[j], nums[m], nums[n]))
                        m, n = m + 1, n - 1
                        while nums[n] == nums[n+1] and m < n:
                            n -= 1
                        while nums[m] == nums[m-1] and m < n:
                            m += 1
                    elif target3 > add:
                        m += 1
                    else:
                        n -= 1
        return result


class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_find(self):
        print(Solution().fourSum([1, 0, -1, 0, -2, 2], 0), [[-1,  0, 0, 1], [-2, -1, 1, 2], [-2,  0, 0, 2]])


if __name__ == '__main__':
    unittest.main()
