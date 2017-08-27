#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 2017/8/27
import unittest


class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stack = []
        for item in path.split("/"):
            if item == "..":
                if stack:
                    stack.pop()
            elif item != "." and item:
                stack.append(item)
        return "/" + "/".join(stack)

    def simplifyPath2(self, path):  # 67.63(42ms)
        stack = []
        for item in (p for p in path.split("/") if p != "." and p != ""):
            if item == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(item)
        return "/" + "/".join(stack)


class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_solution(self):
        self.assertEqual(Solution().simplifyPath("/a/./b/../../c/"), "/c")
        self.assertEqual(Solution().simplifyPath("/../../"), "/")


if __name__ == '__main__':
    unittest.main()
