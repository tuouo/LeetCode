https://leetcode.com/problems/next-permutation

Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers. 
If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order). 
The replacement must be in-place, do not allocate extra memory. 
Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1

############################################################

当我们寻找比当前的数大的新组合时，由于数构成数的数字是一样的，我们需要从数的末尾找，把一个数字与他前面的第一个比它小的数相交换。
在找到之前，所有的数都比前面的（靠近末尾的数）要大。则交换后，交换的较大的数的后面呈递减排列（较大数需要找到最靠后的位置），反过来排列即可。
特殊情况，交换的两数之间没有其他的数，直接换即可。没找到一个数小于后面的数，则是最大情况，反转全部数字。