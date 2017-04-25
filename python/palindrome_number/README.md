https://leetcode.com/problems/palindrome-number/#/description

Determine whether an integer is a palindrome. Do this without extra space.

############################################################

由于题目要求不能使用额外空间，所以只能对数字之间处理。
回文数字，即从左往右数与从右往左数的相同位置的数字是相同的。
另外，负数在左边拥有负号。有些数是十的倍数。

处理时如果从两头一起开始，可能需要快速知道该数有几位数。