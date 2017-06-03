https://leetcode.com/problems/longest-substring-without-repeating-characters/#/description

GGiven a string, find the length of the longest substring without repeating characters.
Examples:
Given "abcabcbb", the answer is "abc", which the length is 3.
Given "bbbbb", the answer is "b", with the length of 1.
Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

############################################################

A. 直接实现法 
Time O(n^2)     Space O(n)
Runtime: 252 ms 2017.03
对数组进行遍历。每个数检查是否在当前的连续字串中，若是，重置连续字串，否则连续字串更新相关信息。

B. 字符字典记录法
Time O(n)     Space O(n)
Runtime: 102 ms 2017.03
对数组进行遍历，对每个数将前为键，下标为值存入字典。若新数不存在，继续存入字典，更新最长信息。若新数存在，且在当前连续字串起点之后，更新起点。

C. 字符字典记录法优化
Time O(n)     Space O(n)
Runtime: 89 ms 2017.04
对于每个新数不在连续字串中，没必要实时更新最长信息。检测到存在，且在当前连续字串起点之后，更新起点时再更新。
