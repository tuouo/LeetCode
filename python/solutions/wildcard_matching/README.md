https://leetcode.com/problems/wildcard-matching  

Implement wildcard pattern matching with support for '?' and '*'.   
'?' Matches any single character.  
'*' Matches any sequence of characters (including the empty sequence).  

The matching should cover the entire input string (not partial).  

The function prototype should be:  
bool isMatch(const char *s, const char *p)  

Some examples:  
isMatch("aa","a") → false  
isMatch("aa","aa") → true  
isMatch("aaa","aa") → false  
isMatch("aa", "*") → true  
isMatch("aa", "a*") → true  
isMatch("ab", "?*") → true  
isMatch("aab", "c*a*b") → false  

############################################################

人工实现来模拟思路。  
对于一个新的‘p’匹配‘s’，如果相等或者‘p’为'?'，则当前对应位置匹配。同时往后继续直到p或s一方抵达末尾。  
如果上述不匹配，当‘p’是'*'，首先视为匹配了一个空字符。并同时记下标记p和s的下一位为尝试匹配位。  
当都不匹配时，如果p之前有'*'，则'*'尝试再匹配一个‘s’。更新s的尝试匹配位。
最后查看p和s是否完全匹配。  
