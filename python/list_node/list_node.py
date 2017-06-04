#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 2017/4/19


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x, next_node=None):
        self.val = x
        self.next = next_node

    def __str__(self):
        result = []
        if self:
            result.append(str(self.val))
        while self.next:
            self = self.next
            result.append(" -> {}".format(self.val))
        return "".join(result)

    __repr__ = __str__

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            raise TypeError("Type error: self:{} -- other:{}".format(self.__class__, type(other)))
        if self.val != other.val:
            return False
        while self.next:
            if not other.next:
                return False
            self, other = self.next, other.next
            if self.val != other.val:
                return False
        if other.next:
            return False
        return self.val == other.val

    def __ne__(self, other):
        """Define a non-equality test"""
        return not self.__eq__(other)

    def __lt__(self, other):
        return self.val < other.val

    def __gt__(self, other):
        return self.val > other.val

    def __le__(self, other):
        return self.val <= other.val

    def __ge__(self, other):
        return self.val >= other.val


class ListNodeDouble(object):
    def __init__(self, key, val, next_node=None, pre_node=None):
        self.key = key
        self.val = val
        self.next = next_node
        self.pre = pre_node


class LinkedListDouble(object):
    def __init__(self):
        self.head = self.tail = None

    def insert(self, node):
        if self.head is None:
            self.head = self.tail = node
        else:
            self.head.pre, node.next = node, self.head
            self.head = node

    def delete(self, node):
        if node.pre:
            node.pre.next = node.next
        else:
            self.head = node.next
        if node.next:
            node.next.pre = node.pre
        else:
            self.tail = node.pre
        del node

    def short(self):
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.tail = self.tail.pre
            del self.tail.next
            self.tail.next = None

    def top(self, node, val=None):
        if self.head != node:
            if self.tail == node:
                self.tail = node.pre
                self.head.pre, node.next, node.pre, self.tail.next = node, self.head, None, None
                self.head = node
            else:
                node.pre.next, node.next.pre = node.next, node.pre
                self.head.pre, node.next, node.pre = node, self.head, None
                self.head = node
        if val:
            node.val = val


class LRUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.dict = {}
        self.list = LinkedListDouble()

    def _insert(self, key, val):
        node = ListNodeDouble(key, val)
        self.list.insert(node)
        self.dict[key] = node

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.dict:
            return -1
        node = self.dict[key]
        self.list.top(node)
        return node.val

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.dict:
            node = self.dict[key]
            self.list.top(node, value)
        else:
            if len(self.dict) == self.capacity:
                del self.dict[self.list.tail.key]
                self.list.short()
            self.list.insert(ListNodeDouble(key, value))
            self.dict[key] = self.list.head


if __name__ == '__main__':
    a = ListNode(0)
    a.next = ListNode(1)
    b = ListNode(0)
    b.next = ListNode(0)
    print(a)
    print(a == b)
    root = ListNode(1, ListNode(2, ListNode(2, ListNode(4, ListNode(5)))))
    print(root)

