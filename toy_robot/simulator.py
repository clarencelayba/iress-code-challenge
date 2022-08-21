from abc import ABC, abstractmethod

from toy_robot.models import Position, Direction


class SimulatorCommand(ABC):
    """The Simulator Command interface declares a method for executing a
    command."""

    def __init__(self, receiver_robot):
        self._robot = receiver_robot

    @abstractmethod
    def execute(self) -> None:
        """execute commands."""


class Place(SimulatorCommand):
    """A concrete command class that defines a binding between a receiver Robot
    and the simulator's set position command."""

    def __init__(self, receiver_robot, x: int, y: int, direction: Direction):
        super().__init__(receiver_robot)
        self._position = Position(x=x, y=y, direction=direction)

    def execute(self) -> None:
        self._robot.set_position(self._position)


class Move(SimulatorCommand):
    """A concrete command class that defines a binding between a receiver Robot
    and the simulator's move forward command."""

    def execute(self) -> None:
        self._robot.move_forward()


class Left(SimulatorCommand):
    """A concrete command class that defines a binding between a receiver Robot
    and the simulator's turn left command."""

    def execute(self) -> None:
        self._robot.turn_left()


class Right(SimulatorCommand):
    """A concrete command class that defines a binding between a receiver Robot
    and the simulator's turn right command."""

    def execute(self) -> None:
        self._robot.turn_right()


class Report(SimulatorCommand):
    """A concrete command class that defines a binding between a receiver Robot
    and the simulator's report position command."""

    def execute(self) -> None:
        self._robot.report_position()
