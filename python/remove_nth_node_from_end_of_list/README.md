https://leetcode.com/problems/remove-nth-node-from-end-of-list

Given a linked list, remove the nth node from the end of list and return its head.
For example,
   Given linked list: 1->2->3->4->5, and n = 2.
   After removing the second node from the end, the linked list becomes 1->2->3->5.

Note:
Given n will always be valid.
Try to do this in one pass. 

############################################################

由于单项链表访问只能从前到后，而题目要求只访问一边，所以访问时一定带有与n相关的信息。
换句话说，就是要借助这个信息，在倒数第n个位置结束访问。
只要能用的信息有从前往后访问x个。最后一个节点可以识别链表结束以及识别列表开头。
好吧，这里需要想到用两个指针来访问（还是不知道如何显式的到这一步）。

所以一个指针先行n步后，另一个指针再一直同步往后。当先行指针到末尾时后指针即指向倒数第n位。