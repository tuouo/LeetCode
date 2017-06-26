https://leetcode.com/problems/longest-palindromic-substring

Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.  
Example:   
Input: "babad"  
Output: "bab"  
Note: "aba" is also a valid answer.  

Example:   
Input: "cbbd"  
Output: "bb"  

############################################################

若直接实现  
对数组进行遍历，对于每个元素，判断以当前为中心是否是回文字符串正中，再判断是否是偶数长度回文字符串的中间位置。  
Time O(n^2)     Space O(n)  

Manacher's algorithm  
https://en.wikipedia.org/wiki/Longest_palindromic_substring  
https://segmentfault.com/a/1190000003914228  
Time O(n)     Space O(n)  
Runtime: 376 ms 2017.03  
直接实现有个麻烦的地方是回文字符串的奇偶性需要区分处理，以及每个位置的判断都是独立的，没有复用。  
