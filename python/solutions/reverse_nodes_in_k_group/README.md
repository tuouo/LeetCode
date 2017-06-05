https://leetcode.com/problems/reverse-nodes-in-k-group

Given a linked list, reverse the nodes of a linked list k at a time and return its modified list. 
k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.
You may not alter the values in the nodes, only nodes itself may be changed.
Only constant memory is allowed.
For example,
Given this linked list: 1->2->3->4->5 
For k = 2, you should return: 2->1->4->3->5 
For k = 3, you should return: 3->2->1->4->5 

############################################################

将每k个元素先存储起来，再倒序访问，这个方案似乎没那么好。

对与每k个元素，逐个通过修改链接的方式实现倒序。再与前后连起来即可。
