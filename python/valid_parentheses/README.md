https://leetcode.com/problems/valid-parentheses

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.

############################################################

栈的特性很好地帮助了我们解决这个问题，因为我们当需要处理符号的右边时，需要的是最近的符号的左边。
对于符号的左半边，入栈。当碰到右边时，弹出栈顶元素，判断是否匹配即可。如果需要匹配时没有左边元素或最后有左边元素剩余则视为不匹配。


然后，采用map存取之后效率依旧很不理想。2017年3月时在leetcode上耗时75ms，为后 %9

是的，这里还蕴含着一个优化。是的，我们表述的时候已经蕴含其中了。

因为每一个右边的符号都需要左边来匹配。