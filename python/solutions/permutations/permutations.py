#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 2017/7/6
import unittest


class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        return self.store(nums)

    def package(self, nums):  # 9.92(115ms,1704)
        from itertools import permutations
        return list(permutations(nums, len(nums)))

    def new_list(self, nums):  # 45.92(79ms,1704)
        def get_permute(current, num, result):
            if not num:
                result.append(current + [])
                return
            for i, v in enumerate(num):
                current.append(num[i])
                get_permute(current, num[:i] + num[i + 1:], result)
                current.pop()
        result = []
        get_permute([], nums, result)
        return result

    def with_tag(self, num):  # 7.2(122ms,1704)
        def permuteRecu(result, used, cur, num):
            if len(cur) == len(num):
                result.append(cur + [])
                return
            for i in range(len(num)):
                if not used[i]:
                    used[i] = True
                    cur.append(num[i])
                    permuteRecu(result, used, cur, num)
                    cur.pop()
                    used[i] = False

        result = []
        used = [False] * len(num)
        permuteRecu(result, used, [], num)
        return result

    def genner(self, nums):  # 45.92(79ms,1704)
        def gen(nums):
            if not nums:
                yield []
            for i, n in enumerate(nums):
                for p in gen(nums[:i] + nums[i + 1:]):
                    yield [n] + p
        return list(gen(nums))

    def store(self, nums):  # 87.53(66ms,1704)
        perms = [[]]
        for n in nums:
            new_perms = []
            for perm in perms:
                for i in range(len(perm) + 1):
                    new_perms.append(perm[:i] + [n] + perm[i:])
            perms = new_perms
        return perms


class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_per(self):
        result = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
        self.assertEqual(Solution().permute([1, 2, 3]), result)

if __name__ == '__main__':
    unittest.main()
