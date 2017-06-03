#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 2017/5/18
import unittest


class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        return self.join_later(digits)

    def append_direct(self, digits):
        from functools import reduce
        if not digits:
            return []
        kvmaps = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        return reduce(lambda pre, digit: [item + letter for item in pre for letter in kvmaps[digit]], digits, [""])

    def join_later(self, digits):
        from functools import reduce
        if not digits:
            return []
        kvmaps = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        return list(map(lambda a: "".join(a),
                        reduce(lambda pre, digit: [item + [letter] for item in pre for letter in kvmaps[digit]],
                               digits, [[]])))

class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_combnation(self):
        self.assertEqual(Solution().letterCombinations("23"), ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf'])


if __name__ == '__main__':
    unittest.main()
