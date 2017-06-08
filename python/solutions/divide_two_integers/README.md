https://leetcode.com/problems/divide-two-integers

Divide two integers without using multiplication, division and mod operator. 
If it is overflow, return MAX_INT. 

############################################################

由于限制了运算符的使用，如果只使用减法的话，效率会比较低。

可以把除数加上自己，直到刚好比被除数小，同时记录当前相对于原除数的倍数。再用被除数减去。
如果除数过大则更新除数与倍数。该方法有好几个变种（效率类似）。

