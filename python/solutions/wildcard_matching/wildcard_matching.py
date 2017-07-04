#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 2017/7/4
import unittest


class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        pos_s, pos_p, mark_s, mark_p, len_s, len_p = 0, 0, -1, -1, len(s), len(p)
        while pos_s < len_s:
            if pos_p < len_p and (s[pos_s] == p[pos_p] or p[pos_p] == "?"):
                # normal match including "?
                pos_s, pos_p = pos_s + 1, pos_p + 1
            elif pos_p < len_p and p[pos_p] == "*":
                # when "*", may empty sequence
                mark_s, mark_p, pos_p = pos_s, pos_p + 1, pos_p + 1
            elif mark_p != -1:
                # when not match, and "*" appeared. "*" match number ++
                mark_s, pos_s, pos_p = mark_s + 1, mark_s + 1, mark_p
            else:
                return False

        while pos_p < len_p and p[pos_p] == "*":
            pos_p += 1
        return pos_p == len_p


class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_match(self):
        self.assertEqual(Solution().isMatch("asddfgh", "a*d?gh"), True)


if __name__ == '__main__':
    unittest.main()
