https://leetcode.com/problems/merge-intervals

Given a collection of intervals, merge all overlapping intervals.  

For example,  
Given [1,3],[2,6],[8,10],[15,18],  
return [1,6],[8,10],[15,18].    

############################################################

需要考虑intervals不一定是有序的。  
可以直接按区间从小到大逐个合并。  

也可以考虑一次性合并与当前区间重叠的其他区间。