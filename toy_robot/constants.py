class CommandErrorMessage:
    """Store all the Command error messages here."""

    INVALID_COMMAND = (
        "Invalid command, available commands: ['PLACE', 'MOVE', 'LEFT', "
        "'RIGHT', 'REPORT']"
    )
    INVALID_PLACE_FORMAT = (
        "Invalid format for 'PLACE' command, Please follow this "
        "format: PLACE <x coordinate>,<y coordinate>,<direction[NORTH|"
        "SOUTH|EAST|WEST]> \nor make sure that there no negative number "
        "coordinates"
    )
    INVALID_PLACE_MISSING_ARGS = (
        "'PLACE' command needs coordinates and direction"
    )
    INVALID_POSITION = "Invalid Position, Robot will fall from the table"
    INVALID_COMMAND_SEQUENCE = (
        "Please place the robot in the table first using 'PLACE' command"
    )


class TableErrorMessage:
    """Store all the Table error messages here."""

    INVALID_WIDTH = "Invalid table width"
    INVALID_HEIGHT = "Invalid table height"
