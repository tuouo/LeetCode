#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 2017/6/22
import unittest


class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        return self.set_valid(board)

    def set_valid(self, board):
        pos = set()
        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    cur = board[i][j]  # cur is str
                    if (i, cur) in pos or (cur, j) in pos or (i // 3, j // 3, cur) in pos:
                        return False
                    pos.add((i, cur))
                    pos.add((cur, i))
                    pos.add((i // 3, j // 3, cur))
        return True

    def base_valid(self, board):
        return self.is_row_valid(board) and self.is_col_valid(board) and self.is_box_valid(board)

    def is_line_valid(self, line):
        line = filter(lambda x: x != ".", line)
        return len(set(line)) == len(list(line))

    def is_row_valid(self, board):
        for row in board:
            if not self.is_line_valid(row):
                return False
        return True

    def is_col_valid(self, board):
        for col in zip(*board):
            if not self.is_line_valid(col):
                return False
        return True

    def is_box_valid(self, board):
        for r in range(3):
            for c in range(3):
                if not self.is_line_valid(
                        [board[i][j] for j in range(3 * r, 3 * r + 3) for i in range(3 * c, 3 * c + 3)]):
                    return False
        return True


class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_valid(self):
        board = ["..4...63.", ".........", "5......9.", "...56....", "4.3.....1", "...7.....", "...5.....",
                 ".........", "........."]
        self.assertEqual(Solution().isValidSudoku(board), False)


if __name__ == '__main__':
    unittest.main()
