#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 2017/5/16
import unittest


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        return Solution.meet(nums)

    @staticmethod
    def meet(nums):
        nums = sorted(nums)
        result, first = [], 0
        while first < len(nums) - 2 and nums[first] <= 0:
            second, third = first + 1, len(nums) - 1
            while second < third:
                target = 0 - nums[first] - nums[second]
                if target == nums[third]:
                    result.append((nums[first], nums[second], nums[third]))
                    third -= 1
                    second += 1
                    while nums[third] == nums[third + 1] and second < third:
                        third -= 1
                    while nums[second] == nums[second - 1] and second < third:
                        second += 1
                elif target < nums[third]:
                    third -= 1
                else:
                    second += 1
            first += 1
            while nums[first] == nums[first - 1] and first < len(nums) - 2:
                first += 1
        return result

    @staticmethod
    def with_dict(nums):
        if len(nums) < 3:
            return []
        nums.sort()
        res = set()
        for i, v in enumerate(nums[:-2]):
            if i >= 1 and v == nums[i - 1]:
                continue
            if v > 0:
                break
            d = {}
            for x in nums[i + 1:]:
                if x not in d:
                    d[-v - x] = 1
                else:
                    res.add((v, -v - x, x))
        return map(list, res)


class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_find(self):
        print(Solution().threeSum([-1, 0, 1, 2, -1, -4]), [[-1, 0, 1], [-1, -1, 2]])

if __name__ == '__main__':
    unittest.main()
