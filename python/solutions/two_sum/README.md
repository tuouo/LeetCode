https://leetcode.com/problems/two-sum

Given an array of integers, return indices of the two numbers such that they add up to a specific target.  
You may assume that each input would have exactly one solution, and you may not use the same element twice.  

Example:  
Given nums = [2, 7, 11, 15], target = 9,  
Because nums[0] + nums[1] = 2 + 7 = 9,  
return [0, 1].  

############################################################

A. 直接实现法   
Time O(n^2)     Space O(n)  
Runtime: 622 ms 2017.03  
对数组进行遍历，每个数进行新一轮遍历，当两者之和与目标同时视为找到。  

B. 反向标记法  
Time O(n)     Space O(n)  
Runtime: 342 ms 2017.03  
对数组进行遍历，对每个数，保存目标与其的差做为遍历结果字典的键，下标为值。  
则当某个数在遍历结果字典中，则表示前面出现了一个数与其的和为目标。  
