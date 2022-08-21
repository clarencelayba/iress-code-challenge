import pytest

from toy_robot.constants import CommandErrorMessage as CmdErrorMsg
from toy_robot.exceptions import CommandError
from toy_robot.helpers import InputHelper

TEST_INVALID_CMD = "INVALID"


@pytest.mark.parametrize(
    "command_list, expected_error, expected_message",
    [
        (
            [f"{TEST_INVALID_CMD} 1,1,NORTH"],
            CommandError,
            CmdErrorMsg.INVALID_COMMAND,
        ),
        (["PLACE 1,NORTH,1"], CommandError, CmdErrorMsg.INVALID_PLACE_FORMAT),
        (["PLACE"], CommandError, CmdErrorMsg.INVALID_PLACE_MISSING_ARGS),
    ],
    ids=[
        "Invalid Command",
        "Invalid PLACE Command Format",
        "Invalid PLACE Command missing args",
    ],
)
def test_parse_command_error(
    robot, command_list, expected_error, expected_message
):
    input_helper = InputHelper(receiver_robot=robot)
    with pytest.raises(expected_error) as exc_info:
        input_helper.parse_command(command_list=command_list)

    assert exc_info.value.message == expected_message


def test_parse_command_success(robot):
    command_list = ["PLACE 1,1,NORTH", "MOVE", "LEFT", "RIGHT", "REPORT"]
    input_helper = InputHelper(receiver_robot=robot)
    result = input_helper.parse_command(command_list=command_list)

    assert len(result) == len(command_list)
