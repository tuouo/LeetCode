https://leetcode.com/problems/merge-k-sorted-lists

Merge k sorted linked lists and return it as one sorted list.   

############################################################

1, 合并多个有序的集合，最常见的例子是归并排序中对子序列的合并了。  
可以对这里的每个 sorted linked list 进行归并即可。  

2，每次从当前每个sorted linked list 中取出最小的值，依次连起来也可以。 每次需要最值，我们可以使用堆。  
需要注意的是，当取出队列的最值后，把这个最值所属sorted linked list的下一个值替换进去再调整堆，比堆中删除该元素再新增要少一个  
