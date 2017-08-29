https://leetcode.com/problems/edit-distance

Given two words word1 and word2, find the minimum number of steps required to convert word1 to word2. (each operation is counted as 1 step.)  

You have the following 3 operations permitted on a word:  

a) Insert a character  
b) Delete a character  
c) Replace a character  
 

############################################################

word1 and word2 可以分解成word1至word2的首字母，再多一个字母，直到word2。
同理word1到一个字母，从首字母逐个进行，一直到word1整个字符串为止。
这是一个动态规划问题。
