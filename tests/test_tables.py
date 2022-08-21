import pytest

from toy_robot.exceptions import TableError
from toy_robot.tables import Table
from toy_robot.constants import TableErrorMessage as TblErrMsg


@pytest.mark.parametrize(
    "width, height, expected_error, expected_message",
    [
        (-1, 5, TableError, TblErrMsg.INVALID_WIDTH),
        (5, -1, TableError, TblErrMsg.INVALID_HEIGHT),
    ],
    ids=[
        "Invalid width",
        "Invalid height",
    ],
)
def test_dimension_error(width, height, expected_error, expected_message):
    with pytest.raises(expected_error) as exc_info:
        Table(width=width, height=height)

    assert exc_info.value.message == expected_message


def test_dimension_success():
    width, height = 1, 1
    table = Table(width=width, height=height)

    assert table.width == width
    assert table.height == height


@pytest.mark.parametrize(
    "x, y, expected_result",
    [(-1, 5, False), (1, 1, True)],
    ids=[
        "Valid Position",
        "Invalid Position",
    ],
)
def test_is_target_position_valid(x, y, expected_result):
    table = Table(width=5, height=5)
    result = table.is_target_position_valid(x=x, y=y)
    assert result is expected_result
