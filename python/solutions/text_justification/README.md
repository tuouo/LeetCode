https://leetcode.com/problems/text-justification

Given an array of words and a length L, format the text such that each line has exactly L characters and is fully (left and right) justified. 
You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly L characters.   
Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line do not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.   
For the last line of text, it should be left justified and no extra space is inserted between words. 
For example,  
words: ["This", "is", "an", "example", "of", "text", "justification."]  
L: 16.   

############################################################

直接实现式解题。  
对于每一行，从当前字符记起，加到一个使字符串长度和与最小间隔符和超过每行长度为止。  
合理分布间隔的字符串（此处实现有好坏）。  
最后一行需按题意处理。  
