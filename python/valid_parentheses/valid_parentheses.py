#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 2017/5/21
import unittest


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        return self.stack(s)

    def stack(self, s):
        couple, get = {"(": ")", "{": "}", "[": "]"}, []
        for i in s:
            if i in couple:
                get.append(i)
            else:
                if not get or couple[get.pop()] != i:
                    return False
        return False if get else True

    def couple_info(self, s):
        if (len(s) & 1) == 1:
            return False
        couple, get = {"(": ")", "{": "}", "[": "]"}, []
        for i in s:
            if i in couple:
                get.append(i)
            else:
                if not get or couple[get.pop()] != i:
                    return False
        return False if get else True


class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_check(self):
        self.assertEqual(Solution().isValid("()[]{}"), True)
        self.assertEqual(Solution().isValid("(()[]{}"), False)

if __name__ == '__main__':
    unittest.main()
