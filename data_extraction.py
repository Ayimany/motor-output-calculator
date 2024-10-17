import logging

from data_formats import VALID_PROPERTIES, represents_floating_point


class MotorStruct:
    """
    Contains the information about a motor.
    """

    def __init__(self, properties: dict[str, float]):
        """
        Constructs a MotorStruct object.

        @param properties: The raw, existing properties of the motor
        """
        self.properties = properties


def data_ext_error(index: int, arg: str, reason: str, logger):
    """
    Formats and output a data extraction error message via a logger object.

    @param index: The index of the element which caused the data extraction
    error
    @param arg: The value of the problematic argument
    @param reason: The reason of failure
    @param logger: The logger with which to output the error message
    """
    logger.warning(
        f"At parameter #{index} ('{arg}'): "
        + reason
        + " This value will not be considered."
    )


def convert_to_motor_data(args: list[str],
                          logger: logging.Logger) -> MotorStruct:
    """
    Converts a list of formatted arguments to a MotorStruct object. The format
    follows the convention `ArgumentName:ArgumentValue`

    @param args: The arguments to parse
    @param logger: The logger with which to log messages
    @return: The parsed data as a MotorStruct
    """
    properties = {}

    for i, arg in enumerate(args):
        delimiter_count = arg.count(":")

        if delimiter_count < 1:
            data_ext_error(i, arg, "Missing property delimiter (':')", logger)
            continue

        elif delimiter_count > 1:
            data_ext_error(
                i, arg, "Can only have one separator per entry (':').", logger
            )
            continue

        name_and_value = [s.strip() for s in arg.split(sep=":")]

        if len(name_and_value) != 2:
            data_ext_error(i, arg, "A property needs a name and a value.",
                           logger)

        name = name_and_value[0]
        value = name_and_value[1]

        if name not in VALID_PROPERTIES:
            data_ext_error(i, arg, f"Invalid property '{name}'.", logger)
            continue

        if not represents_floating_point(value):
            data_ext_error(
                i,
                arg,
                f"Right-hand side of parameter , '{value}', is non-numeric.",
                logger,
            )
            continue

        properties[name] = float(value)

    return MotorStruct(properties)
