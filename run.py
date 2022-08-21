from toy_robot.exceptions import CommandError, TableError
from toy_robot.helpers import InputHelper
from toy_robot.robots import RobotBase, Robot
from toy_robot.tables import Table


class RobotInvoker:
    """this will invoke any receiver robot depending on the command."""

    def __init__(self, robot_receiver: RobotBase):
        self.cmd = None
        self.robot = robot_receiver

    def execute(self, simulator_commands) -> None:
        """This calls the execute function of the interface implementation."""
        input_helper = InputHelper(receiver_robot=self.robot)
        cmd_list = input_helper.parse_command(command_list=simulator_commands)
        for cmd in cmd_list:
            cmd.execute()

    def execute_by_manual_input(self):
        """Executes the command via manual input."""
        try:
            while True:
                command_text = input()
                commands = command_text.splitlines()
                try:
                    self.execute(simulator_commands=commands)
                except CommandError as e:
                    print(e.message)
        except TableError as e:
            print(e.message)

    def execute_by_file_input(self, file_path: str):
        """Executes the command via file input."""
        with open(file_path, "r", encoding="utf-8") as file:
            try:
                self.execute(simulator_commands=file.readlines())
            except CommandError as e:
                print(e.message)


if __name__ == "__main__":
    """Creates and invokes the robot that receives the commands."""

    robot = Robot(surface=Table(height=5, width=5))
    print("Welcome to Robot Toy Simulation, Please enter a valid command: ")
    robot_invoker = RobotInvoker(robot_receiver=robot)
    robot_invoker.execute_by_manual_input()

    # NOTE: this could also be executed via file
    # robot_invoker.execute_by_file_input(file_path="data.txt")
