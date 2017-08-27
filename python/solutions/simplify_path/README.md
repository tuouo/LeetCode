https://leetcode.com/problems/spiral-matrix

Given an absolute path for a file (Unix-style), simplify it.  
For example,  
path = "/home/", => "/home"  
path = "/a/./b/../../c/", => "/c"  
click to show corner cases.  



Corner Cases:   
1. Did you consider the case where path = "/../"?  
In this case, you should return "/".  
2. Another corner case is the path might contain multiple slashes '/' together, such as "/home//foo/".  
In this case, you should ignore redundant slashes and return "/home/foo".  

############################################################


split the path by "/", make sure which one to inside or outside.  
turn to path mode at last.  
