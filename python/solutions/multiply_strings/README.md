https://leetcode.com/problems/multiply-strings

Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2.  

Note:  

The length of both num1 and num2 is < 110.  
Both num1 and num2 contains only digits 0-9.  
Both num1 and num2 does not contain any leading zero.  
You must not use any built-in BigInteger library or convert the inputs to integer directly.  

############################################################

题目的意思其实是不要使用内置函数.Python的内置函数可以达到 94.76%(49ms,1704)  
仅作大整数运算.(测试数据告诉我们只有考虑正整数)  

两个字符映射成整数相乘放置到对应位.  
不用每次都进位,临时数可以直接保持相乘结果的和,最后统一进位,一次就可以了.  