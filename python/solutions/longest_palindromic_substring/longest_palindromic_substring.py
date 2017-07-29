#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 2017/4/21
import unittest


class Solution(object):
    def longestPalindrome(self, s):  # 71.48(376ms, 1703)
        """
        :type s: str
        :rtype: str
        """
        # https://segmentfault.com/a/1190000003914228
        string = "#" + "#".join(s) + "#"
        lens, pos, max_right, max_len = len(string), 0, 0, 0
        rl = [0] * lens
        for i in range(lens):
            if i < max_right:
                rl[i] = min(rl[pos * 2 - i], max_right - i)
            else:
                rl[i] = 1
            while (i - rl[i]) >= 0 and (i + rl[i]) < lens and string[i - rl[i]] == string[i + rl[i]]:
                rl[i] += 1
            if rl[i] + i - 1 > max_right:
                max_right = rl[i] + i - 1
                pos = i
            max_len = max(max_len, rl[i])
        pos = rl.index(max_len)
        start = (pos - max_len + 1) // 2
        return s[start:(start+max_len-1)]

    def little_change(self, s):  # 91.31(95ms, 170729)
        string = "#" + "#".join(s) + "#"
        lens, pos, max_right, max_len = len(string), 0, 0, 0
        rl = [0] * lens
        for i in range(lens):
            cur_radius = min(rl[pos * 2 - i], max_right - i) if i < max_right else 1
            while cur_radius <= i < lens - cur_radius and string[i - cur_radius] == string[i + cur_radius]:
                cur_radius += 1
            if i + cur_radius - 1 > max_right:
                max_right = i + cur_radius - 1
                pos = i
            if cur_radius > max_len:
                max_len = cur_radius
                max_mid = i
            rl[i] = cur_radius
        start = (max_mid - max_len + 1) // 2
        return s[start:(start + max_len - 1)]


class TestCase(unittest.TestCase):
    def setUp(self):
        self.string, self.result = "babad", "bab"
        self.s = Solution()

    def tearDown(self):
        del self.string
        del self.result

    def test_solution(self):
        self.assertEqual(self.s.longestPalindrome(self.string), self.result)


if __name__ == '__main__':
    unittest.main()
