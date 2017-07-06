https://leetcode.com/problems/permutations

Given a collection of distinct numbers, return all possible permutations.  

For example,  
[1,2,3] have the following permutations: 
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]


############################################################
					   
给出所有的组合情况。  
库中itertools下有 permutations这个实现，效率不是很好。  

递归使用中，可以在遍历的时候生成除使用过的元素外的新数组参与下一次递归。如果使用标记数组表示是否使用过效果不好。生成器也可以使用在递归中。    
也可以通过储存中间结果来避免递归。  