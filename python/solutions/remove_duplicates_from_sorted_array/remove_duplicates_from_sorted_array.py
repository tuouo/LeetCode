#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 2017/6/6
import unittest


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        end, sentry = 1, nums[0]
        for i in range(1, len(nums)):
            if sentry != nums[i]:
                sentry = nums[end] = nums[i]
                end += 1
        return end
    
    def removeDuplicates_old(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        check = 0
        for i in range(1, len(nums)):
            if nums[check] != nums[i]:
                check += 1
                nums[check] = nums[i]
        return check + 1


class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testRemove(self):
        origin = [1, 2, 2, 3, 4, 5, 5, 5, 6, 7]
        self.assertEqual((Solution().removeDuplicates(origin)), 7)

if __name__ == '__main__':
    unittest.main()
