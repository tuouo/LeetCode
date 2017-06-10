#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 2017/6/10
import unittest


class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        pos = len(nums) - 2
        if pos >= 0:
            while pos >= 0 and nums[pos] >= nums[pos + 1]:
                pos -= 1
            if pos == len(nums) - 2:
                nums[-2], nums[-1] = nums[-1], nums[-2]
            elif pos == -1:
                nums[:] = reversed(nums[:])
            else:
                bigger = pos + 1
                for i in range(pos + 1, len(nums)):
                    if nums[pos] < nums[i] <= nums[bigger]:
                        bigger = i
                nums[pos], nums[bigger] = nums[bigger], nums[pos]
                nums[pos+1:] = reversed(nums[pos+1:])
        # return nums


class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testNotNeedReturn(self):
        self.assertEqual(Solution().nextPermutation([1, 2, 3, 3, 1]), [1, 3, 1, 2, 3])


if __name__ == '__main__':
    unittest.main()
