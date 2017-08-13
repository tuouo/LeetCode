https://leetcode.com/problems/unique-paths

A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).  
The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).  
How many possible unique paths are there?  

############################################################


对于每一个位置，都可以从左边或者上边过来。第一行与第一列都是只有一种途径抵达。  
可以发现路径的数据关系与杨辉三角很类似。  

对于python，我们需要找到一种快速计算组合值的方式。  
