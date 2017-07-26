#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 2017/7/25
import unittest
from python.data_structure.interval import Interval


class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        return self.start_end_same(intervals)

    def start_end_same(self, intervals):  # 92.09(72ms, 170726)
        if not intervals:
            return intervals
        starts = sorted([_.start for _ in intervals])
        ends = [0] + sorted([_.end for _ in intervals])
        result, s = [], 0
        for pos in range(1, len(starts)):
            if starts[pos] > ends[pos]:
                result.append([starts[s], ends[pos]])
                s = pos
        result.append([starts[s], ends[-1]])
        return result

    def heapq_sab(self, intervals):  # 3.79(178ms, 170727)
        if not intervals:
            return intervals
        import heapq
        starts, ends, result = [], [], []
        for item in intervals:
            heapq.heappush(starts, item.start)
            heapq.heappush(ends, item.end)
        pre = heapq.heappop(starts)
        while starts:
            s = heapq.heappop(starts)
            e = heapq.heappop(ends)
            if s > e:
                result.append([pre, e])
                pre = s
        while ends:
            e = heapq.heappop(ends)
        result.append([pre, e])
        return result

    def start_end_sub(self, intervals):  # 86.2(75ms, 170726)
        if not intervals:
            return intervals
        starts = sorted([_.start for _ in intervals])
        ends = sorted([_.end for _ in intervals])
        # starts = list(sorted((_.start for _ in intervals))) # 84.02(76ms, 170726)
        # ends = list(sorted((_.end for _ in intervals)))
        result, s = [], 0
        for pos in range(len(starts) - 1):
            if starts[pos + 1] > ends[pos]:
                result.append([starts[s], ends[pos]])
                s = pos + 1
        result.append([starts[s], ends[-1]])
        return result

    def start_end(self, intervals):  # 66.10(82ms, 170726)
        if not intervals:
            return intervals
        starts = sorted([_.start for _ in intervals])
        ends = sorted([_.end for _ in intervals])
        result, s = [], 0
        for pos in range(len(starts) - 1):
            if starts[pos + 1] > ends[pos]:
                result.append([starts[s], ends[pos]])
                s = pos + 1
        result.append([starts[s], ends[-1]])
        return result

    def sort_one_by_one_tmp(self, intervals):  # 74.98(79ms, 170726)
        if not intervals:
            return intervals
        intervals = sorted(intervals, key=lambda x: x.start)
        result, pre = [intervals[0]], intervals[0]
        for item in intervals[1:]:
            if pre.end >= item.start:
                if pre.end < item.end:
                    pre.end = item.end
            else:
                result.append(item)
                pre = item
        return result

    def sort_one_by_one(self, intervals):  # 57.14(86ms, 1704)
        if not intervals:
            return intervals
        intervals = sorted(intervals, key=lambda x: x.start)
        result = [intervals[0]]
        for item in intervals[1:]:
            pre = result[-1]
            if pre.end >= item.start:
                if pre.end < item.end:
                    pre.end = item.end
            else:
                result.append(item)
        return result


class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_merge(self):
        given = [[1, 3], [2, 6], [8, 10], [15, 18]]
        get = [[1, 6], [8, 10], [15, 18]]
        intervals = [Interval(s, e) for s, e in given]
        self.assertEqual(str(Solution().merge(intervals)), str(get))


if __name__ == '__main__':
    unittest.main()
