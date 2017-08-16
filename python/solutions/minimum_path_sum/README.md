https://leetcode.com/problems/minimum-path-sum

Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.  

Note: You can only move either down or right at any point in time.  

############################################################


对于每一个位置，都可以从左边或者上边过来。第一行与第一列都是只有一种途径抵达。  
这意味着左边或上边比较小的路径就是构成当前最小路径的那部分。  

建议最好不要改动传进来的数组。  
