https://leetcode.com/problems/climbing-stairs

You are climbing a stair case. It takes n steps to reach to the top.  
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?   
Note: Given n will be a positive integer.   

############################################################

If you think in this way:  
First, each step is 1, then make one step is 2, replace the last by 2, then take the "2" forward. ...   
It may have a result, but take o lot of time.

Ok, you may assume n is 1, is 2, is 3 and so on, look regularity of the result.  
And may be you will find result(n) + result(n + 1) is result(n + 2), this is because 'Each time you can either climb 1 or 2 steps.'  
oh, some one named it [Fibonacci number](https://en.wikipedia.org/wiki/Fibonacci_number)  
