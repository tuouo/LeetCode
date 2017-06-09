https://leetcode.com/problems/substring-with-concatenation-of-all-words

You are given a string, s, and a list of words, words, that are all of the same length. Find all starting indices of substring(s) in s that is a concatenation of each word in words exactly once and without any intervening characters. 
For example, given:
s: "barfoothefoobarman"
words: ["foo", "bar"] 
You should return the indices: [0,9].
(order does not matter). 

############################################################

一般来说，我们不会把所有words里的词拼接成一个词再来看看是不是在s里面。
从头开始遍历s，如果一个词（长度确定的）在words里面，再对后一个词做相同处理。
直到一个词不再里面，或者找到全部单词或者某个单词出现次数多了。

但是这样处理还有优化的余地。比如说，我们找到了一个substring符合要求，按上述方案就直接从下一个位置继续找了。
如果该substring的首个词（出现在words里面），同时出现在substring后面，这种情况在适当保存之前信息会很快捷。

我们按照words里的词长度往后走，如果这个词不在words里，则从后一个词开始找，如果再里面则保存记录。
当一个词的数量超过时，则把起点往后挪（即去除第一个词，可以处理找到所有词的情况）直到该词数量没超过（可能只是某个词在中间重复了。）这样只要开头前 “words里的词长度”的每个位置作为遍历起点往后挪动即可覆盖所有情况了。