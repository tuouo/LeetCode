https://leetcode.com/problems/search-insert-position

Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
You may assume no duplicates in the array.
Here are few examples.
[1,3,5,6], 5 → 2
[1,3,5,6], 2 → 1
[1,3,5,6], 7 → 4
[1,3,5,6], 0 → 0

############################################################

直接使用二分查找（使用对于相同的元素返回最左边位置的查找方式）。
但是从结果来看，时间并不理想。对target不在数组范围内的情况进行优化后，提速明显。

还可以使用bisect