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

<!--
* [Bit Manipulation](#bit-manipulation)
## <span id=""></span>
* [Queue](#queue)
## <span id=""></span>
* [Tree](#tree)
## <span id=""></span>
* [Data Structure](#data-structure)
## <span id=""></span>
* [Sort](#sort)
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
| No. |  Title  |  Difficulty  |  Time  |  Space  |  Solution  |  Tip  | Runtime |
|:---:|:-------|:------------:|:------:|:-------:|:----------:|:-------|:-------|
1 | [Two Sum](https://leetcode.com/problems/two-sum) | Easy | _O(n)_ | _O(n)_ | [Python](./python/solutions/two_sum) | set | 85.53(42ms,170626) ||
4 | [Median of Two Sorted Arrays](https://leetcode.com/problems/median-of-two-sorted-arrays) | Hard | _O(log(m+n))_ | _O(1)_ | [Python](./python/solutions/median_of_two_sorted_arrays) | find kth | 78.16(99ms, 1706) ||
11 | [Container With Most Water](https://leetcode.com/problems/container-with-most-water) | Medium | _O(n)_ | _O(1)_ | [Python](./python/solutions/container_with_most_water) | from limit | 85.39(69ms, 1705) ||
15 | [3Sum](https://leetcode.com/problems/3sum) | Medium | _O(n^2)_ | _O(1)_ | [Python](./python/solutions/3sum) | sorted, meet | 97.21(848ms, 1705) ||
16 | [3Sum Closest](https://leetcode.com/problems/3sum-closest) | Medium | _O(n^2)_ | _O(1)_ | [Python](./python/solutions/3sum_closest) | sorted, meet | 56.32(145ms, 1705) ||
18 | [4Sum](https://leetcode.com/problems/4sum) | Medium | _O(n^3)_ | _O(1)_ | [Python](./python/solutions/4sum) | 3sum | 86.12(132ms, 1703) ||
26 | [Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array) | Easy | _O(n)_ | _O(1)_ | [Python](./python/solutions/remove_duplicates_from_sorted_array) |  | 33.03(112ms, 1703) ||
27 | [Remove Element](https://leetcode.com/problems/remove-element) | Easy | _O(n)_ | _O(1)_ | [Python](./python/solutions/remove_element) |  | 67.84(45ms, 1703) ||
31 | [Next Permutation](https://leetcode.com/problems/next-permutation) | Medium | _O(n)_ | _O(1)_ | [Python](./python/solutions/next_permutation) |  | 56.61(62ms, 1703) ||
33 | [Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array) | Medium | _O(logn)_ | _O(1)_ | [Python](./python/solutions/search_in_rotated_sorted_array) | Binary Search | 21.87(58ms, 1703) ||
34 | [Search for a Range](https://leetcode.com/problems/search-for-a-range) | Medium | _O(logn)_ | _O(1)_ | [Python](./python/solutions/search_for_a_range) | Binary Search left, then right | 73.72(45ms,170620) ||
35 | [Search Insert Position](https://leetcode.com/problems/search-insert-position) | Easy | _O(logn)_ | _O(1)_ | [Python](./python/solutions/search_insert_position) | check range & bisect | 82.93(39ms,170620) ||
39 | [Combination Sum](https://leetcode.com/problems/combination-sum) | Medium | _O(k*n^k)_ | _O(k^2)_ | [Python](./python/solutions/combination_sum) | backtracking, check target | 99.81(72ms,170625) ||
40 | [Combination Sum II](https://leetcode.com/problems/combination-sum-ii) | Medium | _O(k*n^k)_ | _O(k^2)_ | [Python](./python/solutions/combination_sum_II) | | 93.17(65ms,170626) ||
41 | [First Missing Positive](https://leetcode.com/problems/first-missing-positive) | Hard | _O(n)_ | _O(1)_ | [Python](./python/solutions/first_missing_positive) | reset x to position x | 72.06(42ms,170627) ||
42 | [Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water) | Hard | _O(n)_ | _O(n)_ | [Python](./python/solutions/trapping_rain_water) | PEAK peak PEAK | 72.91(52ms,1706278) ||
45 | [Jump Game II](https://leetcode.com/problems/jump-game-ii) | Hard | _O(n)_ | _O(n)_ | [Python](./python/solutions/tjump_game_ii) | | 98.24(49ms,170705) ||
48 | [Rotate Image](https://leetcode.com/problems/rotate-image) | Medium | _O(n^2)_ | _O(1)_ | [Python](./python/solutions/rotate_image) | | 61(45ms,170704) ||

## <span id="hash-table">Hash Table</span>
| No. |  Title  |  Difficulty  |  Time  |  Space  |  Solution  |  Tip  | Runtime |
|:---:|:-------|:------------:|:------:|:-------:|:----------:|:-------|:-------|
1 | [Two Sum](https://leetcode.com/problems/two-sum) | Easy | _O(n)_ | _O(n)_ | [Python](./python/solutions/two_sum) | set | 85.53(42ms,170626) ||
3 | [Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters) | Medium | _O(n)_ | _O(n)_ | [Python](./python/solutions/longest_substring_without_repeating_characters) | between the same | 88.87(89ms, 1704) ||
18 | [4Sum](https://leetcode.com/problems/4sum) | Medium | _O(n^3)_ | _O(1)_ | [Python](./python/solutions/4sum) | 3sum | 86.12(132ms, 1703) ||
30 | [Substring with Concatenation of All Words](https://leetcode.com/problems/substring-with-concatenation-of-all-words) | Hard | _O(mnk)_ | _O(nk)_ | [Python](./python/solutions/substring_with_oncatenation_of_all_words) | use find info | 70.72(98ms,170620) ||
36 | [Valid Sudoku](https://leetcode.com/problems/valid-sudoku) | Medium | _O(9×9)_ | _O(9×9)_ | [Python](./python/solutions/valid_sudoku) | many ways to check | 75.42(76ms,170623) ||
37 | [Sudoku Solver](https://leetcode.com/problems/sudoku-solver) | Hard | _O((9!)^9)_ | _O(1)_ | [Python](./python/solutions/sudoku_solver) | check then put, if wrong backtrack. Or play like human | 90.91(72ms,170623) ||
49 | [Group Anagrams](https://leetcode.com/problems/group-anagrams) | Medium | _O(mn)_ | _O(mn)_ | [Python](./python/solutions/group_anagrams) | frequency with hash | 90.95(212ms, 170711) ||

## <span id="linked-list">Linked List</span>
| No. |  Title  |  Difficulty  |  Time  |  Space  |  Solution  |  Tip  | Runtime |
|:---:|:-------|:------------:|:------:|:-------:|:----------:|:-------|:-------|
2 | [Add Two Numbers](https://leetcode.com/problems/add-two-numbers) | Medium | _O(n)_ | _O(1)_ | [Python](./python/solutions/add_two_numbers) |  | 61.77(135ms,1704) ||
19 | [Remove Nth Node From End of List](https://leetcode.com/problems/remove-nth-node-from-end-of-list) | Easy | _O(n)_ | _O(1)_ | [Python](./python/solutions/remove_nth_node_from_end_of_list) |  | 93.74(42ms,170623) ||
21 | [Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists) | Easy | _O(n)_ | _O(1)_ | [Python](./python/solutions/merge_two_sorted_lists) |  | 73.67(52ms, 1705) ||
23 | [Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists) | Hard | _O(nlogk)_ | _O(1)_ | [Python](./python/solutions/merge_k_sorted_list) |  | 98.15(105ms, 1703) ||
24 | [Swap Nodes in Pairs](https://leetcode.com/problems/swap-nodes-in-pairs) | Easy | _O(n)_ | _O(1)_ | [Python](./python/solutions/swap_nodes_in_pairs) | | 60.77(42ms, 1703) ||
25 | [Reverse Nodes in k-Group](https://leetcode.com/problems/reverse-nodes-in-k-group) | Hard | _O(n)_ | _O(1)_ | [Python](./python/solutions/reverse_nodes_in_k_group) |  | 73.50(72ms,170605) ||

## <span id="math">Math</span>
| No. |  Title  |  Difficulty  |  Time  |  Space  |  Solution  |  Tip  | Runtime |
|:---:|:-------|:------------:|:------:|:-------:|:----------:|:-------|:-------|
2 | [Add Two Numbers](https://leetcode.com/problems/add-two-numbers) | Medium | _O(n)_ | _O(1)_ | [Python](./python/solutions/add_two_numbers) |  | 61.77(135ms,1704) ||
7 | [Reverse Integer](https://leetcode.com/problems/reverse-integer) |  Easy | _O(n)_ | _O(1)_ | [Python](./python/solutions/reverse_integer) |  | 34.12(66ms, 1703) ||
8 | [String to Integer (atoi)](https://leetcode.com/problems/string-to-integer-atoi) | Medium | _O(n)_ | _O(1)_ | [Python](./python/solutions/string_to_integer) | | 44.69(78ms, 1704) ||
9 | [Palindrome Number](https://leetcode.com/problems/palindrome-number) | Easy | _O(n)_ | _O(1)_ | [Python](./python/solutions/palindrome_number) |  | 80.74(216ms, 1704) ||
12 | [Integer to Roman](https://leetcode.com/problems/integer-to-roman) | Medium | _O(n)_ | _O(1)_ | [Python](./python/solutions/Integer_to_Roman) | directly | 90.62(105ms, 1705) ||
13 | [Roman to Integer](https://leetcode.com/problems/roman-to-integer) | Medium | _O(n)_ | _O(1)_ | [Python](./python/solutions/Roman_to_Integer) | lambda | 88.58(132ms, 1705) ||
29 | [Divide Two Integers](https://leetcode.com/problems/divide-two-integers) | Medium | _O(m/n)_ | _O(1)_ | [Python](./python/solutions/divide_two_integers) | | 33.58(68ms, 1703) ||
43 | [Multiply Strings](https://leetcode.com/problems/multiply-strings) | Medium | _O(m*n)_ | _O(m+n)_ | [Python](./python/solutions/multiply_strings) | carry, once |  94.76(49ms,1704)/76.65(168ms,170629) ||
50 | [Pow(x, n)](https://leetcode.com/problems/powx-n) | Medium | _O(m*n)_ | _O(m+n)_ | [Python](./python/solutions/powx_n) | | 74.33(39ns, 1705) ||

## <span id="two-pointers">Two Pointers</span>
| No. |  Title  |  Difficulty  |  Time  |  Space  |  Solution  |  Tip  | Runtime |
|:---:|:-------|:------------:|:------:|:-------:|:----------:|:-------|:-------|
3 | [Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters) | Medium | _O(n)_ | _O(n)_ | [Python](./python/solutions/longest_substring_without_repeating_characters) | between the same | 88.87(89ms, 1704)||
11 | [Container With Most Water](https://leetcode.com/problems/container-with-most-water) | Medium | _O(n)_ | _O(1)_ | [Python](./python/solutions/container_with_most_water) | from limit | 85.39(69ms, 1705)||
15 | [3Sum](https://leetcode.com/problems/3sum) | Medium | _O(n^2)_ | _O(1)_ | [Python](./python/solutions/3sum) | sorted, meet | 97.21(848ms, 1705)||
16 | [3Sum Closest](https://leetcode.com/problems/3sum-closest) | Medium | _O(n^2)_ | _O(1)_ | [Python](./python/solutions/3sum_closest) | sorted, meet | 56.32(145ms, 1705)||
18 | [4Sum](https://leetcode.com/problems/4sum) | Medium | _O(n^3)_ | _O(1)_ | [Python](./python/solutions/4sum) | 3sum | 86.12(132ms, 1703) ||
19 | [Remove Nth Node From End of List](https://leetcode.com/problems/remove-nth-node-from-end-of-list) | Medium | _O(n)_ | _O(1)_ | [Python](./python/solutions/remove_nth_node_from_end_of_list) |  | 93.74(42ms,170623) ||
26 | [Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array) | Easy | _O(n)_ | _O(1)_ | [Python](./python/solutions/remove_duplicates_from_sorted_array) |  | 33.03(112ms, 1703) ||
27 | [Remove Element](https://leetcode.com/problems/remove-element) | Easy | _O(n)_ | _O(1)_ | [Python](./python/solutions/remove_element) |  | 67.84(45ms, 1703) ||
28 | [Implement strStr()](https://leetcode.com/problems/implement-strstr) | Easy | _O(mn)_ | _O(n)_ | [Python](./python/solutions/implement_strStr) | | 41.03(58ms, 1703) ||
30 | [Substring with Concatenation of All Words](https://leetcode.com/problems/substring-with-concatenation-of-all-words) | Hard | _O(mnk)_ | _O(nk)_ | [Python](./python/solutions/substring_with_oncatenation_of_all_words) | use find info | 70.72(98ms,170620) ||
42 | [Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water) | Hard | _O(n)_ | _O(n)_ | [Python](./python/solutions/trapping_rain_water) | PEAK peak PEAK | 72.91(52ms,1706278) ||

## <span id="string">String</span>
| No. |  Title  |  Difficulty  |  Time  |  Space  |  Solution  |  Tip  | Runtime |
|:---:|:-------|:------------:|:------:|:-------:|:----------:|:-------|:-------|
3 | [Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters) | Medium | _O(n)_ | _O(n)_ | [Python](./python/solutions/longest_substring_without_repeating_characters) | between the same | 88.87(89ms, 1704)||
5 | [Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring) | Medium | _O(n)_ | _O(n)_ | [Python](./python/solutions/longest_palindromic_substring) | Manacher | 71.48(376ms, 1703) ||
6 | [ZigZag Conversion](https://leetcode.com/problems/zigzag-conversion) | Medium | _O(n)_ | _O(1)_ | [Python](./python/solutions/zigzag_conversion) | join | 61.39(122ms, 1703) ||
8 | [String to Integer (atoi)](https://leetcode.com/problems/string-to-integer-atoi) | Medium | _O(n)_ | _O(1)_ | [Python](./python/solutions/string_to_integer) | | 44.69(78ms, 1704) ||
10 | [Regular Expression Matching](https://leetcode.com/problems/regular-expression-matching) | Hard | _O(mn)_ | _O(mn)_ | [Python](./python/solutions/regular_expression_matching) | | 85.45(82ms, 1705) ||
12 | [Integer to Roman](https://leetcode.com/problems/integer-to-roman) | Medium | _O(n)_ | _O(1)_ | [Python](./python/solutions/Integer_to_Roman) | directly | 90.62(105ms, 1705) ||
13 | [Roman to Integer](https://leetcode.com/problems/roman-to-integer) | Medium | _O(n)_ | _O(1)_ | [Python](./python/solutions/Roman_to_Integer) | lambda | 88.58(132ms, 1705) ||
14 | [Longest Common Prefix](https://leetcode.com/problems/longest-common-prefix) | Easy | _O(mn)_ | _O(1)_ | [Python](./python/solutions/longest_common_prefix) | zip is better | 84.60(42ms, 1704) ||
17 | [Letter Combinations of a Phone Number](https://leetcode.com/problems/letter-combinations-of-a-phone-number) | Medium | _O(4^n)_ | _O(n)_ | [Python](./python/solutions/letter_combinations_of_a_phone_number) | reduce works | 62.18(42ms, 1705) ||
20 | [Valid Parentheses](https://leetcode.com/problems/valid-parentheses) | Easy | _O(n)_ | _O(n)_ | [Python](./python/solutions/valid_parentheses) | | 92.77(39ms, 1703) ||
22 | [Generate Parentheses](https://leetcode.com/problems/generate-parentheses) | Medium | O(4^n / n^(3/2)) | _O(n)_ | [Python](./python/solutions/generate_parentheses) | generate, closed? | 28.90(65ms, 1703) ||
28 | [Implement strStr()](https://leetcode.com/problems/implement-strstr) | Easy | _O(mn)_ | _O(n)_ | [Python](./python/solutions/implement_strStr) | | 41.03(58ms, 1703) ||
30 | [Substring with Concatenation of All Words](https://leetcode.com/problems/substring-with-concatenation-of-all-words) | Hard | _O(mnk)_ | _O(nk)_ | [Python](./python/solutions/substring_with_oncatenation_of_all_words) | use find info | 70.72(98ms,170620) ||
32 | [Longest Valid Parentheses](https://leetcode.com/problems/longest-valid-parentheses) | Hard | _O(n)_ | _O(1)_ | [Python](./python/solutions/longest_valid_parentheses) | | 72.88(79ms,170614) ||
38 | [Count and Say](https://leetcode.com/problems/count-and-say) | Hard | _O(n)_ | _O(1)_ | [Python](./python/solutions/count_and_say) | pythonchallenge(level 10) | 41.89(55ms, 1705) ||
43 | [Multiply Strings](https://leetcode.com/problems/multiply-strings) | Medium | _O(m*n)_ | _O(m+n)_ | [Python](./python/solutions/multiply_strings) | carry, once |  94.76(49ms,1704)/76.65(168ms,170629) ||
44 | [Wildcard Matching](https://leetcode.com/problems/wildcard-matching) | Hard | _O(m*n)_ | _O(1)_ | [Python](./python/solutions/wildcard_matching) | | 86.49(109ms,1704)  ||
49 | [Group Anagrams](https://leetcode.com/problems/group-anagrams) | Medium | _O(mn)_ | _O(mn)_ | [Python](./python/solutions/group_anagrams) | frequency with hash | 90.95(212ms, 170711) ||

## <span id="binary-search">Binary Search</span>
| No. |  Title  |  Difficulty  |  Time  |  Space  |  Solution  |  Tip  | Runtime |
|:---:|:-------|:------------:|:------:|:-------:|:----------:|:-------|:-------|
4 | [Median of Two Sorted Arrays](https://leetcode.com/problems/median-of-two-sorted-arrays) | Hard | _O(log(m+n))_ | _O(1)_ | [Python](./python/solutions/median_of_two_sorted_arrays) | find kth | 78.16(99ms, 1706)||
29 | [Divide Two Integers](https://leetcode.com/problems/divide-two-integers) | Medium | _O(m/n)_ | _O(1)_ | [Python](./python/solutions/divide_two_integers) | | 33.58(68ms, 1703) ||
33 | [Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array) | Medium | _O(logn)_ | _O(1)_ | [Python](./python/solutions/search_in_rotated_sorted_array) | Binary Search | 21.87(58ms, 1703) ||
34 | [Search for a Range](https://leetcode.com/problems/search-for-a-range) | Medium | _O(logn)_ | _O(1)_ | [Python](./python/solutions/search_for_a_range) | Search left, then right | 73.72(45ms,170620) ||
35 | [Search Insert Position](https://leetcode.com/problems/search-insert-position) | Easy | _O(logn)_ | _O(1)_ | [Python](./python/solutions/search_insert_position) | check range & bisect | 82.93(39ms,170620)  ||
50 | [Pow(x, n)](https://leetcode.com/problems/powx-n) | Medium | _O(m*n)_ | _O(m+n)_ | [Python](./python/solutions/powx_n) | | 74.33(39ns, 1705) ||

## <span id="divide-and-conquer">Divide & Conquer</span>
| No. |  Title  |  Difficulty  |  Time  |  Space  |  Solution  |  Tip  | Runtime |
|:---:|:-------|:------------:|:------:|:-------:|:----------:|:-------|:-------|
4 | [Median of Two Sorted Arrays](https://leetcode.com/problems/median-of-two-sorted-arrays) | Hard | _O(log(m+n))_ | _O(1)_ | [Python](./python/solutions/median_of_two_sorted_arrays) | find kth | 78.16(99ms, 1706)||
23 | [Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists) | Hard | _O(nlogk)_ | _O(1)_ | [Python](./python/solutions/merge_k_sorted_list) |  | 98.15(105ms, 1703) ||

## <span id="backtracking">Backtracking</span>
| No. |  Title  |  Difficulty  |  Time  |  Space  |  Solution  |  Tip  | Runtime |
|:---:|:-------|:------------:|:------:|:-------:|:----------:|:-------|:-------|
10 | [Regular Expression Matching](https://leetcode.com/problems/regular-expression-matching) | Hard | _O(mn)_ | _O(mn)_ | [Python](./python/solutions/regular_expression_matching) | | 85.45(82ms, 1705) ||
17 | [Letter Combinations of a Phone Number](https://leetcode.com/problems/letter-combinations-of-a-phone-number) | Medium | _O(4^n)_ | _O(n)_ | [Python](./python/solutions/letter_combinations_of_a_phone_number) | reduce works | 62.18(42ms, 1705) ||
22 | [Generate Parentheses](https://leetcode.com/problems/generate-parentheses) | Medium | O(4^n / n^(3/2)) | _O(n)_ | [Python](./python/solutions/generate_parentheses) | generate, closed? | 28.90(65ms, 1703) ||
37 | [Sudoku Solver](https://leetcode.com/problems/sudoku-solver) | Hard | _O((9!)^9)_ | _O(1)_ | [Python](./python/solutions/sudoku_solver) | check then put, if wrong backtracking. Or play like human | 90.91(72ms,170623) ||
39 | [Combination Sum](https://leetcode.com/problems/combination-sum) | Medium | _O(k*n^k)_ | _O(k^2)_ | [Python](./python/solutions/combination_sum) | backtracking, check target | 99.81(72ms,170625) ||
40 | [Combination Sum II](https://leetcode.com/problems/combination-sum-ii) | Medium | _O(k*n^k)_ | _O(k^2)_ | [Python](./python/solutions/combination_sum_II) | | 93.17(65ms,170626) ||
44 | [Wildcard Matching](https://leetcode.com/problems/wildcard-matching) | Hard | _O(m*n)_ | _O(1)_ | [Python](./python/solutions/wildcard_matching) | | 86.49(109ms,1704)  ||
46 | [Permutations](https://leetcode.com/problems/permutations) | Medium | _O(n!)_ | _O(n*n!)_ | [Python](./python/solutions/permutations) | | 87.53(66ms,1704)  ||
47 | [Permutations II](https://leetcode.com/problems/permutations-ii) | Medium | _O(n!)_ | _O(n*n!)_ | [Python](./python/solutions/permutationsII) | | _94.36（99ms）_  ||
51 | [N-Queens](https://leetcode.com/problems/n-queens) | Hard | _O(n^3)_ | _O(n*n)_ | [Python](./python/solutions/n_queens) | bit | 100(62ms, 20170717)  ||

## <span id="dynamic-programming">Dynamic Programming</span>
| No. |  Title  |  Difficulty  |  Time  |  Space  |  Solution  |  Tip  | Runtime |
|:---:|:-------|:------------:|:------:|:-------:|:----------:|:-------|:-------|
10 | [Regular Expression Matching](https://leetcode.com/problems/regular-expression-matching) | Hard | _O(mn)_ | _O(mn)_ | [Python](./python/solutions/regular_expression_matching) | | 85.45(82ms, 1705) ||
32 | [Longest Valid Parentheses](https://leetcode.com/problems/longest-valid-parentheses) | Hard | _O(n)_ | _O(1)_ | [Python](./python/solutions/longest_valid_parentheses) | | 72.88(79ms,170614)  ||
44 | [Wildcard Matching](https://leetcode.com/problems/wildcard-matching) | Hard | _O(m*n)_ | _O(1)_ | [Python](./python/solutions/wildcard_matching) | | 86.49(109ms,1704)  ||

## <span id="stack">Stack</span>
| No. |  Title  |  Difficulty  |  Time  |  Space  |  Solution  |  Tip  | Runtime |
|:---:|:-------|:------------:|:------:|:-------:|:----------:|:-------|:-------|
20 | [Valid Parentheses](https://leetcode.com/problems/valid-parentheses) | Easy | _O(n)_ | _O(n)_ | [Python](./python/solutions/valid_parentheses) | | 92.77(39ms, 1703) ||
42 | [Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water) | Hard | _O(n)_ | _O(n)_ | [Python](./python/solutions/trapping_rain_water) | PEAK peak PEAK | 72.91(52ms,1706278) ||

## <span id="heap">Heap</span>
| No. |  Title  |  Difficulty  |  Time  |  Space  |  Solution  |  Tip  | Runtime |
|:---:|:-------|:------------:|:------:|:-------:|:----------:|:-------|:-------|
23 | [Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists) | Hard | _O(nlogk)_ | _O(1)_ | [Python](./python/solutions/merge_k_sorted_list) | replace | 98.15(105ms, 1703) ||


## <span id="greedy">Greedy</span>
| No. |  Title  |  Difficulty  |  Time  |  Space  |  Solution  |  Tip  | Runtime |
|:---:|:-------|:------------:|:------:|:-------:|:----------:|:-------|:-------|
44 | [Wildcard Matching](https://leetcode.com/problems/wildcard-matching) | Hard | _O(m*n)_ | _O(1)_ | [Python](./python/solutions/wildcard_matching) | | 86.49(109ms,1704)  ||
45 | [Jump Game II](https://leetcode.com/problems/jump-game-ii) | Hard | _O(n)_ | _O(n)_ | [Python](./python/solutions/tjump_game_ii) | | 98.24(49ms,170705) ||


<!--
<meta http-equiv="refresh" content="5">
-->


