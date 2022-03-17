import enum

# Snake constants
SNAKE_MIN_LENGTH = 3
SNAKE_MAX_LENGTH = 7

# Board constants
BOARD_MAX_X = BOARD_MAX_Y = 10
BOARD_MIN_X = BOARD_MIN_Y = 1

# Depth constants
MIN_DEPTH = 1
MAX_DEPTH = 20


class SnakeMovement(enum.Enum):
    """
    Possible movements of a snake
    """
    UP = "U"
    DOWN = "D"
    LEFT = "L"
    RIGHT = "R"
