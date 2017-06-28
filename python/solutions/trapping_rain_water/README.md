https://leetcode.com/problems/trapping-rain-water

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.  

For example,   
Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.  

############################################################

峰与峰之间才可以蓄水，在高峰之间的矮峰会被淹没。

找到所有的峰（起始点也算峰）。从最高峰往左右两边找到剩下的最高峰，即可统计之间能畜的水量。
需要注意有些坡是高于峰的。