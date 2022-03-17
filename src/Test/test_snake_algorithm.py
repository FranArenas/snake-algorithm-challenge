"""
Test module for the snake solutions algorithm
"""

import pytest

from ..snake_challenge.data_structures import Snake, Board
from ..snake_challenge.snake_algorithm import calculate_snake_solutions

# --------------------------
# Test 1: test input errors
# --------------------------

# Snake out of board
test_1_snake_1 = [[-1, 0], [0, 1], [1, 1]]
test_1_board_1 = [4, 3]
test_1_depth_1 = 3
test_1_result_1 = None

# Snake len < 2
test_1_snake_2 = [[0, 0]]
test_1_board_2 = [4, 3]
test_1_depth_2 = 3
test_1_result_2 = None

# Snake len > 7
test_1_snake_3 = [[i, 0] for i in range(8)]
test_1_board_3 = [8, 1]
test_1_depth_3 = 3
test_1_result_3 = None

# Snake[i][j] >= board[j]
test_1_snake_4 = [[7, 2], [3, 2], [3, 1]]
test_1_board_4 = [4, 3]
test_1_depth_4 = 3
test_1_result_4 = None

# Board[j] < 1
test_1_snake_5 = [[2, 2], [3, 2], [3, 1], [3, 0], [2, 0], [1, 0], [0, 0]]
test_1_board_5 = [0, 3]
test_1_depth_5 = 3
test_1_result_5 = None

# Board[j] > 10
test_1_snake_6 = [[2, 2], [3, 2], [3, 1], [3, 0], [2, 0], [1, 0], [0, 0]]
test_1_board_6 = [2, 11]
test_1_depth_6 = 3
test_1_result_6 = None

# Depth < 1
test_1_snake_7 = [[2, 2], [3, 2], [3, 1], [3, 0], [2, 0], [1, 0], [0, 0]]
test_1_board_7 = [4, 3]
test_1_depth_7 = 0
test_1_result_7 = 7

# Depth > 20
test_1_snake_8 = [[2, 2], [3, 2], [3, 1], [3, 0], [2, 0], [1, 0], [0, 0]]
test_1_board_8 = [4, 3]
test_1_depth_8 = 21
test_1_result_8 = 7

test_1_params = [(test_1_snake_1, test_1_board_1, test_1_depth_1, test_1_result_1),
                 (test_1_snake_2, test_1_board_2, test_1_depth_2, test_1_result_2),
                 (test_1_snake_3, test_1_board_3, test_1_depth_3, test_1_result_3),
                 (test_1_snake_4, test_1_board_4, test_1_depth_4, test_1_result_4),
                 (test_1_snake_5, test_1_board_5, test_1_depth_5, test_1_result_5),
                 (test_1_snake_6, test_1_board_6, test_1_depth_6, test_1_result_6),
                 (test_1_snake_7, test_1_board_7, test_1_depth_7, test_1_result_7),
                 (test_1_snake_8, test_1_board_8, test_1_depth_8, test_1_result_8)]


@pytest.mark.parametrize("snake, board, depth, result", test_1_params)
def test_calculate_snake_solutions_input(snake: Snake,
                                         board: Board,
                                         depth: int,
                                         result: int):
    """
    Test for calculate_snake_solutions function

    Args:
        snake:  representation of the positions of a snake in the board.
        board: two-dimensional space where the snake will be moving.
        depth: number of movements of the snake.

    """
    try:
        calculate_snake_solutions(snake=snake, board=board, depth=depth)
    except ValueError:
        assert True
    else:
        assert False


# -------------------
# Test 2: test output
# -------------------

test_2_snake_1 = [[2, 2], [3, 2], [3, 1], [3, 0], [2, 0], [1, 0], [0, 0]]
test_2_board_1 = [4, 3]
test_2_depth_1 = 3
test_2_result_1 = 7

test_2_snake_2 = [[0, 2], [0, 1], [0, 0], [1, 0], [1, 1], [1, 2]]
test_2_board_2 = [2, 3]
test_2_depth_2 = 10
test_2_result_2 = 1

test_2_snake_3 = [[5, 5], [5, 4], [4, 4], [4, 5]]
test_2_board_3 = [10, 10]
test_2_depth_3 = 4
test_2_result_3 = 81

test_2_params = [(test_2_snake_1, test_2_board_1, test_2_depth_1, test_2_result_1),
                 (test_2_snake_2, test_2_board_2, test_2_depth_2, test_2_result_2),
                 (test_2_snake_3, test_2_board_3, test_2_depth_3, test_2_result_3)]


@pytest.mark.parametrize("snake, board, depth, result", test_2_params)
def test_calculate_snake_solutions_output(snake: Snake,
                                          board: Board,
                                          depth: int,
                                          result: int):
    """
    Test for calculate_snake_solutions function

    Args:
        snake:  representation of the positions of a snake in the board.
        board: two-dimensional space where the snake will be moving.
        depth: number of movements of the snake.

    """
    assert calculate_snake_solutions(snake=snake, board=board, depth=depth) == result
