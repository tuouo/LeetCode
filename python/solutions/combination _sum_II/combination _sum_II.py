#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 2017/6/26
import unittest


class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if target <= 0:
            return []
        result, length, candidates = [], len(candidates), sorted(candidates)

        def find_items(remain, items, off):
            if remain == 0:
                result.append(items)
            for pos in range(off, length):
                this = candidates[pos]  # speed up
                if pos != off and this == candidates[pos-1]:
                    continue
                if this > remain:
                    break
                else:
                    find_items(remain-this, items + [this], pos+1)

        find_items(target, [], 0)
        return result


class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_find(self):
        self.assertEqual(Solution().combinationSum2([10, 1, 2, 7, 6, 1, 5], 8), [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]])


if __name__ == '__main__':
    unittest.main()
