#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 2017/7/5
import unittest


class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        far, step, pre = 0, 0, 0
        for pos in range(len(nums)):
            if pos > pre:
                step += 1
                pre = far
            far = max(far, pos + nums[pos])
        return step


class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_jump(self):
        self.assertEqual(Solution().jump([2, 3, 1, 1, 4]), 2)


if __name__ == '__main__':
    unittest.main()
