https://leetcode.com/problems/spiral-matrix-ii

Given an integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.  

For example,  
Given n = 3,  

You should return the following matrix:  
[  
 [ 1, 2, 3 ],  
 [ 8, 9, 4 ],  
 [ 7, 6, 5 ]  
]  
############################################################

一般来说，我们按照顺序将数字放入正确的位置即可。  

或者我们将数据想象成绕线团的方式。每次王当前数据上加上线团长度的数据，再转动线团。直到没有数据需要再加为止。  
