#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 2017/6/6
import unittest


class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        return self.move_first(nums, val)

    def check_first(self, nums, val):
        pre, end = 0, len(nums) - 1
        while pre <= end:
            if nums[pre] == val:
                while pre < end and nums[end] == val:
                    end -= 1
                nums[pre], nums[end], end = nums[end], nums[pre], end - 1
            else:
                pre += 1
        # print(nums)
        return pre

    def move_first(self, nums, val):
        pre, end = 0, len(nums) - 1
        while pre <= end:
            if nums[pre] == val:
                nums[pre], nums[end], end = nums[end], nums[pre], end - 1
            else:
                pre += 1
        # print(nums)
        return pre


class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_remove(self):
        origin = [1, 2, 2, 3, 4, 5, 5, 5, 6, 7]
        # origin = [1, 2]
        self.assertEqual((Solution().removeElement(origin, 2)), 1)


if __name__ == '__main__':
    unittest.main()
