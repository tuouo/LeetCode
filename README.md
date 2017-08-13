[LeetCode](https://leetcode.com "An online judge: an online system to test programs in programming contests")
=============
The Python 3 journey of [leetcode Problems Algorithms](https://leetcode.com/problemset/algorithms)  
You may meet some problems on the way, and [it(Problems you may face to)](./python/info.md) may be helpful.  

Here is the classification of free questions.
## Algorithms
* [Array](#array)
* [Hash Table](#hash-table)
* [Linked List](#linked-list)
* [Math](#math)
* [Two Pointers](#two-pointers)
* [String](#string)
* [Binary Search](#binary-search)
* [Divide & Conquer](#divide-and-conquer)
* [Backtracking](#backtracking)
* [Dynamic Programming](#dynamic-programming)
* [Stack](#stack)
* [Heap](#heap)
* [Greedy](#greedy)
* [Sort](#sortsort)

<!--
* [Bit Manipulation](#bit-manipulation)
## <span id=""></span>
* [Queue](#queue)
## <span id=""></span>
* [Tree](#tree)
## <span id=""></span>
* [Data Structure](#data-structure)
## <span id=""></span>
* [Recursion](#recursion)
## <span id=""></span>
* [Binary Search Tree](#binary-search-tree)
## <span id=""></span>
* [Breadth-First Search](#breadth-first-search)
## <span id=""></span>
* [Depth-First Search](#depth-first-search)
## <span id=""></span>
* [Design](#design)
## <span id=""></span>
-->

## <span id="array">Array</span>
| No. |  Title  |  Difficulty  |  Time  |  Space  |  Solution Runtime |  Tip  |
|:---:|:-------|:------------:|:------:|:-------:|:----------:|:-------|
1 | [Two Sum](https://leetcode.com/problems/two-sum) | Easy | _O(n)_ | _O(n)_ | [85.53(42ms,170626)](./python/solutions/two_sum) | set ||
4 | [Median of Two Sorted Arrays](https://leetcode.com/problems/median-of-two-sorted-arrays) | Hard | _O(log(m+n))_ | _O(1)_ | [78.16(99ms, 1706)](./python/solutions/median_of_two_sorted_arrays) | find kth ||
11 | [Container With Most Water](https://leetcode.com/problems/container-with-most-water) | Medium | _O(n)_ | _O(1)_ | [85.39(69ms, 1705)](./python/solutions/container_with_most_water) | from limit ||
15 | [3Sum](https://leetcode.com/problems/3sum) | Medium | _O(n^2)_ | _O(1)_ | [97.21(848ms, 1705)](./python/solutions/3sum) | sorted, meet ||
16 | [3Sum Closest](https://leetcode.com/problems/3sum-closest) | Medium | _O(n^2)_ | _O(1)_ | [56.32(145ms, 1705)](./python/solutions/3sum_closest) | sorted, meet ||
18 | [4Sum](https://leetcode.com/problems/4sum) | Medium | _O(n^3)_ | _O(1)_ | [86.12(132ms, 1703)](./python/solutions/4sum) | 3sum ||
26 | [Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array) | Easy | _O(n)_ | _O(1)_ | [77.68(79ms,170801)](./python/solutions/remove_duplicates_from_sorted_array) | ||
27 | [Remove Element](https://leetcode.com/problems/remove-element) | Easy | _O(n)_ | _O(1)_ | [67.84(45ms, 1703)](./python/solutions/remove_element) | ||
31 | [Next Permutation](https://leetcode.com/problems/next-permutation) | Medium | _O(n)_ | _O(1)_ | [56.61(62ms, 1703)](./python/solutions/next_permutation) | ||
33 | [Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array) | Medium | _O(logn)_ | _O(1)_ | [21.87(58ms, 1703)](./python/solutions/search_in_rotated_sorted_array) | Binary Search ||
34 | [Search for a Range](https://leetcode.com/problems/search-for-a-range) | Medium | _O(logn)_ | _O(1)_ | [73.72(45ms,170620) ](./python/solutions/search_for_a_range) | Binary Search left, then right ||
35 | [Search Insert Position](https://leetcode.com/problems/search-insert-position) | Easy | _O(logn)_ | _O(1)_ | [82.93(39ms,170620)](./python/solutions/search_insert_position) | check range & bisect ||
39 | [Combination Sum](https://leetcode.com/problems/combination-sum) | Medium | _O(k*n^k)_ | _O(k^2)_ | [99.81(72ms,170625)](./python/solutions/combination_sum) | backtracking, check target ||
40 | [Combination Sum II](https://leetcode.com/problems/combination-sum-ii) | Medium | _O(k*n^k)_ | _O(k^2)_ | [93.17(65ms,170626)](./python/solutions/combination_sum_II) | ||
41 | [First Missing Positive](https://leetcode.com/problems/first-missing-positive) | Hard | _O(n)_ | _O(1)_ | [72.06(42ms,170627) ](./python/solutions/first_missing_positive) | reset x to position x ||
42 | [Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water) | Hard | _O(n)_ | _O(n)_ | [72.91(52ms,170628)](./python/solutions/trapping_rain_water) | PEAK peak PEAK ||
45 | [Jump Game II](https://leetcode.com/problems/jump-game-ii) | Hard | _O(n)_ | _O(n)_ | [98.24(49ms,170705)](./python/solutions/tjump_game_ii) | ||
48 | [Rotate Image](https://leetcode.com/problems/rotate-image) | Medium | _O(n^2)_ | _O(1)_ | [61(45ms,170704)](./python/solutions/rotate_image) | ||
53 | [Maximum Subarray](https://leetcode.com/problems/maximum-subarray) | Medium | _O(n)_ | _O(1)_ | [88.17(45ms,170719)](./python/solutions/maximum_subarray) | ||
54 | [Spiral Matrix](https://leetcode.com/problems/spiral-matrix) | Medium | _O(mn)_ | _O(mn)_ | [82.77(32ms,170720)](./python/solutions/spiral_matrix) | ||
55 | [Jump Game](https://leetcode.com/problems/jump-game) | Medium | _O(m)_ | _O(1)_ | [63.92(52ms,170723)](./python/solutions/jump_game) | ||
56 | [Merge Intervals](https://leetcode.com/problems/merge-intervals) | Medium | _O(m)_ | _O(1)_ | [92.09(72ms,170726)](./python/solutions/merge_intervals) | ||
57 | [Insert Interval](https://leetcode.com/problems/insert-interval) | Hard | _O(m)_ | _O(1)_ | [98.84(62ms,170727)](./python/solutions/insert_intervals) | leetcode may give wrong Runtime ||
62 | [Unique Paths](https://leetcode.com/problems/unique-paths) | Medium | _O(1)_ | _O(1)_ | [76.22(32ms,1705)](./python/solutions/unique_paths) | directly ||

## <span id="hash-table">Hash Table</span>
| No. |  Title  |  Difficulty  |  Time  |  Space  |  Solution Runtime |  Tip  |
|:---:|:-------|:------------:|:------:|:-------:|:----------:|:-------|
1 | [Two Sum](https://leetcode.com/problems/two-sum) | Easy | _O(n)_ | _O(n)_ | [85.53(42ms,170626)](./python/solutions/two_sum) | set ||
3 | [Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters) | Medium | _O(n)_ | _O(n)_ | [88.87(89ms, 1704)](./python/solutions/longest_substring_without_repeating_characters) | between the same ||
18 | [4Sum](https://leetcode.com/problems/4sum) | Medium | _O(n^3)_ | _O(1)_ | [86.12(132ms, 1703)](./python/solutions/4sum) | 3sum ||
30 | [Substring with Concatenation of All Words](https://leetcode.com/problems/substring-with-concatenation-of-all-words) | Hard | _O(mnk)_ | _O(nk)_ | [70.72(98ms,170620)](./python/solutions/substring_with_oncatenation_of_all_words) | use find info ||
36 | [Valid Sudoku](https://leetcode.com/problems/valid-sudoku) | Medium | _O(9×9)_ | _O(9×9)_ | [75.42(76ms,170623)](./python/solutions/valid_sudoku) | many ways to check ||
37 | [Sudoku Solver](https://leetcode.com/problems/sudoku-solver) | Hard | _O((9!)^9)_ | _O(1)_ | [90.91(72ms,170623)](./python/solutions/sudoku_solver) | check then put, if wrong backtrack. Or play like human ||
49 | [Group Anagrams](https://leetcode.com/problems/group-anagrams) | Medium | _O(mn)_ | _O(mn)_ | [90.95(212ms,170711)](./python/solutions/group_anagrams) | frequency with hash ||

## <span id="linked-list">Linked List</span>
| No. |  Title  |  Difficulty  |  Time  |  Space  |  Solution Runtime |  Tip  |
|:---:|:-------|:------------:|:------:|:-------:|:----------:|:-------|
2 | [Add Two Numbers](https://leetcode.com/problems/add-two-numbers) | Medium | _O(n)_ | _O(1)_ | [61.77(135ms,1704)](./python/solutions/add_two_numbers) | ||
19 | [Remove Nth Node From End of List](https://leetcode.com/problems/remove-nth-node-from-end-of-list) | Easy | _O(n)_ | _O(1)_ | [93.74(42ms,170623)](./python/solutions/remove_nth_node_from_end_of_list) | ||
21 | [Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists) | Easy | _O(n)_ | _O(1)_ | [73.67(52ms, 1705)](./python/solutions/merge_two_sorted_lists) | ||
23 | [Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists) | Hard | _O(nlogk)_ | _O(1)_ | [98.15(105ms, 1703)](./python/solutions/merge_k_sorted_list) | ||
24 | [Swap Nodes in Pairs](https://leetcode.com/problems/swap-nodes-in-pairs) | Easy | _O(n)_ | _O(1)_ | [60.77(42ms, 1703)](./python/solutions/swap_nodes_in_pairs) | ||
25 | [Reverse Nodes in k-Group](https://leetcode.com/problems/reverse-nodes-in-k-group) | Hard | _O(n)_ | _O(1)_ | [73.50(72ms,170605)](./python/solutions/reverse_nodes_in_k_group) | ||
61 | [Rotate List](https://leetcode.com/problems/rotate-list) | Medium | _O(n)_ | _O(1)_ | [83.99(45ms,170811)](./python/solutions/rotate_list) | ||

## <span id="math">Math</span>
| No. |  Title  |  Difficulty  |  Time  |  Space  |  Solution Runtime |  Tip  |
|:---:|:-------|:------------:|:------:|:-------:|:----------:|:-------|
2 | [Add Two Numbers](https://leetcode.com/problems/add-two-numbers) | Medium | _O(n)_ | _O(1)_ | [61.77(135ms,1704)](./python/solutions/add_two_numbers) | ||
7 | [Reverse Integer](https://leetcode.com/problems/reverse-integer) |  Easy | _O(n)_ | _O(1)_ | [34.12(66ms, 1703)](./python/solutions/reverse_integer) | ||
8 | [String to Integer (atoi)](https://leetcode.com/problems/string-to-integer-atoi) | Medium | _O(n)_ | _O(1)_ | [44.69(78ms, 1704)](./python/solutions/string_to_integer) | ||
9 | [Palindrome Number](https://leetcode.com/problems/palindrome-number) | Easy | _O(n)_ | _O(1)_ | [80.74(216ms, 1704)](./python/solutions/palindrome_number) | ||
12 | [Integer to Roman](https://leetcode.com/problems/integer-to-roman) | Medium | _O(n)_ | _O(1)_ | [90.62(105ms, 1705)](./python/solutions/Integer_to_Roman) | directly ||
13 | [Roman to Integer](https://leetcode.com/problems/roman-to-integer) | Medium | _O(n)_ | _O(1)_ | [88.58(132ms, 1705)](./python/solutions/Roman_to_Integer) | lambda ||
29 | [Divide Two Integers](https://leetcode.com/problems/divide-two-integers) | Medium | _O(m/n)_ | _O(1)_ | [33.58(68ms, 1703)](./python/solutions/divide_two_integers) | ||
43 | [Multiply Strings](https://leetcode.com/problems/multiply-strings) | Medium | _O(m*n)_ | _O(m+n)_ | [94.76(49ms,1704) / 76.65(168ms,170629)](./python/solutions/multiply_strings) | carry, once ||
50 | [Pow(x, n)](https://leetcode.com/problems/powx-n) | Medium | _O(m*n)_ | _O(m+n)_ | [74.33(39ms, 1705)](./python/solutions/powx_n) | ||
60 | [Permutation Sequence](https://leetcode.com/problems/permutation-sequence) | Medium | _O(n)_ | _O(n)_ | [33.52(45ms, 1705)](./python/solutions/permutation_sequence) | ||

## <span id="two-pointers">Two Pointers</span>
| No. |  Title  |  Difficulty  |  Time  |  Space  |  Solution Runtime |  Tip  |
|:---:|:-------|:------------:|:------:|:-------:|:----------:|:-------|
3 | [Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters) | Medium | _O(n)_ | _O(n)_ | [88.87(89ms, 1704)](./python/solutions/longest_substring_without_repeating_characters) | between the same ||
11 | [Container With Most Water](https://leetcode.com/problems/container-with-most-water) | Medium | _O(n)_ | _O(1)_ | [85.39(69ms, 1705)](./python/solutions/container_with_most_water) | from limit ||
15 | [3Sum](https://leetcode.com/problems/3sum) | Medium | _O(n^2)_ | _O(1)_ | [97.21(848ms, 1705)](./python/solutions/3sum) | sorted, meet ||
16 | [3Sum Closest](https://leetcode.com/problems/3sum-closest) | Medium | _O(n^2)_ | _O(1)_ | [56.32(145ms, 1705)](./python/solutions/3sum_closest) | sorted, meet ||
18 | [4Sum](https://leetcode.com/problems/4sum) | Medium | _O(n^3)_ | _O(1)_ | [86.12(132ms, 1703)](./python/solutions/4sum) | 3sum ||
19 | [Remove Nth Node From End of List](https://leetcode.com/problems/remove-nth-node-from-end-of-list) | Medium | _O(n)_ | _O(1)_ | [93.74(42ms,170623)](./python/solutions/remove_nth_node_from_end_of_list) | ||
26 | [Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array) | Easy | _O(n)_ | _O(1)_ | [77.68(79ms,170801)](./python/solutions/remove_duplicates_from_sorted_array) | ||
27 | [Remove Element](https://leetcode.com/problems/remove-element) | Easy | _O(n)_ | _O(1)_ | [67.84(45ms, 1703)](./python/solutions/remove_element) | ||
28 | [Implement strStr()](https://leetcode.com/problems/implement-strstr) | Easy | _O(mn)_ | _O(n)_ | [41.03(58ms, 1703)](./python/solutions/implement_strStr) | ||
30 | [Substring with Concatenation of All Words](https://leetcode.com/problems/substring-with-concatenation-of-all-words) | Hard | _O(mnk)_ | _O(nk)_ | [70.72(98ms,170620)](./python/solutions/substring_with_oncatenation_of_all_words) | use find info ||
42 | [Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water) | Hard | _O(n)_ | _O(n)_ | [72.91(52ms,170627)](./python/solutions/trapping_rain_water) | PEAK peak PEAK ||
61 | [Rotate List](https://leetcode.com/problems/rotate-list) | Medium | _O(n)_ | _O(1)_ | [83.99(45ms,170811)](./python/solutions/rotate_list) | ||

## <span id="string">String</span>
| No. |  Title  |  Difficulty  |  Time  |  Space  |  Solution Runtime |  Tip  |
|:---:|:-------|:------------:|:------:|:-------:|:----------:|:-------|
3 | [Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters) | Medium | _O(n)_ | _O(n)_ | [88.87(89ms, 1704)](./python/solutions/longest_substring_without_repeating_characters) | between the same ||
5 | [Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring) | Medium | _O(n)_ | _O(n)_ | [91.31(95ms, 170729)](./python/solutions/longest_palindromic_substring) | Manacher ||
6 | [ZigZag Conversion](https://leetcode.com/problems/zigzag-conversion) | Medium | _O(n)_ | _O(1)_ | [61.39(122ms, 1703)](./python/solutions/zigzag_conversion) | join ||
8 | [String to Integer (atoi)](https://leetcode.com/problems/string-to-integer-atoi) | Medium | _O(n)_ | _O(1)_ | [44.69(78ms, 1704)](./python/solutions/string_to_integer) | ||
10 | [Regular Expression Matching](https://leetcode.com/problems/regular-expression-matching) | Hard | _O(mn)_ | _O(mn)_ | [85.45(82ms, 1705)](./python/solutions/regular_expression_matching) | ||
12 | [Integer to Roman](https://leetcode.com/problems/integer-to-roman) | Medium | _O(n)_ | _O(1)_ | [90.62(105ms, 1705)](./python/solutions/Integer_to_Roman) | directly ||
13 | [Roman to Integer](https://leetcode.com/problems/roman-to-integer) | Medium | _O(n)_ | _O(1)_ | [88.58(132ms, 1705)](./python/solutions/Roman_to_Integer) | lambda ||
14 | [Longest Common Prefix](https://leetcode.com/problems/longest-common-prefix) | Easy | _O(mn)_ | _O(1)_ | [84.60(42ms, 1704)](./python/solutions/longest_common_prefix) | zip is better ||
17 | [Letter Combinations of a Phone Number](https://leetcode.com/problems/letter-combinations-of-a-phone-number) | Medium | _O(4^n)_ | _O(n)_ | [62.18(42ms, 1705)](./python/solutions/letter_combinations_of_a_phone_number) | reduce works ||
20 | [Valid Parentheses](https://leetcode.com/problems/valid-parentheses) | Easy | _O(n)_ | _O(n)_ | [92.77(39ms, 1703)](./python/solutions/valid_parentheses) | ||
22 | [Generate Parentheses](https://leetcode.com/problems/generate-parentheses) | Medium | O(4^n / n^(3/2)) | _O(n)_ | [28.90(65ms, 1703)](./python/solutions/generate_parentheses) | generate, closed? ||
28 | [Implement strStr()](https://leetcode.com/problems/implement-strstr) | Easy | _O(mn)_ | _O(n)_ | [41.03(58ms, 1703)](./python/solutions/implement_strStr) | ||
30 | [Substring with Concatenation of All Words](https://leetcode.com/problems/substring-with-concatenation-of-all-words) | Hard | _O(mnk)_ | _O(nk)_ | [70.72(98ms,170620)](./python/solutions/substring_with_oncatenation_of_all_words) | use find info ||
32 | [Longest Valid Parentheses](https://leetcode.com/problems/longest-valid-parentheses) | Hard | _O(n)_ | _O(1)_ | [72.88(79ms,170614)](./python/solutions/longest_valid_parentheses) | ||
38 | [Count and Say](https://leetcode.com/problems/count-and-say) | Hard | _O(n)_ | _O(1)_ | [41.89(55ms, 1705)](./python/solutions/count_and_say) | pythonchallenge (level 10) ||
43 | [Multiply Strings](https://leetcode.com/problems/multiply-strings) | Medium | _O(m*n)_ | _O(m+n)_ | [94.76(49ms,1704) / 76.65(168ms,170629)](./python/solutions/multiply_strings) | carry, once ||
44 | [Wildcard Matching](https://leetcode.com/problems/wildcard-matching) | Hard | _O(m*n)_ | _O(1)_ | [86.49(109ms,1704)](./python/solutions/wildcard_matching) | ||
49 | [Group Anagrams](https://leetcode.com/problems/group-anagrams) | Medium | _O(mn)_ | _O(mn)_ | [90.95(212ms, 170711)](./python/solutions/group_anagrams) | frequency with hash ||
58 | [Length of Last Word](https://leetcode.com/problems/length-of-last-words) | Easy | _O(1)_ | _O(1)_ | [84.46(32ms,170729)](./python/solutions/length_of_last_word) | ||

## <span id="binary-search">Binary Search</span>
| No. |  Title  |  Difficulty  |  Time  |  Space  |  Solution Runtime |  Tip  |
|:---:|:-------|:------------:|:------:|:-------:|:----------:|:-------|
4 | [Median of Two Sorted Arrays](https://leetcode.com/problems/median-of-two-sorted-arrays) | Hard | _O(log(m+n))_ | _O(1)_ | [78.16(99ms, 1706)](./python/solutions/median_of_two_sorted_arrays) | find kth ||
29 | [Divide Two Integers](https://leetcode.com/problems/divide-two-integers) | Medium | _O(m/n)_ | _O(1)_ | [33.58(68ms, 1703)](./python/solutions/divide_two_integers) | ||
33 | [Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array) | Medium | _O(logn)_ | _O(1)_ | [21.87(58ms, 1703)](./python/solutions/search_in_rotated_sorted_array) | Binary Search ||
34 | [Search for a Range](https://leetcode.com/problems/search-for-a-range) | Medium | _O(logn)_ | _O(1)_ | [73.72(45ms,170620)](./python/solutions/search_for_a_range) | Search left, then right ||
35 | [Search Insert Position](https://leetcode.com/problems/search-insert-position) | Easy | _O(logn)_ | _O(1)_ | [82.93(39ms,170620)](./python/solutions/search_insert_position) | check range & bisect ||
50 | [Pow(x, n)](https://leetcode.com/problems/powx-n) | Medium | _O(m*n)_ | _O(m+n)_ | [74.33(39ms, 1705)](./python/solutions/powx_n) | ||

## <span id="divide-and-conquer">Divide & Conquer</span>
| No. |  Title  |  Difficulty  |  Time  |  Space  |  Solution Runtime |  Tip  |
|:---:|:-------|:------------:|:------:|:-------:|:----------:|:-------|
4 | [Median of Two Sorted Arrays](https://leetcode.com/problems/median-of-two-sorted-arrays) | Hard | _O(log(m+n))_ | _O(1)_ | [78.16(99ms, 1706)](./python/solutions/median_of_two_sorted_arrays) | find kth ||
23 | [Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists) | Hard | _O(nlogk)_ | _O(1)_ | [98.15(105ms, 1703)](./python/solutions/merge_k_sorted_list) | ||
53 | [Maximum Subarray](https://leetcode.com/problems/maximum-subarray) | Medium | _O(n)_ | _O(1)_ | [88.17(45ms,170719)](./python/solutions/maximum_subarray) | ||

## <span id="backtracking">Backtracking</span>
| No. |  Title  |  Difficulty  |  Time  |  Space  |  Solution Runtime |  Tip  |
|:---:|:-------|:------------:|:------:|:-------:|:----------:|:-------|
10 | [Regular Expression Matching](https://leetcode.com/problems/regular-expression-matching) | Hard | _O(mn)_ | _O(mn)_ | [85.45(82ms, 1705)](./python/solutions/regular_expression_matching) | ||
17 | [Letter Combinations of a Phone Number](https://leetcode.com/problems/letter-combinations-of-a-phone-number) | Medium | _O(4^n)_ | _O(n)_ | [62.18(42ms, 1705)](./python/solutions/letter_combinations_of_a_phone_number) | reduce works ||
22 | [Generate Parentheses](https://leetcode.com/problems/generate-parentheses) | Medium | O(4^n / n^(3/2)) | _O(n)_ | [28.90(65ms, 1703)](./python/solutions/generate_parentheses) | generate, closed? ||
37 | [Sudoku Solver](https://leetcode.com/problems/sudoku-solver) | Hard | _O((9!)^9)_ | _O(1)_ | [90.91(72ms,170623)](./python/solutions/sudoku_solver) | check then put, if wrong backtracking. Or play like human ||
39 | [Combination Sum](https://leetcode.com/problems/combination-sum) | Medium | _O(k*n^k)_ | _O(k^2)_ | [99.81(72ms,170625)](./python/solutions/combination_sum) | backtracking, check target ||
40 | [Combination Sum II](https://leetcode.com/problems/combination-sum-ii) | Medium | _O(k*n^k)_ | _O(k^2)_ | [93.17(65ms,170626)](./python/solutions/combination_sum_II) | ||
44 | [Wildcard Matching](https://leetcode.com/problems/wildcard-matching) | Hard | _O(m*n)_ | _O(1)_ | [86.49(109ms,1704)](./python/solutions/wildcard_matching) | ||
46 | [Permutations](https://leetcode.com/problems/permutations) | Medium | _O(n!)_ | _O(n*n!)_ | [87.53(66ms,1704)](./python/solutions/permutations) | ||
47 | [Permutations II](https://leetcode.com/problems/permutations-ii) | Medium | _O(n!)_ | _O(n*n!)_ | [_94.36(99ms,1703)_](./python/solutions/permutationsII) | ||
51 | [N-Queens](https://leetcode.com/problems/n-queens) | Hard | _O(n^3)_ | _O(n*n)_ | [100(62ms,170717)](./python/solutions/n_queens) | bit ||
52 | [N-Queens II](https://leetcode.com/problems/n-queens-ii) | Hard | _O(n^3)_ | _O(n*n)_ | [99.27(42ms, 1704)](./python/solutions/n_queens_ii) | bit ||
60 | [Permutation Sequence](https://leetcode.com/problems/permutation-sequence) | Medium | _O(n)_ | _O(n)_ | [33.52(45ms, 1705)](./python/solutions/permutation_sequence) | ||

## <span id="dynamic-programming">Dynamic Programming</span>
| No. |  Title  |  Difficulty  |  Time  |  Space  |  Solution Runtime |  Tip  |
|:---:|:-------|:------------:|:------:|:-------:|:----------:|:-------|
10 | [Regular Expression Matching](https://leetcode.com/problems/regular-expression-matching) | Hard | _O(mn)_ | _O(mn)_ | [85.45(82ms, 1705)](./python/solutions/regular_expression_matching) | ||
32 | [Longest Valid Parentheses](https://leetcode.com/problems/longest-valid-parentheses) | Hard | _O(n)_ | _O(1)_ | [72.88(79ms,170614)](./python/solutions/longest_valid_parentheses) | ||
44 | [Wildcard Matching](https://leetcode.com/problems/wildcard-matching) | Hard | _O(m*n)_ | _O(1)_ | [86.49(109ms,1704)](./python/solutions/wildcard_matching) | ||
53 | [Maximum Subarray](https://leetcode.com/problems/maximum-subarray) | Medium | _O(n)_ | _O(1)_ | [88.17(45ms,170719)](./python/solutions/maximum_subarray) | ||
62 | [Unique Paths](https://leetcode.com/problems/unique-paths) | Medium | _O(1)_ | _O(1)_ | [76.22(32ms,1705)](./python/solutions/unique_paths) | directly ||

## <span id="stack">Stack</span>
| No. |  Title  |  Difficulty  |  Time  |  Space  |  Solution Runtime |  Tip  |
|:---:|:-------|:------------:|:------:|:-------:|:----------:|:-------|
20 | [Valid Parentheses](https://leetcode.com/problems/valid-parentheses) | Easy | _O(n)_ | _O(n)_ | [92.77(39ms, 1703)](./python/solutions/valid_parentheses) | ||
42 | [Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water) | Hard | _O(n)_ | _O(n)_ | [72.91(52ms,1706278)](./python/solutions/trapping_rain_water) | PEAK peak PEAK ||

## <span id="heap">Heap</span>
| No. |  Title  |  Difficulty  |  Time  |  Space  |  Solution Runtime |  Tip  |
|:---:|:-------|:------------:|:------:|:-------:|:----------:|:-------|
23 | [Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists) | Hard | _O(nlogk)_ | _O(1)_ | [98.15(105ms, 1703)](./python/solutions/merge_k_sorted_list) | replace ||


## <span id="greedy">Greedy</span>
| No. |  Title  |  Difficulty  |  Time  |  Space  |  Solution Runtime |  Tip  |
|:---:|:-------|:------------:|:------:|:-------:|:----------:|:-------|
44 | [Wildcard Matching](https://leetcode.com/problems/wildcard-matching) | Hard | _O(m*n)_ | _O(1)_ | [86.49(109ms,1704)](./python/solutions/wildcard_matching) | ||
45 | [Jump Game II](https://leetcode.com/problems/jump-game-ii) | Hard | _O(n)_ | _O(n)_ | [98.24(49ms,170705)](./python/solutions/tjump_game_ii) | ||
55 | [Jump Game](https://leetcode.com/problems/jump-game) | Medium | _O(m)_ | _O(1)_ | [63.92(52ms,170723)](./python/solutions/jump_game) | ||


## <span id="sortsort">Sort</span>
| No. |  Title  |  Difficulty  |  Time  |  Space  |  Solution Runtime |  Tip  |
|:---:|:-------|:------------:|:------:|:-------:|:----------:|:-------|
56 | [Merge Intervals](https://leetcode.com/problems/merge-intervals) | Medium | _O(m)_ | _O(1)_ | [92.09(72ms,170726)](./python/solutions/merge_intervals) | ||
57 | [Insert Interval](https://leetcode.com/problems/insert-interval) | Hard | _O(m)_ | _O(1)_ | [98.84(62ms,170727)](./python/solutions/insert_intervals) | leetcode may give wrong Runtime ||

<!--
<meta http-equiv="refresh" content="5">
-->
