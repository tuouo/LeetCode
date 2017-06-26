https://leetcode.com/problems/roman-to-integer

Given a roman numeral, convert it to an integer.  
Input is guaranteed to be within the range from 1 to 3999.  

############################################################

不同的罗马数字对应不同的符号  

A. 对于每个字母，如果比后一个出现的字母小则减去，否则加上  

B. 对于每个字母，借助匿名函数与当前位置，计算实际需要的值（原值或负值）  

C. 对于每个字母，先加起来，再根据对应情况减去。减去时可以根据出现特性在优化一下  
