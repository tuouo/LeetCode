https://leetcode.com/problems/insert-interval

Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).  

You may assume that the intervals were initially sorted according to their start times.  

Example 1:  
Given intervals [1,3],[6,9], insert and merge [2,5] in as [1,5],[6,9].  

Example 2:  
Given [1,2],[3,5],[6,7],[8,10],[12,16], insert and merge [4,9] in as [1,2],[3,10],[12,16].  

This is because the new interval [4,9] overlaps with [3,5],[6,7],[8,10].  


############################################################

恰当的把新的区间原有区间合并即可。  

找到 距该区间左边最近的最右边， 在距该区间右边最近的最左边

本题目的测试数据或运行环境可能会导致重大偏差。
