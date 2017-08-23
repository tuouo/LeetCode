#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 2017/8/23
import unittest


class Solution(object):
    def fullJustify(self, words, maxWidth):  # 59.32 35ms
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        result, start, get = [], 0, 0
        for i in range(len(words)):
            get += len(words[i])
            if get + (i - start) > maxWidth:
                if i - start == 1:
                    result += [words[start] + (maxWidth - len(words[start])) * " "]
                else:
                    avg, least = divmod(maxWidth - get + len(words[i]), i - start - 1)
                    line = words[start:i]
                    for count in range(least):
                        line[count] += " "
                    result += [(" " * avg).join(line)]
                get, start = len(words[i]), i

        line = " ".join(words[start:])
        result += [line + (maxWidth - len(line)) * " "]
        return result


class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_solution(self):
        self.assertEqual(Solution().fullJustify(["This", "is", "an", "example", "of", "text", "justification."], 16),
                         ["This    is    an", "example  of text", "justification.  "])


if __name__ == '__main__':
    unittest.main()
