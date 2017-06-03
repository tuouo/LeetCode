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


if __name__ == '__main__':
    a = ListNode(0)
    a.next = ListNode(1)
    b = ListNode(0)
    b.next = ListNode(0)
    print(a)
    print(a == b)
