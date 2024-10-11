import logging

import m_out_strman as mstr


class MotorStruct:

    def __init__(self, properties: dict[str, float]):
        self.properties = properties


def data_ext_error(index: int, arg: str, reason: str, logger):
    logger.warning(
        f"At parameter #{index} ('{arg}'): "
        + reason
        + " This value will not be considered."
    )


def convert_to_motor_data(args: list[str],
                          logger: logging.Logger) -> MotorStruct:
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

        if name not in mstr.VALID_PROPERTIES:
            data_ext_error(i, arg, f"Invalid property '{name}'.", logger)
            continue

        if not mstr.represents_floating_point(value):
            data_ext_error(
                i,
                arg,
                f"Right-hand side of parameter , '{value}', is non-numeric.",
                logger,
            )
            continue

        properties[name] = float(value)

    return MotorStruct(properties)
