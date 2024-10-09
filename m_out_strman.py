import re

VALID_PROPERTIES = {
    "p_out": "Mechanical Power Output",
    "p_in": "Mechanical Power Input",
    "eff": "Efficiency",
    "v": "Input Voltage",
    "i": "Input Current",
    "r": "Input Resistance",
    "w": "Angular Velocity",
    "t": "Output Torque",
    "rpm": "Revolutions per Minute",
}


def represents_floating_point(what: str) -> bool:
    """Determines whether a string can be parsed as a floating point number or
    not. The usual `isnumeric()` method is not great at recognizing
    floating-point numbers. This method fixes said issue."""

    match = re.match(r"^[-+]?[0-9]*\.?[0-9]+", what)

    if match is None:
        return False

    return match.group() == what
