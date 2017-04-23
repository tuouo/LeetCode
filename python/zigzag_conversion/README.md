https://leetcode.com/problems/zigzag-conversion/#/solutions

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility) 
P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows: 
string convert(string text, int nRows);
convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".

############################################################

A. 直接实现法 
通过计算，在每次遍历类列表的时候算出对应行的字符位置。
将新增字符添加到结果集中，最后做输出转化。
Time O(mn)     Space O(n)	Runtime: 122 ms 2017.03		+=
Time O(mn)     Space O(n)	Runtime: 122 ms 2017.03		append
Time O(mn)     Space O(n)	Runtime: 156 ms 2017.03		StringIO


B. 反向标记法
Time O(n)     Space O(n)
Runtime: 342 ms 2017.03
对数组进行遍历，对每个数，保存目标与其的差做为遍历结果字典的键，下标为值。
则当某个数在遍历结果字典中，则表示前面出现了一个数与其的和为目标。
