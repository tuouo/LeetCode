https://leetcode.com/problems/unique-paths-ii

Follow up for "Unique Paths":  

Now consider if some obstacles are added to the grids. How many unique paths would there be?  

An obstacle and empty space is marked as 1 and 0 respectively in the grid.  

For example,  
There is one obstacle in the middle of a 3x3 grid as illustrated below. 

[  
  [0,0,0],  
  [0,1,0],  
  [0,0,0]  
]  
The total number of unique paths is 2.  

Note: m and n will be at most 100.  

############################################################


对于每一个位置，都可以从左边或者上边过来。第一行与第一列都是只有一种途径抵达。  
可以发现路径的数据关系与杨辉三角很类似。  

发生变化的是有障碍点，则障碍点的路径为0，其余不变。
