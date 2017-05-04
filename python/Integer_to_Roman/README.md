https://leetcode.com/problems/integer-to-roman/#/description

Given an integer, convert it to a roman numeral. 
Input is guaranteed to be within the range from 1 to 3999 

############################################################

不同的罗马数字对应不同的符号，将原数分别从大到小减去对应罗马数字再串联即可。
由于有些小的数（对应罗马数）会出现在大的数前面（“IV”），则将这些情况视为一个独立情况。


由于上述方案中已经存在与转化范围相关的预处理数组，则可以将所有情况都预处理。
