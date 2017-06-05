#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 2017/6/5
import unittest
from python.list_node.list_node import ListNode


class Solution(object):

    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or k <= 1:
            return head

        cur = sentry = ListNode(0)
        cur.next = head
        while cur:
            cur = self.reverseK(cur, k)
        return sentry.next

    def reverseK(self, node, num):
        check = node
        for i in range(num):
            if check.next:
                check = check.next
            else:
                return None
        check = check.next
        tail, cur, move = node.next, node, node.next
        for i in range(num):
            left = move.next
            move.next = cur
            cur = move
            move = left
        node.next, tail.next = cur, check
        return tail

    def reverseKGroup_store(self, head, k):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if k == 1:
            return head

        def get_next_k(cur, k, tmp):
            for i in range(k):
                if cur.next:
                    tmp[i] = cur.next
                else:
                    return None, None
                cur = cur.next
            return cur, tmp

        cur = sentry = ListNode(0)
        cur.next, tmp = head, [[] for _ in range(k)]
        while cur.next:
            new, tmp = get_next_k(cur, k, tmp)
            if new:
                left = new.next
                for i in range(k - 1, -1, -1):
                    cur.next = tmp[i]
                    cur = cur.next
                cur.next = left
            else:
                return sentry.next
        return sentry.next


class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testReverse(self):
        root = ListNode(0, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
        result = "2 -> 0 -> 4 -> 3 -> 5"
        self.assertEqual(str(Solution().reverseKGroup(root, 2)), result)

if __name__ == '__main__':
    unittest.main()
