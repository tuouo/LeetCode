https://leetcode.com/problems/combination-sum-ii

Given a set of candidate numbers (C) (without duplicates) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.    
Each number in C may only be used once in the combination.    

Note:  
&emsp;&emsp;All numbers (including target) will be positive integers.  
&emsp;&emsp;The solution set must not contain duplicate combinations.  
For example, given candidate set [10, 1, 2, 7, 6, 1, 5] and target 8,   
A solution set is: 
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]

############################################################

在combination-sum基础上，确保相同的数只开头一次即可。
（如果在找到一个结果是再看看是否重复，天生慢了一步。）


