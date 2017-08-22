#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 2017/8/22
import unittest


class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        # return "{:b}".format(int(a, 2) + int(b, 2)) 66ms 18.19
        return bin(int(a, 2) + int(b, 2))[2:]  # 42ms 82.49


class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_solution(self):
        self.assertEqual(Solution().addBinary("1101", "111"), "10100")


if __name__ == '__main__':
    unittest.main()
