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
        return self.speed_up(nums)

    def speed_up(self, nums):  # 98.24(49ms,170705)
        if len(nums) < 2:
            return 0
        far, step, pre = nums[0], 0, 0
        for pos in range(1, len(nums)):
            if pos > pre:
                step += 1
                pre = far
            far = max(far, pos + nums[pos])
        return step

    def origin(self, nums):  # 71.03(62ms,1704)
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
