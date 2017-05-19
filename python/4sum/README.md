https://leetcode.com/problems/4sum

Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

For example, given array S = [1, 0, -1, 0, -2, 2], and target = 0.
A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]

############################################################
主导思路与3sum类似。

首先将数组排序。从头遍历数组，对于每一个的元素，检查与目标数的倍数关系。
对其之后剩余的数据进行3sum查找。即第二个数从改数后续的数开始遍历，第三个与第四个数在第二个数后面的部分从两端往中间靠拢。

每个Xsum都进行与目标数的倍数关系，用来跳过无用查找。
结果的唯一性需要跳过对应想重复元素（相对同一个序号的数而言，不同序号可以相同）。
