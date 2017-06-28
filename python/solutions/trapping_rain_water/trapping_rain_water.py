#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 2017/6/28
import unittest


class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        return self.check_peak(height)

    def check_peak(self, height):
        if not height or len(height) < 3:
            return 0
        water, length, tops = 0, len(height), [(0, height[0])]
        for i in range(1, length - 1):
            if height[i - 1] < height[i] >= height[i + 1]:
                tops += [(i, height[i])]
        tops += [(length - 1, height[-1])]  # for begin and end, does not matter are not really top

        cur = top = max(tops, key=lambda one: one[1])
        tops_pre, tops_after = [tops[0]], [tops[-1]]
        for item in tops[1:tops.index(top)]:
            if item[1] > tops_pre[-1][1]:
                tops_pre.append(item)
        for item in reversed(tops[tops.index(top)+1:]):
            if item[1] > tops_after[-1][1]:
                tops_after.append(item)

        for top_pre in tops_pre[::-1]:
            for i in range(top_pre[0] + 1, cur[0]):
                if top_pre[1] >= height[i]:
                    water += top_pre[1] - height[i]
                else:
                    break
            cur = top_pre
        cur = top
        for top_after in tops_after[::-1]:
            for i in range(cur[0] + 1, top_after[0]):
                if top_after[1] > height[i]:
                    water += top_after[1] - height[i]
            cur = top_after
        return water

    def find_peak(self, height):
        if not height or len(height) < 3:
            return 0
        water, length, tops = 0, len(height), [(0, height[0])]
        for i in range(1, length - 1):
            if height[i - 1] < height[i] >= height[i + 1]:
                tops += [(i, height[i])]
        tops += [(length - 1, height[-1])]  # for begin and end, does not matter are not really top

        top2 = top = max(tops, key=lambda item: item[1])
        while top != tops[0]:
            top_pre = max(tops[:tops.index(top)], key=lambda item: item[1])
            for i in range(top_pre[0] + 1, top[0]):
                if top_pre[1] > height[i]:
                    water += top_pre[1] - height[i]
            top = top_pre
        top = top2
        while top != tops[-1]:
            top_after = max(tops[tops.index(top) + 1:], key=lambda item: item[1])
            for i in range(top[0] + 1, top_after[0]):
                if top_after[1] > height[i]:
                    water += top_after[1] - height[i]
            top = top_after

        return water


class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_count(self):
        self.assertEqual(Solution().trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]), 6)
        self.assertEqual(Solution().trap([5, 4, 1, 2]), 1)


if __name__ == '__main__':
    unittest.main()
