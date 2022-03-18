"""
Module with logic to calculate the solutions for the snake algorithm
"""
import copy

from .constants import (SNAKE_MIN_LENGTH, SNAKE_MAX_LENGTH, MAX_DEPTH, MIN_DEPTH,
                        BOARD_MAX_X, BOARD_MIN_X, BOARD_MAX_Y, BOARD_MIN_Y, SnakeMovementDirection)
from .data_structures import Snake, Board

solutions: int  # Global variable used by the backtracking algorithm


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
    global solutions
    solutions = 0

    _check_input(snake, board, depth)
    _search_solutions(snake, board, depth)

    return solutions


def _search_solutions(snake: Snake,
                      board: Board,
                      depth: int) -> None:
    """
    Recursive function used to perform the backtracking algorithm

    Args:
        snake:  representation of the positions of a snake in the board.
        board: two-dimensional space where the snake will be moving.
        depth: number of movements of the snake.
    """
    global solutions

    match depth:
        case 0:  # base case, all movements have been completed
            solutions += 1
            return
        case _:  # There are still movements to check

            # UP
            if _is_valid_snake((snake_moved := _move_snake(snake, SnakeMovementDirection.UP)), board):
                _search_solutions(snake_moved, board, depth - 1)  # Recursive call
            # RIGHT
            if _is_valid_snake((snake_moved := _move_snake(snake, SnakeMovementDirection.RIGHT)), board):
                _search_solutions(snake_moved, board, depth - 1)  # Recursive call

            # DOWN
            if _is_valid_snake((snake_moved := _move_snake(snake, SnakeMovementDirection.DOWN)), board):
                _search_solutions(snake_moved, board, depth - 1)  # Recursive call

            # LEFT
            if _is_valid_snake((snake_moved := _move_snake(snake, SnakeMovementDirection.LEFT)), board):
                _search_solutions(snake_moved, board, depth - 1)  # Recursive call

            return  # Backtrack


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
    if _snake_is_out_of_board(snake, board):
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


def _snake_is_out_of_board(snake: Snake,
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
                body_part[0] >= board[0] or body_part[1] >= board[1]):
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


def _move_snake(snake: Snake,
                direction: SnakeMovementDirection) -> Snake:
    """
    Performs a move on the snake body

    Notes:
        The original snake is not modified, the method uses a copy and return
        the copy with the movement applied

    Args:
        snake: representation of the positions of a snake in the board.
        direction: movement direction of the snake

    Returns:
        An Snake object with the selected movement direction applied

    """
    snake_moved = copy.deepcopy(snake)

    # Displace all the body parts pointers (except the head and the second part)
    for i in range(len(snake_moved) - 1, 1, -1):
        snake_moved[i] = snake_moved[i - 1]

    # Deep copy the head to avoid passing the same pointer
    snake_moved[1] = copy.deepcopy(snake[0])

    # Move the head to the desired direction
    match direction:
        case SnakeMovementDirection.UP:
            snake_moved[0][0] -= 1
        case SnakeMovementDirection.RIGHT:
            snake_moved[0][1] += 1
        case SnakeMovementDirection.DOWN:
            snake_moved[0][0] += 1
        case SnakeMovementDirection.LEFT:
            snake_moved[0][1] -= 1

    return snake_moved


def _is_valid_snake(snake: Snake,
                    board: Board) -> bool:
    """
    Checks if a position for a new snake object is valid or not

    Args:
        snake: snake object to check if is valid
        board: two-dimensional space where the snake will be moving.

    Returns:
        True if the new snake is in a valid position, otherwise else.

    """
    if _snake_is_out_of_board(snake, board) or _is_head_colliding(snake):
        return False
    else:
        return True


def _is_head_colliding(snake: Snake) -> bool:
    """
    Checks if the snake_head is in an empty position

    Args:
        snake: representation of the positions of a snake in the board.

    Returns:
        True if the snake head is colliding with the snake, else otherwise

    """
    snake_head = snake[0]
    for body_part in snake[1:]:  # Only iterate the body avoiding head
        if body_part == snake_head:
            return True

    return False
