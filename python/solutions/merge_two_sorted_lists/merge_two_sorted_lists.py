#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 2017/5/22
import unittest
from python.list_node.list_node import ListNode


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        return self.origin_less_check(l1, l2)

    def with_new(self, l1, l2):
        if not l1 or not l2:
            return l1 or l2
        new = sentry = ListNode(0)
        while l1 and l2:
            if l1.val > l2.val:
                new.next = l2
                l2 = l2.next
            else:
                new.next = l1
                l1 = l1.next
            new = new.next
        new.next = l1 if l1 else l2
        return sentry.next

    def user_origin(self, l1, l2):
        if not l1 or not l2:
            return l1 or l2
        sentry = ListNode(0)
        sentry.next = l1
        while l1 and l2:
            if l1.val > l2.val:
                l1.val, l2.val = l2.val, l1.val
                l1.next, l2.next, l2 = l2, l1.next, l2.next
            if l1.next:
                l1 = l1.next
            else:
                break
        if l2:
            l1.next = l2
        return sentry.next

    def origin_less_check(self, l1, l2):
        if not l1 or not l2:
            return l1 or l2
        sentry = l1
        while l2:
            if l1.val > l2.val:
                l1.val, l2.val = l2.val, l1.val
                l1.next, l2.next, l1, l2 = l2, l1.next, l2, l2.next
            else:
                if l1.next:
                    l1 = l1.next
                else:
                    break
        if l2:
            l1.next = l2
        return sentry


class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_join(self):
        root1 = ListNode(1)
        root2 = ListNode(0, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
        self.assertEqual(str(Solution().mergeTwoLists(root1, root2)), "0 -> 1 -> 2 -> 3 -> 4 -> 5")

if __name__ == '__main__':
    unittest.main()
