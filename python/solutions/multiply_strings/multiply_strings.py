#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 2017/6/29
import unittest


class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        return self.use_dict(num1, num2)

    def use_build_in(self, num1, num2):  # 94.76(49ms,1704)
        return str(int(num1) * int(num2))

    def use_dict(self, num1, num2):  # 75.6(182ms,170629)
        if num1 == "0" or num2 == "0":
            return "0"
        maps = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9}
        length = len(num1) + len(num2)
        temp = [0] * length
        for i, value1 in enumerate(reversed(num1)):
            for j, value2 in enumerate(reversed(num2)):
                temp[i + j] += maps[value1] * maps[value2]
        carry = 0
        for i in range(length):
            carry, temp[i] = divmod(carry + temp[i], 10)
        while i >= 0 and temp[i] == 0:
            i -= 1
        return "".join(map(str, temp[:i+1][::-1]))

    def use_dict_old(self, num1, num2):  # 76.65(168ms,170629)
        if num1 == "0" or num2 == "0":
            return "0"
        maps = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9}
        len_1, len_2, num1, num2 = len(num1), len(num2), num1[::-1], num2[::-1]
        temp = [0] * (len_1 + len_2)
        for i in range(len_1):
            for j in range(len_2):
                temp[i + j] += maps[num1[i]] * maps[num2[j]]
        carry = 0
        for i in range(len_1 + len_2):
            carry, temp[i] = divmod(carry + temp[i], 10)
        while i >= 0 and temp[i] == 0:
            i -= 1
        # maps = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9")
        # return "".join((maps[i] for i in temp[:i+1][::-1]))
        return "".join(map(str, temp[:i+1][::-1]))

    def base(self, num1, num2):
        if num1 == "0" or num2 == "0":
            return "0"
        len_1, len_2, num1, num2 = len(num1), len(num2), num1[::-1], num2[::-1]
        temp = [0] * (len_1 + len_2)
        for i in range(len_1):
            for j in range(len_2):
                temp[i + j] += int(num1[i]) * int(num2[j])
        carry = 0
        for i in range(len_1 + len_2):
            ad = carry + temp[i]
            temp[i], carry = ad % 10, ad // 10
        while i >= 0 and temp[i] == 0:
            i -= 1
        return "".join(map(str, temp[:i+1][::-1]))


class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_join(self):
        self.assertEqual(Solution().multiply("124", "1100"), "136400")

if __name__ == '__main__':
    unittest.main()
