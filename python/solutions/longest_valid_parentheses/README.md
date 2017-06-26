https://leetcode.com/problems/longest-valid-parentheses

Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.   
For "(()", the longest valid parentheses substring is "()", which has length = 2.   
Another example is ")()())", where the longest valid parentheses substring is "()()", which has length = 4.  

############################################################

从头开始遍历数组。碰到“(”存储当前位置，碰到“)”；如果没有“(”在前则跳过，并标识当前位置是新的开始，如果有则对应一个“(”，要是全部匹配则，从此次开始的位置到当前位置之前，都是符合要求的。要是还有“(”剩余，则从该“(”后一个位置算起。  

如果使用动态规划，dp[i]表示以i为子字符串末尾时的最大长度，最后的结果就是dp中的最大值。  
对于“(”不会确定匹配。对于“)”，则找到前面对应的“(”，由于中间的都是匹配的，所以当前“)”前面的位置储存着中间匹配的长度，如果对于位置不是“(”则也不能确定匹配。同时还需要把匹配位置之前的匹配也连起来。  
