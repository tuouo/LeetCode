https://leetcode.com/problems/search-for-a-range

Given an array of integers sorted in ascending order, find the starting and ending position of a given target value.
Your algorithm's runtime complexity must be in the order of O(log n).
If the target is not found in the array, return [-1, -1].

For example,
Given [5, 7, 7, 8, 8, 10] and target value 8,
return [3, 4].

############################################################

需要找到升序数组中某个元素开始和结束的位置.
可以在二分查找时直接查找最左边的元素,再在后方查找最右边的元素即可.