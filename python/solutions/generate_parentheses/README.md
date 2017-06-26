https://leetcode.com/problems/generate-parentheses

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.   
For example, given n = 3, a solution set is:   
[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]

############################################################

使用递归时，首先我们标记没有成对出现的“（）”的数量为 数num ，然后我们生成当前已有字符串右边的内容。  
如果已经有足够的左边符号“（ ”时，补上对应的右边的“ ）”  
则当数num为0时：在原数组的左边添加“（ ”，进入递归  
当数num不为0时：在原数组的右边添加“ ）”，或者在原数组的左边添加“（ ”，进入递归  
