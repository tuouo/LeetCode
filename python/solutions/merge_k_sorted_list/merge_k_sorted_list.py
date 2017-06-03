#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 2017/6/1
import unittest
from python.list_node.list_node import ListNode


class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        # return self.mergeKListerHelper(lists, 0, len(lists)-1)
        return self.with_heap_replace(lists)

    def with_heap_replace(self, lists):
        if not lists:
            return None
        import heapq
        heap_min = [(item.val, item) for item in lists if item]
        heapq.heapify(heap_min)
        cur = sentry = ListNode(0)

        while heap_min:
            v, item = heap_min[0]
            if item.next:
                heapq.heapreplace(heap_min, (item.next.val, item.next))
            else:
                heapq.heappop(heap_min)
            cur.next = item
            cur = cur.next

        return sentry.next

    def with_heap(self, lists):
        if not lists:
            return None
        import heapq
        heap_min = [(item.val, item) for item in lists if item]
        heapq.heapify(heap_min)
        cur = sentry = ListNode(0)

        while heap_min:
            cur.next = heapq.heappop(heap_min)[1]
            cur = cur.next
            if cur.next:
                heapq.heappush(heap_min, (cur.next.val, cur.next))

        return sentry.next


    def mergeTwoLists(self, l1, l2):
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

    def mergeKListerHelper(self, lists, start, end):
        if start > end:
            return None
        elif start == end:
            return lists[start]
        return self.mergeTwoLists(self.mergeKListerHelper(lists, start, (start + end) // 2),
                                  self.mergeKListerHelper(lists, (start + end) // 2 + 1, end))


class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_join(self):
        root1 = ListNode(1)
        root2 = ListNode(0, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
        root3 = ListNode(1, ListNode(2, ListNode(2, ListNode(4, ListNode(5)))))
        result = "0 -> 1 -> 1 -> 2 -> 2 -> 2 -> 3 -> 4 -> 4 -> 5 -> 5"
        self.assertEqual(str(Solution().mergeKLists([root1, root2, root3])), result)

if __name__ == '__main__':
    unittest.main()
