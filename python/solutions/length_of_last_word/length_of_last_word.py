#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 2017/7/29
import unittest


class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        return self.with_build_in(s)

    def with_build_in(self, s):  # 84.46(32ms,170729)
        length = 0
        for n in reversed(s):
            if n.isspace():
                if length:
                    break
            else:
                length += 1
        return length

    def use_build_in(self, s):  # 29.02（45ms,170729)
        return len(s.rstrip(" ").split(" ")[-1])

    def just_find(self, s):  # 12.08（52ms,170729)
        pos = len(s) - 1
        while pos >= 0 and s[pos] == " ":
            pos -= 1
        pos_end = pos
        while pos >= 0 and s[pos] != " ":
            pos -= 1
        return pos_end - pos


class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_length(self):
        self.assertEqual(Solution().lengthOfLastWord("Hello World "), 5)


if __name__ == '__main__':
    unittest.main()
