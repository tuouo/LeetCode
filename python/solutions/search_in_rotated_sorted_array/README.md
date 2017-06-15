https://leetcode.com/problems/search-in-rotated-sorted-array

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
You are given a target value to search. If found in the array return its index, otherwise return -1.
You may assume no duplicate exists in the array.

############################################################

一般查询时二分查询能具有较好的性能。
在这里数组大致是上升的，除了一个跳跃的地方（下称跳跃位）。
当我们二分查找时，跳跃位在中点的一边，另一边依旧是上升的，上升区域依旧可以正常比较，所以二分法查找可行。

特别的，可以异或将判断条件合并。