#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 2017/5/4
import unittest


class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        Find a way lead to the max, start from length, when bigger?
        """
        return Solution.find_check(height)

    @staticmethod
    def all_check(height):
        area, left, right = 0, 0, len(height) - 1
        while left < right:
            area = max(area, min(height[left], height[right]) * (right - left))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return area

    @staticmethod
    def find_check(height):
        area, high, left, right = 0, 0, 0, len(height) - 1
        while left < right:
            area = max(area, min(height[left], height[right]) * (right - left))
            if height[left] < height[right]:
                high = height[left]
                while left < right and height[left] <= high:
                    left += 1
            else:
                high = height[right]
                while left < right and height[right] <= high:
                    right -= 1
        return area


class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_area(self):
        self.assertEqual(Solution().maxArea([1, 2, 3, 4, 3, 2, 1, 5]), 5)


if __name__ == '__main__':
    unittest.main()
