https://leetcode.com/problems/maximum-subarray

Find the contiguous subarray within an array (containing at least one number) which has the largest sum.  

For example, given the array [-2,1,-3,4,-1,2,1,-5,4],  
the contiguous subarray [4,-1,2,1] has the largest sum = 6.  

############################################################

需要的是连续子序列中最大的和。如果全是非负数，所求的就是全体的和了。
对于有负数的情况，在当前序列新增新元素时，若当前的和是负数，则舍弃，新的子序列从后一位开始，否则当前子序列变长（包括下一位）。对于每个新的子序列的和，与最大值比较更新即可。

