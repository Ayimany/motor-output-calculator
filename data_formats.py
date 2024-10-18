import re

VALID_PROPERTIES = {
    "p_out": "Mechanical Power Output (W)",
    "p_in": "Mechanical Power Input (W)",
    "eff": "Efficiency (0-1)",
    "v": "Input Voltage (V)",
    "i": "Input Current (A)",
    "r": "Input Resistance (Ohms)",
    "w": "Angular Velocity (rad/s)",
    "t": "Output Torque (Nm)",
    "rpm": "Revolutions per Minute (rev/min)",
}


def represents_floating_point(what: str) -> bool:
    """
    Determines whether a string can be parsed as a floating point number or
    not. The usual `isnumeric()` method is not great at recognizing
    floating-point numbers. This method fixes this issue.

    @param what: The string to check
    @return: Whether the value represents a floating point number
    """

    # Regex.
    match = re.match(r"^[-+]?[0-9]*\.?[0-9]+", what)

    if match is None:
        return False

    return match.group() == what
