https://leetcode.com/problems/3sum

Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

############################################################

A. 首先将数组排序。从头遍历数组，对于每一个不大于0的元素，将其之后剩余的数据的首尾相视为第二与第三个元素，并将第二与第三个和视为“查找数”。  
根据“查找数”正负变更第二与第三个元素。同时注意跳过相同的元素（根据测试，有些时候不用处理，视数据而定）。  

B. 首先将数组排序。从头遍历数组，对于每一个不大于0的元素，遍历其后的数。  
将他们与0的差存入字典，如果已经存在视为找到。需要注意去重。  
