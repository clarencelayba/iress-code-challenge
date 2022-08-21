from abc import ABC, abstractmethod
from typing import Union

from toy_robot.constants import TableErrorMessage as TblErrMsg
from toy_robot.exceptions import TableError


class TableBase(ABC):
    """Abstract Base class for the table (Table Interface)"""

    @abstractmethod
    def mark_position(self) -> None:
        """Lets you mark all the occupied coordinates in the table, Detects
        potential collision if ever there are multiple robots in a table."""

    @abstractmethod
    def is_target_position_valid(self, x, y) -> None:
        """Checks if the target position for placement or movement of the robot
        is valid or available in the table."""


class Table(TableBase):
    """Actual Table that allows placement of the Robot."""

    def __init__(
        self,
        width: int = 5,
        height: int = 5,
        marked_positions: list = None,
    ):
        self.width = width
        self.height = height
        self.marked_positions = marked_positions

    @property
    def width(self) -> int:
        return self._width

    @width.setter
    def width(self, value: Union[int, str]) -> None:
        """Sets natural number width of the table."""
        if value <= 0:
            raise TableError(msg=TblErrMsg.INVALID_WIDTH)
        self._width = int(value)

    @property
    def height(self) -> int:
        return self._height

    @height.setter
    def height(self, value: Union[int, str]) -> None:
        """Sets natural number height of the table."""
        if value <= 0:
            raise TableError(msg=TblErrMsg.INVALID_HEIGHT)
        self._height = int(value)

    def mark_position(self) -> None:
        """For future proofing."""

    def is_target_position_valid(self, x, y) -> bool:
        if (0 > x or x > self.width - 1) or (0 > y or y > self.height - 1):
            return False
        return True
