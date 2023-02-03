############################################################
# CIS 5210: Homework 4
############################################################

# Include your imports here, if any are used.

import collections
import copy
import itertools
import random
import math

student_name = "Type your full name here."

############################################################
# Section 1: Dominoes Game
############################################################
leaf = 0


def create_dominoes_game(rows, cols):
    lst = [[False for _ in range(cols)] for _ in range(rows)]
    return DominoesGame(lst)


class DominoesGame(object):

    # Required
    def __init__(self, board):
        self.board = board
        self.rows = len(board)
        self.cols = len(board[0])

    def get_board(self):
        return self.board

    def reset(self):
        self.board = [[False] * self.cols for _ in range(self.rows)]

    def is_legal_move(self, row, col, vertical):
        if row < 0 or row >= self.rows or col < 0 or col >= self.cols:
            return False
        if self.board[row][col]:
            return False
        if not vertical:
            if col + 1 >= self.cols:
                return False
            if self.board[row][col + 1]:
                return False
        if vertical:
            if row + 1 >= self.rows:
                return False
            if self.board[row + 1][col]:
                return False
        return True

    def legal_moves(self, vertical):
        for row in range(self.rows):
            for col in range(self.cols):
                if self.is_legal_move(row, col, vertical):
                    yield (row, col)

    def perform_move(self, row, col, vertical):
        self.board[row][col] = True
        if vertical:
            self.board[row + 1][col] = True
        else:
            self.board[row][col + 1] = True

    def game_over(self, vertical):
        for row in range(self.rows):
            for col in range(self.cols):
                if self.is_legal_move(row, col, vertical):
                    return False
        return True

    def copy(self):
        cpy = [[self.board[row][col]
                for col in range(self.cols)] for row in range(self.rows)]
        return DominoesGame(cpy)

    def successors(self, vertical):
        for row, col in self.legal_moves(vertical):
            cpy = self.copy()
            cpy.perform_move(row, col, vertical)
            yield (row, col), cpy, cpy.get_value(vertical)

    def get_value(self, vertical):
        return len(list(self.legal_moves(vertical))) - len(list(self.legal_moves(not vertical)))

    # Required

    def get_best_move(self, vertical, limit):
        """
        In the DominoesGame class, write a method get_best_move(self, vertical, limit) which returns a 3
        -element tuple containing:
        1.The best move for the current player as a (row, column) tuple, 
        2.Its associated value (defined below), 
        3.The number of leaf nodes visited during the search. 

        Moves should be explored row-major order:
        When looking at the board as a 2-d array, your method should be visualizable as iterating through the rows from top to bottom, and within rows from left to right), starting from the top-left corner of the board.

        To find a board's value, you should compute the number of moves available to the current player, then subtract the number of moves available to the opponent.
        """
        best_move = None
        best_value = None
        for successor in self.successors(vertical):
            value = successor[1].minimax(limit, not vertical, -math.inf, math.inf,
                                         successor[1].get_value(vertical))
            if best_value is None or value > best_value:
                best_value = value
                best_move = successor[0]
        return best_move, best_value, leaf

    def minimax(self, limit, vertical, alpha, beta, value):
        global leaf
        leaf += 1
        if limit == 0 or self.game_over(vertical):
            return value
        if vertical:
            max_eval = -math.inf
            for successor in self.successors(vertical):
                Eval = successor[1].minimax(
                    limit - 1, not vertical, alpha, beta, value)
                max_eval = max(max_eval, Eval)
                # if successor[1] > max_eval:
                #     maxx = successor[1]
                #     best_move = successor[0]
                alpha = max(alpha, max_eval)
                if beta <= alpha:
                    break
            return max_eval
        else:
            min_eval = math.inf
            for successor in self.successors(vertical):
                Eval = successor[1].minimax(
                    limit - 1, not vertical, alpha, beta, value)
                min_eval = min(min_eval, Eval)
                # if successor[1] < min_eval:
                #     minn = successor[1]
                #     best_move = successor[0]
                beta = min(beta, min_eval)
                if beta <= alpha:
                    break
            return min_eval


############################################################
# Section 2: Feedback
############################################################

feedback_question_1 = """
Type your response here.
Your response may span multiple lines.
Do not include these instructions in your response.
"""

feedback_question_2 = """
Type your response here.
Your response may span multiple lines.
Do not include these instructions in your response.
"""

feedback_question_3 = """
Type your response here.
Your response may span multiple lines.
Do not include these instructions in your response.
"""


def main():
    p = create_dominoes_game(3, 3)
    p.perform_move(0, 1, True)
    print(p.get_best_move(False, 2))


if __name__ == "__main__":
    main()
