https://leetcode.com/problems/first-missing-positive

Given an unsorted integer array, find the first missing positive integer.  

For example,  
Given [1,2,0] return 3,  
and [3,4,-1,1] return 2.  

Your algorithm should run in O(n) time and uses constant space.  

############################################################

要求在线性时间完成，要么在一次遍历中直接找到，要么先构造合适的数据结构再遍历得到结果。  
此处是找到首个缺失的正数，那么可能在一个序列里，其余的数都是对应的，知道一个缺失的数。  
比如，将所有的数都放在与角标对应的位置。（第0位放0可能更加便利。）  
