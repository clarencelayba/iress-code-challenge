from unittest import mock

from toy_robot.models import Direction
from toy_robot.simulator import Place, Move, Left, Right, Report


def test_simulator_place_command(robot):
    with mock.patch.object(robot, "set_position") as mocked_set_position:
        x, y, direction = 1, 1, Direction.SOUTH
        place = Place(receiver_robot=robot, x=x, y=y, direction=direction)
        place.execute()
        mocked_set_position.assert_called_once()


def test_simulator_move_command(robot):
    with mock.patch.object(robot, "move_forward") as mocked_set_position:
        move = Move(receiver_robot=robot)
        move.execute()
        mocked_set_position.assert_called_once()


def test_simulator_left_command(robot):
    with mock.patch.object(robot, "turn_left") as mocked_set_position:
        turn_left = Left(receiver_robot=robot)
        turn_left.execute()
        mocked_set_position.assert_called_once()


def test_simulator_right_command(robot):
    with mock.patch.object(robot, "turn_right") as mocked_set_position:
        turn_right = Right(receiver_robot=robot)
        turn_right.execute()
        mocked_set_position.assert_called_once()


def test_simulator_report_command(robot):
    with mock.patch.object(robot, "report_position") as mocked_set_position:
        report_position = Report(receiver_robot=robot)
        report_position.execute()
        mocked_set_position.assert_called_once()
