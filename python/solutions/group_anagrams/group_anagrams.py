#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 2017/7/11
import unittest

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        return self.use_default(strs)

    def use_default(self, strs):  # 64.74(232ms, 1705)
        from collections import defaultdict
        items = defaultdict(list)
        for item in strs:
            items["".join(sorted(item))].append(item)
        return [value for key, value in items.items()]

    def use_dict(self, strs):  # 62.59(235ms, 1705)
        items = {}
        for item in strs:
            same = "".join(sorted(item))
            if same not in items:
                items[same] = [item]
            else:
                items[same].append(item)
        return [value for key, value in items.items()]

    def hash_default(self, strs):  # 26.96(278ms, 1705)
        from collections import defaultdict
        change = {"a": 2, "b": 3, "c": 5, "d": 7, "e": 11, "f": 13, "g": 17, "h": 19, "i": 23, "j": 29, "k": 31,
                  "l": 37, "m": 41, "n": 43, "o": 47, "p": 53, "q": 59, "r": 61, "s": 67, "t": 71, "u": 73, "v": 79,
                  "w": 83, "x": 89, "y": 97, "z": 101}

        items = defaultdict(list)
        for item in strs:
            hash_num = 1
            for i in item:
                hash_num *= change[i]
            items[hash_num].append(item)
        return [value for key, value in items.items()]

    def hash_dict(self, strs):  # 64.74(232ms, 1705)
        change = {"a": 2, "b": 3, "c": 5, "d": 7, "e": 11, "f": 13, "g": 17, "h": 19, "i": 23, "j": 29, "k": 31,
                  "l": 37, "m": 41, "n": 43, "o": 47, "p": 53, "q": 59, "r": 61, "s": 67, "t": 71, "u": 73, "v": 79,
                  "w": 83, "x": 89, "y": 97, "z": 101}
        items, result = {}, []
        for item in strs:
            hash_num = 1
            for i in item:
                hash_num *= change[i]
            if hash_num not in items:
                items[hash_num] = [item]
            else:
                items[hash_num].append(item)
        return [value for key, value in items.items()]

    def frequency_dict(self, strs):  # 90.95(212ms, 170711)
        change = {"e": 2, "t": 3, "a": 5, "o": 7, "i": 11, "n": 13, "s": 17, "h": 19, "r": 23, "d": 29, "l": 31,
                  "c": 37, "u": 41, "m": 43, "w": 47, "f": 53, "g": 59, "y": 61, "p": 67, "b": 71, "v": 73, "k": 79,
                  "j": 83, "x": 89, "q": 97, "z": 101}
        items, hash_num = {}, 1
        for item in strs:
            hash_num = 1
            for i in item:
                hash_num *= change[i]
            if hash_num not in items:
                items[hash_num] = [item]
            else:
                items[hash_num].append(item)
        return [value for key, value in items.items()]

    def frequency_default(self, strs):  # 90.95(212ms, 170711)
        from collections import defaultdict
        change = {"e": 2, "t": 3, "a": 5, "o": 7, "i": 11, "n": 13, "s": 17, "h": 19, "r": 23, "d": 29, "l": 31,
                  "c": 37, "u": 41, "m": 43, "w": 47, "f": 53, "g": 59, "y": 61, "p": 67, "b": 71, "v": 73, "k": 79,
                  "j": 83, "x": 89, "q": 97, "z": 101}
        items, hash_num = defaultdict(list), 1
        for item in strs:
            hash_num = 1
            for i in item:
                hash_num *= change[i]
            items[hash_num].append(item)
        return [value for key, value in items.items()]

    def normal(self, strs):  # 51.49(245ms, 1705)
        items = {}
        for item in strs:
            same = "".join(sorted(item))
            if same not in items:
                items[same] = [item]
            else:
                items[same].append(item)
        result = []
        for value in items.values():
            result += [value]
        return result


class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
