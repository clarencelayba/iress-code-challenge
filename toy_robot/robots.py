from abc import ABC, abstractmethod
from typing import Optional

from toy_robot.constants import CommandErrorMessage as CmdErrorMsg
from toy_robot.exceptions import CommandError
from toy_robot.models import Position, Direction
from toy_robot.tables import TableBase


class RobotBase(ABC):
    """Abstract Base class for the robot (Robot Interface)"""

    @abstractmethod
    def set_position(self, position: Position) -> None:
        """Sets the position of the robot in the table."""

    @abstractmethod
    def turn_left(self) -> None:
        """Turns the robot direction left in the table."""

    @abstractmethod
    def turn_right(self) -> None:
        """Turns the robot direction right in the table."""

    @abstractmethod
    def move_forward(self) -> None:
        """Moves the robot forward in the table."""

    @abstractmethod
    def report_position(self) -> None:
        """Reports the actual position of the robot in the table."""


class Robot(RobotBase):
    """A receiver robot class that performs the commands."""

    def __init__(self, table: TableBase):
        self.current_position: Optional[Position] = None
        self.table = table

    def _validate_command_sequence(func):  # noqa
        """This wrapper function ensures that the command sequence starts from
        'PLACE' command first."""

        def wrapper(*args, **kwargs):
            robot = args[0]
            if not robot.current_position:
                raise CommandError(msg=CmdErrorMsg.INVALID_COMMAND_SEQUENCE)
            return func(*args, **kwargs)  # noqa

        return wrapper

    def set_position(self, position: Position):
        if not self.table.is_target_position_valid(x=position.x, y=position.y):
            raise CommandError(msg=CmdErrorMsg.INVALID_POSITION)
        self.current_position = position

    @_validate_command_sequence
    def turn_left(self):
        new_direction = Direction(
            (self.current_position.direction.value + 3) % 4
        )
        self.current_position.direction = new_direction

    @_validate_command_sequence
    def turn_right(self):
        new_direction = Direction(
            (self.current_position.direction.value + 1) % 4
        )
        self.current_position.direction = new_direction

    @_validate_command_sequence
    def move_forward(self):
        new_x = self.current_position.x
        new_y = self.current_position.y
        match self.current_position.direction:
            case Direction.NORTH:
                new_y += 1
            case Direction.SOUTH:
                new_y -= 1
            case Direction.EAST:
                new_x += 1
            case Direction.WEST:
                new_x -= 1

        if not self.table.is_target_position_valid(x=new_x, y=new_y):
            raise CommandError(msg=CmdErrorMsg.INVALID_POSITION)
        self.current_position.x = new_x
        self.current_position.y = new_y

    @_validate_command_sequence
    def report_position(self):
        print(f"Robot's current position: {self.current_position}")
