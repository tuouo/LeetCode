#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 2017/6/9
import unittest


class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        return self.use_pre_find(s, words)

    def use_pre_find(self, s, words):
        if not s or not words:
            return []
        from collections import Counter
        from collections import defaultdict
        result, word_num, word_len, items = [], len(words), len(words[0]), Counter(words)

        for step in range(word_len):
            start, find, count = step, defaultdict(int), 0
            for word_start in range(step, len(s) - word_len + 1, word_len):
                word = s[word_start:word_start + word_len]
                if word in items:
                    find[word], count = find[word] + 1, count + 1
                    while find[word] > items[word]:
                        find[s[start:start + word_len]], count = find[s[start:start + word_len]] - 1, count - 1
                        start += word_len
                    if count == word_num:
                        result.append(start)
                else:
                    start, find, count = word_start + word_len, defaultdict(int), 0

        return result

    def just_find_for_join(self, s, words):
        from collections import defaultdict
        if not s or not words:
            return []
        result, word_num, word_len, items = [], len(words), len(words[0]), defaultdict(int)
        for i in words:
            items[i] += 1
        for i in range(len(s) + 1 - word_len * word_num):
            cur, j = defaultdict(int), 0
            while j < word_num:
                word = s[i + j * word_len:i + j * word_len + word_len]
                if word not in items:
                    break
                cur[word] += 1
                if cur[word] > items[word]:
                    break
                j += 1
            if j == word_num:
                result.append(i)
        return result


class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_find_next(self):
        self.assertEqual(Solution().findSubstring("barfoothefoobarman", ["foo", "bar"]), [0, 9])

if __name__ == '__main__':
    unittest.main()
