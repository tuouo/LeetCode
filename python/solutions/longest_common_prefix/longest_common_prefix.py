#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 2017/5/4
import unittest


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        return Solution.use_zip(strs)

    @staticmethod
    def all_to_end(strs):
        if not strs:
            return ""
        for i in range(len(strs[0])):
            for string in strs:
                if i >= len(string) or strs[0][i] != string[i]:
                    return strs[0][:i]
        return strs[0]

    @staticmethod
    def use_package(strs):
        import os
        return os.path.commonprefix(strs)

    @staticmethod
    def use_zip(strs):
        if not strs:
            return ""
        pos = 0
        for item in zip(*strs):
            if len(set(item)) > 1:
                return strs[0][:pos]
            pos += 1
        return strs[0][:pos]


class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_compare(self):
        self.assertEqual(Solution().longestCommonPrefix(["hello", "heabc", "hell"]), "he")


if __name__ == '__main__':
    unittest.main()
