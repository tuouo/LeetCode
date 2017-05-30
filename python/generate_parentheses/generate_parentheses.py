#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 2017/5/24
import unittest


class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int. how many parenthesis can still be opened
        :type open: int. how many parenthesis are opened
        :rtype: List[str]
        """
        return self.gen_recursion(n, 0)

    def gen_recursion(self, n, num=0):
        if n == 0:
            return [')' * num]
        if num == 0:
            return ['('+x for x in self.gen_recursion(n-1, 1)]
        else:
            return [')' + x for x in self.gen_recursion(n, num - 1)] + \
                   ['(' + x for x in self.gen_recursion(n - 1, num + 1)]


class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_gen(self):
        print("['((()))', '(()())', '(())()', '()(())', '()()()']")
        print(str(Solution().generateParenthesis(3)))


if __name__ == '__main__':
    unittest.main()
