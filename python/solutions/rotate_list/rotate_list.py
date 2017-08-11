#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 2017/8/11
import unittest
from python.list_node.list_node import ListNode


class Solution(object):
    def rotate_right(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or k == 0:
            return head
        count = 1
        left = right = head
        while count <= k:
            right_next = right.next
            if right_next:
                count, right = count + 1, right_next
            else:
                k %= count
                if k == 0:
                    return head
                count, right = 1, head
        right_next = right.next
        while right_next:
            left, right, right_next = left.next, right.next, right_next.next
        sentry = left.next
        left.next, right.next = None, head
        return sentry

    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if k == 0 or not head:
            return head
        count = 1
        left = right = head
        while right.next and count <= k:
            count, right = count + 1, right.next
        if count <= k:
            return self.rotateRight(head, k % count)
        while right.next:
            left, right = left.next, right.next
        sentry = left.next
        left.next, right.next = None, head
        return sentry


class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_join(self):
        root1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
        root2 = ListNode(4, ListNode(5, ListNode(1, ListNode(2, ListNode(3)))))
        self.assertEqual(Solution().rotate_right(root1, 2), root2)


if __name__ == '__main__':
    unittest.main()
