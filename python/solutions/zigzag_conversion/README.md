https://leetcode.com/problems/zigzag-conversion

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)   
P&emsp;&nbsp;A&emsp;&nbsp;H&emsp;&nbsp;N  
A&nbsp;P&nbsp;&nbsp;L&nbsp;S&nbsp;&nbsp;I&nbsp;&nbsp;I&nbsp;&nbsp;G  
Y&emsp;&nbsp;&nbsp;I&emsp;&nbsp;&nbsp;R  
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
还可以使用zip_longest  

如果只一次遍历，则需要定量个（the number of rows）数组来存储每个的结果  
