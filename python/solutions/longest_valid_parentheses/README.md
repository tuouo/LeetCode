https://leetcode.com/problems/longest-valid-parentheses

Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring. 
For "(()", the longest valid parentheses substring is "()", which has length = 2. 
Another example is ")()())", where the longest valid parentheses substring is "()()", which has length = 4.

############################################################

从头开始遍历数组。碰到“(”存储当前位置，碰到“)”；如果没有“(”在前则跳过，并标识当前位置是新的开始，如果有则对应一个“(”，要是全部匹配则，从此次开始的位置到当前位置之前，都是符合要求的。要是还有“(”剩余，则从该“(”后一个位置算起。