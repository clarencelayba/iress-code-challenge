import re
from typing import List, Match

from toy_robot.constants import CommandErrorMessage as CmdErrorMsg
from toy_robot.simulator import (
    Place,
    Report,
    Move,
    Left,
    Right,
    SimulatorCommand,
)
from toy_robot.exceptions import CommandError
from toy_robot.models import Direction
from toy_robot.robots import RobotBase


class InputHelper:
    """This helps in parsing and validating the input command."""

    COMMAND_MAPPER = {
        "PLACE": Place,
        "MOVE": Move,
        "LEFT": Left,
        "RIGHT": Right,
        "REPORT": Report,
    }
    PLACE_PATTERN: str = (
        r"(?P<X>\d+),(?P<Y>\d+),(?P<F>NORTH|north|EAST|east|WEST|west|SOUTH|"
        r"south)"
    )

    def __init__(self, receiver_robot: RobotBase):
        self.robot = receiver_robot

    def parse_command(self, command_list: List[str]) -> List[SimulatorCommand]:
        """Parses and validates the user's command input."""
        simulator_commands: List[SimulatorCommand] = []
        for sim_command_text in command_list:
            command_and_args = sim_command_text.strip().split(" ")
            cmd = command_and_args[0].upper()
            args = []
            if len(command_and_args) > 1:
                args = command_and_args[1:]

            if cmd not in self.COMMAND_MAPPER:
                raise CommandError(msg=CmdErrorMsg.INVALID_COMMAND)
            class_kwargs = {"receiver_robot": self.robot}
            if cmd == "PLACE":
                try:
                    match: Match = re.compile(self.PLACE_PATTERN).match(
                        args[0]
                    )
                    if not match:
                        raise CommandError(
                            msg=CmdErrorMsg.INVALID_PLACE_FORMAT
                        )
                    arguments = args[0].split(",")
                    class_kwargs.update(
                        x=int(arguments[0]),
                        y=int(arguments[1]),
                        direction=Direction[arguments[2].upper()],
                    )
                except IndexError:
                    raise CommandError(
                        msg=CmdErrorMsg.INVALID_PLACE_MISSING_ARGS
                    )
            simulator_commands.append(self.COMMAND_MAPPER[cmd](**class_kwargs))

        return simulator_commands
