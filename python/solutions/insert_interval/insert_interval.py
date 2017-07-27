#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 2017/7/27
import unittest
from python.data_structure.interval import Interval


class Solution(object):
    def insert(self, intervals, newInterval):  # 98.84(62ms, 20170727)
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        if not intervals:
            return [newInterval]

        i, s, e, length = 0, newInterval.start, newInterval.end, len(intervals)
        while i < length and s > intervals[i].end:
            i += 1
        result = intervals[:i]
        if i < length:
            newInterval.start = min(s, intervals[i].start)
        while i < length and e >= intervals[i].start:
            i += 1
        if i > 0 and e >= intervals[i - 1].start:
            newInterval.end = max(e, intervals[i - 1].end)
        result += [newInterval] + intervals[i:]
        return result

    def wrong(self, intervals, newInterval):  # 10.96(116ms, 20170727)
        if not intervals:
            return [newInterval]

        i, s, e, length = 0, newInterval.start, newInterval.end, len(intervals)
        while i < length and s > intervals[i].end:
            i += 1
        result = intervals[:i]
        if i < length:
            newInterval.start = min(s, intervals[i].start)
        while i < length and e >= intervals[i].start:
            i += 1
        if i > 0 and e >= intervals[i - 1].start:
            newInterval.end = max(e, intervals[i - 1].end)
        return result + [newInterval] + intervals[i:]  # Yes, just different here!!!

    def insert_2(self, intervals, newInterval):  # 69.44(75ms, 20170727)
        if not intervals:
            return [newInterval]
        s, e = newInterval.start, newInterval.end
        if e < intervals[0].start:
            return [newInterval] + intervals[:]
        if s > intervals[-1].end:
            return intervals[:] + [newInterval]

        i, length = 0, len(intervals)
        while s > intervals[i].end:
            i += 1
        result = intervals[:i]
        newInterval.start = min(s, intervals[i].start)
        while i < length and e >= intervals[i].start:
            i += 1
        if e >= intervals[i - 1].start:
            newInterval.end = max(e, intervals[i - 1].end)
        result += [newInterval] + intervals[i:]
        return result


class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_merge(self):
        given = [1, 2], [3, 5], [6, 7], [8, 10], [12, 16]
        get = [[1, 2], [3, 10], [12, 16]]
        intervals = [Interval(s, e) for s, e in given]
        self.assertEqual(str(Solution().insert(intervals, Interval(4, 9))), str(get))


if __name__ == '__main__':
    unittest.main()
