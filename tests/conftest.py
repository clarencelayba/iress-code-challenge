import pytest as pytest

from toy_robot.models import Position
from toy_robot.robots import Robot
from toy_robot.tables import Table


@pytest.fixture
def robot() -> Robot:
    robot = Robot(table=Table(height=5, width=5))
    return robot


@pytest.fixture
def position() -> Position:
    def _position(x, y, direction):
        position = Position(x=x, y=y, direction=direction)
        return position

    return _position
