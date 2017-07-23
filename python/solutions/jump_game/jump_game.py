#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 2017/7/23
import unittest


class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) < 2:
            return True
        reach = 0
        for pos, num in enumerate(nums):
            if reach < pos:
                return False
            reach = max(reach, pos + num)
        return True


class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_reach(self):
        self.assertEqual(Solution().canJump([2, 3, 1, 1, 4]), True)
        self.assertEqual(Solution().canJump([3, 2, 1, 0, 4]), False)


if __name__ == '__main__':
    unittest.main()
