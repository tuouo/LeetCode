https://leetcode.com/problems/container-with-most-water/#/description

Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water. 
Note: You may not slant the container and n is at least 2. 

############################################################

面积由长度与高度（较矮的）决定。
从长度出发，则开始结尾最长。而高度不确定是哪个。
若取开始结尾的位置为最大值，当其不是最大值时，则最大值组合的高度比高于其。所以从开始结尾中矮的一边往里找高一点的位置，更新最大值。高度增加同时长度减少，面积是可以变大的。
由于最大值必然存在，若组合出现在中间，其高度必定比开始结尾区间组合的高度要高。则往里的过程中，必定有一边先抵达最大值一边（若为抵达则停下，当前区间更长，又不是最大值，只能高度更低），此时另一边必定会经过最大值的另一边。