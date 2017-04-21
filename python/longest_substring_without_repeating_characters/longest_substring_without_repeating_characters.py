#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 2017/4/19
import unittest


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        return Solution.length_of_longest_substring_a(s)

    @staticmethod
    def length_of_longest_substring_a(s):
        items, max_len, length = set(), 0, 0
        for i in range(len(s)):
            if s[i] not in items:
                items.add(s[i])
                length += 1
                if length > max_len:
                    max_len = length
            else:
                pos = s.rfind(s[i], i - length, i)
                length = i - pos
                items = set(s[pos:i])
        return max_len

    @staticmethod
    def length_of_longest_substring_b(s):
        chars, pos, max_len = {}, 0, 0
        for i in range(len(s)):
            if s[i] in chars and pos <= chars[s[i]]:
                pos = chars[s[i]] + 1
            else:
                max_len = max(max_len, i - pos + 1)
            chars[s[i]] = i
        return max_len

    @staticmethod
    def length_of_longest_substring_c(s):
        chars, pos, max_len = {}, 0, 0
        for i in range(len(s)):
            if s[i] in chars and pos <= chars[s[i]]:
                max_len = max(max_len, i - pos)
                pos = chars[s[i]] + 1
            chars[s[i]] = i
        return max(max_len, len(s) - pos)

    @staticmethod
    def length_of_longest_substring_c2(s):
        chars, pos, max_len = {}, 0, 0
        for k, v in enumerate(s):
            if v in chars and pos <= chars[v]:
                max_len = max(max_len, k - pos)
                pos = chars[v] + 1
            chars[v] = k
        return max(max_len, len(s) - pos)


class TestCase(unittest.TestCase):
    def setUp(self):
        self.string, self.result = "abcabcbb", 3
        self.s = Solution()

    def tearDown(self):
        del self.string
        del self.result

    def test_solution(self):
        self.assertEqual(self.s.lengthOfLongestSubstring(self.string), self.result)
        self.assertEqual(Solution.length_of_longest_substring_a(self.string), self.result)
        self.assertEqual(Solution.length_of_longest_substring_b(self.string), self.result)
        self.assertEqual(Solution.length_of_longest_substring_c(self.string), self.result)
        self.assertEqual(Solution.length_of_longest_substring_c2(self.string), self.result)


if __name__ == '__main__':
    unittest.main()
