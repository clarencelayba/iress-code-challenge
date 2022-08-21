import pytest

from toy_robot.exceptions import CommandError
from toy_robot.models import Direction
from toy_robot.constants import CommandErrorMessage as CmdErrorMsg


def test_set_position_error(robot, position):
    # default table size is 5x5, therefore position is invalid
    pos = position(x=6, y=1, direction=Direction.EAST)
    with pytest.raises(CommandError) as exc_info:
        robot.set_position(position=pos)

    assert exc_info.value.message == CmdErrorMsg.INVALID_POSITION


def test_set_position_success(robot, position):
    x, y, direction = 4, 1, Direction.EAST
    pos = position(x=x, y=y, direction=direction)
    robot.set_position(position=pos)
    assert (
        str(robot.current_position)
        == f"x: {x}, y: {y}, facing: {direction.name}"
    )


def test_turn_left_error(robot):
    with pytest.raises(CommandError) as exc_info:
        robot.turn_left()
    assert exc_info.value.message == CmdErrorMsg.INVALID_COMMAND_SEQUENCE


def test_turn_left_success(robot, position):
    x, y, direction = 4, 1, Direction.EAST
    pos = position(x=x, y=y, direction=direction)
    robot.set_position(position=pos)
    robot.turn_left()

    assert robot.current_position.direction == Direction.NORTH


def test_turn_right_success(robot, position):
    x, y, direction = 4, 1, Direction.EAST
    pos = position(x=x, y=y, direction=direction)
    robot.set_position(position=pos)
    robot.turn_right()

    assert robot.current_position.direction == Direction.SOUTH


def test_move_forward_error(robot, position):
    x, y, direction = 4, 1, Direction.EAST
    pos = position(x=x, y=y, direction=direction)
    with pytest.raises(CommandError) as exc_info:
        robot.set_position(position=pos)
        robot.move_forward()

    assert exc_info.value.message == CmdErrorMsg.INVALID_POSITION


@pytest.mark.parametrize(
    "x, y, direction, expected_result",
    [
        (1, 1, Direction.NORTH, (1, 2)),
        (1, 1, Direction.SOUTH, (1, 0)),
        (1, 1, Direction.EAST, (2, 1)),
        (1, 1, Direction.WEST, (0, 1)),
    ],
    ids=["Move North", "Move South", "Move East", "Move West"],
)
def test_move_forward_success(
    robot, position, x, y, direction, expected_result
):
    pos = position(x=x, y=y, direction=direction)
    robot.set_position(position=pos)
    robot.move_forward()
    assert (
        robot.current_position.x,
        robot.current_position.y,
    ) == expected_result


def test_report_position_success(robot, position):
    x, y, direction = 3, 1, Direction.EAST
    pos = position(x=x, y=y, direction=direction)
    robot.set_position(position=pos)
    robot.report_position()
