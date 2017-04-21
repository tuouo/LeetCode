#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 2017/4/19
import unittest
from python.list_node.list_node import ListNode


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        return Solution.add_two_numbers_2(l1, l2)

    @staticmethod
    def add_two_numbers_1(l1, l2):
        carry = 0
        result = pre = ListNode(0)
        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            pre.next = ListNode(carry % 10)
            carry //= 10
            pre = pre.next
        return result.next

    @staticmethod
    def add_two_numbers_2(l1, l2):
        if not l1:
            l1, l2 = l2, l1
        carry, l1.val = divmod(l1.val + l2.val, 10)
        sentry = l1
        while l1.next and l2.next:
            l1, l2 = l1.next, l2.next
            carry, l1.val = divmod(carry + l1.val + l2.val, 10)
        if l2.next:
            l1.next = l2.next
        while l1.next and carry:
            l1 = l1.next
            carry, l1.val = divmod(carry + l1.val, 10)
        if carry:
            l1.next = ListNode(1)
        return sentry


class TestCase(unittest.TestCase):
    def setUp(self):
        self.list_1 = ListNode(9)
        self.list_1.next = ListNode(8)
        self.list_2 = ListNode(3)
        self.result = ListNode(2)
        self.result.next = ListNode(9)
        self.s = Solution()

    def tearDown(self):
        del self.list_1
        del self.list_2

    def test_solution(self):
        self.assertEqual(Solution.add_two_numbers_1(self.list_1, self.list_2) == self.result, True)
        self.assertEqual(Solution.add_two_numbers_2(self.list_1, self.list_2) == self.result, True)
        # self.list_1 have been changed
        self.assertEqual(self.s.addTwoNumbers(self.list_1, self.list_2) == self.result, False)


if __name__ == '__main__':
    unittest.main()

