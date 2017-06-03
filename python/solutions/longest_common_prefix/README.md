https://leetcode.com/problems/longest-common-prefix/#/description

Write a function to find the longest common prefix string amongst an array of strings. 

############################################################

A. 同时比较每个字符串首字母再依次往后

B. 使用库 os.path.commonprefix

C. 通过zip将相同位置的字符聚集，再计算集合是否单一元素，同时更新验证的位置信息。