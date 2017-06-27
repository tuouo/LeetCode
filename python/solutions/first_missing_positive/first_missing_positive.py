#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 2017/6/27
import unittest


class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums += [0]  # cos index start from 0
        pos, length = 0, len(nums)
        while pos < length:
            this = nums[pos]
            if 0 <= this < length and this != pos and this != nums[this]:
                nums[pos], nums[this] = nums[this], this
            else:
                pos += 1
        for i in range(1, length):
            if nums[i] != i:
                return i
        return length


class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_find(self):
        self.assertEqual((Solution().firstMissingPositive([3, 4, -1, 1])), 2)
        self.assertEqual((Solution().firstMissingPositive([3])), 1)
        self.assertEqual((Solution().firstMissingPositive([1, 2, 3])), 4)


if __name__ == '__main__':
    unittest.main()
