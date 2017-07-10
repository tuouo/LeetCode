#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 2017/6/4
import unittest
from python.list_node.list_node import ListNode


class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        return self.by_store(head)

    def use_next(self, head):
        if not head or not head.next:
            return head
        cur = sentry = ListNode(0)
        cur.next = head
        while cur.next and cur.next.next:
            node1, node2 = cur.next, cur.next.next
            cur.next, node2.next, node1.next = node2, node1, node2.next
            cur = cur.next.next
        return sentry.next

    def by_store(self, head):
        if not head or not head.next:
            return head
        cur = sentry = ListNode(0)
        cur.next = head
        node1, node2 = cur.next, cur.next.next
        while node2:
            cur.next, node2.next, node1.next = node2, node1, node2.next
            cur = cur.next.next
            if cur.next:
                node1 = cur.next
            else:
                break
            node2 = node1.next
        return sentry.next


class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_join(self):
        root = ListNode(0, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
        result = "2 -> 0 -> 4 -> 3 -> 5"
        self.assertEqual(str(Solution().swapPairs(root)), result)

if __name__ == '__main__':
    unittest.main()
