https://leetcode.com/problems/n-queens

The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.  
　　　　&emsp;&emsp;![](8-queens.png)    
Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space respectively.  

For example,  
There exist two distinct solutions to the 4-queens puzzle:  
[  
&nbsp;[".Q..",  // Solution 1  
&nbsp; "...Q",  
&nbsp; "Q...",    
&nbsp; "..Q."],  

&nbsp;["..Q.",  // Solution 2  
&nbsp; "Q...",  
&nbsp; "...Q",  
&nbsp; ".Q.."]  
]  

############################################################

这里有四个限制性条件，每个棋子的横竖斜（包括正向反向）都只能只有一个棋子。  

通辅助数组记录已占用的位置信息，简单计算得出可选的位置。
对于每一行，选择一个可行位置作为一种解法。（通过竖向（n个位置）与两个斜向（2×n-1个位置，可适当增加）的限制确定）

每个解法可以只保存对应行的位置信息即可。在最后再生成图形化信息。  
