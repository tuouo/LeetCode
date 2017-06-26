https://leetcode.com/problems/regular-expression-matching

Implement regular expression matching with support for '.' and '*'.  
'.' Matches any single character.  
'*' Matches zero or more of the preceding element.  

The matching should cover the entire input string (not partial).  

The function prototype should be:  
bool isMatch(const char *s, const char *p)  

Some examples:  
isMatch("aa","a") → false  
isMatch("aa","aa") → true  
isMatch("aaa","aa") → false  
isMatch("aa", "a*") → true  
isMatch("aa", ".*") → true  
isMatch("ab", ".*") → true  
isMatch("aab", "c*a*b") → true  


############################################################
首先用递归解决。  

使用动态规划  
在确认当前字符串第i位匹配模式第j位时，  
如果模式第j-1位不为 * ，则当前字符串第i-1位匹配模式第j-1位匹配 且 当前字符串第i位匹配模式第j位才匹配  
否则当前字符串第i位匹配模式第j-2位时（即模式当前最后的 * 匹配空）；  
&emsp;&emsp;当前字符串第i-1位匹配模式第j位，且模式第j-2位为 . (此时字符串任意新字符都可匹配) ; 模式第j-2位为 字符串第i位 (此时 * 再匹配一个)    
都能使得当前字符串第i位匹配模式第j位      							   