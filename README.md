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
* [Greedy](#greedy)
## <span id=""></span>
* [Design](#design)
## <span id=""></span>
-->

## <span id="array">Array</span>
| No. |  Title  |  Difficulty  |  Time  |  Space  |  Solution  |  Tip  | 
|:---:|:-------|:------------:|:------:|:-------:|:----------:|:-------|
1 | [Two Sum](https://leetcode.com/problems/two-sum) | Easy | _O(n)_ | _O(n)_ | [Python](./python/solutions/two_sum) | set ||
4 | [Median of Two Sorted Arrays](https://leetcode.com/problems/median-of-two-sorted-arrays) | Hard | _O(log(m+n))_ | _O(1)_ | [Python](./python/solutions/median_of_two_sorted_arrays) | find kth ||
11 | [Container With Most Water](https://leetcode.com/problems/container-with-most-water) | Medium | _O(n)_ | _O(1)_ | [Python](./python/solutions/container_with_most_water) | from limit ||
15 | [3Sum](https://leetcode.com/problems/3sum) | Medium | _O(n^2)_ | _O(1)_ | [Python](./python/solutions/3sum) | sorted, meet ||
16 | [3Sum Closest](https://leetcode.com/problems/3sum-closest) | Medium | _O(n^2)_ | _O(1)_ | [Python](./python/solutions/3sum_closest) | sorted, meet ||
18 | [4Sum](https://leetcode.com/problems/4sum) | Medium | _O(n^3)_ | _O(1)_ | [Python](./python/solutions/4sum) | 3sum ||
26 | [Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array) | Easy | _O(n)_ | _O(1)_ | [Python](./python/solutions/remove_duplicates_from_sorted_array) |  ||
27 | [Remove Element](https://leetcode.com/problems/remove-element) | Easy | _O(n)_ | _O(1)_ | [Python](./python/solutions/remove_element) |  ||
31 | [Next Permutation](https://leetcode.com/problems/next-permutation) | Medium | _O(n)_ | _O(1)_ | [Python](./python/solutions/next_permutation) |  ||
33 | [Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array) | Medium | _O(logn)_ | _O(1)_ | [Python](./python/solutions/search_in_rotated_sorted_array) | Binary Search ||
34 | [Search for a Range](https://leetcode.com/problems/search-for-a-range) | Medium | _O(logn)_ | _O(1)_ | [Python](./python/solutions/search_for_a_range) | Binary Search left, then right ||

## <span id="hash-table">Hash Table</span>
| No. |  Title  |  Difficulty  |  Time  |  Space  |  Solution  |  Tip  | 
|:---:|:-------|:------------:|:------:|:-------:|:----------:|:-------|
1 | [Two Sum](https://leetcode.com/problems/two-sum) | Easy | _O(n)_ | _O(n)_ | [Python](./python/solutions/two_sum) | set ||
3 | [Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters) | Medium | _O(n)_ | _O(n)_ | [Python](./python/solutions/longest_substring_without_repeating_characters) | between the same ||
18 | [4Sum](https://leetcode.com/problems/4sum) | Medium | _O(n^3)_ | _O(1)_ | [Python](./python/solutions/4sum) | 3sum ||
30 | [Substring with Concatenation of All Words](https://leetcode.com/problems/substring-with-concatenation-of-all-words) | Hard | _O(mnk)_ | _O(nk)_ | [Python](./python/solutions/substring_with_oncatenation_of_all_words) | use find info ||

## <span id="linked-list">Linked List</span>
| No. |  Title  |  Difficulty  |  Time  |  Space  |  Solution  |  Tip  | 
|:---:|:-------|:------------:|:------:|:-------:|:----------:|:-------|
2 | [Add Two Numbers](https://leetcode.com/problems/add-two-numbers) | Medium | _O(n)_ | _O(1)_ | [Python](./python/solutions/add_two_numbers) |  ||
19 | [Remove Nth Node From End of List](https://leetcode.com/problems/remove-nth-node-from-end-of-list) | Easy | _O(n)_ | _O(1)_ | [Python](./python/solutions/remove_nth_node_from_end_of_list) |  ||
21 | [Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists) | Easy | _O(n)_ | _O(1)_ | [Python](./python/solutions/merge_two_sorted_lists) |  ||
23 | [Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists) | Hard | _O(nlogk)_ | _O(1)_ | [Python](./python/solutions/merge_k_sorted_list) |  ||
24 | [Swap Nodes in Pairs](https://leetcode.com/problems/swap-nodes-in-pairs) | Easy | _O(n)_ | _O(1)_ | [Python](./python/solutions/swap_nodes_in_pairs) |  ||
25 | [Reverse Nodes in k-Group](https://leetcode.com/problems/reverse-nodes-in-k-group) | Hard | _O(n)_ | _O(1)_ | [Python](./python/solutions/reverse_nodes_in_k_group) |  ||


## <span id="math">Math</span>
| No. |  Title  |  Difficulty  |  Time  |  Space  |  Solution  |  Tip  | 
|:---:|:-------|:------------:|:------:|:-------:|:----------:|:-------|
2 | [Add Two Numbers](https://leetcode.com/problems/add-two-numbers) | Medium | _O(n)_ | _O(1)_ | [Python](./python/solutions/add_two_numbers) |  ||
7 | [Reverse Integer](https://leetcode.com/problems/reverse-integer) |  Easy | _O(n)_ | _O(1)_ | [Python](./python/solutions/reverse_integer) |  ||
8 | [String to Integer (atoi)](https://leetcode.com/problems/string-to-integer-atoi) | Medium | _O(n)_ | _O(1)_ | [Python](./python/solutions/string_to_integer) |  ||
9 | [Palindrome Number](https://leetcode.com/problems/palindrome-number) | Easy | _O(n)_ | _O(1)_ | [Python](./python/solutions/palindrome_number) |  ||
12 | [Integer to Roman](https://leetcode.com/problems/integer-to-roman) | Medium | _O(n)_ | _O(1)_ | [Python](./python/solutions/Integer_to_Roman) | directly ||
13 | [Roman to Integer](https://leetcode.com/problems/roman-to-integer) | Medium | _O(n)_ | _O(1)_ | [Python](./python/solutions/Roman_to_Integer) | lambda ||
29 | [Divide Two Integers](https://leetcode.com/problems/divide-two-integers) | Medium | _O(m/n)_ | _O(1)_ | [Python](./python/solutions/divide_two_integers) |  ||

## <span id="two-pointers">Two Pointers</span>
| No. |  Title  |  Difficulty  |  Time  |  Space  |  Solution  |  Tip  | 
|:---:|:-------|:------------:|:------:|:-------:|:----------:|:-------|
3 | [Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters) | Medium | _O(n)_ | _O(n)_ | [Python](./python/solutions/longest_substring_without_repeating_characters) | between the same ||
11 | [Container With Most Water](https://leetcode.com/problems/container-with-most-water) | Medium | _O(n)_ | _O(1)_ | [Python](./python/solutions/container_with_most_water) | from limit ||
15 | [3Sum](https://leetcode.com/problems/3sum) | Medium | _O(n^2)_ | _O(1)_ | [Python](./python/solutions/3sum) | sorted, meet ||
16 | [3Sum Closest](https://leetcode.com/problems/3sum-closest) | Medium | _O(n^2)_ | _O(1)_ | [Python](./python/solutions/3sum_closest) | sorted, meet ||
18 | [4Sum](https://leetcode.com/problems/4sum) | Medium | _O(n^3)_ | _O(1)_ | [Python](./python/solutions/4sum) | 3sum ||
19 | [Remove Nth Node From End of List](https://leetcode.com/problems/remove-nth-node-from-end-of-list) | Medium | _O(n)_ | _O(1)_ | [Python](./python/solutions/remove_nth_node_from_end_of_list) |  ||
26 | [Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array) | Easy | _O(n)_ | _O(1)_ | [Python](./python/solutions/remove_duplicates_from_sorted_array) |  ||
27 | [Remove Element](https://leetcode.com/problems/remove-element) | Easy | _O(n)_ | _O(1)_ | [Python](./python/solutions/remove_element) |  ||
28 | [Implement strStr()](https://leetcode.com/problems/implement-strstr) | Easy | _O(mn)_ | _O(n)_ | [Python](./python/solutions/implement_strStr) |  ||
30 | [Substring with Concatenation of All Words](https://leetcode.com/problems/substring-with-concatenation-of-all-words) | Hard | _O(mnk)_ | _O(nk)_ | [Python](./python/solutions/substring_with_oncatenation_of_all_words) | use find info ||

## <span id="string">String</span>
| No. |  Title  |  Difficulty  |  Time  |  Space  |  Solution  |  Tip  | 
|:---:|:-------|:------------:|:------:|:-------:|:----------:|:-------|
3 | [Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters) | Medium | _O(n)_ | _O(n)_ | [Python](./python/solutions/longest_substring_without_repeating_characters) | between the same ||
5 | [Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring) | Medium | _O(n)_ | _O(n)_ | [Python](./python/solutions/longest_palindromic_substring) | Manacher ||
6 | [ZigZag Conversion](https://leetcode.com/problems/zigzag-conversion) | Medium | _O(n)_ | _O(1)_ | [Python](./python/solutions/zigzag_conversion) | join ||
8 | [String to Integer (atoi)](https://leetcode.com/problems/string-to-integer-atoi) | Medium | _O(n)_ | _O(1)_ | [Python](./python/solutions/string_to_integer) |  ||
10 | [Regular Expression Matching](https://leetcode.com/problems/regular-expression-matching) | Hard | _O(mn)_ | _O(mn)_ | [Python](./python/solutions/regular_expression_matching) |  ||
12 | [Integer to Roman](https://leetcode.com/problems/integer-to-roman) | Medium | _O(n)_ | _O(1)_ | [Python](./python/solutions/Integer_to_Roman) | directly ||
13 | [Roman to Integer](https://leetcode.com/problems/roman-to-integer) | Medium | _O(n)_ | _O(1)_ | [Python](./python/solutions/Roman_to_Integer) | lambda ||
14 | [Longest Common Prefix](https://leetcode.com/problems/longest-common-prefix) | Easy | _O(mn)_ | _O(1)_ | [Python](./python/solutions/longest_common_prefix) | zip is better ||
17 | [Letter Combinations of a Phone Number](https://leetcode.com/problems/letter-combinations-of-a-phone-number) | Medium | _O(4^n)_ | _O(n)_ | [Python](./python/solutions/letter_combinations_of_a_phone_number) | reduce works ||
20 | [Valid Parentheses](https://leetcode.com/problems/valid-parentheses) | Easy | _O(n)_ | _O(n)_ | [Python](./python/solutions/valid_parentheses) |  ||
22 | [Generate Parentheses](https://leetcode.com/problems/generate-parentheses) | Medium | O(4^n / n^(3/2)) | _O(n)_ | [Python](./python/solutions/generate_parentheses) | generate, closed? ||
28 | [Implement strStr()](https://leetcode.com/problems/implement-strstr) | Easy | _O(mn)_ | _O(n)_ | [Python](./python/solutions/implement_strStr) |  ||
30 | [Substring with Concatenation of All Words](https://leetcode.com/problems/substring-with-concatenation-of-all-words) | Hard | _O(mnk)_ | _O(nk)_ | [Python](./python/solutions/substring_with_oncatenation_of_all_words) | use find info ||
32 | [Longest Valid Parentheses](https://leetcode.com/problems/longest-valid-parentheses) | Hard | _O(n)_ | _O(1)_ | [Python](./python/solutions/longest_valid_parentheses) | ||

## <span id="binary-search">Binary Search</span>
| No. |  Title  |  Difficulty  |  Time  |  Space  |  Solution  |  Tip  | 
|:---:|:-------|:------------:|:------:|:-------:|:----------:|:-------|
4 | [Median of Two Sorted Arrays](https://leetcode.com/problems/median-of-two-sorted-arrays) | Hard | _O(log(m+n))_ | _O(1)_ | [Python](./python/solutions/median_of_two_sorted_arrays) | find kth ||
29 | [Divide Two Integers](https://leetcode.com/problems/divide-two-integers) | Medium | _O(m/n)_ | _O(1)_ | [Python](./python/solutions/divide_two_integers) |  ||
33 | [Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array) | Medium | _O(logn)_ | _O(1)_ | [Python](./python/solutions/search_in_rotated_sorted_array) | Binary Search ||
34 | [Search for a Range](https://leetcode.com/problems/search-for-a-range) | Medium | _O(logn)_ | _O(1)_ | [Python](./python/solutions/search_for_a_range) | Search left, then right ||

## <span id="divide-and-conquer">Divide & Conquer</span>
| No. |  Title  |  Difficulty  |  Time  |  Space  |  Solution  |  Tip  | 
|:---:|:-------|:------------:|:------:|:-------:|:----------:|:-------|
4 | [Median of Two Sorted Arrays](https://leetcode.com/problems/median-of-two-sorted-arrays) | Hard | _O(log(m+n))_ | _O(1)_ | [Python](./python/solutions/median_of_two_sorted_arrays) | find kth ||
23 | [Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists) | Hard | _O(nlogk)_ | _O(1)_ | [Python](./python/solutions/merge_k_sorted_list) |  ||

## <span id="backtracking">Backtracking</span>
| No. |  Title  |  Difficulty  |  Time  |  Space  |  Solution  |  Tip  | 
|:---:|:-------|:------------:|:------:|:-------:|:----------:|:-------|
10 | [Regular Expression Matching](https://leetcode.com/problems/regular-expression-matching) | Hard | _O(mn)_ | _O(mn)_ | [Python](./python/solutions/regular_expression_matching) |  ||
17 | [Letter Combinations of a Phone Number](https://leetcode.com/problems/letter-combinations-of-a-phone-number) | Medium | _O(4^n)_ | _O(n)_ | [Python](./python/solutions/letter_combinations_of_a_phone_number) | reduce works ||
22 | [Generate Parentheses](https://leetcode.com/problems/generate-parentheses) | Medium | O(4^n / n^(3/2)) | _O(n)_ | [Python](./python/solutions/generate_parentheses) | generate, closed? ||

## <span id="dynamic-programming">Dynamic Programming</span>
| No. |  Title  |  Difficulty  |  Time  |  Space  |  Solution  |  Tip  | 
|:---:|:-------|:------------:|:------:|:-------:|:----------:|:-------|
10 | [Regular Expression Matching](https://leetcode.com/problems/regular-expression-matching) | Hard | _O(mn)_ | _O(mn)_ | [Python](./python/solutions/regular_expression_matching) |  ||
32 | [Longest Valid Parentheses](https://leetcode.com/problems/longest-valid-parentheses) | Hard | _O(n)_ | _O(1)_ | [Python](./python/solutions/longest_valid_parentheses) | ||

## <span id="stack">Stack</span>
| No. |  Title  |  Difficulty  |  Time  |  Space  |  Solution  |  Tip  | 
|:---:|:-------|:------------:|:------:|:-------:|:----------:|:-------|
20 | [Valid Parentheses](https://leetcode.com/problems/valid-parentheses) | Easy | _O(n)_ | _O(n)_ | [Python](./python/solutions/valid_parentheses) |  ||

## <span id="heap">Heap</span>
| No. |  Title  |  Difficulty  |  Time  |  Space  |  Solution  |  Tip  | 
|:---:|:-------|:------------:|:------:|:-------:|:----------:|:-------|
23 | [Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists) | Hard | _O(nlogk)_ | _O(1)_ | [Python](./python/solutions/merge_k_sorted_list) | replace ||

<!--
<meta http-equiv="refresh" content="5">
-->


