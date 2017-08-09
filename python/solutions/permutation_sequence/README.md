https://leetcode.com/problems/permutation-sequence  

The set [1,2,3,…,n] contains a total of n! unique permutations.  

By listing and labeling all of the permutations in order,  
We get the following sequence (ie, for n = 3):  

1. "123"
2. "132"
3. "213"
4. "231"
5. "312"
6. "321"

Given n and k, return the kth permutation sequence.    

Note: Given n will be between 1 and 9 inclusive.  

############################################################
					   
在n个数组成n！个组合时，如果某个k大于n！，意味着需要增大n。  
n增大1变为n+1，则组成的组合增加n！个。又因为新增的位置可以放置任意数（1到n+1），则通过k与组合数量的关系，可以确定
新增位置的数的值。
