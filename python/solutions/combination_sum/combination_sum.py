#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 2017/6/25
import unittest


class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        return self.store_pos(candidates, target)

    def store_pos(self, candidates, target):
        if target <= 0:
            return []
        result, candidates, length = [], sorted(candidates), len(candidates)

        def find_items(remain, items, off):
            if remain == 0:
                result.append(items)
            for pos in range(off, length):
                this = candidates[pos]  # speed up
                if this > remain:
                    break
                find_items(remain - this, items + [this], pos)

        find_items(target, [], 0)
        return result

    def check_item(self, candidates, target):
        if target <= 0:
            return []
        result, candidates = [], sorted(candidates)

        def find_items(remain, items):
            if remain == 0:
                result.append(items)
            for item in candidates:
                if item > remain:
                    break
                if items and item < items[-1]:
                    continue
                else:
                    find_items(remain - item, items + [item])

        find_items(target, [])
        return result

    def base(self, candidates, target):
        result, candidates = [], sorted(candidates)

        def find_items(remain, items):
            if remain == 0:
                result.append(items)
            for item in candidates:
                if item > remain:
                    break
                if items and item < items[-1]:
                    continue
                else:
                    find_items(remain - item, items + [item])

        find_items(target, [])
        return result


class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_find(self):
        self.assertEqual(Solution().combinationSum([2, 3, 6, 7], 7), [[2, 2, 3], [7]])


if __name__ == '__main__':
    unittest.main()
