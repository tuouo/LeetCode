#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 2017/6/7
import unittest


class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        return self.sunday(haystack, needle)

    def generate_offset(self, pattern):
        from collections import defaultdict
        len_par = len(pattern)
        skip = defaultdict(lambda: len_par)
        for i in range(len_par):
            skip[pattern[i]] = len_par - 1 - i
        return skip

    def sunday(self, text, pattern):
        len_text, len_par = len(text), len(pattern)
        if len_par > len_text:
            return -1
        skip = self.generate_offset(pattern)
        pos = 0
        while pos < len_text - len_par + 1:
            off = 0
            while off < len_par and text[pos + off] == pattern[off]:
                off += 1
            if off == len_par:
                return pos
            pos += skip[text[pos + len_par]] + 1 if pos + len_par < len_text and text[pos + len_par] in skip \
                else len_par + 1
        return -1

    def by_find(self, haystack, needle):
        return haystack.find(needle)


class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_find(self):
        self.assertEqual((Solution().strStr("abcdefg", "fg")), 5)


if __name__ == '__main__':
    unittest.main()
