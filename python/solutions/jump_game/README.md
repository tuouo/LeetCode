https://leetcode.com/problems/jump-game

Given an array of non-negative integers, you are initially positioned at the first index of the array.  

Each element in the array represents your maximum jump length at that position.  

Determine if you are able to reach the last index.  

For example:  
A = [2,3,1,1,4], return true.  

A = [3,2,1,0,4], return false.  

############################################################

从一个位置往后跳，可以跳到下一位和该位最远可达距离（不是必须要跳这么多距离）。在最远可达距离之后意味着需要再跳一步。  

在该位可跳达的这段区间，其中一个位置会产生一个新的最远可达距离，在此之前不需要多跳一步。  

依照上述逻辑可以发现每一位的最远可达距离，调至该位的步数，进而确定最后一位需要的步数。  

如果有一个位置超过之前的最远可达距离，则不能抵达最后。
