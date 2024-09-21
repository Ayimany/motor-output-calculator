import logging
import re

VALID_PROPERTIES = {
    "Targets": "targets",
    "Mechanical Power Output": "p_out",
    "Mechanical Power Input": "p_in",
    "Efficiency": "eff",
    "Input Voltage": "v_in",
    "Input Current": "i_in",
    "Input Resistance": "o_in",
    "Output Voltage": "v_out",
    "Output Current": "i_out",
    "Output Resistance": "o_out",
}


class motor_struct:

    def __init__(self, targets: list[str], properties: dict[str, float]):
        self.targets = targets
        self.properties = properties


def print_mprop_err(index: int, arg: str, reason: str, logger):
    logger.warning(
        f"At argument #{index} ('{arg}'):"
        + reason
        + "This value will not be considered."
    )


def represents_floating_point(what: str) -> bool:
    """Determines whether a string can be parsed as a floating point number or
    not. The usual `isnumeric()` method is not great at recognizing
    floating-point numbers. This method fixes said issue."""

    match = re.match(r"^[-+]?[0-9]*\.?[0-9]+", what)

    if match is None:
        return False

    return match.group() == what


def extract_motor_data(args: list[str], logger: logging.Logger) -> motor_struct:
    targets = []
    properties = {}

    for i, arg in enumerate(args):
        delimiter_count = arg.count(":")

        if delimiter_count < 1:
            print_mprop_err(i, arg, "Missing property delimiter (':')", logger)
            continue

        elif delimiter_count > 1:
            print_mprop_err(
                i, arg, "Can only have one separator per entry (':').", logger
            )
            continue

        segments = [s.strip() for s in arg.split(sep=":")]

        property = segments[0]
        value = segments[1]

        if not value or value.isspace():
            print_mprop_err(i, arg, "Property with no value.", logger)
            continue

        if property == "targets":
            targets += [s.strip() for s in value.split(",")]
            continue

        if property not in VALID_PROPERTIES.values():
            print_mprop_err(i, arg, f"Invalid property '{property}'.", logger)
            continue

        if not represents_floating_point(value):
            print_mprop_err(
                i,
                arg,
                f"Right-hand side of argument, '{value}', is non-numeric.",
                logger,
            )
            continue

        properties[property] = float(value)

    return motor_struct(targets, properties)
