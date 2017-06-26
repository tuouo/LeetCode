https://leetcode.com/problems/count-and-say

The count-and-say sequence is the sequence of integers with the first five terms as following:  
1.&emsp;&emsp;1  
2.&emsp;&emsp;11  
3.&emsp;&emsp;21  
4.&emsp;&emsp;1211  
5.&emsp;&emsp;111221  
1 is read off as "one 1" or 11.  
11 is read off as "two 1s" or 21.  
21 is read off as "one 2, then one 1" or 1211.  
Given an integer n, generate the nth term of the count-and-say sequence.  

Note: Each term of the sequence of integers will be represented as a string.  

Example 1:  Input: 1    Output: "1"  
Example 2:  Input: 4    Output: "1211"  

############################################################

如果不想直接数数字，groupby 和 正则表达式是个不错的选择。  

[pythonchallenge 的 level 10](
http://www.pythonchallenge.com/pc/return/sequence.txt)就是这题的前辈。  
