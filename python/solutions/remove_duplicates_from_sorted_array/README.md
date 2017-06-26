https://leetcode.com/problems/remove-duplicates-from-sorted-array

Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.
Do not allocate extra space for another array, you must do this in place with constant memory.   
For example,  
Given input array nums = [1,1,2],   
Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively. It doesn't matter what you leave beyond the new length.   

############################################################

给定的排好序的数组中含有重复项，要求的数组没有重复项。  
直接把后一个不重复的数（与当前处理好的数的最后一位不同）放到当前处理好的数的后一位即可。  
