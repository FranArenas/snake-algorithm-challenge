"""
Module with logic to calculate the solutions for the snake algorithm
"""

from .constants import (SNAKE_MIN_LENGTH, SNAKE_MAX_LENGTH, MAX_DEPTH, MIN_DEPTH,
                        BOARD_MAX_X, BOARD_MIN_X, BOARD_MAX_Y, BOARD_MIN_Y)
from .data_structures import Snake, Board


def calculate_snake_solutions(snake: Snake,
                              board: Board,
                              depth: int) -> int:
    """
    Calculate the possible solutions for the snake algorithm with a given depth

    Args:
        snake:  representation of the positions of a snake in the board.
        board: two-dimensional space where the snake will be moving.
        depth: number of movements of the snake.

    Returns:
        The number of possible solutions for the snake algorithm
    """
    ...
    _check_input(snake, board, depth)


def _check_input(snake: Snake,
                 board: Board,
                 depth: int) -> None:
    """
    Checks if the input values are correct

    Args:
        snake:  representation of the positions of a snake in the board.
        board: two-dimensional space where the snake will be moving.
        depth: number of movements of the snake.
    Raises:
         ValueError if the input aren't correct

    """
    # snake
    if SNAKE_MIN_LENGTH > len(snake) or SNAKE_MAX_LENGTH < len(snake):
        raise ValueError(f"Snake len should be > {SNAKE_MIN_LENGTH} and < {SNAKE_MAX_LENGTH}")
    if _is_out_of_board(snake, board):
        raise ValueError(f"The snake can't be outside the board!")
    if not _snake_body_parts_are_two_dimensional(snake):
        raise ValueError("Snake body parts should be two-dimensional!")

    # board
    if (board[0] < BOARD_MIN_X or board[1] < BOARD_MIN_Y or
            board[0] > BOARD_MAX_X or board[1] > BOARD_MAX_Y):
        raise ValueError("Board dimension are out of specified boundaries")

    # depth
    if depth < MIN_DEPTH or depth > MAX_DEPTH:
        raise ValueError(f"Depth should be < {MIN_DEPTH} and > {MAX_DEPTH}")


def _is_out_of_board(snake: Snake,
                     board: Board) -> bool:
    """
    Checks if the snake is out of the board

    Args:
        snake:  representation of the positions of a snake in the board.
        board: two-dimensional space where the snake will be moving.

    Returns:
        True if it is outside the board, otherwise False.
    """
    for body_part in snake:
        if (body_part[0] < 0 or body_part[1] < 0 or
                body_part[0] > board[0] or body_part[1] > board[0]):
            return True

    return False


def _snake_body_parts_are_two_dimensional(snake: Snake) -> bool:
    """
    Checks if all the body parts of the snake are two-dimensional
    Args:
        snake: representation of the positions of a snake in the board.

    Returns:
        True if it all the body parts are two-dimensional, otherwise False.
    """
    for body_part in snake:
        if len(body_part) != 2:
            return False
    return True
