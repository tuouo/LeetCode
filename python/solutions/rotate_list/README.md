https://leetcode.com/problems/rotate-list

Given a list, rotate the list to the right by k places, where k is non-negative.  

For example:  
Given 1->2->3->4->5->NULL and k = 2,  
return 4->5->1->2->3->NULL.Given a list, rotate the list to the right by k places, where k is non-negative.  

For example:  
Given 1->2->3->4->5->NULL and k = 2,  
return 4->5->1->2->3->NULL.  

############################################################

把后面的k个元素移到前面来，就需要知道倒数第k个元素。  
关于数数，我们可以从1数到k也可以从k数到1，同时不同的是数的方向的问题。  
同样的，从右往左数到k，也可以从所往右数到长度减k。

需要注意的是k只是表示式非负的。
