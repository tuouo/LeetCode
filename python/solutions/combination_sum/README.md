https://leetcode.com/problems/combination-sum

Given a set of candidate numbers (C) (without duplicates) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.  
The same repeated number may be chosen from C unlimited number of times.  

Note:  
&emsp;&emsp;All numbers (including target) will be positive integers.  
&emsp;&emsp;The solution set must not contain duplicate combinations.  
For example, given candidate set [2, 3, 6, 7] and target 7,   
A solution set is:   
[
  [7],
  [2, 2, 3]
]

############################################################

如果不想遍历整个 set of candidate numbers，  
通过先行排序之后，可以不跳过比最后一个比较的数大的（或小的）的数。 

遍历set of candidate numbers，  
如果要找的数为小于当前遍历的数，结束本次查找。  
否则要找的数更新为要找的数减去当前遍历的数。保证下一次减去的数不小于这次减去的数。  
保证下一次减去的数不小于这次减去的数，可以有两种处理。  

  
提速点：  
不使用默认参数  
对target进行预处理  
存储要比较的数据  


