https://leetcode.com/problems/merge-two-sorted-lists

Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

############################################################

由于是对两个排序的列表操作，所以只需要从头比较，将较小的先添加即可。

我们可以使用一个新链表，逐个加入小的节点。

如果不使用辅助数组，直接在某个传入的sorted linked list操作，则当另一个列表中的数据较小时需要特殊处理。
或者把当前另一个列表的较小数据换到当前位置就不用辅助指针。

主要可以对空列表优先处理
