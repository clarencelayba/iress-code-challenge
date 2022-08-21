from enum import Enum


class Direction(Enum):
    """This holds available direction for the robot."""

    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3


class Position:
    """This holds the information of the position of the robot on the table
    (coordinates and direction)"""

    def __init__(self, x: int, y: int, direction: Direction):
        self.x, self.y, self.direction = x, y, direction

    def __repr__(self) -> str:
        return f"x: {self.x}, y: {self.y}, facing: {self.direction.name}"
