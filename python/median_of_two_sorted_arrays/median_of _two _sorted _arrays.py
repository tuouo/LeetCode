#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 2017/4/20
import unittest


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if not nums1 and not nums2:
            return
        else:
            if not nums1:
                nums1, nums2 = nums2, nums1
            if not nums2:
                if len(nums1) % 2:
                    return nums1[len(nums1) // 2]
                else:
                    return (nums1[len(nums1) // 2 - 1] + nums1[len(nums1) // 2]) / 2.0
        lens = len(nums1) + len(nums2)
        if lens & 1:
            return self.find_k_th(nums1, 0, nums2, 0, lens // 2 + 1)
        else:
            return (self.find_k_th(nums1, 0, nums2, 0, lens // 2) +
                    self.find_k_th(nums1, 0, nums2, 0, lens // 2 + 1)) / 2.0

    def find_k_th_2(self, a, start_a, b, start_b, k):
        while k > 0:
            if start_a >= len(a):
                print(b[start_b + k - 1])
                return b[start_b + k - 1]
            if start_b >= len(b):
                return a[start_a + k - 1]
            if k == 1:
                return min(a[start_a], b[start_b])
            check_a = a[start_a + k // 2 - 1] if start_a + k // 2 - 1 < len(a) else float('inf')
            check_b = b[start_b + k // 2 - 1] if start_b + k // 2 - 1 < len(b) else float('inf')
            if check_a < check_b:
                start_a += k // 2
            else:
                start_b += k // 2
            k -= k // 2

    def find_k_th(self, a, start_a, b, start_b, k):
        while k > 0:
            len_a, len_b = len(a), len(b)
            if start_a >= len_a:
                return b[start_b + k - 1]
            if start_b >= len_b:
                return a[start_a + k - 1]
            if k == 1:
                return min(a[start_a], b[start_b])
            move_a, move_b = start_a + k // 2 - 1, start_b + k // 2 - 1
            if move_a >= len_a:
                start_b += k - 1 - (len_a - start_a)
                if a[len(a) - 1] < b[start_b]:
                    return b[start_b]
                else:
                    k = len_a - start_a + 1
            elif move_b >= len_b:
                start_a += k - 1 - (len_b - start_b)
                if b[len_b - 1] < a[start_a]:
                    return a[start_a]
                else:
                    k = len_b - start_b + 1
            else:
                if a[move_a] < b[move_b]:
                    start_a += k // 2
                else:
                    start_b += k // 2
                k -= k // 2


class TestCase(unittest.TestCase):
    def setUp(self):
        self.nums1, self.nums2, self.result = [4], [1, 2, 3, 5, 6], 3.5
        self.s = Solution()

    def tearDown(self):
        del self.nums1
        del self.nums2
        del self.result

    def test_insert(self):
        self.assertEqual(self.s.findMedianSortedArrays(self.nums1, self.nums2), self.result)


if __name__ == '__main__':
    unittest.main()
