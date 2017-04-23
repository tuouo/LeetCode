#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 2017/4/23
import unittest


class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        return Solution.convert_append(s, numRows)

    @classmethod
    def convert_zip(cls, s, num_rows):
        if num_rows < 2 or num_rows > len(s):
            return s
        from itertools import zip_longest
        step, end = 2 * num_rows - 2, num_rows - 1
        zigzag = s[::step]
        for i in range(1, end):
            for left, right in zip_longest(s[i::step], s[step-i::step], fillvalue=""):
                zigzag += left + right
        return zigzag + s[end::step]

    @classmethod
    def convert_add_list(cls, s, num_rows):
        if num_rows < 2 or num_rows > len(s):
            return s
        zigzag, num, step, end = [[]] * num_rows, 0, -1, num_rows - 1
        for item in s:
                zigzag[num] += item
                if num == 0 or num == end:
                    step = -step
                num += step
        return "".join("".join(row) for row in zigzag)

    @classmethod
    def convert_add_list2(cls, s, num_rows):
        if num_rows < 2 or num_rows > len(s):
            return s
        zigzag, num, step, end = [[]] * num_rows, 0, -1, num_rows - 1
        for item in s:
                zigzag[num] += item
                if num == 0 or num == end:
                    step = -step
                num += step
        return "".join([item for row in zigzag for item in row])

    @classmethod
    def convert_str_list(cls, s, num_rows):
        if num_rows < 2 or num_rows > len(s):
            return s
        zigzag, num, step, end = [""] * num_rows, 0, -1, num_rows - 1
        for item in s:
            zigzag[num] += item
            if num == 0 or num == end:
                step = -step
            num += step
        return "".join(zigzag)

    @classmethod
    def convert_append(cls, s, num_rows):
        if num_rows < 2 or num_rows > len(s):
            return s
        zigzag, length, step = [], len(s), 2 * num_rows - 2
        for i in range(num_rows):
            for j in range(i, length, step):
                zigzag.append(s[j])
                if 0 < i < num_rows - 1 and j + step - 2 * i < length:
                    zigzag.append(s[j + step - 2 * i])
        return "".join(zigzag)

    @classmethod
    def convert_add(cls, s, num_rows):
        if num_rows < 2 or num_rows > len(s):
            return s
        zigzag, length, step = "", len(s), 2 * num_rows - 2
        for i in range(num_rows):
            for j in range(i, length, step):
                zigzag += s[j]
                if 0 < i < num_rows - 1 and j + step - 2 * i < length:
                    zigzag += s[j + step - 2 * i]
        return zigzag

    @classmethod
    def convert_io(cls, s, num_rows):
        if num_rows < 2 or num_rows > len(s):
            return s
        # from cStringIO import StringIO
        from io import StringIO
        file_str = StringIO()
        length, step = len(s), 2 * num_rows - 2
        for i in range(num_rows):
            for j in range(i, length, step):
                file_str.write(s[j])
                if 0 < i < num_rows - 1 and j + step - 2 * i < length:
                    file_str.write(s[j + step - 2 * i])
        return file_str.getvalue()

    @classmethod
    def convert_list(cls, s, num_rows):
        if num_rows < 2 or num_rows > len(s):
            return s
        limit = 2 * num_rows - 2
        return "".join(s[j] for i in range(num_rows) for j in range(len(s)) if j % limit == i or (j + i) % limit == 0)

    @classmethod
    def convert_gen(cls, s, numRows):
        if numRows < 2 or numRows > len(s):
            return s

        def index_list(lens, num_rows):
            limit = 2 * (num_rows - 1)
            for num in range(num_rows):
                for pos in range(lens):
                    if pos % limit == num or (pos + num) % limit == 0:
                        yield pos

        return "".join(s[i] for i in index_list(len(s), numRows))


class TestCase(unittest.TestCase):
    def setUp(self):
        self.string = "wkpacxzafxqkxsvmjqeadpbmvbtbupgsbysdvtecqwmqqiecaicdyervhkyebhwcfricmofdmttddxfehjhhnbdxnbbp"
        self.result = "wcfxjdvubvqqayhbfmmdhnnkaxaxksmqapmbbpsydtcwqicidevkehcrcodtdxejhbxbppzqvebtgsemecrywiftfhdb"
        self.numRows = 3
        self.s = Solution()

    def tearDown(self):
        del self.string
        del self.numRows
        del self.s

    def test_solution(self):
        self.assertEqual(Solution.convert_append(self.string, self.numRows), self.result)
        self.assertEqual(Solution.convert_add(self.string, self.numRows), self.result)
        self.assertEqual(Solution.convert_io(self.string, self.numRows), self.result)
        self.assertEqual(Solution.convert_list(self.string, self.numRows), self.result)
        self.assertEqual(Solution.convert_gen(self.string, self.numRows), self.result)
        self.assertEqual(Solution.convert_str_list(self.string, self.numRows), self.result)
        self.assertEqual(Solution.convert_add_list(self.string, self.numRows), self.result)
        self.assertEqual(Solution.convert_add_list2(self.string, self.numRows), self.result)
        self.assertEqual(Solution.convert_zip(self.string, self.numRows), self.result)


if __name__ == '__main__':

    def timeit_test():
        import timeit
        timeit_str, setup_str = "Solution.{}({})", "from __main__ import Solution"
        args = "'wkpacxzafxqkxsvmjqeadpbmvbtbupgsbysdvtecqwmqqiecaicdyervhkyebhwcfricmofdmttddxfehjhhnbdxnbbp', 3"
        for method in dir(Solution):
            if not method.startswith("_"):
                fn = getattr(Solution, method, None)
                if callable(fn) and type(fn).__name__ == "method":
                    print(timeit.timeit(timeit_str.format(method, args), setup=setup_str), "\t", fn)

    unittest.main()
    # timeit_test()
