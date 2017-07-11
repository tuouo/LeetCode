https://leetcode.com/problems/group-anagrams

Given an array of strings, group anagrams together.  

For example, given: ["eat", "tea", "tan", "ate", "nat", "bat"],   
Return:  

[
  ["ate", "eat","tea"],
  ["nat","tan"],
  ["bat"]
]  
Note: All inputs will be in lower-case.

############################################################

通过相同的点区分出anagrams.
可以通过映射某个字符串或数值(自定义哈希)来实现.
注意 defaultdict 与 生成式的使用.