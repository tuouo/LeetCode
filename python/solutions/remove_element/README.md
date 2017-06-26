https://leetcode.com/problems/remove-element

Given an array and a value, remove all instances of that value in place and return the new length.   
Do not allocate extra space for another array, you must do this in place with constant memory.  
The order of elements can be changed. It doesn't matter what you leave beyond the new length.  
Example:  
Given input array nums = [3,2,2,3], val = 3   
Your function should return length = 2, with the first two elements of nums being 2.  

############################################################

删除给定数组中的指定元素，需要记录有多少个元素剩下。  
如果直接删除指定元素，效率不高。可以通过在后面找到一个保留的元素替换当前需要删除的元素即可。  
（可以先把后面的元素先替换过来在检查，也可以先找到一个再替换。这取决与指定元素出现的概率高低）  
