https://leetcode.com/problems/valid-sudoku

Determine if a Sudoku is valid, according to: [Sudoku Puzzles - The Rules](http://sudoku.com.au/TheRules.aspx).   
The Sudoku board could be partially filled, where empty cells are filled with the character '.'.   
　　　　&emsp;&emsp;![](250px-Sudoku-by-L2G-20050714.png)   
　　　　&emsp;&emsp;A partially filled sudoku which is valid.   
Note:
A valid Sudoku board (partially filled) is not necessarily solvable. Only the filled cells need to be validated. 

############################################################

根据规则，每一行每一列每个区块都不能有相同的数字。根据这一点判断即可。 
 
有很多很多种方法可以高效实现。  
