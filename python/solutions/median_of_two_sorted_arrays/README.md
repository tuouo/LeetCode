https://leetcode.com/problems/median-of-two-sorted-arrays/#/description

There are two sorted arrays nums1 and nums2 of size m and n respectively.
Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

Example 1:
nums1 = [1, 3]
nums2 = [2]
The median is 2.0

Example 2:
nums1 = [1, 2]
nums2 = [3, 4]
The median is (2 + 3)/2 = 2.5

############################################################

Time O(m+n)     Space O(m+n)
2017.03 	Runtime: 119 ms 
根据长度和的奇偶性需要分类处理。
折半查找时，如果对数组同时折半则排除的数据量与单个数组长度有关。
若对k（the median of the two sorted arrays）折半，则排除的数据量与K有关。故对k折半。

2017.04		Runtime: 102 ms - 185 ms
当对k折半后某一数组剩余可查询长度小于该值，可以特殊处理。

