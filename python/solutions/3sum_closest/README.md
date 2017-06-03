https://leetcode.com/problems/3sum-closest

Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

For example, given array S = {-1 2 1 -4}, and target = 1.
The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

############################################################

首先将数组排序。从头遍历数组，对于每一个元素（跳过重复的），将其之后剩余的数据的首尾相视为第二与第三个元素，并将取与第二与第三个和。
若和大于目标数，更新和与目标数的差，返回最小差对应的和
否则，更新和与目标数的数轴距离（差绝对值），大小关系。
    并将第二与第三个元素靠近，更新和与目标数的数轴距离（差绝对值）
    和与目标数若相等则结束。若和小于则第二数增大，更新大小关系。若和大于则第三数变小，若之前和小于则表示超过目标数了，同时调整第二与第三个数。