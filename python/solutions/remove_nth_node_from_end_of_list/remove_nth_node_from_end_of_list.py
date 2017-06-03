#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 2017/5/20
import unittest
from python.list_node.list_node import ListNode


class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        first = second = sentry = ListNode(0)
        sentry.next = head
        while n:
            second = second.next
            n -= 1
        while second and second.next:
            first, second = first.next, second.next

        first.next = first.next.next
        return sentry.next


class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_haha(self):
        root = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
        self.assertEqual(str(Solution().removeNthFromEnd(root, 5)), "2 -> 3 -> 4 -> 5")

if __name__ == '__main__':
    unittest.main()
